"""Independent finite sanity checks for the exact binary three-factor deletion theorem.

The infinite assertion is established in RESULT.md; finite enumeration alone
cannot prove it.  Uses only the Python standard library.
"""
from itertools import combinations, product
from collections import Counter


def words(n):
    return [''.join(xs) for xs in product('01', repeat=n)]


def enumerate_triplets(n):
    W = words(n)
    vertices = words(n - 1)
    vid = {s: j for j, s in enumerate(vertices)}
    E = [(vid[s[:-1]], vid[s[1:]]) for s in W]
    answer = Counter()
    rejected = set()
    all_compatible = set()
    for tri in combinations(range(len(W)), 3):
        delta = Counter()
        for eid in tri:
            a, b = E[eid]
            delta[a] += 1
            delta[b] -= 1
        signs = sorted(x for x in delta.values() if x)
        if signs not in ([], [-1, 1]):
            continue
        all_compatible.add(tri)
        answer['degree_compatible'] += 1
        answer['balanced' if not signs else 'open'] += 1
        nloops = sum(E[eid][0] == E[eid][1] for eid in tri)
        assert nloops <= 2
        twocycle = any(
            E[i][0] == E[j][1] and E[i][1] == E[j][0]
            for i, j in combinations(tri, 2)
        )
        answer[f'loops_{nloops}_two_cycle_{int(twocycle)}_open_{int(bool(signs))}'] += 1
        removed = set(tri)
        adj = [set() for _ in vertices]
        active = set()
        for eid, (a, b) in enumerate(E):
            if eid in removed:
                continue
            adj[a].add(b)
            adj[b].add(a)
            active.add(a)
            active.add(b)
        todo = [next(iter(active))]
        visited = set()
        while todo:
            v = todo.pop()
            if v not in visited:
                visited.add(v)
                todo.extend(adj[v] - visited)
        if visited == active:
            answer['universal_word'] += 1
        else:
            rejected.add(tri)
    answer['disconnects'] = len(rejected)
    return W, E, answer, rejected, all_compatible


def predicted_exceptions(W, E):
    n = len(W[0]); eid = {w: i for i, w in enumerate(W)}
    bad = set()
    for a, b in [('0', '1'), ('1', '0')]:
        leaving = a * (n - 1) + b
        entering = b + a * (n - 1)
        tail_of_out = a * (n - 2) + b
        head_of_in = b + a * (n - 2)
        choices = [b * n]
        choices += [tail_of_out + c for c in '01']
        choices += [c + head_of_in for c in '01']
        assert len(set(choices)) == 5
        for t in choices:
            bad.add(tuple(sorted([eid[leaving], eid[entering], eid[t]])))
    assert len(bad) == 10
    return bad


def run():
    for n in range(4, 8):
        W, E, got, bad, compatible = enumerate_triplets(n)
        N = 2 ** n
        assert got['balanced'] == 4
        assert got['loops_2_two_cycle_0_open_1'] == N - 2
        assert got['loops_1_two_cycle_1_open_0'] == 2
        assert got['loops_1_two_cycle_0_open_1'] == 4 * N - 16
        assert got['loops_0_two_cycle_1_open_1'] == N - 4
        assert got['loops_0_two_cycle_0_open_0'] == 2
        assert got['loops_0_two_cycle_0_open_1'] == 4 * N - 28
        assert got['degree_compatible'] == 10 * N - 46
        assert bad == predicted_exceptions(W, E)
        assert got['universal_word'] == 10 * N - 56
        assert got['disconnects'] == 10
        print(f'n={n} total={N*(N-1)*(N-2)//6} '
              f'compatible={got["degree_compatible"]} '
              f'disconnected={got["disconnects"]} '
              f'valid={got["universal_word"]}')
    print('PASS (finite checks only; proof in RESULT.md)')


if __name__ == '__main__':
    run()
