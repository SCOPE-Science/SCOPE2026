"""Exact finite certificates for packing five-domatic coloring of cycles.

No nonstandard dependencies. Invoke: python3 verify.py
The all-length conclusion also uses the written eight-symbol splicing lemma.
"""
import itertools
import json
from pathlib import Path

DATA = json.loads(Path(__file__).with_name('witnesses.json').read_text(encoding='utf-8'))


def distance(n, i, j):
    delta = abs(i - j)
    return min(delta, n - delta)


def valid_word(radii, layers):
    n = len(radii)
    if n < 5 or n != len(layers) or any(not 1 <= x <= 6 for x in radii) or any(not 0 <= x < 5 for x in layers):
        return False
    for u in range(n):
        for v in range(u + 1, n):
            if radii[u] == radii[v] and distance(n, u, v) <= radii[u]:
                return False
    for v in range(n):
        for a in range(5):
            if not any(layers[u] == a and distance(n, u, v) <= radii[u] for u in range(n)):
                return False
    return True


def record(n):
    x = DATA[str(n)]
    return [int(j) for j in x['radii']], [int(a) for a in x['layers']]


def negative_four_color_certificate(n):
    """Enumerate EVERY length-n 4-palette packing word, not just optimized words.

    A radius-depth < 5 is an obstruction. For radius-depth >= 5,
    a 5-covered vertex forces all 5 covering broadcasters to have distinct layers;
    the resulting forced-distinct graph contains K6 in the sole exceptional case.
    """
    f = []
    stats = [0, 0, 0]

    def analyze():
        for j in range(1, 5):
            positions = [v for v in range(n) if f[v] == j]
            if any(distance(n, u, v) <= j for u, v in itertools.combinations(positions, 2)):
                return
        stats[0] += 1
        covering = [tuple(u for u in range(n) if distance(n, u, v) <= f[u]) for v in range(n)]
        if any(len(C) < 5 for C in covering):
            return
        stats[1] += 1
        # Construct the forced-distinct graph from all exactly-five covers.
        adj = [0] * n
        for C in covering:
            if len(C) == 5:
                for u, v in itertools.combinations(C, 2):
                    adj[u] |= 1 << v
                    adj[v] |= 1 << u
        six_clique = False
        for C in itertools.combinations(range(n), 6):
            if all((adj[u] >> v) & 1 for u, v in itertools.combinations(C, 2)):
                six_clique = True
                break
        if six_clique:
            stats[2] += 1
        else:
            raise AssertionError(('unresolved four-color candidate', n, f[:]))

    def dfs(i):
        if i == n:
            analyze()
            return
        for j in range(1, 5):
            if any(f[h] == j for h in range(max(0, i-j), i)):
                continue
            f.append(j)
            dfs(i + 1)
            f.pop()

    dfs(0)
    return tuple(stats)


def rotate_after_common_prefix(word):
    return word[8:] + word[:8]


def constructed(n):
    """Construct for every n>=30 by splicing with a ten-vertex periodic word."""
    assert n >= 30
    s = 30 + (n - 30) % 10
    q = (n - s) // 10
    rf, ra = record(s)
    bf, ba = record(10)
    assert (rf[:8], ra[:8]) == (bf[:8], ba[:8])
    rf, ra = rotate_after_common_prefix(rf), rotate_after_common_prefix(ra)
    bf, ba = rotate_after_common_prefix(bf), rotate_after_common_prefix(ba)
    return rf + bf * q, ra + ba * q


def main():
    for n in sorted(map(int, DATA)):
        f, a = record(n)
        assert len(f) == len(a) == n, n
        assert valid_word(f, a), n
        target = 6 if n in (5, 6) else 5 if n in (7, 8, 9, 11, 12, 13, 14, 18) else 4
        assert max(f) == target, n
    print('BASE_WITNESSES_OK', len(DATA))

    expected = {
        7: (28, 0, 0), 8: (68, 0, 0), 9: (72, 0, 0),
        11: (440, 44, 44), 12: (760, 0, 0), 13: (1092, 0, 0),
        14: (1554, 0, 0), 18: (17172, 0, 0),
    }
    for n, counts in expected.items():
        got = negative_four_color_certificate(n)
        assert got == counts, (n, got, counts)
    print('EXHAUSTIVE_NEGATIVE_FOUR_PALETTE_OK', sum(x[0] for x in expected.values()))
    print('ELEVEN_VERTEX_K6_OBSTRUCTION_OK', expected[11][1])

    # Checks instances of the proof's indefinite construction, not a substitute
    # for the splicing lemma proved in RESULT.md.
    for n in range(30, 221):
        f, a = constructed(n)
        assert len(f) == n and valid_word(f, a), n
        assert max(f) == 4
    print('SPLICING_CONSTRUCTION_TEST_OK', 191)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
