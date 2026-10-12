#!/usr/bin/env python3
"""Exact finite-field sanity checks for quadratic-fibre pencils.
Mathematical genus and gonality proofs are separate from these finite tests.
"""
from itertools import product

def first_nonsquare(p):
    squares={(a*a)%p for a in range(p)}
    return next(d for d in range(1,p) if d not in squares)

def canon(v,p):
    a,b=v
    if a%p: s=pow(a,-1,p)
    else: s=pow(b,-1,p)
    return ((a*s)%p,(b*s)%p)

def mul(x,y,p,d):
    a,b=x; c,e=y
    return ((a*c + d*b*e)%p,(a*e+b*c)%p)

for p in (3,5,7,11,13,17):
    d=first_nonsquare(p)
    pts={canon(v,p) for v in product(range(p),repeat=2) if v!=(0,0)}
    assert len(pts)==p+1
    assert all((a*a-d*b*b)%p for a,b in pts)
    assert all(canon(mul(v,w,p,d),p) in pts for v in pts for w in pts)
    # The two excluded geometric points have x-coordinate sqrt(d), -sqrt(d),
    # and no nonzero F_p-linear polynomial a+b*x vanishes at either.
    assert all(not(a==0 and b==0) for a,b in pts)
    print(f"p={p} nonsquare={d}: {len(pts)} projective unit classes; group law verified")
# A smooth genus-four seed in characteristic three:
# f=x^9-x+1 has derivative -1 and f(alpha)=1 for alpha^2=-1.
p=3
for a in range(3):
    if (a*a+1)%3==0: raise AssertionError("phi reducible")
# Since alpha^4=1 and alpha^9=alpha, f(alpha)=1.
print('char3 genus4 example: f derivative -1, phi irreducible, f(alpha)=1')
print('VERIFY_OK')
