"""Exact symbolic and integer checks for cubic spherical-harmonic sampling on type-A roots."""
from fractions import Fraction
from itertools import combinations
import sympy as s

m = s.symbols('m', integer=True, positive=True)
d = m - 1
kernel = lambda t: s.factor(d * (d + 4) * ((d + 2) * t**3 - 3 * t) / 6)
k = s.factor(kernel(s.Integer(1)))
a = s.factor(kernel(s.Rational(1, 2)))
cycle = s.factor(k-2*a)
grad = s.factor(k+(m-2)*a)
assert s.simplify(k - (m-1)*(m-2)*(m+3)/6) == 0
assert s.simplify(a - (m-1)*(m+3)*(m-11)/48) == 0
assert s.simplify(cycle - (m-1)*(m+1)*(m+3)/8) == 0
assert s.simplify(grad - (m-1)*(m-2)*(m-3)*(m+3)/48) == 0
assert s.factor(grad-cycle) == m*a
assert s.factor((m-2)*(m-3)-6*(m+1)) == m*(m-11)
checks=6

for n in list(range(4, 21))+[23, 29]:
    edges=list(combinations(range(n),2))
    N=len(edges)
    B=s.zeros(n,N)
    for z,(i,j) in enumerate(edges):
        B[i,z]=1; B[j,z]=-1
    assert B*B.T == n*s.eye(n)-s.ones(n,n)
    checks+=1
    P=B.T*B/s.Integer(n)
    assert P*P==P
    checks+=1
    kn=s.Rational(int(k.subs(m,n)))
    an=s.Rational(a.subs(m,n))
    c=s.Rational(cycle.subs(m,n));g=s.Rational(grad.subs(m,n))
    G=(kn-2*an)*s.eye(N)+an*B.T*B
    assert G==c*(s.eye(N)-P)+g*P
    checks+=1
    assert c>0 and g>0
    checks+=1
    # Exact nontrivial interpolant and minimum-norm identity.
    y=s.Matrix([s.Rational((7*i*i+3*i+1)%(2*n+3),1+(i%4)) for i in range(N)])
    v=(s.eye(N)-P)*y/c+P*y/g
    assert G*v==y
    checks+=1
    assert s.expand((y.T*v)[0]-((y.T*(s.eye(N)-P)*y)[0]/c+(y.T*P*y)[0]/g))==0
    checks+=1
    # Check sampled polynomial kernel against its incidence Gram entrywise.
    if n<=14 or n==11:
        for u,(i,j) in enumerate(edges):
            for w,(h,l) in enumerate(edges):
                t=s.Rational(int(i==h)-int(i==l)-int(j==h)+int(j==l),2)
                assert s.simplify(kernel(t).subs(m,n)-G[u,w])==0
                checks+=1
    if n==11:
        assert G==210*s.eye(55)
        checks+=1
assert (grad/cycle).subs(m,11)==1
checks+=1
print(f'PASS {checks} checks; symbolic two-sector Gram, exact projector/interpolation, unique tight m=11')
