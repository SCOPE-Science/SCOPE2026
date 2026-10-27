#!/usr/bin/env python3
"""Exact finite-field checks for the characteristic-three Igusa-quartic Jacobian scheme.

Requires Python 3 and SymPy. All polynomial and matrix arithmetic relevant to the
claim is over GF(3); no floating-point arithmetic is used.
"""
from collections import defaultdict
from itertools import combinations
from math import comb
import sympy as sp

P = 3
x = sp.symbols("x0:5")
x5 = -sum(x)
xs = list(x) + [x5]
S2 = sum(z**2 for z in xs)
S4 = sum(z**4 for z in xs)
F = sp.expand(S2**2 - 4*S4)
G = [sp.diff(F, xi) for xi in x]  # derivatives of the restricted equation

def monomials_deg(n, d):
    if n == 1:
        yield (d,)
        return
    for a in range(d, -1, -1):
        for tail in monomials_deg(n-1, d-a):
            yield (a,) + tail

def rank_modp(rows, p=3):
    pivots = {}
    rank = 0
    for row in rows:
        r = {j: c % p for j, c in row.items() if c % p}
        while r:
            j = min(r)
            if j not in pivots:
                inv = pow(r[j], -1, p)
                pivots[j] = {k: (v*inv) % p for k, v in r.items() if v % p}
                rank += 1
                break
            pivot = pivots[j]
            fac = r[j]
            for k, v in pivot.items():
                nv = (r.get(k, 0) - fac*v) % p
                if nv:
                    r[k] = nv
                elif k in r:
                    del r[k]
    return rank

def pair_partitions(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    a = items[0]
    for j in range(1, len(items)):
        b = items[j]
        rest = items[1:j] + items[j+1:]
        for sub in pair_partitions(rest):
            yield ((a, b),) + sub

parts = []
for raw in pair_partitions(tuple(range(6))):
    part = tuple(sorted(tuple(sorted(pair)) for pair in raw))
    if part not in parts:
        parts.append(part)
assert len(parts) == 15

# In the chart x5=1 around P=(1:...:1), a line direction is +1 on
# one pair, -1 on another pair, and 0 on the pair containing index 5.
directions = []
for part in parts:
    C = next(pair for pair in part if 5 in pair)
    AB = [pair for pair in part if pair != C]
    A, B = sorted(AB)
    v5 = [0]*5
    for i in A:
        if i < 5: v5[i] = 1
    for i in B:
        if i < 5: v5[i] = -1
    assert sum(v5) % 3 == 0
    directions.append(tuple(v5[:4]))
# Distinct projective directions, including sign identification.
def projective_key(v, p=3):
    v = tuple(c % p for c in v)
    first = next(c for c in v if c)
    inv = pow(first, -1, p)
    return tuple((c*inv) % p for c in v)
assert len({projective_key(v) for v in directions}) == 15

def eval_rank(d):
    mons = list(monomials_deg(4, d))
    rows = []
    for v in directions:
        row = {}
        for j, alpha in enumerate(mons):
            val = 1
            for z, e in zip(v, alpha):
                val = (val * pow(z, e, P)) % P
            if val: row[j] = val
        rows.append(row)
    return rank_modp(rows, P)

direction_ranks = [eval_rank(d) for d in range(4)]
assert direction_ranks == [1, 4, 10, 15], direction_ranks

# Exact Groebner basis of the Jacobian ideal in GF(3)[x0,...,x4].
gb = sp.groebner(G, *x, modulus=3, order="grevlex")
lmexp = sorted(tuple(g.LM(order=gb.order).exponents) for g in gb.polys)
expected_lm = sorted([
    (0,2,1,3,0), (0,5,0,0,0), (0,2,3,0,0), (0,2,2,1,0),
    (1,3,0,0,0), (0,3,1,0,0), (1,1,2,0,0), (0,3,0,1,0),
    (1,1,1,1,0), (0,0,3,1,0), (3,0,0,0,0), (2,1,0,0,0),
    (2,0,1,0,0), (2,0,0,1,0)
])
assert lmexp == expected_lm, lmexp

# Hilbert numerator of a monomial ideal by inclusion-exclusion over lcms.
def lcm_exp(a, b):
    return tuple(max(u, v) for u, v in zip(a, b))
entries = [((0,)*5, 1)]
for m in lmexp:
    entries += [(lcm_exp(exp, m), -sgn) for exp, sgn in entries]
num = defaultdict(int)
for exp, sgn in entries:
    num[sum(exp)] += sgn
num = {d:c for d,c in sorted(num.items()) if c}
assert num == {0:1, 3:-4, 6:11, 7:-9, 9:1}, num

t = sp.symbols("t")
N = sum(c*t**d for d, c in num.items())
HJ = sp.cancel(N/(1-t)**5)
HJ_expected = (1+3*t+6*t**2+6*t**3+3*t**4-3*t**5-t**6)/(1-t)**2
assert sp.cancel(HJ-HJ_expected) == 0

# For the reduced union of lines, h_d is the cumulative sum of the Hilbert
# function of the 15 direction points. Once rank 15 is reached in degree 3,
# it stays 15 in all higher degrees over the infinite algebraic closure.
HI_expected = (1+3*t+6*t**2+5*t**3)/(1-t)**2
difference = sp.cancel(HJ-HI_expected)
assert sp.cancel(difference - t**3*(1+4*t+t**2)/(1-t)) == 0
assert sp.limit((1-t)*difference, t, 1) == 6

# The Hessian rank at a non-concurrent point of one line is 3, the normal
# codimension of the affine cone over the singular curve.
Hess = sp.hessian(F, x)
sub = {x[0]:0, x[1]:0, x[2]:1, x[3]:1, x[4]:2}
Hmat = [[int(sp.Poly(Hess[i,j], *x, modulus=3).eval(sub)) % 3
         for j in range(5)] for i in range(5)]
assert rank_modp([{j:c for j,c in enumerate(row) if c} for row in Hmat], 3) == 3

print("VERIFY_OK")
print("pair_partition_lines=15")
print("direction_point_hilbert_ranks_deg_0_to_3=", direction_ranks)
print("jacobian_hilbert_series=", sp.sstr(HJ))
print("reduced_union_hilbert_series=", sp.sstr(HI_expected))
print("excess_sheaf_length=", 6)
print("hessian_rank_at_(0,0,1,1,2)=", 3)
