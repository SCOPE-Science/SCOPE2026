#!/usr/bin/env python3
"""Exact rational certificate for an inverse-Hankel equality classification.
Run: python3 verify_inverse_hankel.py. Standard-library only.
"""
from fractions import Fraction as F
from math import comb


def add(*polys):
    z = {}
    for p in polys:
        for e,c in p.items():
            z[e] = z.get(e,F(0)) + c
    return {e:c for e,c in z.items() if c}


def scale(p,c):
    return {e:c*v for e,v in p.items() if v*c}


def mul(a,b):
    z={}
    for e,c in a.items():
        for d,v in b.items():
            k=tuple(x+y for x,y in zip(e,d))
            z[k]=z.get(k,F(0))+c*v
    return {e:c for e,c in z.items() if c}


def power(a,n,dimension):
    out={(0,)*dimension:F(1)}
    for i in range(n):out=mul(out,a)
    return out


def constant(x,dim):return {(0,)*dim:F(x)}


def variable(dim,j):
    e=[0]*dim;e[j]=1
    return {tuple(e):F(1)}


def bernstein_on_box(P,degrees,bounds):
    """All exact multivariate Bernstein coefficients, using affine expansion."""
    n=len(degrees)
    for k in P:assert len(k)==n
    C={}
    for mon,val in P.items():
        T=constant(val,n)
        for j,degree in enumerate(mon):
            left,right=bounds[j]
            affine=add(constant(left,n),scale(variable(n,j),right-left))
            T=mul(T,power(affine,degree,n))
        C=add(C,T)
    out={}
    from itertools import product
    for ix in product(*[range(d+1) for d in degrees]):
        v=F(0)
        for exp,c in C.items():
            if all(exp[j]<=ix[j] for j in range(n)):
                fac=F(1)
                for j in range(n):fac*=F(comb(ix[j],exp[j]),comb(degrees[j],exp[j]))
                v+=c*fac
        out[ix]=v
    return out


def from_monomials(dim,terms):
    p={}
    for ex,coeff in terms:
        assert len(ex)==dim
        p[tuple(ex)]=p.get(tuple(ex),F(0))+F(coeff)
    return {e:c for e,c in p.items() if c}

# Exact source polynomial Phi(p, x, y), from Allu--Kumar Eq. (2.6).
phi=from_monomials(3,[
((4,3,0),-1),((4,2,0),16),((4,1,0),-33),((4,0,0),18),
((3,3,1),4),((3,2,1),-12),((3,1,1),-28),((3,0,1),-12),
((2,3,2),4),((2,3,0),4),((2,2,2),-68),((2,2,0),-64),
((2,1,2),-4),((2,1,0),72),((2,0,2),68),((2,0,0),36),
((1,3,1),-16),((1,2,1),-96),((1,1,1),-80),
((0,3,2),-16),((0,2,2),128),((0,2,0),144),
((0,1,2),16),((0,1,0),144),((0,0,2),-128),((0,0,0),288)
])
bs=bernstein_on_box(phi,(4,3,2),((F(0),F(2)),(F(0),F(1)),(F(0),F(1))))
assert len(bs)==60 and min(bs.values())>=0
assert all(bs[(0,j,k)]>0 for j in range(4) for k in range(3))
print('Phi: 60 exact rational Bernstein entries nonnegative; first p-row strictly positive')
print('Phi: minimal entry',min(bs.values()),'first-row minimum', min(bs[(0,j,k)] for j in range(4) for k in range(3)))

# N(p,g) = 1152 H_{3,1}(f^{-1}) in the unimodular gamma case.
N=from_monomials(2,[
((6,0),18),((6,1),51),((4,1),-204),
((2,2),688),((4,2),-368),((6,2),49),
((0,3),-1152),((2,3),704),((4,3),-172),((6,3),17),
((2,4),16),((4,4),-8),((6,4),1)
])
rev={(p,-g):c for (p,g),c in N.items()}
actual=add(constant(1,2),scale(mul(N,rev),F(-1,1152**2)))

# Q(p,x)=4*(...), x=(g+g^-1)/2, v=(1+x)/2.
Qpx=from_monomials(2,[
((8,3),144),((8,2),1284),((8,1),2168),((8,0),1028),
((6,3),-576),((6,2),-8544),((6,1),-15744),((6,0),-7776),
((4,2),24000),((4,1),52128),((4,0),30432),
((2,1),-123008),((2,0),-58496),((0,0),202752)
])
# Polynomial Q(t,v) by substituting p^(2k)=(4t)^k and x=2v-1.
T=variable(2,0);V=variable(2,1)
Qtv={}
for (pdeg,xdeg),coef in Qpx.items():
    assert pdeg%2==0
    term=mul(scale(power(T,pdeg//2,2),coef*4**(pdeg//2)),power(add(scale(V,2),constant(-1,2)),xdeg,2))
    Qtv=add(Qtv,term)
assert max(e[0] for e in Qtv)==4 and max(e[1] for e in Qtv)==3

# Independent exact coefficientwise identity for every unit-modulus g.
pp=variable(2,0);gg=variable(2,1);g_inv={(0,-1):F(1)}
x=scale(add(gg,g_inv),F(1,2));tt=scale(power(pp,2,2),F(1,4));vv=scale(add(constant(1,2),x),F(1,2))
expected_q={}
for (i,j),coef in Qtv.items():
    expected_q=add(expected_q,scale(mul(power(tt,i,2),power(vv,j,2)),coef))
expected=scale(mul(mul(tt,add(constant(1,2),scale(tt,-1))),mul(vv,expected_q)),F(1,20736))
assert actual==expected, f'phase defect identity incorrect ({len(add(actual,scale(expected,-1)))} terms)'
print('Exact Laurent identity 1-|H|^2 = t(1-t)v Q(t,v)/20736: verified coefficientwise')

for lo,hi in [(F(0),F(1,2)),(F(1,2),F(1))]:
    coeffs=bernstein_on_box(Qtv,(4,3),((lo,hi),(F(0),F(1))))
    assert len(coeffs)==20 and min(coeffs.values())>0
    print(f'Q Bernstein on t in [{lo},{hi}], v in [0,1]: 20 positive exact entries, min={min(coeffs.values())}')

# Equality endpoints via symbolic reduction of N.
def evaluate_gamma(gvalue):
    out={}
    for (pd,ge),coef in N.items():
        out[pd]=out.get(pd,F(0))+coef*gvalue**ge
    return {k:v for k,v in out.items() if v}
assert evaluate_gamma(-1)=={0:F(1152)}
assert {(ex[1],coeff) for ex,coeff in N.items() if ex[0]==0}=={(3,F(-1152))}
print('Endpoint gamma=-1: H=1 for every p; p=0: H=-gamma^3; p=2 from Caratheodory rigidity')
# Exact determinant identity for rational two-pole extremizers, a=xi+eta and b=xi*eta.
a=variable(2,0);b=variable(2,1)
A2=scale(a,-1)
A3=add(power(a,2,2),b)
A4=scale(add(power(a,3,2),scale(mul(a,b),3)),-1)
A5=add(power(a,4,2),scale(mul(power(a,2,2),b),6),scale(power(b,2,2),2))
H=add(scale(mul(mul(A2,A3),A4),2),scale(power(A3,3,2),-1),scale(power(A4,2,2),-1),mul(A3,A5),scale(mul(power(A2,2,2),A5),-1))
assert H==power(b,3,2)
print('Direct inverse-series determinant identity H_{3,1}=b^3: checked exactly')
print('CERTIFICATE PASS')
