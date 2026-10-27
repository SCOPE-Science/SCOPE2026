#!/usr/bin/env python3
"""Direct finite checks for involutive partial graph automorphisms of paths."""
from itertools import combinations, permutations
from math import comb, factorial


def formula_profile(n):
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    a[1] = 1
    for length in range(2, n + 1):
        a[length] = 2
    if n >= 2:
        b[2] = 1
    for twice_length in range(4, n + 1, 2):
        b[twice_length] = 2

    def multiply(first, second):
        out = [0] * (n + 1)
        for i, value in enumerate(first):
            if value:
                for j, other in enumerate(second[: n + 1 - i]):
                    out[i + j] += value * other
        return out

    apowers = [[1] + [0] * n]
    bpowers = [[1] + [0] * n]
    for _ in range(n):
        apowers.append(multiply(apowers[-1], a))
        bpowers.append(multiply(bpowers[-1], b))

    answer = [1] + [0] * n
    for r in range(1, (n + 1) // 2 + 1):
        component = [0] * (n + 1)
        for paired in range(r // 2 + 1):
            multiplicity = factorial(r) // (
                factorial(r - 2 * paired) * factorial(paired) * 2 ** paired
            )
            term = multiply(apowers[r - 2 * paired], bpowers[paired])
            for rank in range(n + 1):
                component[rank] += multiplicity * term[rank]
        for rank in range(r, n - r + 2):
            answer[rank] += comb(n - rank + 1, r) * component[rank]
    return answer


def direct_profile(n):
    answer = [0] * (n + 1)
    candidates = 0
    for rank in range(n + 1):
        for subset in combinations(range(n), rank):
            edges = {
                (i, j)
                for i in range(rank)
                for j in range(i + 1, rank)
                if subset[j] - subset[i] == 1
            }
            for permutation in permutations(range(rank)):
                candidates += 1
                if any(permutation[permutation[i]] != i for i in range(rank)):
                    continue
                new_edges = {
                    (
                        min(permutation[i], permutation[j]),
                        max(permutation[i], permutation[j]),
                    )
                    for i, j in edges
                }
                if new_edges == edges:
                    answer[rank] += 1
    return answer, candidates


def main():
    total = 0
    for n in range(1, 10):
        formula = formula_profile(n)
        direct, count = direct_profile(n)
        assert formula == direct, (n, formula, direct)
        total += count
        print(f"path_n={n} rank_profile={direct} raw_candidates={count}")
    assert total == 1112082
    print(f"ALL_PATH_PARTIAL_INVOLUTION_CHECKS_PASSED 9 {total}")


if __name__ == "__main__":
    main()
