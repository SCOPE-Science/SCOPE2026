#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
from math import gcd


def hamilton(pop, h):
    total = sum(pop)
    quota = [Fraction(h*x, total) for x in pop]
    floors = [q.numerator // q.denominator for q in quota]
    remaining = h - sum(floors)
    remainders = [quota[i] - floors[i] for i in range(len(pop))]
    best = None
    out = set()
    for chosen in combinations(range(len(pop)), remaining):
        val = sum((remainders[i] for i in chosen), Fraction(0))
        a = floors[:]
        for i in chosen:
            a[i] += 1
        t = tuple(a)
        if best is None or val > best:
            best = val
            out = {t}
        elif val == best:
            out.add(t)
    return out


def webster(pop, h):
    # Highest-averages form with odd divisors 1,3,5,...; exact cutoff ties retained.
    entries = []
    for i, v in enumerate(pop):
        for j in range(h):
            entries.append((Fraction(v, 2*j+1), i, j))
    values = sorted((x[0] for x in entries), reverse=True)
    cutoff = values[h-1]
    above = [x for x in entries if x[0] > cutoff]
    tied = [x for x in entries if x[0] == cutoff]
    need = h - len(above)
    out = set()
    for choice in combinations(tied, need):
        chosen = above + list(choice)
        chosen_ij = {(i,j) for _,i,j in chosen}
        if any(any((i,k) not in chosen_ij for k in range(j)) for _,i,j in chosen):
            continue
        a = [0]*len(pop)
        for _,i,_ in chosen:
            a[i] += 1
        out.add(tuple(a))
    return out

# Exact theorem check on a broad integer box for the 3-state, 2-seat cone.
checked = 0
for p in range(1, 41):
    for q in range(p+1, 61):
        for r in range(q+1, 181):
            H = hamilton((p,q,r), 2)
            W = webster((p,q,r), 2)
            conflict = len(H)==1 and len(W)==1 and H != W
            predicted = 3*q < r < p + 3*q
            assert conflict == predicted, (p,q,r,H,W,predicted)
            if predicted:
                assert H == {(0,1,1)}
                assert W == {(0,0,2)}
            checked += 1

# Exact boundary correspondences.
for p in range(1, 31):
    for q in range(p+1, 41):
        r = 3*q
        assert webster((p,q,r),2) == {(0,1,1),(0,0,2)}
        assert hamilton((p,q,r),2) == {(0,1,1)}
        r = p + 3*q
        assert hamilton((p,q,r),2) == {(0,1,1),(0,0,2)}
        assert webster((p,q,r),2) == {(0,0,2)}

# Two-state equivalence replay over a large finite window, retaining ties.
for a in range(1, 61):
    for b in range(1, 61):
        for h in range(1, 41):
            assert hamilton((a,b),h) == webster((a,b),h), (a,b,h)

# One-seat agreement for arbitrary numbers of states in a bounded replay.
for pop in [(1,2,3),(1,1,2),(2,5,5,7),(3,4,8,9,12)]:
    assert hamilton(pop,1) == webster(pop,1)

# Primitive integer minimal witness by total population, sorted strictly.
first_sum = None
first = []
for s in range(6, 80):
    for p in range(1, s):
        for q in range(p, s):
            r = s-p-q
            if r < q or gcd(gcd(p,q),r) != 1:
                continue
            H = hamilton((p,q,r),2)
            W = webster((p,q,r),2)
            if len(H)==len(W)==1 and H != W:
                first_sum = s
                first.append((p,q,r,H,W))
    if first:
        break
assert first_sum == 15
assert [(x[0],x[1],x[2]) for x in first] == [(2,3,10)]
assert first[0][3] == {(0,1,1)}
assert first[0][4] == {(0,0,2)}

print('VERIFY_OK')
print('integer_triples_checked', checked)
print('disagreement_cone', '3q < r < p+3q')
print('primitive_minimal_witness', (2,3,10), 'population_sum', 15)
print('Hamilton', sorted(first[0][3]))
print('Webster', sorted(first[0][4]))
