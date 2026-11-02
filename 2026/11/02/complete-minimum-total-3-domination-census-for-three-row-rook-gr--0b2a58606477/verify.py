"""Independent finite checks of exact minimum total-three-domination counts.

Run with Python 3.9+; no third-party dependencies.
"""
from collections import Counter
from math import comb, factorial


def prediction(n):
    if n == 2:
        return 6, 1
    if n == 3:
        return 8, 9
    if n == 4:
        return 8, 18
    if n == 5:
        return 9, 160
    return 9, comb(n, 3) + n * (n - 1) * (n - 2) * (n - 3)


def exhaustive_open_neighborhood_check(n):
    """Construct all edges directly; enumerate all sets up to predicted optimum."""
    adjacency = []
    for a in range(3):
        for j in range(n):
            neighbors = 0
            for b in range(3):
                for k in range(n):
                    if (a == b and j != k) or (a != b and j == k):
                        neighbors |= 1 << (b * n + k)
            adjacency.append(neighbors)
    optimum = prediction(n)[0]
    accepted = Counter()
    for chosen in range(1 << (3 * n)):
        size = chosen.bit_count()
        if size > optimum:
            continue
        if all((chosen & neighborhood).bit_count() >= 3
               for neighborhood in adjacency):
            accepted[size] += 1
    return accepted


def compositions(parts, total):
    """All frequency vectors of `parts` nonnegative entries summing to total."""
    if parts == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(parts - 1, total - first):
                yield (first,) + rest


def independent_column_type_count(n):
    """Enumerate frequency vectors for 8 possible column masks; not graph subsets."""
    target = prediction(n)[0]
    facts = [factorial(i) for i in range(n + 1)]
    total_count = 0
    for counts in compositions(8, n):
        row_sums = [sum(counts[col] * ((col >> row) & 1)
                        for col in range(8)) for row in range(3)]
        if sum(row_sums) != target:
            continue
        if any(row_sums[row] + col.bit_count()
               - 2 * ((col >> row) & 1) < 3
               for col in range(8) if counts[col]
               for row in range(3)):
            continue
        denominator = 1
        for count in counts:
            denominator *= facts[count]
        total_count += facts[n] // denominator
    return total_count


def main():
    exhaustive_cases = 0
    for n in range(2, 8):
        minimum, count = prediction(n)
        observed = exhaustive_open_neighborhood_check(n)
        assert observed == {minimum: count}, (n, observed, minimum, count)
        exhaustive_cases += 1
    composition_cases = 0
    for n in range(8, 13):
        assert independent_column_type_count(n) == prediction(n)[1], n
        composition_cases += 1
    print(f"VERIFY_OK: {exhaustive_cases} exhaustive graphs, "
          f"{composition_cases} independent column-multiset counts")


if __name__ == '__main__':
    main()
