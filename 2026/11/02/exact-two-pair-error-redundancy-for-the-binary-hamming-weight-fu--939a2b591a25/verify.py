"""Independent exhaustive checks of a four-periodic check label for pair-read function coding."""
from itertools import product


def check_bits(weight):
    return (weight & 1, (weight >> 1) & 1, weight & 1)


def encode(message):
    return tuple(message) + check_bits(sum(message))


def pair_distance(x, y):
    n = len(x)
    return sum((x[i] != y[i] or x[(i + 1) % n] != y[(i + 1) % n]) for i in range(n))


def main():
    tested = 0
    minima = {}
    for k in range(2, 12):
        words = list(product(range(2), repeat=k))
        codewords = [encode(w) for w in words]
        weights = [sum(w) for w in words]
        minimum = k + 3
        for i, a in enumerate(codewords):
            for j in range(i):
                if weights[i] != weights[j]:
                    distance = pair_distance(a, codewords[j])
                    if distance < 5:
                        raise AssertionError((k, words[i], words[j], distance))
                    minimum = min(distance, minimum)
                    tested += 1
        assert minimum == 5, (k, minimum)
        minima[k] = minimum
    for k in range(1, 40):
        for r in range(0, 3):
            prefix_a = (0,) * k
            prefix_b = (0,) * (k - 1) + (1,)
            for p in product(range(2), repeat=r):
                for q in product(range(2), repeat=r):
                    assert pair_distance(prefix_a + p, prefix_b + q) <= 4
    for k in range(1, 15):
        assert pair_distance((0,) * (k + 4), (1,) * (k + 4)) == k + 4
    print('PAIR_WEIGHT_FCC_VERIFY_OK', tested, 'distinct-weight unordered message pairs', len(minima), 'complete lengths')
    print('minima', minima)


if __name__ == '__main__':
    main()
