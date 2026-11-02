#!/usr/bin/env python3
"""Exact, self-contained finite checks for the three-progression gap-sum theorem.

Uses dynamic semigroup membership and independently enumerated Minkowski sums.
The finite checks are supplementary to the mathematical proof.
"""


def enumerate_gaps(g):
    generators = (6, 9, g, g + 3)
    upper = 2 * g + 20
    representable = [False] * (upper + 1)
    representable[0] = True
    for v in range(1, upper + 1):
        representable[v] = any(
            v >= generator and representable[v - generator]
            for generator in generators
        )
    return {v for v in range(1, upper + 1) if not representable[v]}


def predicted_sumset(g, h):
    F = 2 * g - 3
    full = set(range(h, h * F + 1))
    holes_1 = {h * F - g + 3 * j for j in range(1, g // 3 + 1)}
    holes_2 = {
        h * F - (2 * g - 6) + 3 * j
        for j in range(1, (2 * g - 6) // 3 + 1)
    }
    assert holes_1.isdisjoint(holes_2)
    assert holes_1 | holes_2 <= full
    return full - (holes_1 | holes_2)


def run():
    checked = 0
    sampled = []
    for g in range(13, 121):
        if g % 3 == 0:
            continue
        G = enumerate_gaps(g)
        F = 2 * g - 3
        assert len(G) == g and max(G) == F, (g, len(G))
        current = {0}
        for h in range(1, 13):
            current = {u + v for u in current for v in G}
            exact = predicted_sumset(g, h)
            assert current == exact, (g, h, min(current ^ exact))
            expected_size = (2 * h - 1) * g - 4 * h + 4
            assert len(current) == expected_size, (g, h)
            if h >= 2:
                assert ((2 * h - 1) * (g - 1) - len(current) == 2 * h - 3)
            checked += 1
        if g in (13, 14, 16, 17, 19, 20, 100, 101, 119):
            sampled.append((g, len(G), len(predicted_sumset(g, 2)),
                            len(predicted_sumset(g, 3))))
    print('VERIFY_OK', 'parameter_pairs=', checked, 'samples=', sampled)


if __name__ == '__main__':
    run()
