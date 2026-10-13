from fractions import Fraction
import random

def zz(t): return 1+t-t*t

a=Fraction(7,3); gamma=Fraction(6,5); G=Fraction(11,7)
tau=Fraction(2,5); zeta=Fraction(13,12); y=Fraction(9,4)
sp=Fraction(-5,6); beta=Fraction(17,10); E=a*y
theta=zeta/G+beta*(E*sp)/(E*E)
d=-theta*E+beta*sp
assert d==-(zeta/G)*E
s=gamma*tau*d; p=a*s
raw=-G*(p*p)/(tau*zeta*p*E)
assert raw==gamma*a
zp=y+tau*d; Ez=a*zp
xi=Ez*(y-zp)/(Ez*Ez)
assert y-gamma*xi*Ez==y+gamma*tau*d

rng=random.Random(34)
for _ in range(300):
    aa=Fraction(rng.randint(1,20),rng.randint(1,20))
    gg=Fraction(rng.randint(1,19),10)
    GG=Fraction(rng.randint(1,20),rng.randint(1,20))
    tt=Fraction(rng.randint(1,10),10)
    zet=Fraction(rng.randint(10,12),10)
    yy=Fraction(rng.choice([i for i in range(-20,21) if i]),rng.randint(1,10))
    spp=Fraction(rng.randint(-20,20),rng.randint(1,10))
    bb=Fraction(rng.randint(-20,20),rng.randint(1,10))
    EE=aa*yy
    th=zet/GG+bb*(EE*spp)/(EE*EE)
    dd=-th*EE+bb*spp
    assert dd==-(zet/GG)*EE
    ss=gg*tt*dd; pp=aa*ss
    rr=-GG*(pp*pp)/(tt*zet*pp*EE)
    assert rr==gg*aa

gamma=Fraction(7,5); sigma=Fraction(1); nu=Fraction(3,10); a=Fraction(1)
basin=4*gamma/(5*sigma*nu)
assert basin==Fraction(56,15)
y0=Fraction(1); z0=Fraction(5,4); d0=-(z0/gamma)*y0
pt=y0+d0
lhs=-(a*pt)*d0
rhs=sigma*d0*d0*(nu*abs(a*pt))
assert abs(y0)<=basin and lhs>=rhs
y1=y0+gamma*d0
assert y1==Fraction(-1,4)
z1=zz(Fraction(1)); assert z1==1
d1=-(z1/gamma)*y1; pt1=y1+d1
assert -(a*pt1)*d1 >= sigma*d1*d1*(nu*abs(a*pt1))
y2=y1+gamma*d1
assert y2==0

for i in range(1000):
    t=Fraction(i+1,1000)
    assert Fraction(1)<=zz(t)<=Fraction(5,4)
print("VERIFY_OK")
