#!/usr/bin/env python3
"""Exact polynomial audit for weighted-disk Bergman zero bifurcation.

No external packages. Polynomial tuples store ascending powers of a real
parameter, with exact integer coefficients. In particular, tests below
are algebraic identities, not finite-parameter interpolation.
"""
from math import comb

def const(a): return (a,)
def lin(a, b=1): return (a,b)
def trim(p):
    z=list(p)
    while len(z)>1 and z[-1]==0:z.pop()
    return tuple(z)
def add(a,b):return trim(tuple((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))))
def neg(a):return tuple(-i for i in a)
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)
def scale(a,c):return trim(tuple(c*x for x in a))
def prod(*f):
    a=const(1)
    for b in f:a=mul(a,b)
    return a

def numerator(q):
    d=q+1
    b=[prod(*(lin(k+h) for h in range(1,d+1))) for k in range(d+1)]
    return [sum_poly([scale(b[k],(-1)**(j-k)*comb(d+1,j-k)) for k in range(j+1)]) for j in range(d+1)]
def sum_poly(ps):
    a=const(0)
    for p in ps:a=add(a,p)
    return a

def cayley(q):
    d=q+1
    pp=numerator(q)
    out=[]
    # Coefficient of s^k in P((s-1)/(s+1))*(s+1)^d
    for k in range(d+1):
        coefficients=[]
        for j in range(d+1):
            c=sum(comb(j,u)*(-1)**(j-u)*comb(d-j,k-u) for u in range(max(0,k-(d-j)),min(j,k)+1))
            coefficients.append(scale(pp[j],c))
        out.append(sum_poly(coefficients))
    return out

L=lambda a:lin(a)
M=lambda *args:prod(*args)
W={q:cayley(q) for q in range(5)}
for q in range(5):
    for i,a in enumerate(W[q]):assert len(a)<=q+2, ('degree bound',q,i)

# Small degrees: all Cayley roots are in the open left half plane.
assert W[0]==[add(scale(L(0),2),const(1)),const(1)]
assert W[1][2]==const(2)
assert W[1][1]==scale(L(1),4)
assert W[1][0]==scale((1,4,2),2)

# Cubic and quartic Routh first-column identities.
for q in [2,3]:
    a=list(reversed(W[q]))
    if q==2:
        b1=scale(M(L(1),L(2)),8)
    else:
        b1=scale(M(lin(3,2),lin(5,2)),8)
    assert mul(b1,a[1])==sub(mul(a[1],a[2]),mul(a[0],a[3]))
    if q==3:
        cn=scale(M(L(1),L(2),L(3),(6,4,1)),32)
        cd=M(lin(3,2),lin(5,2))
        assert mul(mul(cd,sub(mul(b1,a[3]),mul(a[1],a[4]))),const(1))==mul(b1,cn)

# Quintic Routh polynomial identities. q=4 and real m>=0.
a=list(reversed(W[4]))
b1=scale(M(L(2),L(3)),160)
b2=scale(M(L(2),L(3),(3,10,2)),32)
c1=scale(M(lin(3,2),lin(5,2),lin(7,2)),8)
dn=scale(M(lin(-1),L(1),L(2),L(3),L(4),L(6)),-64)
dd=M(lin(3,2),lin(7,2))
assert mul(b1,a[1])==sub(mul(a[1],a[2]),mul(a[0],a[3]))
assert mul(b2,a[1])==sub(mul(a[1],a[4]),mul(a[0],a[5]))
assert mul(c1,b1)==sub(mul(b1,a[3]),mul(a[1],b2))
assert mul(dd,sub(mul(c1,b2),mul(b1,a[5])))==mul(c1,dn)

# Special boundary factorization at m=1:
# Q(s)=120(s+3)(s^2+3)(s^2+4s+7).
symbolic=M((3,1),(3,0,1),(7,4,1))
q1=[sum(a_i*(1**i) for i,a_i in enumerate(p)) for p in W[4]]
assert q1==list(scale(symbolic,120))

# Numeric locations supplement, but do not replace, the exact identities.
# A direct finite series tests a few q,m cases inside the convergence disk.
for q,m in [(0,0),(2,4),(3,2),(4,0),(4,1),(4,2),(4,3)]:
    coeff=numerator(q)
    for x in [0.0,0.15,0.41,-0.2]:
        p=sum(sum(c_j*m**j for j,c_j in enumerate(c))*x**k for k,c in enumerate(coeff))
        lhs=p/(1-x)**(q+2)
        rhs=sum((__import__('math').prod(n+m+h for h in range(1,q+2)))*x**n for n in range(100))
        assert abs(lhs-rhs)<2e-7*max(1,abs(rhs))
print('BERGMAN_ROUTH_EXACT_POLYNOMIAL_IDENTITIES_OK')
