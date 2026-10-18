"""Exact arithmetic checks for a two-patch Hill-survival Beverton--Holt model.

Run with Python 3: python verify.py
The computation is auxiliary; the theorem requires the written proof.
"""
from fractions import Fraction as Q
from itertools import product


def T(x):
    return x * (17 + 7*x*x) / ((1+x)*(11+x*x))


def F(x,y):
    a,b = T(x),T(y)
    return (Q(3,5)*a+Q(2,5)*b, Q(2,5)*a+Q(3,5)*b)


def Tp(x):
    return (7*x**4+120*x**3+214*x*x+187)/((1+x)**2*(11+x*x)**2)

# Parameters and dispersal survival.
a=Q(10); u=Q(17,110); v=Q(6,11); H=Q(11)
assert 0 < u < u+v < 1
K=a*u-1; L=a*(u+v)-1
assert K==Q(6,11) and L==Q(6)
assert L>9*K

# Cubic/discriminant and three positive roots, no numerically fitted parameters.
def P(x): return x**3-L*x*x+H*x-H*K
assert [P(Q(i)) for i in (1,2,3)]==[0,0,0]
assert [Tp(Q(i)) for i in (1,2,3)] == [Q(11,12),Q(47,45),Q(37,40)]
assert [T(Q(i)) for i in (1,2,3)]==[Q(i) for i in (1,2,3)]
assert [T(Q(i))-Q(i) for i in (0,1,2,3,4)]==[0,0,0,0,T(Q(4))-Q(4)]

# Exact derivative certificate: 3(1+x)^2(11+x^2)^2 - numerator(T') has all positive coefficients.
# Coefficients low degree to high degree.
def pmul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def pscale(a,c): return [c*z for z in a]

D=pmul(pmul([1,2,1],[11,0,1]),[11,0,1])
N=[187,0,214,120,7]
certificate=[3*(D[i] if i<len(D) else 0)-(N[i] if i<len(N) else 0) for i in range(len(D))]
assert certificate == [176,726,215,12,62,6,3] and min(certificate)>0

# Discriminant cusp factorization is a formal degree-four polynomial identity.
for L0,K0 in product(range(2,17),range(1,5)):
    A0=L0*L0+18*L0*K0-27*K0*K0
    assert A0*A0-64*L0**3*K0 == (L0-9*K0)**3*(L0-K0)
for x in [Q(i,j) for i in range(0,24) for j in range(1,9)]:
    assert Q(0) < Tp(x) < Q(3)
    assert T(x) >=0
    assert T(x) < Q(7) if x>0 else T(x)==0
    assert T(x)-x == -x*(x-1)*(x-2)*(x-3)/((x+1)*(x*x+11))
    assert T(x)== a*x*(u+v*x*x/(H+x*x))/(1+x)

# Exact hyperbolic types in the full, genuinely coupled planar map.
for root, target in [(1,'sink'),(2,'saddle'),(3,'sink')]:
    longitudinal=Tp(Q(root)); transverse=longitudinal/Q(5)
    assert 0<transverse<1
    if target=='sink': assert longitudinal<1
    else: assert longitudinal>1

# Difference contracts, even away from the synchrony diagonal.
cases=0
for i,j in product(range(0,5), repeat=2):
    x,y=Q(i,3),Q(j,4)
    for t in range(4):
        nx,ny=F(x,y)
        assert abs(nx-ny)<=Q(3,5)*abs(x-y)
        assert nx>=0 and ny>=0
        x,y=nx,ny
        cases+=1
print('PASS: exact equilibrium polynomial, parameter identity, derivative and contraction certificates; %d transition checks' % cases)
