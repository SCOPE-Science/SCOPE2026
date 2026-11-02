"""Standalone finite check of maximal-index nilpotents in cluster-graph partial automorphism monoids."""
from itertools import permutations
from math import factorial


def partitions(n, least=1):
    if n == 0:
        yield ()
        return
    for x in range(least, n + 1):
        for suffix in partitions(n - x, x):
            yield (x,) + suffix


def direct_count(sizes):
    vertex_parts = tuple(j for j, size in enumerate(sizes) for _ in range(size))
    n = len(vertex_parts)
    count = 0
    for ordering in permutations(range(n)):
        source = ordering[:-1]
        target = ordering[1:]
        valid = True
        for i in range(n - 1):
            for j in range(i + 1, n - 1):
                a = vertex_parts[source[i]] == vertex_parts[source[j]]
                b = vertex_parts[target[i]] == vertex_parts[target[j]]
                if a != b:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            count += 1
    return count


def proposed_count(sizes):
    if max(sizes) - min(sizes) > 1:
        return 0
    r = len(sizes)
    n = sum(sizes)
    t = n % r
    placements = factorial(r) if t == 0 else factorial(t) * factorial(r - t)
    for s in sizes:
        placements *= factorial(s)
    return placements


def main():
    configurations = 0
    for n in range(2, 8):
        for sizes in partitions(n):
            got = direct_count(sizes)
            expected = proposed_count(sizes)
            assert got == expected, (sizes, got, expected)
            configurations += 1
    for sizes in [(4, 4), (3, 3, 2), (4, 3, 1), (2, 2, 2, 2)]:
        got = direct_count(sizes)
        expected = proposed_count(sizes)
        assert got == expected, (sizes, got, expected)
        configurations += 1
    assert proposed_count((3, 2)) == 12
    assert proposed_count((3, 3)) == 72
    assert proposed_count((2, 2, 1)) == 8
    assert proposed_count((4, 2)) == 0
    print(f"VERIFY_OK cluster partial-automorphism nilpotents: {configurations} exhaustive configurations")


if __name__ == "__main__":
    main()
