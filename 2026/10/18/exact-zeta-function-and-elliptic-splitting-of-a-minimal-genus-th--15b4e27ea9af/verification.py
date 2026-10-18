#!/usr/bin/env python3
"""Exact finite-field counts for a smooth genus-three curve. Python standard library only."""
from itertools import product
P = (1, 1, 4, 9, 12, 9, 27)
# Irreducible defining polynomials over F_3, coefficients low to high.
MOD = {1:(0,1), 2:(1,0,1), 3:(1,0,2,1),
       4:(1,0,1,1,1), 5:(1,0,0,0,2,1)}

def poly_mod(a,b):
    v=list(a)
    while len(v)>=len(b):
        d=len(v)-len(b); c=v[-1]*pow(b[-1],-1,3)%3
        for i,z in enumerate(b):v[d+i]=(v[d+i]-c*z)%3
        v.pop()
    return v

def assert_irreducible(mod):
    n=len(mod)-1
    for degree in range(1,n//2+1):
        for v in product(range(3),repeat=degree):
            if not any(poly_mod(mod,v+(1,))):
                raise AssertionError('reducible field modulus')

def count(n):
    mod=MOD[n]; assert_irreducible(mod)
    z=(0,)*n; one=(1,)+(0,)*(n-1)
    def add(a,b):return tuple((x+y)%3 for x,y in zip(a,b))
    def mul(a,b):
        v=[0]*(2*n-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):v[i+j]+=x*y
        for d in range(2*n-2,n-1,-1):
            c=v[d]%3
            for i in range(n):v[d-n+i]-=c*mod[i]
        return tuple(w%3 for w in v[:n])
    def power(a,k):
        v=one
        while k:
            if k&1:v=mul(v,a)
            a=mul(a,a); k//=2
        return v
    good=0
    for x in product(range(3),repeat=n):
        if x==z:continue
        value=add(add(mul(x,x),x),power(x,3**n-2))
        trace=z; term=value
        for _ in range(n):
            trace=add(trace,term); term=power(term,3)
        assert trace[1:]==(0,)*(n-1)
        if trace==z:good+=1
    return good,2+3*good

def mult(a,b):
    v=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):v[i+j]+=x*y
    return tuple(v)

assert mult(mult((1,-1,3),(1,-1,3)),(1,3,3))==P
counts=[count(n) for n in range(1,6)]
assert counts==[(1,5),(5,17),(14,44),(25,77),(51,155)],counts
s=[]
for n in range(1,6):
    z=-n*P[n]-sum(P[j]*s[n-j-1] for j in range(1,n))
    s.append(z)
    assert counts[n-1][1]==3**n+1-z
assert sum(P)==63
for coeffs,wanted in [((1,1,0,2),3),((1,0,2,1),7)]:
    # Coefficients specify u^3+a*u^2+b*u+c, constant written last.
    _,a,b,c=coeffs
    assert 1+sum(y*y%3==(x**3+a*x*x+b*x+c)%3
                 for x in range(3) for y in range(3))==wanted
print('VERIFIED: n=1..5 point counts',counts,'Weil numerator',P,'Jacobian order',sum(P))
