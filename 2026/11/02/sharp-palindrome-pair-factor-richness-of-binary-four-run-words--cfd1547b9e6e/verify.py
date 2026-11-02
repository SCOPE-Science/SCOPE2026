#!/usr/bin/env python3
"""Check exact four-run palindrome-pair formulas and sharp witnesses.

No external dependencies. Executing this file verifies finite spot checks,
not the unbounded integer inequalities proved in RESULT.md.
"""
from itertools import product


def is_palindrome_pair(word):
    return any(word[:i] == word[:i][::-1] and
               word[i:] == word[i:][::-1]
               for i in range(len(word) + 1))


def direct_count(word):
    factors = {""}
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            factors.add(word[i:j])
    return sum(is_palindrome_pair(x) for x in factors)


def four_run_count(a, b, c, d):
    if min(a, b, c, d) < 1:
        raise ValueError("each maximal run must be nonempty")
    ca, db = int(c <= a), int(b <= d)
    return (1 + max(a, c) + max(b, d)
            + a*b + c*d - min(a, c)*min(b, d)
            + b*c + a*c + b*d + d*ca + a*db - ca*db)


def three_run_count(a, b, c):
    if min(a, b, c) < 1:
        raise ValueError("each maximal run must be nonempty")
    return 1 + max(a, c) + b + a*b + b*c + a*c


def goal_four(n):
    return (n*n + n + 11)//3  # ceil((n^2+n+9)/3)


def benchmark_three(n):
    return (n*n + 2*n + 5)//3  # ceil((n^2+2*n+3)/3)


def witness_four(n):
    m, r = divmod(n, 3)
    if r == 0:
        return 1, m, m+1, m-2
    if r == 1:
        return 1, m+1, m+1, m-2
    return 1, m+1, m+1, m-1


def witness_three(n):
    m, r = divmod(n, 3)
    if r == 0:
        return m, m, m
    if r == 1:
        return m, m, m+1
    return m, m+1, m+1


def all_compositions(n, parts):
    if parts == 1:
        if n >= 1:
            yield (n,)
        return
    for first in range(1, n-parts+2):
        for rest in all_compositions(n-first, parts-1):
            yield (first,) + rest


def check():
    # Direct checker independent of run-shape counting; check every
    # parameter composition in the specified short range.
    definition_comparisons = 0
    for n in range(4, 17):
        for a,b,c,d in all_compositions(n,4):
            w = "0"*a + "1"*b + "0"*c + "1"*d
            assert direct_count(w) == four_run_count(a,b,c,d), (n,a,b,c,d)
            definition_comparisons += 1
    for n in range(3, 18):
        for a,b,c in all_compositions(n,3):
            w = "0"*a + "1"*b + "0"*c
            assert direct_count(w) == three_run_count(a,b,c), (n,a,b,c)
            definition_comparisons += 1

    # Exhaustively optimize the proved closed-form count in a large finite
    # prefix; the written analytic inequalities cover every larger n.
    parameter_comparisons = 0
    for n in range(8, 76):
        best = -1
        for a,b,c,d in all_compositions(n,4):
            best = max(best, four_run_count(a,b,c,d))
            parameter_comparisons += 1
        assert best == goal_four(n), (n,best,goal_four(n))
    for n in range(8, 300):
        a,b,c,d = witness_four(n)
        assert min(a,b,c,d) >= 1 and a+b+c+d == n
        assert four_run_count(a,b,c,d) == goal_four(n), n
        a,b,c = witness_three(n)
        assert min(a,b,c) >= 1 and a+b+c == n
        assert three_run_count(a,b,c) == benchmark_three(n), n
        assert benchmark_three(n)-goal_four(n) == (n-5)//3, n  # ceil((n-7)/3)
    print("definition_comparisons", definition_comparisons)
    print("parameter_comparisons", parameter_comparisons)
    print("four_run_values_n8_through_16", [goal_four(n) for n in range(8,17)])
    print("VERIFY_OK")


if __name__ == "__main__":
    check()
