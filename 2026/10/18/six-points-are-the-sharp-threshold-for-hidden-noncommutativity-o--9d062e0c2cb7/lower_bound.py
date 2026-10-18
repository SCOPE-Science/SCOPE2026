"""Complete finite lower-bound check in the binary-relation signature."""
from collections import Counter, defaultdict
from itertools import permutations


def local_atomic_histograms(f, g):
    n = len(f)
    finv = [0] * n
    ginv = [0] * n
    for a in range(n):
        finv[f[a]] = a
        ginv[g[a]] = a
    point_histograms = []
    for a in range(n):
        counts = Counter()
        for b in range(n):
            atomic = (
                a == b, f[a] == b, f[b] == a,
                g[a] == b, g[b] == a
            )
            counts[atomic] += 1
        point_histograms.append(tuple(sorted(counts.items())))
    return tuple(sorted(Counter(point_histograms).items()))


def commute(f, g):
    return all(f[g[i]] == g[f[i]] for i in range(len(f)))


def main():
    for n in range(1, 6):
        p = list(permutations(range(n)))
        flags = {}
        compared = 0
        for f in p:
            for g in p:
                key = local_atomic_histograms(f, g)
                commuting = commute(f, g)
                if key in flags:
                    assert flags[key] == commuting, (n, f, g)
                else:
                    flags[key] = commuting
                compared += 1
        assert compared == len(p)**2
        print(f"n={n}, ordered_permutation_pairs={compared}, first_round_profiles={len(flags)}, ambiguous=0")
    print("LOWER_BOUND_PASS")


if __name__ == '__main__':
    main()
