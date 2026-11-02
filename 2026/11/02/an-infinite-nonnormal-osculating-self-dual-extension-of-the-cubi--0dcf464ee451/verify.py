#!/usr/bin/env python3
"""Exact supplementary algebraic checks for a family of monomial surfaces.
The uniform theorem is proved in RESULT.md; finite specialization is not its proof.
Requires sympy >= 1.10; run python verify.py.
"""
import sympy as S
from math import factorial
D=S.symbols('d',integer=True)
E=[(D-1,1),(D-1,0),(1,D-1),(0,D-1),(1,0),(0,1)]
sign=S.Matrix([-1,1,1,-1,-1,1])
jet=S.Matrix([[1 for a,b in E],
[a for a,b in E],[b for a,b in E],
[a*(a-1)/2 for a,b in E],
[a*b for a,b in E],
[b*(b-1)/2 for a,b in E]])
assert all(S.cancel(v)==0 for v in jet*sign)
minor=S.factor(jet.extract([0,1,2,3,4],[0,1,2,4,5]).det())
assert S.factor(minor/(D-2)**2/(D-1)**2) in [S.Rational(1,2),-S.Rational(1,2)]
print('JET_OK: rank 5 and unique constant-sign kernel for all integer d>=3')
x,y,z=S.symbols('x y z')
for n in range(3,14):
    f=-x**(n-1)*y+x**(n-1)*z+x*y**(n-1)-y**(n-1)*z-x*z**(n-1)+y*z**(n-1)
    h=sum(x**i*y**j*z**(n-3-i-j) for i in range(n-2) for j in range(n-2-i))
    assert S.expand(f+(x-y)*(x-z)*(y-z)*h)==0
print('CONTACT_OK: alternating polynomial factors, tested degrees 3 through 13')
for n in range(3,14):
    V=[(0,1),(1,0),(n-1,0),(n-1,1),(1,n-1),(0,n-1)]
    area2=abs(sum(V[i][0]*V[(i+1)%6][1]-V[i][1]*V[(i+1)%6][0] for i in range(6)))
    assert area2==n*n-3
    from math import gcd
    edge=[gcd(abs(V[(i+1)%6][0]-V[i][0]),abs(V[(i+1)%6][1]-V[i][1])) for i in range(6)]
    assert sorted(edge)==sorted([1,1,1,n-2,n-2,n-2])
print('POLYGON_OK: normalized area d^2-3 and edge length pattern 1,d-2')
for n in range(4,14):
    a,b=n-2,n-1
    gaps=[j for j in range(a*b) if not any(j==a*r+b*s for r in range(j//a+1) for s in range(j//b+1))]
    assert len(gaps)==(a-1)*(b-1)//2
print('DELTA_OK: numerical semigroup gap counts for degrees 4 through 13')
print('VERIFY_OK')
