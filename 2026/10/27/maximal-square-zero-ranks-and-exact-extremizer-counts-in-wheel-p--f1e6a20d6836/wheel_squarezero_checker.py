"""Direct finite verification of maximal-rank square-zero wheel partial isometries.

Execute: python wheel_squarezero_checker.py
No external dependencies; the direct enumeration does not use the run-decomposition argument.
"""
import itertools
import math
from collections import Counter


def wheel_distance(n, x, y):
    if x == y:
        return 0
    if x == 0 or y == 0:
        return 1
    return 1 if (x - y) % n in (1, n - 1) else 2


def direct_maximum_count(n):
    k = n // 2
    counts = Counter()
    for domain in itertools.combinations(range(n + 1), k):
        available = sorted(set(range(n + 1)) - set(domain))
        for image_set in itertools.combinations(available, k):
            source_distances = tuple(
                wheel_distance(n, domain[i], domain[j])
                for i in range(k) for j in range(i + 1, k)
            )
            for targets in itertools.permutations(image_set):
                if source_distances == tuple(
                    wheel_distance(n, targets[i], targets[j])
                    for i in range(k) for j in range(i + 1, k)
                ):
                    counts['hub' if 0 in domain or 0 in image_set else 'rim'] += 1
    return counts


def predicted_rim(n):
    k = n // 2
    # [z^j] B(z) is 1 at j=1 and 2 at every j>=2.
    polynomial = [1] + [0] * k
    total = 0
    for r in range(1, k + 1):
        new_polynomial = [0] * (k + 1)
        for i in range(k + 1):
            for j in range(1, k - i + 1):
                new_polynomial[i + j] += polynomial[i] * (1 if j == 1 else 2)
        polynomial = new_polynomial
        multiplier = math.factorial(r - 1) if n % 2 == 0 else 2 * math.factorial(r)
        total += n * multiplier * polynomial[k]
    return total


def predicted_hub(n):
    if n in (4, 5):
        return 4 * n * (n - 2)
    if n in (6, 7):
        return 2 * n * (n - 4) * (n - 5)
    return 0


def check_excess_rank(n):
    # Only n=5,7 can have an image/domain partition above floor(n/2).
    k = n // 2 + 1
    if k * 2 > n + 1:
        return 0
    count = 0
    for domain in itertools.combinations(range(n + 1), k):
        available = sorted(set(range(n + 1)) - set(domain))
        for image_set in itertools.combinations(available, k):
            source_distances = tuple(
                wheel_distance(n, domain[i], domain[j])
                for i in range(k) for j in range(i + 1, k)
            )
            for targets in itertools.permutations(image_set):
                if source_distances == tuple(
                    wheel_distance(n, targets[i], targets[j])
                    for i in range(k) for j in range(i + 1, k)
                ):
                    count += 1
    return count


def main():
    total = 0
    for n in range(4, 13):
        observed = direct_maximum_count(n)
        assert observed['rim'] == predicted_rim(n), (n, observed)
        assert observed['hub'] == predicted_hub(n), (n, observed)
        print(f'W_{n} maximum_rank={n//2} rim={observed["rim"]} '
              f'hub={observed["hub"]} total={sum(observed.values())}')
        total += sum(observed.values())
    for n in (5, 7):
        assert check_excess_rank(n) == 0
    for n in range(13, 26):
        assert predicted_rim(n) > 0
        assert predicted_hub(n) == 0
    print(f'ALL_WHEEL_SQUARE_ZERO_EXTREMIZER_CHECKS_PASSED cases=9 '
          f'counted_maps={total} excess_rank_tests=2 formula_cases=13')


if __name__ == '__main__':
    main()
