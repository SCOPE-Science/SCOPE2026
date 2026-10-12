from fractions import Fraction as F

La=d=F(1)
gamma=F(2)
omega=F(1)
beta=F(10)
V=F(1)
eps=F(4,5)
beta0=F(0)
a0=F(1,10)
alpha=F(5)
eta=F(1)

def c(B):
    return beta*V*(1-eps*B)+beta0

def rhs(x):
    S,I,R,B=x
    N=S+I+R
    inf=c(B)*S*I/N
    return (La-inf-d*S+omega*R,
            inf-(gamma+d)*I,
            gamma*I-(omega+d)*R,
            a0*(1-B)+alpha*(I/N)*(1-B)-eta*B)

B0=a0/(a0+eta)
R0=c(B0)/(gamma+d)
assert B0 == F(1,11)
assert R0 == F(34,11)
assert R0 > 1

xs=(F(27,50),F(23,100),F(23,100),F(5,9))
assert rhs(xs) == (F(0),F(0),F(0),F(0))

x=(F(3,4),F(1,100),F(1,20),F(19,20))
v=rhs(x)
assert v == (F(5,18),-F(7,900),-F(2,25),-F(15259,16200))

wdot=sum((1-zs/z)*dz for z,zs,dz in zip(x,xs,v))
assert wdot == F(2019503,13851000)
assert wdot > 0

S,I,R,B=x
Ss,Is,Rs,Bs=xs
q13=-(d*(S-Ss)**2/S
      +(gamma+d)*(I-Is)**2/I
      +(omega+d)*(R-Rs)**2/R
      +eta*(B-Bs)**2/B)
assert q13 == -F(30854209,1923750)
assert q13 < 0
assert not (wdot <= q13)

print('VERIFY_OK')
