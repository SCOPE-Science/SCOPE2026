#!/usr/bin/env python3
"""Exact finite checks for power-index comparisons in redundant terminal-path games.

This is a direct finite check of formulas. The all-parameter argument
uses the analytical proof accompanying this script.
"""
import json
import math
from fractions import Fraction


def shapley_long(a, b, m):
    answer = Fraction(1)
    for k in range(1, m + 1):
        answer *= Fraction(k * a, k * a + b)
    return answer


def banzhaf_long(a, b, m):
    return Fraction(b * (2**a - 1), m * a * (2**b - 1) + b * (2**a - 1))


def coalition_indices(a, b, m):
    """Brute force over ALL coalitions of the edges, with exact weights."""
    blocks = [list(range(i*a, (i+1)*a)) for i in range(m)]
    blocks += [list(range(m*a, m*a+b))]
    n = m*a+b
    paths = [sum(1 << k for k in block) for block in blocks]
    win = [any((state & path) == path for path in paths) for state in range(1 << n)]
    sh = [Fraction(0) for _ in range(n)]
    bz = [Fraction(0) for _ in range(n)]
    fact = math.factorial
    for state in range(1 << n):
        if win[state]:
            continue
        size = state.bit_count()
        w_sh = Fraction(fact(size) * fact(n-size-1), fact(n)) if size<n else 0
        for i in range(n):
            bit=1<<i
            if state&bit:
                continue
            if win[state|bit]:
                sh[i] += w_sh
                bz[i] += Fraction(1,1 << (n-1))
    bzsum = sum(bz)
    bzn = [x/bzsum for x in bz]
    return sum(sh[m*a:]), sum(bzn[m*a:]), sum(sh), n*(1 << (n-1))


def verify():
    cases = [(2,3,1),(2,3,2),(2,3,3),(2,4,1),(2,4,2),(3,4,1),(3,4,2),(2,5,2),(2,6,2)]
    outputs = []
    total_states = 0
    pivotal_tests = 0
    for a,b,m in cases:
        s, t, shapley_total, ptests = coalition_indices(a,b,m)
        assert s == shapley_long(a,b,m), (a,b,m,'Shapley')
        assert t == banzhaf_long(a,b,m), (a,b,m,'Banzhaf')
        assert shapley_total == 1
        outputs.append({'a':a,'b':b,'m':m,'shapley_long':str(s),'normalized_banzhaf_long':str(t)})
        total_states += 1 << (m*a+b)
        pivotal_tests += ptests
    assert shapley_long(2,3,1) == Fraction(2,5)
    assert banzhaf_long(2,3,1) == Fraction(9,23)
    assert shapley_long(2,3,2) == Fraction(8,35)
    assert banzhaf_long(2,3,2) == Fraction(9,37)
    assert shapley_long(2,3,1) > banzhaf_long(2,3,1)
    assert shapley_long(2,3,2) < banzhaf_long(2,3,2)
    tested_pairs = 0
    tested_ratios = 0
    for a in range(2,13):
        for b in range(a+1,22):
            tested_pairs += 1
            A = Fraction(b,a)
            T = Fraction(a*(2**b-1), b*(2**a-1))
            assert T>A
            R = Fraction(1)
            below = False
            for m in range(1,81):
                R *= Fraction(m*a,m*a+b)
                current = R*(1+m*T)
                nxt = R*Fraction((m+1)*a,(m+1)*a+b)*(1+(m+1)*T)
                lhs = (nxt-current)>0
                rhs = A-T+(A-1)*m*T < 0
                assert lhs == rhs
                if current <= 1:
                    below = True
                if below:
                    assert nxt < 1
                tested_ratios += 1
    return {'claim':'Exact Shapley/Banzhaf reversal in parallel-path connectivity games',
            'full_coalition_cases':outputs,'complete_subsets_evaluated':total_states,
            'pivotal_coalition_tests':pivotal_tests,'analytic_ratio_checks':tested_ratios,
            'parameter_pairs_checked':tested_pairs,
            'critical_example':'(a,b)=(2,3): long-path shares 2/5 versus 9/23 at m=1, and 8/35 versus 9/37 at m=2',
            'all_checks':'passed'}


if __name__ == '__main__':
    print(json.dumps(verify(),sort_keys=True,ensure_ascii=False,indent=2))
