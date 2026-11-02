"""Exhaustive exact computation for the Nash-product cost of sex-equal stability.

Run with Python 3; standard library only. The loops are over every complete
strict preference profile for one, two, and three agents on each side.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import prod, factorial

EXPECTED_THREE = {
    Fraction(1, 1): 44136,
    Fraction(9, 8): 504,
    Fraction(3, 2): 1728,
    Fraction(2, 1): 144,
    Fraction(9, 4): 144,
}


def stable_matchings(orders, n):
    # Rank tables are computed independently of the permutations of matchings.
    rank = [{x: row.index(x) for x in range(n)} for row in orders]
    for assignment in permutations(range(n)):
        # assignment[i] is the female partner of male i.
        inverse = [assignment.index(j) for j in range(n)]
        blocked = False
        for i in range(n):
            for j in range(n):
                if j != assignment[i] and (rank[i][j] < rank[i][assignment[i]]
                      and rank[n + j][i] < rank[n + j][inverse[j]]):
                    blocked = True
                    break
            if blocked:
                break
        if blocked:
            continue
        male = sum(rank[i][assignment[i]] for i in range(n))
        female = sum(rank[n + j][inverse[j]] for j in range(n))
        P = prod(n - rank[i][assignment[i]] for i in range(n))
        P *= prod(n - rank[n + j][inverse[j]] for j in range(n))
        yield (assignment, male, female, P)


def profile_ratio(orders, n):
    stable = tuple(stable_matchings(orders, n))
    assert stable, "Complete strict balanced markets have stable matchings."
    minimum_gap = min(abs(m - w) for _, m, w, _ in stable)
    best_sex_equal = max(p for _, m, w, p in stable if abs(m-w) == minimum_gap)
    best_nash = max(p for _, m, w, p in stable)
    return Fraction(best_nash, best_sex_equal), stable


def main():
    summaries = {}
    for n in (1, 2, 3):
        orderings = tuple(permutations(range(n)))
        hist = Counter()
        stable_counts = Counter()
        for orders in product(orderings, repeat=2*n):
            ratio, stable = profile_ratio(orders, n)
            hist[ratio] += 1
            stable_counts[len(stable)] += 1
        assert sum(hist.values()) == factorial(n)**(2*n)
        summaries[n] = (hist, stable_counts)
    assert summaries[1][0] == {Fraction(1): 1}
    assert summaries[2][0] == {Fraction(1): 16}
    assert summaries[3][0] == EXPECTED_THREE
    assert summaries[3][1] == {1:34080, 2:11484, 3:1092}

    # Fully specified six-person witness with unique optimal solutions.
    witness = (
        (0,1,2), (0,1,2), (0,2,1),
        (0,1,2), (2,0,1), (1,0,2),
    )
    ratio, stable = profile_ratio(witness, 3)
    assert ratio == Fraction(9,4)
    assert stable == (
        ((0,1,2), 2, 4, 36),
        ((0,2,1), 4, 0, 81),
    )
    for n in (1,2,3):
        print(f"n={n} total={sum(summaries[n][0].values())} ratio_histogram="
              f"{sorted((str(k),v) for k,v in summaries[n][0].items())}")
    print('VERIFY_OK profiles=46673 sharp_ratio=9/4 maximizing_profiles=144')


if __name__ == '__main__':
    main()
