"""Independent direct checker for edge-deletion sensitivity of cycle powers.

Run: python3 verify.py. No external libraries required.
"""
from itertools import combinations


def graph(n, k, d):
    g = [set() for _ in range(n)]
    for a in range(n):
        for b in range(a + 1, n):
            if min(b-a, n-(b-a)) <= k and (a, b) != (0, d):
                g[a].add(b)
                g[b].add(a)
    return g


def closes(g, initial):
    blue = set(initial)
    while True:
        forced = set()
        for v in blue:
            white = g[v] - blue
            if len(white) == 1:
                forced.update(white)
        if not forced:
            return len(blue) == len(g)
        blue.update(forced)


def predicted_sets(g, n, k, d):
    if d != k:
        return set()
    ans = set()
    for center in (0, d):
        for w in g[center]:
            ans.add(frozenset((g[center] - {w}) | {center}))
    return ans


def main():
    cases = 0
    configurations = 0
    for k in range(1, 5):
        for n in range(2*k + 3, 2*k + 11):
            for d in range(1, k + 1):
                g = graph(n, k, d)
                expected = predicted_sets(g, n, k, d)
                got = set()
                for tup in combinations(range(n), 2*k-1):
                    configurations += 1
                    if closes(g, tup):
                        got.add(frozenset(tup))
                assert got == expected, (k,n,d,len(got),len(expected))
                assert len(got) == (4*k-2 if d == k else 0)
                if d < k:
                    # Test an explicit ordinary-size forcing seed; first-step necessity
                    # rules out any smaller size, as explained in the proof.
                    consecutive = {i % n for i in range(-k, k)}
                    assert closes(g, consecutive), (k,n,d)
                cases += 1
    print('ALL_EDGE_LENGTH_CASES_OK', cases)
    print('EXHAUSTIVE_MINIMUM_CANDIDATES_OK', configurations)
    print('OPTIMAL_SEED_COUNT_OK 4k-2 when d=k, zero when d<k')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
