#!/usr/bin/env python3
"""Exact characteristic-seven checks for the Klein plane quartic degeneration.
Requires SymPy. All coefficient comparisons are in GF(7), not floating point.
"""
import sympy as S
from itertools import combinations_with_replacement
from sympy.polys.domains import GF
from sympy.polys.matrices import DomainMatrix

u, x, y, z = S.symbols('u x y z')
p = 7
P = lambda expr: S.Poly(S.expand(expr), u, modulus=p)
rank = lambda mat: DomainMatrix.from_Matrix(mat).convert_to(GF(p)).rank()
X = 2*u**4+u**2-2*u+2
Y = 4*u**4+u**2+3*u+1
Z = u**4+u**2-u+4
F = x**3*y+y**3*z+z**3*x
assert P(F.subs({x:X,y:Y,z:Z})) == S.Poly(0,u,modulus=p)
# Coordinates span exactly W=span(1,u^2,u^4+6u), with no basepoints.
coeff = S.Matrix([[int(P(q).coeff_monomial(u**j))%p for q in (X,Y,Z)] for j in (0,2,4)])
assert rank(coeff) == 3
for q in (X,Y,Z):
    pq=P(q)
    assert pq.coeff_monomial(u**3) == 0
    assert (pq.coeff_monomial(u)-6*pq.coeff_monomial(u**4))%p == 0
# Quadrics in the three coordinate sections are linearly independent.
monomials=[a*b for a,b in combinations_with_replacement((X,Y,Z),2)]
M=S.Matrix([[int(P(q).coeff_monomial(u**j))%p for q in monomials] for j in range(9)])
assert rank(M) == 6
# Singular affine scheme has one geometric support point.
f=F.subs({z:1}); gx=S.diff(f,x);gy=S.diff(f,y)
G=S.groebner([f,gx,gy],x,y,order='lex',modulus=p)
assert [str(a.as_expr()) for a in G.polys] == ['x - 2*y**3', 'y**7 + 3']
# The only points at infinity on F are [1:0:0] and [0:1:0], both smooth.
for triple in [(1,0,0),(0,1,0)]:
    assert any(int(S.diff(F,var).subs(dict(zip((x,y,z),triple))))%7 for var in (x,y,z))
# Local orders in the normalization coordinate q=t/s near [s:t]=[1:0].
N=12
zero=[0]*N
def plus(a,b):return [(a[i]+b[i])%p for i in range(N)]
def minus(a,b):return [(a[i]-b[i])%p for i in range(N)]
def scale(a,n):return [v*n%p for v in a]
def prod(a,b):return [sum(a[j]*b[i-j] for j in range(i+1))%p for i in range(N)]
def inverse(a):
    out=[0]*N;out[0]=pow(a[0],-1,p)
    for i in range(1,N):out[i]=(-out[0]*sum(a[j]*out[i-j] for j in range(1,i+1)))%p
    return out
A=[2,0,1,-2,2]+[0]*(N-5)
B=[4,0,1,3,1]+[0]*(N-5)
C=[1,0,1,-1,4]+[0]*(N-5)
invC=inverse(C)
v=prod(minus(B,scale(C,4)),invC)
w=minus(prod(minus(A,scale(C,2)),invC),scale(v,5))
h=minus(minus(w,scale(prod(v,v),3)),scale(prod(prod(v,v),v),2))
order=lambda coeff:next(i for i,a in enumerate(coeff) if a)
assert (order(v),v[2],order(w),w[4],order(h),h[7])==(2,4,4,6,7,1)
# The cusp preimage is unique: the two affine equations have no common root.
assert S.gcd(P(X-2*Z),P(Y-4*Z)).degree() == 0
# The coordinate cyclic permutation is the order-three scaling u -> 4u.
for a,b in ((X,2*Y),(Y,2*Z),(Z,2*X)):
    assert P(a.subs(u,4*u)-b)==S.Poly(0,u,modulus=p)
# Every affine linear reparametrization preserving the cusp and W has b=0,
# then a^3=1: coefficient of u^3 in (a*u+b)^4 is 4*a^3*b.
assert [j for j in range(1,7) if pow(j,3,7)==1]==[1,2,4]
print('KLEIN_CHAR7_NORMALIZATION_A6_PROJECTIVE_C3_CERTIFIED')
