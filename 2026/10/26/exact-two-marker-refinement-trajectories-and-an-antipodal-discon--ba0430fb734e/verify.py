"""Direct counting-colour-refinement test on two-individualized cycles."""
from collections import defaultdict


def partition(values):
    buckets = defaultdict(set)
    for vertex, value in values.items():
        buckets[value].add(vertex)
    return frozenset(map(frozenset, buckets.values()))


def iterate_colours(n, a, b):
    colours = {x: 0 if x == a else (1 if x == b else 2) for x in range(n)}
    for round_index in range(n + 1):
        yield round_index, partition(colours)
        keys = {x: (colours[x], tuple(sorted((colours[(x - 1) % n], colours[(x + 1) % n])))) for x in range(n)}
        palette = {key: i for i, key in enumerate(sorted(set(keys.values())))}
        colours = {x: palette[keys[x]] for x in range(n)}


def theorem_depth(n, t):
    if 2 * t == n:
        return (t - 1) // 2
    return max(t - 1, (n - t - 1) // 2)


def truncated_partition(n, a, b, round_index):
    radius = round_index + 1
    d = lambda x, y: min((x - y) % n, (y - x) % n)
    return partition({x: (min(d(x, a), radius), min(d(x, b), radius)) for x in range(n)})


def main():
    configurations = comparisons = 0
    for n in range(3, 91):
        for t in range(1, n // 2 + 1):
            configurations += 1
            depth = theorem_depth(n, t)
            steps = list(iterate_colours(n, 0, t))
            for r, part in steps:
                expected = truncated_partition(n, 0, t, r)
                assert part == expected, (n, t, r, 'round partition')
                comparisons += 1
            earliest_stable = next(r for r, part in steps if part == steps[-1][1])
            assert earliest_stable == depth, (n, t, earliest_stable, depth)
            stable_count = n // 2 + 1 if 2 * t == n else n
            assert len(steps[-1][1]) == stable_count, (n, t, 'stable classes')
            assert all(steps[r][1] != steps[r + 1][1] for r in range(depth))
    print(f'ALL_TESTS_PASS configurations={configurations} round_partitions={comparisons}')


if __name__ == '__main__':
    main()
