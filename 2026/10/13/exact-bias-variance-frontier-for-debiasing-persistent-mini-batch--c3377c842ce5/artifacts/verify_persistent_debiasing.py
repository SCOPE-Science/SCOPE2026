from fractions import Fraction as F
from itertools import combinations

def vadd(a,b):
    return tuple(x+y for x,y in zip(a,b))
def vscale(c,a):
    return tuple(c*x for x in a)
def vsub(a,b):
    return tuple(x-y for x,y in zip(a,b))
def norm2(a):
    return sum(x*x for x in a)
def mean(xs):
    n=F(len(xs))
    out=tuple(F(0) for _ in xs[0])
    for x in xs:
        out=vadd(out,x)
    return vscale(F(1,n),out)

# A nontrivial rational vector population.
pop=[
    (F(8),F(-3)),
    (F(6),F(5)),
    (F(-2),F(1)),
    (F(1),F(7)),
    (F(4),F(-4)),
    (F(-5),F(2)),
    (F(3),F(9)),
    (F(-1),F(-6)),
]
N=len(pop)
r=2
s=3
B=r+s
R=pop[:r]
C=pop[r:]
M=len(C)
a=mean(R)
b=mean(C)
g=mean(pop)
V=sum(norm2(vsub(x,b)) for x in C)/F(M)
sigma2=F(M-s,s*(M-1))*V
q=F(s,B)
p=F(M,N)
D=p-q
Delta2=norm2(vsub(a,b))
assert D==F(r*(N-B),B*N)>0

subs=list(combinations(C,s))
Us=[]
Cs=[]
for S in subs:
    bs=mean(S)
    U=vadd(vscale(F(r,B),a),vscale(F(s,B),bs))
    CC=vadd(vscale(F(r,N),a),vscale(F(M,N),bs))
    Us.append(U); Cs.append(CC)

EU=mean(Us)
EC=mean(Cs)
assert EC==g
assert vsub(EU,g)==vscale(D,vsub(a,b))
varU=sum(norm2(vsub(x,EU)) for x in Us)/F(len(Us))
varC=sum(norm2(vsub(x,g)) for x in Cs)/F(len(Cs))
assert varU==q*q*sigma2
assert varC==p*p*sigma2
assert varC/varU==(p/q)**2

# Exact partial-debiasing MSE and oracle.
num=D*Delta2-q*sigma2
if num<=0:
    tstar=F(0)
else:
    tstar=num/(D*(Delta2+sigma2))
assert F(0)<=tstar<F(1)

def mse_enum(t):
    vals=[]
    for U,CC in zip(Us,Cs):
        G=vadd(vscale(1-t,U),vscale(t,CC))
        vals.append(norm2(vsub(G,g)))
    return sum(vals,F(0))/F(len(vals))
def mse_formula(t):
    return (1-t)**2*D*D*Delta2+(q+t*D)**2*sigma2

for t in [F(0),F(1,4),F(1,2),F(3,4),F(1),tstar]:
    assert mse_enum(t)==mse_formula(t)
assert mse_formula(tstar)<=mse_formula(F(0))
assert mse_formula(tstar)<mse_formula(F(1))

# Full correction versus no correction threshold.
assert (mse_formula(F(1)) < mse_formula(F(0))) == (
    Delta2 > (p+q)*sigma2/D
)

# Independent 50%-overlap algebraic check.
N2=12
B2=4
r2=s2=2
p2=F(N2-r2,N2)
q2=F(1,2)
assert (p2/q2)**2 == (F(2)-F(B2,N2))**2
assert (p2/q2)**2 == F(25,9)

print("VERIFY_OK")
