"""Independent complete finite proof by canonical set-partition enumeration."""
from collections import Counter

EXPECTED = {
    1: (1,), 2: (1, 1), 3: (1, 3), 4: (1, 7, 1),
    5: (1, 15, 4), 6: (1, 31, 17), 7: (1, 63, 55),
    8: (1, 127, 180, 3), 9: (1, 255, 539, 23),
    10: (1, 511, 1658, 134), 11: (1, 1023, 4880, 608, 4),
}
BELLS = (0, 1, 2, 5, 15, 52, 203, 877, 4140, 21147, 115975, 678570)


def canonical_partitions(n):
    def extend(prefix, maximum):
        if len(prefix) == n:
            yield tuple(prefix)
        else:
            for x in range(maximum + 2):
                prefix.append(x)
                yield from extend(prefix, max(x, maximum))
                prefix.pop()
    yield from extend([0], 0)


def border_array(word):
    n = len(word)
    result = [0] * n
    for length in range(2, n + 1):
        left = [0] * n
        right = [0] * n
        for border in range(1, length):
            left[word[border - 1]] += 1
            right[word[length - border]] += 1
            if left == right:
                result[length - 1] = border
    return tuple(result)


def main():
    for n in range(1, 12):
        minima = {}
        visited = 0
        for word in canonical_partitions(n):
            visited += 1
            profile = border_array(word)
            rank = max(word) + 1
            if rank < minima.get(profile, n + 1):
                minima[profile] = rank
        counts = Counter(minima.values())
        actual = tuple(counts[i] for i in range(1, len(EXPECTED[n]) + 1))
        assert visited == BELLS[n], (n, visited)
        assert actual == EXPECTED[n], (n, actual)
        assert sum(actual) == len(minima)
        print(n, visited, actual)
    print("INDEPENDENT_VERIFY_OK")


if __name__ == "__main__":
    main()
