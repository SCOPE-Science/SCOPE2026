#!/usr/bin/env python3
"""Finite independent checks for periodic-marker maximal-pattern formulas.

Run with: python3 verify_pattern.py
Only finite word and residue-set calculations are performed.
"""
from itertools import product

MOD = 257
STEP = 98
BASE = [((i+1)*STEP)//MOD - (i*STEP)//MOD for i in range(MOD)]
checks = 0


def finite_patterns(offsets):
    return {tuple(BASE[(start+t)%MOD] for t in offsets)
            for start in range(MOD)}


def marker_distinct(marker, support):
    m = len(marker)+1
    distinct = set()
    for phase in range(m):
        if all((phase+r)%m != 0 for r in support):
            distinct.add(tuple(marker[(phase+r)-1 if (phase+r)<m else
                                          ((phase+r)%m)-1]
                               for r in support))
    return len(distinct)


def marker_distinct2(marker, support):
    m = len(marker)+1
    vals = set()
    for start in range(m):
        row = []
        for r in support:
            residue = (start+r)%m
            if residue == 0:
                break
            row.append(marker[residue-1])
        else:
            vals.add(tuple(row))
    return len(vals)


def sampled_word(marker, offsets):
    m = len(marker)+1
    vectors = set()
    for start in range(m*MOD):
        row = []
        for t in offsets:
            idx = start+t
            residue = idx%m
            row.append(BASE[(idx//m)%MOD] if residue == 0 else marker[residue-1])
        vectors.add(tuple(row))
    return len(vectors)


# The finite rational rotation is a *test sequence*, not a proof for
# arbitrary irrational rotations. It realizes 2n patterns on these windows.
for n in range(1,11):
    assert len(finite_patterns([2*j for j in range(n)])) == 2*n
    checks += 1

# Independent direct word enumeration against the phase decomposition.
for m in range(2,7):
    for marker in product(('A','B'), repeat=m-1):
        for mask in range(1,1<<m):
            support = [r for r in range(m) if mask & (1<<r)]
            d1 = marker_distinct(marker, support)
            d2 = marker_distinct2(marker, support)
            assert d1 == d2
            checks += 1
            for k in range(len(support),7):
                offsets = list(support)
                # Add 2-step base samples in one active residue.
                for j in range(1,k-len(support)+1):
                    offsets.append(support[0]+m*(2*j))
                offsets.sort()
                observed = sampled_word(marker, offsets)
                assert observed == 2*k+d1, (m,marker,support,k,observed,d1)
                checks += 1

# Compare the exact decomposition for sampled windows that need not maximize
# the base-language pattern count.
for m in range(2,8):
    marker = tuple('AB'[(2*r + m)%2] for r in range(1,m))
    for k in range(1,7):
        offsets = sorted({(3*j*j+7*j+1)%(17*m) for j in range(k)})
        if len(offsets)!=k:
            offsets = [j*j*m+j for j in range(k)]
        support = sorted({t%m for t in offsets})
        contribution = sum(len(finite_patterns([(t-r)//m for t in offsets
                                                   if t%m == r])) for r in support)
        predicted = contribution+marker_distinct2(marker,support)
        assert sampled_word(marker,offsets)==predicted,(m,k,offsets,predicted)
        checks += 1

# Sharp all-k correction for the one-exception binary marker skeleton.
for m in range(3,12):
    marker = ('A',)*(m-2)+('B',)
    phase_max = [0]*(m+1)
    for mask in range(1,1<<m):
        support = [r for r in range(m) if mask & (1<<r)]
        t = len(support)
        d = marker_distinct2(marker,support)
        transitions = sum(((r+1)%m not in support) for r in support)
        assert d == transitions + int(m-t > transitions)
        phase_max[t] = max(phase_max[t],d)
        checks += 1
    for k in range(1,m+1):
        correction = max(phase_max[1:k+1])
        assert correction == min(k+1,(m+1)//2),(m,k,correction)
        checks += 1

# Explicit attaining windows on the four-letter, single-defect family.
for m in range(3,12):
    marker = ('A',)*(m-2)+('B',)
    for k in range(1,m+3):
        wanted = min(k+1,(m+1)//2)
        for mask in range(1,1<<m):
            support = [r for r in range(m) if mask & (1<<r)]
            if len(support)<=k and marker_distinct2(marker,support)==wanted:
                offsets = support + [support[0]+m*2*j
                                     for j in range(1,k-len(support)+1)]
                observed = sampled_word(marker,sorted(offsets))
                assert observed == 2*k+wanted, (m,k,observed,wanted)
                checks += 1
                break
        else:
            raise AssertionError(('missing finite witness',m,k))

print('VERIFY_OK: {} independent finite exact assertions'.format(checks))
