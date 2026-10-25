"""Exhaustive first-level differential-row tests for the sparse polynomial P_{5,3}.
Run: python3 check_exceptional_row.py.  Standard library only.
The characteristic-four ring is Z_4[t]/(t^5+t^2+1), with binary
reduction irreducible, hence the ring is GR(4,5).
The general theorem requires the separate algebraic proof.
"""
from collections import Counter
from random import Random

# Exact GF(2) polynomial tests for the required exceptional identity.
def exponents(m,r):
    v=[1<<i for i in range(r-2)]
    w=1<<(r-2)
    y=1<<(m-2)
    z=1<<(m-1)
    out=set()
    for e in v+[w]+[w+t for t in v]+[w+y,w+z]+[y+t for t in v]+[y+z]:
        if e in out: out.remove(e)
        else: out.add(e)
    return out

def delta1_poly(exps):
    out=set()
    for e in exps:
        t=e
        while True:
            # k is submask of e iff binomial(e,k) odd.
            if t!=e:
                if t in out:out.remove(t)
                else:out.add(t)
            if t==0:break
            t=(t-1)&e
    return out

def derivative(exps):
    return {e-1 for e in exps if e&1}

from math import gcd
for m in (5,7,9,11):
    for r in range(3,m,2):
        if gcd(r,m)>1:continue
        es=exponents(m,r)
        assert len(es)==3*r-2
        assert delta1_poly(es)==derivative(es)=={0,1<<(r-2),1<<(m-2)}
print('Exact polynomial identities verified for all admissible m<=11.')

M=5
SIZE=4**M

def vec(x):
    return [(x>>(2*i)) & 3 for i in range(M)]
def ind(v):
    return sum((v[i]&3)<<(2*i) for i in range(M))
def add(x,y):
    return ind([(x>>(2*i)&3)+(y>>(2*i)&3) for i in range(M)])
def mul(x,y):
    a,b=vec(x),vec(y)
    c=[0]*9
    for i in range(M):
        for j in range(M):
            c[i+j]+=a[i]*b[j]
    for k in range(8,4,-1):
        z=c[k]
        c[k-5]-=z
        c[k-3]-=z
    return ind(c)

def poly_eval(coeffs,x):
    p=0
    for c in reversed(coeffs):
        p=add(mul(p,x),c)
    return p

def row_check(coeffs):
    values=[poly_eval(coeffs,x) for x in range(SIZE)]
    # All 32 lift choices of residue direction 1 (a=1+2u).
    for u in range(32):
        a=add(1,ind([2*((u>>i)&1) for i in range(M)]))
        counts=Counter(add(values[add(x,a)],neg(values[x])) for x in range(SIZE))
        assert len(counts)==16 and set(counts.values())=={64}, (a,counts)

def neg(x):
    return ind([-c for c in vec(x)])

# P_{5,3}(X)=X+X^2+X^3+X^9+X^10+X^18+X^24.
exps=(1,2,3,9,10,18,24)
coeffs=[0]*25
for e in exps:
    coeffs[e]=1
assert add(1,1)==2 and mul(1,4)==4
# t^5=-t^2-1 in this quotient.
t=4
p=1
for _ in range(5):
    p=mul(p,t)
assert p==neg(add(1,16))
row_check(coeffs)
print('Canonical coefficients: all 32 exceptional unit rows have sixteen cells of multiplicity 64.')

rng=Random(20261018)
for seed in range(2):
    cc=list(coeffs)
    for j in range(len(cc)):
        if rng.randrange(2):
            cc[j]=add(cc[j],2)
    row_check(cc)
    print(f'Coefficient lift {seed+1}: all 32 exceptional unit rows verified.')
print('CERTIFICATE_OK')
