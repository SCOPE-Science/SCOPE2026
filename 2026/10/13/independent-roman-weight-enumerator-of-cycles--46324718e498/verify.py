from collections import Counter
from itertools import product
from math import ceil, factorial


def is_irdf(labels):
    n = len(labels)
    for i in range(n):
        if labels[i] > 0 and labels[(i + 1) % n] > 0:
            return False
    for i, value in enumerate(labels):
        if value == 0 and labels[(i - 1) % n] != 2 and labels[(i + 1) % n] != 2:
            return False
    return True


def gap_characterization(labels):
    n = len(labels)
    twos = [i for i, value in enumerate(labels) if value == 2]
    if not twos:
        return False
    patterns = {
        2: [2, 0, 2],
        3: [2, 0, 0, 2],
        4: [2, 0, 1, 0, 2],
    }
    for j, start in enumerate(twos):
        finish = twos[(j + 1) % len(twos)]
        distance = (finish - start) % n
        if distance == 0:
            distance = n
        expected = patterns.get(distance)
        if expected is None:
            return False
        actual = [labels[(start + t) % n] for t in range(distance + 1)]
        if actual != expected:
            return False
    return True


def formula(n):
    result = Counter()
    for a in range(n // 2 + 1):
        for b in range(n // 3 + 1):
            for c in range(n // 4 + 1):
                k = a + b + c
                if k and 2 * a + 3 * b + 4 * c == n:
                    count = n * factorial(k - 1) // (factorial(a) * factorial(b) * factorial(c))
                    result[2 * a + 2 * b + 3 * c] += count
    return result


def minimum_count(n):
    if n % 3 == 0:
        return 3
    if n % 3 == 1:
        return n
    return n * (n + 1) // 6


def main():
    labelings = 0
    valid_functions = 0
    criterion_checks = 0
    coefficient_checks = 0
    minimum_checks = 0

    for n in range(5, 13):
        brute = Counter()
        for labels in product(range(3), repeat=n):
            labelings += 1
            literal = is_irdf(labels)
            structural = gap_characterization(labels)
            if literal != structural:
                raise AssertionError(("criterion", n, labels, literal, structural))
            criterion_checks += 1
            if literal:
                valid_functions += 1
                brute[sum(labels)] += 1

        predicted = formula(n)
        for weight in range(0, 2 * n + 1):
            if brute[weight] != predicted[weight]:
                raise AssertionError(("coefficient", n, weight, brute[weight], predicted[weight]))
            coefficient_checks += 1

        best = min(brute)
        if best != ceil(2 * n / 3):
            raise AssertionError(("minimum", n, best))
        if brute[best] != minimum_count(n):
            raise AssertionError(("minimum-count", n, brute[best], minimum_count(n)))
        minimum_checks += 1

    print(
        "VERIFY_OK n_range=5..12 "
        f"labelings={labelings} irdf_functions={valid_functions} "
        f"criterion_checks={criterion_checks} coefficient_checks={coefficient_checks} "
        f"minimum_checks={minimum_checks} max_order=12"
    )


if __name__ == "__main__":
    main()
