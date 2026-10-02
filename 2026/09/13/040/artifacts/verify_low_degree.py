"""Exact finite low-degree certificate; no assertion of uniform stability.

Run from the package root: python -X utf8 artifacts/verify_low_degree.py
Historical orbit enumerators supply spanning Reynolds sums. This certificate
independently projects the relation quotient, multiplies the four diagonal
terms, checks EVERY relation column and every adjacent-transposition action,
then asserts exact ranks. No floating-point rank test is used.
"""
import itertools
import json
from collections import defaultdict
from collections import Counter
from fractions import Fraction
from math import factorial
from pathlib import Path
import sympy as sp

root = Path(__file__).resolve().parents[1]
ns = {}
exec((root / 'artifacts/h5_explore.py').read_text(encoding='utf-8').split('reps=gen_reps()')[0], ns)
ns6 = {}
source6 = (root / 'artifacts/h6_check.py').read_text(encoding='utf-8').split('reps=gen_A6_reps()')[0]
exec(source6, ns6)


def clean(v):
    return {i: x for i, x in v.items() if x}


def rank(vectors):
    return int(sp.Matrix([[sum(x * b.get(i, 0) for i, x in a.items())
                           for b in vectors] for a in vectors]).rank())


def decode(index, k, maps):
    _, wlist, dw, _, edges, ne, _, _ = maps
    block, wi = divmod(index, dw)
    ej, si = divmod(block, ne)
    et, j = divmod(ej, k)
    return et, j, edges[si], wlist[wi]


def quotient(v, k, maps):
    # (e_l-e_m)G_lm identifies two disjoint basis coordinates in
    # EACH etype/edge/W block; map e_m to e_l. Kernel is precisely R.
    wi, _, dw, si, _, ne, _, _ = maps
    out = defaultdict(int)
    for index, value in v.items():
        et, j, (l, m), w = decode(index, k, maps)
        if j == m:
            j = l
        out[((et * k + j) * ne + si[l, m]) * dw + wi[w]] += value
    return clean(out)


def independent_D(et, j, l, m, w, k, maps):
    wi, _, dw, _, _, _, ai, _ = maps
    out = defaultdict(int)
    for factors in (((l, 3),), ((m, 3),), ((l, 1), (m, 1)), ((l, 2), (m, 2))):
        monomial = [0] * k
        monomial[j] = et + 1
        zero = False
        for p, factor in factors:
            old = monomial[p]
            if not old:
                monomial[p] = factor
            elif old in (1, 2) and factor == old:
                monomial[p] = 3
            else:
                zero = True
                break
        if zero:
            continue
        pts = [p for p, x in enumerate(monomial) if x == 3]
        twos = [p for p, x in enumerate(monomial) if x in (1, 2)]
        if pts:
            assert len(pts) == len(twos) == 1
            key = ('PA' if monomial[twos[0]] == 1 else 'PB', pts[0], twos[0])
        else:
            assert len(twos) == 3
            key = ('T', *twos, *(monomial[p] - 1 for p in twos))
        out[ai[key] * dw + wi[w]] += 1
    return clean(out)


def image(v, k, maps):
    out = defaultdict(int)
    for index, value in v.items():
        et, j, (l, m), w = decode(index, k, maps)
        for ti, c in independent_D(et, j, l, m, w, k, maps).items():
            out[ti] += value * c
    return clean(out)


def action(v, permutation, k, maps):
    wi, _, dw, si, _, ne, _, _ = maps
    out = defaultdict(int)
    for index, value in v.items():
        et, j, (l, m), (p, q) = decode(index, k, maps)
        edge = tuple(sorted((permutation[l], permutation[m])))
        base = ((et * k + permutation[j]) * ne + si[edge]) * dw
        for w, c in ns['wedge_image_dict'](p, q, permutation[p], permutation[q], k).items():
            out[base + wi[w]] += value * c
    return clean(out)


def partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    for size in range(min(n, maximum or n), 0, -1):
        for rest in partitions(n - size, size):
            yield (size,) + rest


for k in range(2, 13):
    sums = [Fraction(0) for _ in range(5)]
    for partition in partitions(k):
        cycles = Counter(partition)
        denominator = 1
        for size, count in cycles.items():
            denominator *= size ** count * factorial(count)
        f, m2 = cycles[1], cycles[2]
        w = Fraction(f * (f-1), 2) - f + 1 - m2
        g = Fraction(f * (f-1), 2) + m2
        characters = (1, 2*f, g, f+2*g+f*(f-1), 2*f*g)
        for j, character in enumerate(characters):
            sums[j] += Fraction(character * w, denominator)
    expected = (0, 0, 0, 0 if k == 2 else 1,
                0 if k == 2 else 2 if k == 3 else 4)
    assert tuple(sums) == expected
print('EXACT_CHARACTER_ASSERTIONS_OK k=2..12: trivial_W=0, H2_W=0, G_W=0, A4_W=1 for k>=3', flush=True)

results = []
for k in range(3, 8):
    maps = ns['build_index_maps'](k)
    wi, wl, dw, si, edges, ne, ai, al = maps
    vectors = [clean(ns['orbit_sum_C5'](k, rep, maps)) for rep in ns['gen_reps']()]
    # Reynolds averaging of monomials spans the full invariant subspace.
    # All five-role equality patterns are enumerated, including disjoint ones.
    nI = rank(vectors)
    assert nI == (2 if k == 3 else 4)
    basis = []
    for v in vectors:
        if rank(basis + [v]) > len(basis):
            basis.append(v)
    for p in range(k - 1):
        permutation = list(range(k))
        permutation[p], permutation[p + 1] = permutation[p + 1], permutation[p]
        for v in basis:
            assert action(v, permutation, k, maps) == v
    # Differential comparison for every free-domain basis, not just invariants.
    for et, j, (l, m), w in itertools.product((0, 1), range(k), edges, wl):
        got = independent_D(et, j, l, m, w, k, maps)
        old = clean(ns['D_image_of_domain_basis'](k, et, j, l, m, {w: 1}, maps))
        assert got == old
    relation_count = 0
    for et, (l, m), w in itertools.product((0, 1), edges, wl):
        left = independent_D(et, l, l, m, w, k, maps)
        right = independent_D(et, m, l, m, w, k, maps)
        assert left == right
        relation_count += 1
    assert relation_count == 2 * ne * dw
    qrank = rank([quotient(v, k, maps) for v in basis])
    cap = nI - qrank
    drank = rank([image(v, k, maps) for v in basis])
    assert cap == 2 and drank == (0 if k == 3 else 2)
    assert qrank - drank == 0
    a6rank = rank([clean(ns6['orbit_sum_A6W'](k, r, maps)) for r in ns6['gen_A6_reps']()])
    assert a6rank == (2 if k == 3 else 4)
    row = dict(k=k, invC5=nI, rankR=relation_count, quotient_rank=qrank,
               intersection=cap, differential_rank=drank, H5=0,
               invA6=a6rank, A6_piece=a6rank - drank,
               all_relations_checked=relation_count)
    results.append(row)
    print(json.dumps(row, sort_keys=True), flush=True)
print('VERIFY_LOW_DEGREE_OK')
