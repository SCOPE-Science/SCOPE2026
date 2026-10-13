#!/usr/bin/env python3
"""Exact finite checks for the hypergeometric singleton-extremizer theorem.

Run with Python 3; uses only the standard library. Finite tests support but do
not prove the unrestricted algebraic and asymptotic assertions.
"""
from math import comb
from itertools import combinations


def C(n, r):
    return comb(n, r) if 0 <= r <= n else 0


def f(N, k, a):
    return a * C(N-a, k-1)


def objective(N, k, parts):
    return sum(f(N, k, a) for a in parts)


def partitions(total, count, minimum=1):
    """All nondecreasing partitions of total into count positive parts."""
    if count == 1:
        if total >= minimum:
            yield (total,)
        return
    for first in range(minimum, total//count+1):
        for tail in partitions(total-first, count-1, first):
            yield (first,) + tail


def special_profiles(N, S):
    seen = set()
    for L in range(1, N-S+2):
        q, r = divmod(N-L, S-1)
        a = tuple(sorted([L] + [q]*(S-1-r) + [q+1]*r))
        seen.add(a)
    return seen


def exact_finite_checks():
    case_count = 0
    total_partitions = 0
    for N in range(2, 29):
        for S in range(2, min(7, N)+1):
            pp = list(partitions(N, S))
            ss = special_profiles(N, S)
            assert ss <= set(pp)
            for k in range(2, N+1):
                actual = max(objective(N, k, p) for p in pp)
                reduced = max(objective(N, k, p) for p in ss)
                assert actual == reduced, (N, S, k, actual, reduced)
                case_count += 1
                total_partitions += len(pp)
    return case_count, total_partitions


def difference_checks():
    count = 0
    for N in range(3, 75):
        for k in range(3, N+1):
            def D(a):
                return f(N, k, a+1) - f(N, k, a)
            for a in range(1, N):
                if a <= N-k+1:
                    expected = C(N-a-1, k-2)*(N-k+1-k*a)//(k-1)
                    assert C(N-a-1, k-2)*(N-k+1-k*a) % (k-1) == 0
                else:
                    expected = 0
                assert D(a) == expected, (N, k, a)
                count += 1
            for a in range(1, N-1):
                delta = D(a+1) - D(a)
                if a <= N-k+1:
                    rhsnum = C(N-a-2, k-3)*(k*a-2*(N+1-k))
                    assert rhsnum % (k-2) == 0
                    expected = rhsnum//(k-2)
                else:
                    expected = 0
                assert delta == expected, ('curvature', N, k, a, delta, expected)
            # Global shape of the discrete first difference.
            t = max(1, (2*(N+1-k)+k-1)//k)
            assert all(D(a+1) <= D(a) for a in range(1, min(N-1,t)))
            assert all(D(a+1) >= D(a) for a in range(t, N-1))
    return count


def direct_sampling_checks():
    tests = 0
    for N in range(3, 11):
        for S in range(2, min(4, N)+1):
            for p in partitions(N, S):
                labels = [i for i,a in enumerate(p) for _ in range(a)]
                for k in range(2, N+1):
                    numerator = sum(sum(1 for c in range(S) if [labels[x] for x in draw].count(c)==1)
                                    for draw in combinations(range(N), k))
                    assert numerator == objective(N, k, p)
                    tests += 1
    return tests


def named_examples():
    expected = {4:(3,3,3), 5:(2,2,5), 6:(1,1,7)}
    for k, profile in expected.items():
        pp = list(partitions(9, 3))
        best = max(objective(9, k, p) for p in pp)
        winners = [p for p in pp if objective(9,k,p) == best]
        assert winners == [profile], (k, winners)
    for N, S, k, m in [(200,3,60,3), (360,4,144,2), (300,5,210,1), (400,3,112,3)]:
        winning_value = max(objective(N,k,p) for p in special_profiles(N,S))
        expected_profile = tuple(sorted([N-(S-1)*m]+[m]*(S-1)))
        assert objective(N,k,expected_profile) == winning_value, (N,S,k,m)
        # In fact this profile is the sole maximizing special profile.
        assert [p for p in special_profiles(N,S) if objective(N,k,p)==winning_value] == [expected_profile]
    return len(expected), 4


if __name__ == '__main__':
    cases, parts = exact_finite_checks()
    diffs = difference_checks()
    direct = direct_sampling_checks()
    examples, large = named_examples()
    print(f'VERIFY_OK finite_cases={cases} partition_comparisons={parts} difference_identities={diffs} direct_draw_checks={direct} transition_examples={examples} macroscopic_instances={large}')
