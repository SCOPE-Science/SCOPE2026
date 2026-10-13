from collections import defaultdict
from math import ceil


def build_spider(d, a, c):
    assert d >= 3 and 1 <= a <= c
    lengths = [a] * (d - 1) + [c]
    adj = [[]]
    meta = [("center", 0, 0)]
    next_v = 1
    for arm, length in enumerate(lengths):
        prev = 0
        kind = "short" if arm < d - 1 else "long"
        for x in range(1, length + 1):
            adj.append([])
            meta.append((kind, x, length))
            adj[prev].append(next_v)
            adj[next_v].append(prev)
            prev = next_v
            next_v += 1
    return adj, meta


def partition(colors):
    classes = defaultdict(list)
    for v, color in enumerate(colors):
        classes[color].append(v)
    return tuple(sorted(tuple(vs) for vs in classes.values()))


def refinement_partitions(adj):
    colors = [0] * len(adj)
    parts = [partition(colors)]
    while True:
        signatures = [
            (colors[v], tuple(sorted(colors[w] for w in adj[v])))
            for v in range(len(adj))
        ]
        palette = {s: i for i, s in enumerate(sorted(set(signatures), key=repr))}
        new_colors = [palette[s] for s in signatures]
        new_part = partition(new_colors)
        if new_part == parts[-1]:
            return parts
        colors = new_colors
        parts.append(new_part)


def predicted_partition(meta, r):
    if r == 0:
        return partition([("uniform",)] * len(meta))
    descriptors = []
    for _, x, length in meta:
        if length == 0:
            descriptors.append(("center",))
        elif x == length:
            descriptors.append(("leaf", min(length, r)))
        else:
            descriptors.append(("internal", min(x, r), min(length - x, r)))
    return partition(descriptors)


def predicted_depth(a, c):
    if c == a:
        return ceil(a / 2)
    return max(a + 1, ceil(c / 2))


def main():
    depth_cases = 0
    for d in range(3, 9):
        for a in range(1, 21):
            for c in range(a, 51):
                adj, _ = build_spider(d, a, c)
                depth = len(refinement_partitions(adj)) - 1
                expected = predicted_depth(a, c)
                assert depth == expected, (d, a, c, depth, expected)
                depth_cases += 1

    profile_checks = 0
    for d in range(3, 8):
        for a in range(1, 11):
            for c in range(a, 26):
                adj, meta = build_spider(d, a, c)
                parts = refinement_partitions(adj)
                for r, actual in enumerate(parts):
                    expected = predicted_partition(meta, r)
                    assert actual == expected, (d, a, c, r)
                    profile_checks += 1
                # The descriptor at the next round must already give the same stable partition.
                r = len(parts)
                assert predicted_partition(meta, r) == parts[-1], (d, a, c, r)
                profile_checks += 1

    print(
        "VERIFY_OK "
        f"depth_cases={depth_cases} "
        f"profile_checks={profile_checks} "
        "d_depth=3..8 a_depth=1..20 c_depth=a..50 "
        "d_profile=3..7 a_profile=1..10 c_profile=a..25"
    )


if __name__ == "__main__":
    main()
