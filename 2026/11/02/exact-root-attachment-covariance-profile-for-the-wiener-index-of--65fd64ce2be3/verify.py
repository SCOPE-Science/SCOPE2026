"""Exact independent finite checks for root-attachment/Wiener covariance."""
from fractions import Fraction as F
from itertools import product


def harmonic(n, power=1):
    return sum((F(1, k ** power) for k in range(1, n + 1)), F(0))


def local_formula(n, j):
    return F(n * (n + 1), j * (j + 1)) * (
        3 - F(j + 1, j - 1) * harmonic(j - 1)
    )


def total_formula(n):
    return n * (n + 1) * (F(3, 2) - harmonic(n - 1, 2)) + (
        n + 1
    ) * harmonic(n - 1) - 3 * n


def wiener_from_parents(parents):
    n = len(parents) + 1
    neighbors = [[] for _ in range(n)]
    for child, parent in enumerate(parents, 1):
        neighbors[child].append(parent)
        neighbors[parent].append(child)
    total = 0
    for source in range(n):
        distances = [-1] * n
        distances[source] = 0
        queue = [source]
        for u in queue:
            for v in neighbors[u]:
                if distances[v] == -1:
                    distances[v] = distances[u] + 1
                    queue.append(v)
        total += sum(distances[source + 1 :])
    return total


def main():
    local_count = 0
    tree_count = 0
    for n in range(2, 9):
        trees = list(product(*(range(child) for child in range(1, n))))
        tree_count += len(trees)
        wieners = [wiener_from_parents(parents) for parents in trees]
        mean_w = F(sum(wieners), len(trees))
        assert mean_w == n * (n + 1) * harmonic(n) - 2 * n * n
        accumulated = F(0)
        for j in range(2, n + 1):
            joint = F(
                sum(
                    w for parents, w in zip(trees, wieners)
                    if parents[j - 2] == 0
                ),
                len(trees),
            )
            empirical_cov = joint - F(1, j - 1) * mean_w
            expected_cov = local_formula(n, j)
            assert empirical_cov == expected_cov, (n, j)
            if j <= 3:
                assert expected_cov == 0
            else:
                assert expected_cov < 0
            accumulated += expected_cov
            local_count += 1
        assert accumulated == total_formula(n)
    for n in range(2, 151):
        assert sum((local_formula(n, j) for j in range(2, n + 1)), F(0)) == total_formula(n)
        assert (total_formula(n) < 0) == (n >= 4)
    print(
        f"PASS: {tree_count} recursive trees exhaustively enumerated "
        f"(sizes 2..8), {local_count} exact local covariance checks; "
        "149 exact symbolic-sum comparisons (sizes 2..150)."
    )


if __name__ == "__main__":
    main()
