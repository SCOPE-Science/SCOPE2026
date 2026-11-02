"""Executable finite checks for weight-two circular coverings (Python >= 3.8).

The all-order lower bound is mathematical (periodicity/Fine--Wilf), not
established by these finite tests.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb


def mandatory_words(n):
    result = set()
    for i, j in combinations(range(n), 2):
        w = ['0'] * n
        w[i] = w[j] = '1'
        result.add(''.join(w))
    return result


def rotate(w):
    return w[1:] + w[0]


def necklaces(n):
    unvisited = mandatory_words(n)
    answer = []
    while unvisited:
        start = min(unvisited)
        orbit = []
        w = start
        while w in unvisited:
            unvisited.remove(w)
            orbit.append(w)
            w = rotate(w)
        assert w == start
        answer.append(orbit)
    return answer


def euler_cover(n):
    assert n >= 4
    required = mandatory_words(n)
    bridge = '1' + '0' * (n-2) + '1'
    added = [bridge]
    for j in range(1, n - 1):
        added.append('0' * j + '1' + '0' * (n-j-1))
    assert len(added) == n - 1
    assert sum(w.count('1') == 2 for w in added) == 1
    assert all(w.count('1') == 1 for w in added[1:])
    assert bridge in required
    graph = defaultdict(list)
    for word in sorted(required) + added:
        graph[word[:-1]].append((word[1:], word))
    count = sum(map(len, graph.values()))
    start = min(graph)
    stack = [(start, None)]
    tour = []
    while stack:
        v = stack[-1][0]
        if graph[v]:
            nxt, label = graph[v].pop()
            stack.append((nxt, label))
        else:
            _, last = stack.pop()
            if last is not None:
                tour.append(last)
    tour.reverse()
    assert len(tour) == count, 'Not connected'
    assert all(tour[i][1:] == tour[(i+1) % count][:-1] for i in range(count))
    seq = ''.join(w[-1] for w in tour)
    windows = Counter(''.join(seq[(i+j) % count] for j in range(n))
                      for i in range(count))
    assert windows == Counter(sorted(required) + added), 'Incorrect cyclic windows'
    assert all(windows[w] > 0 for w in required)
    assert len(seq) == comb(n, 2) + n - 1
    assert windows[bridge] == 2
    assert sum(1 for w in required if windows[w] == 2) == 1
    assert all(windows[w] == 1 for w in required if w != bridge)
    assert len(necklaces(n)) >= 2
    return seq


def primitive_cycle(period):
    p = len(period)
    return all(period != (period[:d] * (p//d)) for d in range(1, p) if p%d == 0)


def short_cycle_checks(n):
    """Finite stress test for the critical period/bridge separation lemma."""
    cycle_vertex_sets = []
    seen = set()
    for p in range(1, n-1):
        for symbols in product('01', repeat=p):
            word = ''.join(symbols)
            if not primitive_cycle(word):
                continue
            rotations = [word[j:] + word[:j] for j in range(p)]
            key = min(rotations)
            if (p, key) in seen:
                continue
            seen.add((p, key))
            vertices = {''.join(word[(offset+j) % p] for j in range(n-1))
                        for offset in range(p)}
            assert len(vertices) == p
            cycle_vertex_sets.append((p, vertices))
    special = {'1'+'0'*(n-2), '0'*(n-2)+'1'}
    special.update('0'*j + '11' + '0'*(n-3-j) for j in range(n-2))
    required_vertices = {w[:-1] for w in mandatory_words(n)}
    other = required_vertices - special
    for i, (p, vs) in enumerate(cycle_vertex_sets):
        if vs & special:
            assert not (vs & other), (n, p, vs & special, vs & other)
        for q, ws in cycle_vertex_sets[i+1:]:
            if p+q <= n-2:
                assert not (vs & ws), (n, p, q, vs & ws)


def brute_force_small(n, optimum):
    """Exhaustive cyclic binary necklaces for n=4,5 (independent of graph proof)."""
    need = mandatory_words(n)
    for L in range(1, optimum):
        for bits in product('01', repeat=L):
            # Removing root duplicates is unnecessary, so this is exhaustive.
            if bits[0] != '0':
                continue  # every cover must have at least one zero; rotate to zero first
            factors = {''.join(bits[(i+j) % L] for j in range(n)) for i in range(L)}
            assert not need <= factors, (n, L, bits)


def main():
    for n in range(4, 16):
        cover = euler_cover(n)
        print('n={} size={} mandatory={} components={} cover={}'.format(
            n, len(cover), comb(n, 2), len(necklaces(n)), cover))
    for n in range(4, 10):
        short_cycle_checks(n)
    for n in (4, 5):
        brute_force_small(n, comb(n, 2) + n - 1)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
