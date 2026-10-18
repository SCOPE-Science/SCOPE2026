"""Exact coefficient-space and tangent-incidence census for binary (4,3) curves.

Run: python verify.py
Requires SymPy >= 1.12. All arithmetic is over F_2; the Groebner
unit-ideal test is over its algebraic closure by the Nullstellensatz.
"""
import collections
import itertools
import json
import sympy as sp

x, y = sp.symbols('x y')
monomials = [(i, j) for i in range(5) for j in range(4)]
points = [(1, 0), (0, 1), (1, 1)]

def monomial_at(i, j, p, q):
    a, b = p
    c, d = q
    return a**(4-i)*b**i*c**(3-j)*d**j

rows = []
for p, q in itertools.product(points, repeat=2):
    rows.append(sum((monomial_at(i, j, p, q)&1)<<k
                    for k, (i, j) in enumerate(monomials)))

# Find the kernel of the nine rational-point evaluations in the
# 20-dimensional bihomogeneous coefficient space.
pivots = {}
for row in rows:
    t = row
    while t:
        lead = t.bit_length()-1
        if lead not in pivots:
            pivots[lead] = t
            break
        t ^= pivots[lead]
free = [i for i in range(20) if i not in pivots]
basis = []
for k in free:
    a = 1 << k
    for lead in sorted(pivots):
        if (a & pivots[lead]).bit_count() % 2:
            a ^= 1 << lead
    assert all((a & row).bit_count() % 2 == 0 for row in rows)
    basis.append(a)
assert len(basis) == 11

def coefficient_mask(code):
    z = 0
    for k, v in enumerate(basis):
        if code >> k & 1:
            z ^= v
    return z

# The four coordinate charts (X_0 != 0 or X_1 != 0) x
# (Y_0 != 0 or Y_1 != 0).
charts = [[x**(i if a == 0 else 4-i)*y**(j if b == 0 else 3-j)
           for i, j in monomials]
          for a, b in itertools.product((0, 1), repeat=2)]

def smooth_geometric(mask):
    for chart in charts:
        f = sum(chart[k] for k in range(20) if mask >> k & 1)
        gb = sp.groebner([f, sp.diff(f, x), sp.diff(f, y)], x, y,
                         modulus=2, order='lex')
        if list(gb.exprs) != [sp.Integer(1)]:
            return False
    return True

def tangent(mask, p, q):
    # Local x-coordinate is X1/X0 if X0 != 0, otherwise X0/X1.
    # The y-coordinate is selected analogously.
    aa, bb = p
    cc, dd = q
    val_x = val_y = 0
    for k, (i, j) in enumerate(monomials):
        if not (mask >> k & 1):
            continue
        if aa:
            if i % 2:
                val_x ^= aa**(4-i)*bb**(i-1)*cc**(3-j)*dd**j
        else:
            if (4-i) % 2:
                val_x ^= aa**(3-i)*bb**i*cc**(3-j)*dd**j
        if cc:
            if j % 2:
                val_y ^= aa**(4-i)*bb**i*cc**(3-j)*dd**(j-1)
        else:
            if (3-j) % 2:
                val_y ^= aa**(4-i)*bb**i*cc**(2-j)*dd**j
    return ((val_x&1)<<1) | (val_y&1)

N = (1<<len(basis))-1
locally_smooth, globally_smooth = [], []
patterns = {}
for code in range(1, N+1):
    m = coefficient_mask(code)
    patt = tuple(tangent(m, p, q) for p, q in
                 itertools.product(points, repeat=2))
    if 0 not in patt:
        locally_smooth.append(code)
    if smooth_geometric(m):
        globally_smooth.append(code)
        assert 0 not in patt
        patterns[code] = patt

assert len(globally_smooth) == 66
agree = collections.Counter()
for n, a in enumerate(globally_smooth):
    for b in globally_smooth[n+1:]:
        agree[sum(u == v for u, v in zip(patterns[a], patterns[b]))] += 1

locset = set(locally_smooth)
local_pencils = set()
for n, a in enumerate(locally_smooth):
    for b in locally_smooth[n+1:]:
        if (a^b) in locset:
            local_pencils.add(tuple(sorted((a, b, a^b))))
globset = set(globally_smooth)
local_pencil_hist = collections.Counter(sum(a in globset for a in p)
                                        for p in local_pencils)
assert agree == {3: 642, 5: 981, 7: 468, 9: 54}
assert local_pencil_hist == {0:272, 1:240}
assert all(0 not in p for p in patterns.values())
print(json.dumps({
    'coefficient_dimension': len(basis),
    'filling_nonzero_forms': N,
    'rationally_smooth_forms': len(locally_smooth),
    'geometrically_smooth_forms': len(globally_smooth),
    'different_rational_tangent_patterns': len(set(patterns.values())),
    'pair_shared_tangents': dict(sorted(agree.items())),
    'all_rationally_smooth_pencils': len(local_pencils),
    'locally_smooth_pencils_by_globally_smooth_members':
      dict(sorted(local_pencil_hist.items())),
    'all_smooth_filling_pencils': 0,
}, sort_keys=True))
