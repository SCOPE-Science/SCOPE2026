#!/usr/bin/env python3
"""Independent distance-quotient color refinement using exact transition counts."""


def matrix(n, k):
    d = n // 2
    strata = [[j, n - j] if j and 2 * j != n else [j] for j in range(d + 1)]
    # j=0 is [0]; every element of each other stratum is symmetric.
    assert strata[0] == [0]
    assert sorted(v for stratum in strata for v in stratum) == list(range(n))
    return [[sum(1 for v in strata[i] if min((j - v) % n, (v - j) % n) <= k and v != j)
             for i in range(d + 1)] for j in range(d + 1)]


def partition_evolution(n, k):
    q = matrix(n, k)
    d = n // 2
    colors = [1] + [0] * d
    layers = [colors[:]]
    while True:
        sig = [(colors[j], tuple(sum(q[j][i] for i in range(d + 1) if colors[i] == c)
                                  for c in sorted(set(colors)))) for j in range(d + 1)]
        palette = {p: i for i, p in enumerate(sorted(set(sig)))}
        nc = [palette[x] for x in sig]
        if len(set(nc)) == len(set(colors)):
            break
        layers.append(nc)
        colors = nc
    return layers


def main():
    cases = boundary = profile_checks = 0
    for k in range(1, 13):
        for n in range(4 * k + 1, min(4 * k + 71, 136)):
            layers = partition_evolution(n, k)
            assert len(layers) - 1 == (n // 2 - 2) // k + 1, (n, k, 'depth')
            for r, colors in enumerate(layers):
                if r == 0:
                    expected = [0] + [1] * (n // 2)
                elif r == 1:
                    expected = [0] + [1 if j <= k else 2 for j in range(1, n // 2 + 1)]
                else:
                    expected = [j if j <= r * k else r * k + 1 for j in range(n // 2 + 1)]
                a, b = {}, {}
                for j, c in enumerate(colors):
                    e = expected[j]
                    assert a.setdefault(c, e) == e, (n, k, r, j)
                    assert b.setdefault(e, c) == c, (n, k, r, j)
                    profile_checks += 1
            cases += 1
    for k in range(2, 31):
        layers = partition_evolution(4 * k, k)
        assert len(layers) - 1 == 3, (k, len(layers) - 1)
        # At the second round, precisely the two antipodal-most strata coalesce.
        c = layers[2]
        assert c[2 * k - 1] == c[2 * k]
        assert all(c[i] != c[j] for i in range(2 * k + 1) for j in range(i + 1, 2 * k + 1)
                   if (i, j) != (2 * k - 1, 2 * k))
        assert len(set(layers[3])) == 2 * k + 1
        boundary += 1
    print(f'quotient_main_cases={cases}')
    print(f'quotient_boundary_cases={boundary}')
    print(f'quotient_profile_checks={profile_checks}')
    print('ALL_TESTS_PASS')


if __name__ == '__main__':
    main()
