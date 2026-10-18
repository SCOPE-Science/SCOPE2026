#!/usr/bin/env python3
"""Exact integer-arithmetic verifier for a quartic binomid recognition theorem.

No external dependencies. The branch bounds are proved in RESULT.md;
termination and completeness do not depend on any numerical cutoff.
"""
from fractions import Fraction
from math import prod

DEG = 4
EXPECTED = ((0,0,0,0),(0,0,0,1),(0,0,1,1),(0,0,1,2),(0,1,2,3))


def fval(t, n):
    return prod(n+a for a in t)


def upper_bound(r, t, slots):
    return r * Fraction(t+2, t+1)**slots


def bounded_prefixes():
    """Bounded exact search for the initial ratio f(2)/f(1) integral."""
    results = []
    stage_sizes = [0]*5
    def visit(prefix, r):
        stage_sizes[len(prefix)] += 1
        if len(prefix) == 4:
            if r.denominator == 1:
                results.append(prefix)
            return
        target = r.numerator//r.denominator+1
        slots = 4-len(prefix)
        t = prefix[-1] if prefix else 0
        while upper_bound(r, t, slots) >= target:
            visit(prefix+(t,), r*Fraction(t+2, t+1))
            t += 1
    visit((), Fraction(1))
    return set(results), stage_sizes


def solve_last_algebraically():
    """Independent last-coordinate solution, using (m-R)(d+1)=R."""
    results = set()
    def visit(prefix, r):
        slots = 4-len(prefix)
        start = prefix[-1] if prefix else 0
        if slots == 1:
            c = start
            mmax = int(r*Fraction(c+2,c+1))
            for m in range(int(r)+1, mmax+1):
                d_plus_1 = r/(m-r)
                if d_plus_1.denominator == 1:
                    d = int(d_plus_1)-1
                    if d >= c:
                        results.add(prefix+(d,))
            return
        target = int(r)+1
        t = start
        while r*Fraction(t+2,t+1)**slots >= target:
            visit(prefix+(t,), r*Fraction(t+2,t+1))
            t += 1
    visit((), Fraction(1))
    return results


def passes_first_two(t):
    return fval(t,2) % fval(t,1) == 0 and fval(t,3) % fval(t,1) == 0


def passes_three(t):
    return passes_first_two(t) and (fval(t,3)*fval(t,4))%(fval(t,1)*fval(t,2)) == 0


def generalized_ratio(t,n,k):
    return Fraction(prod(fval(t,i) for i in range(n-k+1,n+1)),
                    prod(fval(t,i) for i in range(1,k+1)))


def main():
    x, sizes = bounded_prefixes()
    y = solve_last_algebraically()
    assert x == y, (len(x),len(y),sorted(x^y))
    assert len(x)==83
    z = sorted(filter(passes_first_two,x))
    assert z == [(0,0,0,0),(0,0,0,1),(0,0,1,1),(0,0,1,2),
                 (0,0,1,5),(0,1,1,2),(0,1,2,3),(1,2,3,4)]
    w=tuple(sorted(filter(passes_three,x)))
    assert w==EXPECTED
    for t in EXPECTED:
        for n in range(1,81):
            for k in range(0,n+1):
                assert generalized_ratio(t,n,k).denominator==1,(t,n,k)
    eliminated = []
    for t in z:
        if t not in EXPECTED:
            t42 = generalized_ratio(t,4,2)
            assert t42.denominator!=1
            eliminated.append((t,str(t42)))
    print('Exact branch stages:', sizes)
    print('First divisibility test count:',len(x))
    print('First two divisibility tests:',len(z),z)
    print('All three tests:',len(w),list(w))
    print('Excluded at (n,k)=(4,2):',eliminated)
    print('Two enumeration methods agree: PASS')
    print('80-row binomid check of five candidates: PASS')
    print('FINITE_CLASSIFICATION_CERTIFICATE_OK')

if __name__=='__main__': main()
