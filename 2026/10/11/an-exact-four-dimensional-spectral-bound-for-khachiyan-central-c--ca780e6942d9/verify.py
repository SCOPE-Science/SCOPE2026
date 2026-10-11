from fractions import Fraction
from decimal import Decimal, getcontext

# Polynomials are stored in ascending coefficient order.

def strip(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p

def deriv(p):
    return strip([Fraction(i)*p[i] for i in range(1,len(p))] or [Fraction(0)])

def divmod_poly(a,b):
    a=strip(a)
    b=strip(b)
    if b==[0]:
        raise ZeroDivisionError
    q=[Fraction(0)]*max(1,(len(a)-len(b)+1))
    r=a[:]
    while len(r)>=len(b) and r!=[0]:
        k=len(r)-len(b)
        c=r[-1]/b[-1]
        q[k]+=c
        for j in range(len(b)):
            r[j+k]-=c*b[j]
        r=strip(r)
    return strip(q),strip(r)

def sturm(p):
    seq=[strip([Fraction(c) for c in p])]
    seq.append(deriv(seq[0]))
    while seq[-1]!=[0]:
        _,r=divmod_poly(seq[-2],seq[-1])
        if r==[0]:
            break
        seq.append([-c for c in r])
    return seq

def peval(p,x):
    y=Fraction(0)
    for c in reversed(p):
        y=y*x+c
    return y

def variations(seq,x):
    signs=[]
    for p in seq:
        v=peval(p,x)
        if v>0: signs.append(1)
        elif v<0: signs.append(-1)
        else: raise AssertionError("endpoint is a root")
    return sum(signs[i]!=signs[i-1] for i in range(1,len(signs)))

def roots_between(p,a,b):
    s=sturm(p)
    return variations(s,a)-variations(s,b)

# Crossing polynomial P.
P=[
    16777216,
    -33554432,
    1048576,
    3145728,
    548864,
    -8192,
    -3840,
    0,
    1,
]

# Derivative-elimination polynomial Q for the second finite-dimensional branch.
Q=[
    -268435456,
    67108864,
    603979776,
    471859200,
    115867648,
    -12046336,
    -9777664,
    -689520,
    228488,
    28561,
]

assert roots_between(P,Fraction(0),Fraction(1)) == 1
aL=Fraction(523194,10**6)
aU=Fraction(523195,10**6)
assert peval(P,aL)>0 and peval(P,aU)<0
assert roots_between(P,aL,aU) == 1

assert roots_between(Q,Fraction(0),Fraction(1)) == 1
bL=Fraction(5165,10**4)
bU=Fraction(5166,10**4)
assert peval(Q,bL)<0 and peval(Q,bU)>0
assert roots_between(Q,bL,bU) == 1

# First logarithmic derivative is positive at the crossing.
def q1(x):
    return 49*x**3+224*x**2+192*x-256
assert q1(aU)<0

# Exact second-branch derivative at alpha=1/2.
assert Fraction(1)-Fraction(12)*Fraction(1,2)*Fraction(43,84)/Fraction(25,8) == Fraction(3,175)

# Independent high-precision bisection of the original unsquared crossing.
getcontext().prec=60
def dsqrt(x):
    return x.sqrt()
def f1(a):
    return dsqrt(a+a*a/Decimal(4))
def f2(a):
    return dsqrt(f1(a)+a*a/Decimal(16))
def cross(a):
    return (Decimal(4)-f2(a))**2-Decimal(3)*(Decimal(4)-f1(a))
lo=Decimal(523194)/Decimal(10**6)
hi=Decimal(523195)/Decimal(10**6)
assert cross(lo)>0 and cross(hi)<0
for _ in range(180):
    mid=(lo+hi)/2
    if cross(mid)>0:
        lo=mid
    else:
        hi=mid
a=(lo+hi)/2
C=a*((Decimal(4)-f1(a))/Decimal(3))**6
C2=a*((Decimal(4)-f2(a))/Decimal(3))**12
assert abs(C-C2) < Decimal("1e-50")
assert Decimal("0.81623940332040") < C < Decimal("0.81623940332042")
assert Decimal("0.52319428700279") < a < Decimal("0.52319428700280")

print("VERIFY_OK")
print("alpha_star", a)
print("C4", C)
