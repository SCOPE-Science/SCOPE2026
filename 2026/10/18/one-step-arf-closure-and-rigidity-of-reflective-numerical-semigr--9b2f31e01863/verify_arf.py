#!/usr/bin/env python3
"""Independent finite validation of reflective-semigroup Arf closure formulas.

The theorem for arbitrary parameters is proved separately; finite checks do
not substitute for the proof. Uses only Python's standard library.
"""
from math import gcd


def shor_generators(g, a):
    r = g % a
    assert g >= 1 and 2 <= a <= g + 1 and r != 0
    return [a, 2 * g + a - r, *range(g + 1, g + a)]


def closure_by_generators(g, a):
    r = g % a
    f = 2*g-r
    gens = shor_generators(g, a)
    reachable = [False] * (f + 1)
    reachable[0] = True
    for n in range(f+1):
        if reachable[n]:
            for b in gens:
                if n+b <= f:
                    reachable[n+b] = True
    return {i for i, b in enumerate(reachable) if b}


def arf_saturate(u, f):
    s = set(u)
    for _ in range(f+2):
        t = set(s)
        for x in s:
            for y in s:
                if x + y <= f:
                    t.add(x+y)
                if x >= y and 2*x-y <= f:
                    t.add(2*x-y)
        if t == s:
            return s
        s = t
    raise AssertionError('Saturation did not stabilize')


def expected(g, a, f):
    q,r = divmod(g,a)
    if q == 0 or a == 2:
        return {n for n in range(f+1)
                if n%2 == 0 or n >= 2*g+1} if a == 2 else {0}
    return {n for n in range(f+1) if (n <= q*a and n%a == 0) or n >= g+1}


def run():
    cases = 0
    strict = 0
    added = 0
    gap_checks = 0
    direct_triple_cases = 0
    for g in range(1,91):
        for a in range(2,g+2):
            if g%a == 0:
                continue
            q,r = divmod(g,a)
            f = 2*g-r
            s = closure_by_generators(g,a)
            assert len(s) == f + 1 - g, (g,a,'genus')
            gaps = {n for n in range(1,f+1) if n not in s}
            calculated = {n for n in range(1,g) if n%a != 0}
            calculated.update(g+k*a for k in range(q+1))
            assert gaps == calculated, (g,a,'gaps')
            if g <= 35:
                # Independently evaluate the *full* Arf operator in one step,
                # not merely the equivalent two-variable test.
                immediate = set()
                for x in s:
                    for y in s:
                        if y > x: continue
                        for z in s:
                            if z > y: continue
                            value = x + y - z
                            if value <= f: immediate.add(value)
                assert immediate == expected(g,a,f),(g,a,'one-step A(S)')
                direct_triple_cases += 1
            c = arf_saturate(s,f)
            e = expected(g,a,f)
            assert c == e,(g,a,sorted(c^e))
            assert len(c-s) == (q if a>=3 and q>=1 else 0),(g,a,'number added')
            if c != s: strict += 1
            added += len(c-s)
            cases += 1
            gap_checks += len(gaps)
    print(f'PASS cases={cases}, strict_closures={strict}, added_gaps={added}, original_gap_checks={gap_checks}, direct_triple_cases={direct_triple_cases}, max_genus=90')


if __name__ == '__main__':
    run()
