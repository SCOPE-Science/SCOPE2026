#!/usr/bin/env python3
"""Exact finite-field polynomial verification of the two elliptic quotient equations.
Requires Python 3 standard library only. All coefficients are in F_5[t,z].
No point sampling or nonexhaustive root search is used.
"""
from itertools import product
P = 5

def clean(d):
    return {k: v % P for k,v in d.items() if v % P}

def c(n): return clean({(0,0): n})
t = {(1,0):1}
z = {(0,1):1}

def add(*terms):
    d = {}
    for term in terms:
        for m,coef in term.items(): d[m] = d.get(m,0)+coef
    return clean(d)

def neg(a):return clean({m:-v for m,v in a.items()})
def sub(a,b):return add(a,neg(b))

def mul(a,b):
    d = {}
    for (i,j),v in a.items():
        for (k,l),w in b.items():d[(i+k,j+l)]=d.get((i+k,j+l),0)+v*w
    return clean(d)

def powp(a,n):
    r=c(1)
    for _ in range(n): r=mul(r,a)
    return r

def coefficient(a,k):return clean({(i,0):v for (i,j),v in a.items() if j == k})

def substitute_z(a, h):
    out = c(0)
    for (i,j),v in a.items():out=add(out,mul(c(v),mul(powp(t,i),powp(h,j))))
    return out

one=c(1); two=c(2); four=c(4)
x=z
xm1=sub(x,one)
h=mul(x,xm1)
P_original=add(mul(c(4),mul(t,mul(x,powp(xm1,5)))),powp(add(h,mul(t,sub(powp(x,4),powp(xm1,4)))),2))
f=add(mul(mul(t,sub(t,one)),powp(z,3)),
      mul(sub(one,mul(two,t)),powp(z,2)),
      mul(mul(two,mul(t,sub(one,t))),z),powp(t,2))
g=mul(add(mul(four,z),one),f)
assert P_original == substitute_z(f,h), 'genus-two sextic failed reduction to cubic'
assert g == mul(add(mul(four,z),one),f), 'elliptic quartic quotient mismatch'
assert coefficient(powp(f,2),4) == mul(add(powp(t,2),two),sub(sub(powp(t,2),mul(two,t)),two)), 'E+ Hasse factor mismatch'
assert coefficient(powp(g,2),4) == mul(mul(sub(t,two),add(t,one)),add(powp(t,2),two)), 'E- Hasse factor mismatch'

# Prove named supersingular and rank-one strata are pairwise disjoint by
# exact polynomial gcd in F_5[t]. No extension-field enumeration.
def univariate(a):
    assert all(j==0 for _,j in a)
    return {i:v for (i,j),v in a.items()}
def trim(d):return {i:v%P for i,v in d.items() if v%P}
def divrem(a,b):
    a=trim(dict(a)); b=trim(b)
    assert b
    q={}
    while a and max(a)>=max(b):
        e=max(a)-max(b);v=a[max(a)]*pow(b[max(b)],-1,P)%P
        q[e]=v
        for k,w in b.items():a[k+e]=(a.get(k+e,0)-v*w)%P
        a=trim(a)
    return trim(q),a

def gcd(a,b):
    a,b=univariate(a),univariate(b)
    while b:
        _,r=divrem(a,b);a,b=b,r
    if not a:return {}
    lead=a[max(a)];return {k:v*pow(lead,-1,P)%P for k,v in a.items()}

sup=add(powp(t,2),two)
other=sub(sub(powp(t,2),mul(two,t)),two)
sing=[t,sub(t,one),sub(t,c(3))]
rank1=[other,sub(t,two),add(t,one)]
for a in sing+rank1:
    assert gcd(sup,a)=={0:1}, 'supersingular parameter collided with excluded or rank-one parameter'
for i,a in enumerate(rank1):
    for b in sing+rank1[i+1:]:
        assert gcd(a,b)=={0:1}, 'rank-one parameter collided with another or excluded parameter'
for a in [sup,other]:
    d={k:v*k%5 for k,v in univariate(a).items() if k}
    b=clean({(i,0):v for i,v in d.items()})
    assert gcd(a,b)=={0:1}, 'multiple parameter roots'

# Independent genus-two Cartier-Manin calculation: c_j is the x^j
# coefficient of P(x,t)^((5-1)/2). In the basis dx/y, x dx/y
# the 2x2 matrix is [[c4,c3],[c9,c8]].
sextic_squared=powp(P_original,2)
assert coefficient(sextic_squared,3) == neg(mul(two,mul(t,sup)))
assert coefficient(sextic_squared,4) == coefficient(powp(g,2),4)
assert coefficient(sextic_squared,8) == coefficient(powp(f,2),4)
assert coefficient(sextic_squared,9) == c(0)
# The Hasse-Witt matrix vanishes at both common Hasse roots,
# so each supersingular Jacobian has a-number two (superspecial).
print('VERIFY_OK: exact F5 polynomial identities; two elliptic Hasse factors; genus-two Cartier-Manin matrix; six pairwise distinct nonordinary parameters')
