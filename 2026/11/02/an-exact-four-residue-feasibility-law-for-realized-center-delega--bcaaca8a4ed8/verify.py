#!/usr/bin/env python3
"""Exact feasibility checks for the homogeneous four-agent delegated allocation model.

No dependencies beyond the Python standard library.  All comparisons are integral.
"""
from itertools import product


def formula(m: int, p: int, q: int) -> bool:
    """True iff the claimed allocation exists when rho=p/q, 0<p<q."""
    assert 1 <= p < q and m >= 1
    t, r = divmod(m, 4)
    if r in (0, 2):
        return t * p >= (t - 1) * q
    if r == 1:
        return t * p >= (t - 2) * q
    return (t + 1) * p >= (t - 1) * q


def directly_fair(counts, p: int, q: int) -> bool:
    """Use the definitions, not the closed form, to test one count vector."""
    a, b, c, d = counts
    # Lower-level inter-EF1, including the ε-valued fourth agent.
    weights = (q, q, q, p)
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            # Remove an arbitrary good from j's bundle if nonempty.
            if weights[i] * counts[i] < weights[i] * max(counts[j] - 1, 0):
                return False
    # Center A realizes exactly its number of goods; each foreign good
    # is worth 1 to it under item-based hypothetical reallocation.
    if q * (a + b) < q * max(c + d - 1, 0):
        return False
    # Center B realizes c + rho*d; it could allocate each foreign good
    # to its first member for unit value under the item-based comparison.
    if q * c + p * d < q * max(a + b - 1, 0):
        return False
    return True


def count_vectors(m):
    for a in range(m + 1):
        for b in range(m - a + 1):
            for c in range(m - a - b + 1):
                yield a, b, c, m - a - b - c


def run():
    tests = 0
    examples = {}
    # Every count vector is realizable as a labeled allocation, since
    # goods are indistinguishable by value but are separately assigned.
    for m in range(1, 21):
        for q in range(2, 11):
            for p in range(1, q):
                actual = False
                for x in count_vectors(m):
                    if directly_fair(x, p, q):
                        actual = True
                        examples.setdefault((m, p, q), x)
                        break
                assert actual == formula(m, p, q), (m, p, q, actual)
                tests += 1
    # The all-size check uses only vectors compatible with inter-EF1.
    # This reduction is independently proved by the pairwise EF1 definition.
    from itertools import combinations
    for m in range(21, 129):
        t, r = divmod(m, 4)
        vectors = []
        for extra in combinations(range(4), r):
            vectors.append(tuple(t + (i in extra) for i in range(4)))
        for q in range(2, 17):
            for p in range(1, q):
                actual = any(directly_fair(x, p, q) for x in vectors)
                assert actual == formula(m, p, q), (m, p, q)
                tests += 1
    # An independent labeled-allocation walk for the sharp eight-good
    # failure and the nine-good re-entrance at rho=1/4.
    labeled = {}
    for m in (7, 8, 9):
        surviving = 0
        for assignment in product(range(4), repeat=m):
            cnt = [0, 0, 0, 0]
            for i in assignment:
                cnt[i] += 1
            if directly_fair(tuple(cnt), 1, 4):
                surviving += 1
        labeled[m] = surviving
    assert labeled[7] > 0
    assert labeled[8] == 0
    assert labeled[9] == 7560, labeled
    assert directly_fair((2, 2, 3, 2), 1, 4)
    assert not directly_fair((2, 2, 2, 2), 1, 4)
    assert formula(12, 1, 4) is False  # The previously published witness.
    print("VERIFY_OK", "rational_parameter_tests=", tests,
          "labeled_7=", labeled[7], "labeled_8=", labeled[8],
          "labeled_9=", labeled[9], "example_9=", examples[(9, 1, 4)])


if __name__ == "__main__":
    run()
