#!/usr/bin/env python3
"""Exact independent finite-field checks for diagonal double sextic K3 models."""
from itertools import product
from collections import Counter

P = 5
K = [(a,b) for a in range(P) for b in range(P)]
ZERO = (0,0)
ONE = (1,0)

def add(x,y): return ((x[0]+y[0])%P,(x[1]+y[1])%P)
def mul(x,y): return ((x[0]*y[0]+2*x[1]*y[1])%P,(x[0]*y[1]+x[1]*y[0])%P)
def powk(x,n):
    out=ONE
    while n:
        if n&1: out=mul(out,x)
        x=mul(x,x);n//=2
    return out

def canonical(q):
    z=q[0] if isinstance(q[0],tuple) else 0
    if isinstance(q[0],tuple):
        mulf, invf, one, zero=mul,lambda a:powk(a,23),ONE,ZERO
    else:
        mulf, invf, one, zero=lambda x,y:x*y%5,lambda x:pow(x,3,5),1,0
    for pos in range(3):
        if q[pos]!=zero:
            k=invf(q[pos]);return tuple(mulf(t,k) for t in q)
    raise AssertionError('Zero vector')

base5=sorted({canonical(q) for q in product(range(5), repeat=3) if any(q)})
assert len(base5)==31
# On F5, x^6 = x^2. For each [x:y:z], the fiber has 1+chi((a*x^6+b*y^6+c*z^6)/d) rational points.
def n5(a,b,c,d):
    return sum(sum((d*w*w-a*x**6-b*y**6-c*z**6)%5==0 for w in range(5))
               for x,y,z in base5)
assert sum(pow(x,6,5)==pow(x,2,5) for x in range(5))==5
counts=Counter()
for a,b,c,d in product(range(1,5),repeat=4):
    n=n5(a,b,c,d)
    split=pow(a*b*c*d%5,2,5)==1
    assert n==(36 if split else 26),(a,b,c,d,n)
    counts[(split,n)]+=1
assert counts=={(True,36):128,(False,26):128}, counts
# Independent GF25 extension enumeration for all representative classes.
assert all(powk((x,0),24)==ONE for x in range(1,5))
sixth={powk(u,6) for u in K if u!=ZERO}
assert sixth=={(x,0) for x in range(1,5)},sixth
# Note square roots of every F5* lie in F25.
assert {(x,0) for x in range(1,5)} <= {mul(z,z) for z in K}
base25=sorted({canonical(q) for q in product(K, repeat=3) if any(t!=ZERO for t in q)})
assert len(base25)==651
squares=Counter(mul(w,w) for w in K)
def n25(a,b,c,d):
    invd=powk((d,0),23)
    ret=0
    for x,y,z in base25:
        s=add(add(mul((a,0),powk(x,6)),mul((b,0),powk(y,6))),mul((c,0),powk(z,6)))
        s=mul(s,invd)
        ret+=squares[s]
    return ret
for coeff in ((1,1,1,1),(2,1,1,1),(2,3,4,1),(4,4,4,4)):
    nn=n25(*coeff)
    assert nn==1176,(coeff,nn)
print('VERIFY_OK: all 256 coefficient quadruples over F5 split into 128 of N1=36 and 128 of N1=26; all 256 Frobenius parity cases; GF25 sixth-power and square-root descent; projective F25 count N2=1176 for four contrasting models.')
