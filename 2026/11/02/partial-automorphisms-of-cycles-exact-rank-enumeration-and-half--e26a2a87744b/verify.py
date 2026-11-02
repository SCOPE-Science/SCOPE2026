"""Independent exact finite checks for induced-cycle partial graph automorphisms."""
from collections import Counter
from itertools import combinations, permutations
from math import comb, factorial


def partitions(k, cap=None):
    if cap is None:
        cap = k
    if k == 0:
        yield ()
    else:
        for x in range(min(cap, k), 0, -1):
            for tail in partitions(k - x, x):
                yield (x,) + tail


def coefficients(n):
    assert n >= 3
    out = [0] * (n + 1)
    out[0], out[n] = 1, 2 * n
    for k in range(1, n):
        for shape in partitions(k):
            counts = Counter(shape)
            r = len(shape)
            if r > n - k:
                continue
            multiplicity_factor = 1
            for m in counts.values():
                multiplicity_factor *= factorial(m)
            numerator = n * factorial(r - 1) * comb(n - k - 1, r - 1)
            assert numerator % multiplicity_factor == 0
            choices = numerator // multiplicity_factor
            aut = multiplicity_factor * 2 ** (r - counts[1])
            out[k] += choices * choices * aut
    return out


def exhaustive(n):
    result = [0] * (n + 1)

    def edge(x, y):
        return (x - y) % n in (1, n - 1)

    for k in range(n + 1):
        sets = list(combinations(range(n), k))
        for domain in sets:
            for image in sets:
                for assignment in permutations(image):
                    if all(edge(domain[i], domain[j]) ==
                           edge(assignment[i], assignment[j])
                           for i in range(k) for j in range(i)):
                        result[k] += 1
    return result


def main():
    expected = {
        3: [1, 9, 18, 6],
        4: [1, 16, 40, 32, 8],
        5: [1, 25, 100, 100, 50, 10],
        6: [1, 36, 234, 384, 216, 72, 12],
        7: [1, 49, 490, 1274, 1078, 392, 98, 14],
        8: [1, 64, 928, 3712, 4832, 2432, 640, 128, 16],
        9: [1, 81, 1620, 9612, 18954, 14256, 4806, 972, 162, 18],
    }
    for n in range(3, 10):
        by_partitions = coefficients(n)
        by_graphs = exhaustive(n)
        assert by_partitions == by_graphs == expected[n], (n, by_partitions, by_graphs)
        print('n=', n, 'rank_counts=', by_partitions, 'total=', sum(by_partitions))
    assert coefficients(20)[19] == 800
    assert coefficients(20)[18] == 13600
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
