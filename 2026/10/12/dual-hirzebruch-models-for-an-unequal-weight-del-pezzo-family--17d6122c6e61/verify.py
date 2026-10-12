#!/usr/bin/env python3
"""Exact bookkeeping checks for the dual Hirzebruch resolution formulas.

This script does not replace the geometric proof.  It verifies the polynomial
identities used for self-intersections and birational invariants.
"""

from fractions import Fraction

# Tiny polynomial ring Q[n,m], represented by {(i,j): coefficient}.
def add(p, q):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, Fraction(0)) + v
        if not r[k]:
            del r[k]
    return r

def neg(p):
    return {k: -v for k, v in p.items()}

def sub(p, q):
    return add(p, neg(q))

def mul(p, q):
    r = {}
    for (i,j), a in p.items():
        for (k,l), b in q.items():
            key = (i+k, j+l)
            r[key] = r.get(key, Fraction(0)) + a*b
    return {k:v for k,v in r.items() if v}

def const(c): return {(0,0): Fraction(c)} if c else {}
n = {(1,0): Fraction(1)}
m = {(0,1): Fraction(1)}
one = const(1)
two = const(2)
eight = const(8)

a = add(n, one)
b = add(m, one)
d = add(add(n, m), two)

assert sub(d, add(a,b)) == {}
# Blow up d points on the +b section of F_b: b-d=-a.
assert sub(sub(b,d), neg(a)) == {}
# Equivalently, on the resolution E_z starts at -a and gains d after
# contracting the d components that meet it.
assert sub(add(neg(a),d), b) == {}
# Symmetric model.
assert sub(add(neg(b),d), a) == {}
# The surviving component of a reducible fiber changes -1 -> 0.
assert Fraction(-1) + Fraction(1) == 0
# Birational invariants.
rho = add(two,d)
assert sub(rho, add(add(n,m), const(4))) == {}
K2 = sub(eight,d)
assert sub(K2, sub(const(6), add(n,m))) == {}

print('VERIFY_OK')
