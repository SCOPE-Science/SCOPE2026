"""Independent finite checks of the exact leaf/Wiener covariance in uniform recursive trees.
Run: python verify_leaf_wiener.py. Standard library only.
"""
from itertools import product
from fractions import Fraction
from math import factorial


def harmonic(n):
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction())


def claimed(n):
    return n * harmonic(n) - Fraction(n * n + 5 * n - 2, 4)


def statistics(parents):
    """parents[j-2] is the zero-based parent of vertex j-1; vertex 0 is root."""
    n = len(parents) + 1
    neighbors = [[] for _ in range(n)]
    nonleaves = set()
    for j, p in enumerate(parents, 1):
        neighbors[p].append(j)
        neighbors[j].append(p)
        nonleaves.add(p)
    leaf_set = set(range(n)) - nonleaves
    assert 0 not in leaf_set if n >= 2 else True
    total_distances = [0] * n
    for source in range(n):
        distance = [-1] * n
        distance[source] = 0
        queue = [source]
        for v in queue:
            for w in neighbors[v]:
                if distance[w] == -1:
                    distance[w] = distance[v] + 1
                    queue.append(w)
        assert len(queue) == n
        total_distances[source] = sum(distance)
    assert sum(total_distances) % 2 == 0
    return len(leaf_set), sum(total_distances) // 2, sum(total_distances[v] for v in leaf_set)


def all_parents(n):
    return product(*(range(j) for j in range(1, n)))


def mean(values):
    values = list(values)
    return Fraction(sum(values), len(values))


def exhaustive_checks():
    number_of_trees = 0
    for n in range(2, 10):
        moments = [0] * 4  # L, W, A, LW
        total = 0
        for parents in all_parents(n):
            L, W, A = statistics(parents)
            moments[0] += L
            moments[1] += W
            moments[2] += A
            moments[3] += L * W
            total += 1
        assert total == factorial(n - 1)
        number_of_trees += total
        el, ew, ea, elw = (Fraction(x, total) for x in moments)
        assert el == Fraction(n, 2)
        assert ew - ea == -Fraction((n - 1) * (n - 2), 4)
        assert elw - el * ew == claimed(n)
        assert ew == n * (n + 1) * harmonic(n) - 2 * n * n
        if n <= 3:
            assert claimed(n) == 0
        else:
            assert claimed(n) < 0
    assert number_of_trees == 46233
    return number_of_trees


def recurrence_checks():
    """Check conditional first-moment identities on every parent choice up to n=7."""
    conditional_parent_trials = 0
    for n in range(2, 8):
        for parents in all_parents(n):
            L, W, A = statistics(parents)
            # Fresh child has label n+1; its zero-based parent can be 0,...,n-1.
            children = [statistics(parents + (p,)) for p in range(n)]
            expect_L = Fraction(sum(x[0] for x in children), n)
            expect_W = Fraction(sum(x[1] for x in children), n)
            expect_difference = Fraction(sum(x[1] - x[2] for x in children), n)
            assert expect_L == Fraction(n - 1, n) * L + 1
            assert expect_W == Fraction(n + 2, n) * W + n
            assert expect_difference == W - A - Fraction(n - 1, n) * L
            conditional_parent_trials += n
    return conditional_parent_trials


def long_recurrence_checks():
    mean_L = Fraction(1)
    mean_W = Fraction(1)
    mean_A = Fraction(1)
    mean_LW = Fraction(1)
    for n in range(3, 201):
        m = n - 1
        next_L = Fraction(m - 1, m) * mean_L + 1
        next_W = Fraction(m + 2, m) * mean_W + m
        next_A = mean_A + Fraction(m - 1, m) * mean_L + m + Fraction(2, m) * mean_W
        next_LW = (Fraction(m + 1, m) * mean_LW
                   + Fraction(m + 2, m) * mean_W
                   + (m - 1) * mean_L + m - mean_A / m)
        mean_L, mean_W, mean_A, mean_LW = next_L, next_W, next_A, next_LW
        assert mean_LW - mean_L * mean_W == claimed(n)
        assert mean_W - mean_A == -Fraction((n - 1) * (n - 2), 4)
    return 198


if __name__ == "__main__":
    t = exhaustive_checks()
    p = recurrence_checks()
    k = long_recurrence_checks()
    print(f"PASS: {t} recursive trees enumerated (n=2..9); {p} conditional parent transitions; {k} exact moment-recursion steps")
