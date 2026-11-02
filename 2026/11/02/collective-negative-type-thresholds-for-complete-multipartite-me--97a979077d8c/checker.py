"""Exact rational checks for multipartite negative-type quadratic identities.

Python 3 standard library only. The proof in RESULT.md, not this finite test,
justifies the all-size theorem and the eigenvalue classification.
"""
from fractions import Fraction as F
from random import Random


def form_and_reduction(parts, t, coefficients):
    assert len(coefficients) == sum(parts)
    assert sum(coefficients) == 0
    groups = []
    offset = 0
    for n in parts:
        groups.append(coefficients[offset:offset + n])
        offset += n
    u = [sum(group) for group in groups]
    lhs = F(0)
    for i, group_i in enumerate(groups):
        for j, group_j in enumerate(groups):
            for x, ai in enumerate(group_i):
                for y, aj in enumerate(group_j):
                    if i != j or x != y:
                        lhs += ai * aj * (t if i == j else 1)
    rhs = t * sum((1 - F(1, n)) * s * s for n, s in zip(parts, u))
    rhs -= sum(s * s for s in u)
    rhs -= t * sum(
        sum((a - F(s, n)) ** 2 for a in group)
        for n, s, group in zip(parts, u, groups)
    )
    assert lhs == rhs, (parts, lhs, rhs)
    return lhs


def test():
    partitions = ([4, 2, 2, 2], [2, 2, 2], [3, 1], [1, 1, 1, 1],
                  [3, 2, 1, 2], [5, 1, 4], [2, 1])
    rng = Random(20231028)
    count = 0
    for parts in partitions:
        for _ in range(45):
            alpha = [F(rng.randrange(-5, 6), rng.randrange(1, 6))
                     for _ in range(sum(parts) - 1)]
            alpha.append(-sum(alpha))
            t = F(rng.randrange(1, 19), rng.randrange(1, 7))
            form_and_reduction(parts, t, alpha)
            count += 1
    parts = [4, 2, 2, 2]
    alpha = [F(3, 4)] * 4 + [F(-1, 2)] * 6
    assert sum(alpha) == 0
    assert form_and_reduction(parts, F(3, 2), alpha) == F(3, 8)
    assert form_and_reduction(parts, F(16, 11), alpha) == 0
    assert F(16, 11) < F(3, 2) < F(8, 5)
    a_large, a_small = F(3, 4), F(1, 2)
    lam_full = (3 * a_large + a_small) / 4
    lam_pair = (a_large + a_small) / 2
    assert lam_full == F(11, 16)
    assert lam_pair == F(5, 8)
    assert F(3, 2) * lam_full > 1
    assert F(3, 2) * lam_pair < 1
    print(f"PASS: {count} generic exact quadratic decompositions, "
          "critical witness and pair threshold comparisons")


if __name__ == "__main__":
    test()
