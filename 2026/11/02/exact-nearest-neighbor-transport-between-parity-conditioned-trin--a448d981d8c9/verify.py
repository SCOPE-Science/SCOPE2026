#!/usr/bin/env python3
"""Exact independent finite checks of the parity-conditioned transport theorem.
No numerical simulation is used for the exhaustive tests.
"""
from fractions import Fraction
from itertools import product
from random import Random


def coefficients(triples):
    out = [1]
    for l, t, w in triples:
        new = [0] * (len(out) + 2)
        for j, a in enumerate(out):
            new[j] += a*l
            new[j+1] += a*t
            new[j+2] += a*w
        out = new
    return out


def verify_sandwich(coef):
    even, odd = coef[0::2], coef[1::2]
    pe, po = sum(even), sum(odd)
    if pe == 0 or po == 0:
        return 0
    tests = 0
    for k in range(len(even)):
        x = sum(even[:k+1])*po
        lo = sum(odd[:k])*pe
        hi = sum(odd[:k+1])*pe
        assert 0 <= lo <= x <= hi, (coef, k, lo, x, hi)
        tests += 2
    return tests


def verify_quantile_transport(coef):
    even, odd = coef[0::2], coef[1::2]
    pe, po = sum(even), sum(odd)
    if pe == 0 or po == 0:
        return 0
    ev = [Fraction(x, pe) for x in even]
    od = [Fraction(x, po) for x in odd]
    i = j = 0
    remaining_e = ev[0]
    remaining_o = od[0]
    moved = Fraction(0)
    work = 0
    while i < len(ev) and j < len(od):
        if remaining_e == 0:
            i += 1
            if i < len(ev): remaining_e = ev[i]
            continue
        if remaining_o == 0:
            j += 1
            if j < len(od): remaining_o = od[j]
            continue
        mass = min(remaining_e, remaining_o)
        assert mass > 0
        assert i == j or i == j+1, (coef,i,j)
        moved += mass
        remaining_e -= mass
        remaining_o -= mass
        work += 1
    assert moved == 1, (coef, moved)
    return work


def main():
    options = [(l,t,4-l-t) for l in range(5) for t in range(5-l)]
    assert len(options) == 15
    sequences = assertions = 0
    for n in range(1, 5):
        for seq in product(options, repeat=n):
            assertions += verify_sandwich(coefficients(seq))
            sequences += 1
    rng = Random(26030919)
    coupled = 0
    for n in range(1, 13):
        for _ in range(180):
            seq = []
            for i in range(n):
                l = rng.randrange(8)
                t = rng.randrange(8-l)
                seq.append((l,t,7-l-t))
            co = coefficients(seq)
            assertions += verify_sandwich(co)
            coupled += verify_quantile_transport(co)
    # The sharpness example consists of one nontrivial ternary variable,
    # P(X=0) = P(X=1/2) = 1/2; the two conditional laws are point masses.
    assert coefficients([(1,1,0)]) == [1,1,0]
    assert verify_quantile_transport(coefficients([(1,1,0)])) == 1
    print(f'PASS exhaustive_sequences={sequences} exact_CDF_inequalities={assertions} greedy_coupling_edges={coupled} boundary_cases_included=true')

if __name__ == '__main__':
    main()
