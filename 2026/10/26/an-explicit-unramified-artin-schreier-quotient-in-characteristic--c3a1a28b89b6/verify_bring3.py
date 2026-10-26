#!/usr/bin/env python3
"""Exact polynomial checks for the characteristic-three Bring complete intersection.

Requires Python 3 and SymPy. Infinite geometric arguments are supplied separately.
"""
from itertools import combinations, product
import sympy as sp

p=3
u,v,a,b,c,T,r,s=sp.symbols('u v a b c T r s')
def ff(poly,*variables):
    return sp.Poly(sp.expand(poly),*variables,modulus=3).as_expr()
def is_zero(poly,*variables):
    assert ff(poly,*variables)==0,(poly,ff(poly,*variables))

A=u+v
B=u*u+u*v+v*v
C=(u+v)*(u*u+v*v)
D=-u**6+u**4*v**2+u**3*v**3+u**2*v**4-v**6
P=T**3+A*T*T+B*T+C
is_zero(sp.discriminant(P,T)-D,u,v)
is_zero(A*A*B*B-B**3-A**3*C-D,u,v)
# The full five-variable defining equations and the triple's eliminants.
V=[a,b,c,u,v]
e1=sum(V)
e2=sum(V[i]*V[j] for i,j in combinations(range(5),2))
e3=sum(V[i]*V[j]*V[k] for i,j,k in combinations(range(5),3))
s1=a+b+c
s2=a*b+b*c+c*a
s3=a*b*c
is_zero(e1-(s1+A),a,b,c,u,v)
is_zero(e2-(s2+s1*A+u*v),a,b,c,u,v)
is_zero(e3-(s3+s2*A+s1*u*v),a,b,c,u,v)
is_zero(B-(A*A-u*v),u,v)
# In the quotient e1=e2=e3, s1=-A, s2=B, s3=-A*(u²+v²).
assert ff(D.subs({u:T,v:1}),T) == -T**6+T**4+T**3+T**2-1
f=sp.Poly(D.subs({u:T,v:1}),T,modulus=3)
assert sp.gcd(f,f.diff()).degree()==0
assert [int(f.eval(i))%3 for i in range(3)]==[2,1,2]
# Hyperelliptic Cartier--Manin matrix, i,j=1,2; f^( (p-1)/2 )=f.
coeff={int(m[0]):int(k)%3 for m,k in f.terms()}
H=[[coeff.get(3*i-j,0) for j in (1,2)] for i in (1,2)]
assert H==[[1,0],[0,1]],H
# Cyclic permutation (a,b,c)->(b,c,a) translates z=(a-b)/A by 1.
W=(a-b)*(b-c)*(c-a)
is_zero(W-((a-b)**3-(a-b)*(-a-b-c)**2),a,b,c)
is_zero((b-c)-(a-b)-(-a-b-c),a,b,c)
# For 5 coordinates, the Jacobian columns on e1=e2=e3 are (1,-xi,xi²).
# Rank drop iff the 5 xi assume at most two values. Inspect multiplicities.
for m in (1,2):
    vals=[r]*m+[s]*(5-m)
    h1=sum(vals)
    h2=sum(vals[i]*vals[j] for i,j in combinations(range(5),2))
    h3=sum(vals[i]*vals[j]*vals[k] for i,j,k in combinations(range(5),3))
    if m==1:
        is_zero(h1.subs(r,-s),s)
        assert ff(h2.subs(r,-s),s)==-s**2
    else:
        is_zero(h1.subs(r,0),s)
        is_zero(h2.subs(r,0),s)
        assert ff(h3.subs(r,0),s)==s**3
# The map [u:v] has no base point on the complete intersection.
# With u=v=0, e1 gives c=-a-b, e3=abc; any zero coordinate forces e2 !=0 unless all zero.
E2=ff(e2.subs({u:0,v:0,c:-a-b}),a,b)
E3=ff(e3.subs({u:0,v:0,c:-a-b}),a,b)
assert E2==ff(-a*a-a*b-b*b,a,b)
assert E3==ff(-a*b*(a+b),a,b)
# Rational points: a small independent finite sanity check, not an infinite proof.
count=0
for coords in product(range(3),repeat=5):
    if not any(coords): continue
    first=next(z for z in coords if z)
    if first!=1: continue
    if (sum(coords)%3==0 and sum(coords[i]*coords[j] for i,j in combinations(range(5),2))%3==0
        and sum(coords[i]*coords[j]*coords[k] for i,j,k in combinations(range(5),3))%3==0):
        count+=1
assert count==0
print('VERIFY_OK: exact discriminant, Artin--Schreier relation, smoothness cases, base-point exclusion, ordinary quotient')
