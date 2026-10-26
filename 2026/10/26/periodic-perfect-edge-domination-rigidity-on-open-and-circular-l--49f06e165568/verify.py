"""Exact local-state and independent subset tests for perfect edge domination on 2-row ladders."""
from collections import Counter
from itertools import combinations


def bits(t):
    return ((t >> 2) & 1, (t >> 1) & 1, t & 1)


def admissible(left, middle, right):
    _, a0, b0 = bits(left)
    r1, a1, b1 = bits(middle)
    r2, a2, b2 = bits(right)
    return (
        (r1 == 1 or a0 + b0 + a1 + b1 == 1)
        and (a1 == 1 or a0 + a2 + r1 + r2 == 1)
        and (b1 == 1 or b0 + b2 + r1 + r2 == 1)
    )


def automaton():
    d = {u: [] for u in range(64)}
    for x in range(8):
        for y in range(8):
            u = 8 * x + y
            for z in range(8):
                if admissible(x, y, z):
                    d[u].append(8 * y + z)
    return d


def accessible(G, starts):
    seen = set(starts)
    stack = list(starts)
    while stack:
        for t in G[stack.pop()]:
            if t not in seen:
                seen.add(t)
                stack.append(t)
    return seen


def start_and_terminal(G):
    initial = set(range(8))
    terminal = {
        8*x+y for x in range(8) for y in (0, 4)
        if bits(y)[0] == 1 or bits(x)[1] + bits(x)[2] == 1
    }
    reverse = {i: [] for i in range(64)}
    for u, adj in G.items():
        for v in adj:
            reverse[v].append(u)
    active = accessible(G, initial) & accessible(reverse, terminal)
    return initial, terminal, active


def edge_sets(n, circular):
    es = [(('t', i), ('b', i)) for i in range(n)]
    for layer in ('t', 'b'):
        for i in range(n-1):
            es.append(((layer, i), (layer, i+1)))
        if circular:
            es.append(((layer, n-1), (layer, 0)))
    return es


def exhaustive_poly(n, circular):
    edges = edge_sets(n, circular)
    m = len(edges)
    masks = []
    for i, e in enumerate(edges):
        neigh = sum(1 << j for j, f in enumerate(edges)
                    if i != j and (e[0] in f or e[1] in f))
        masks.append(neigh)
    counts = Counter()
    for choice in range(1 << m):
        if all((choice & masks[i]).bit_count() == 1
               for i in range(m) if not ((choice >> i) & 1)):
            counts[choice.bit_count()] += 1
    return dict(counts)


def transfer_poly_open(n, G):
    initial, final, _ = start_and_terminal(G)
    dp = Counter({(s, 0): 1 for s in initial})
    for _ in range(n-1):
        out = Counter()
        for (s, w), multiplicity in dp.items():
            for t in G[s]:
                middle = s % 8
                out[t, w+sum(bits(middle))] += multiplicity
        dp = out
    result = Counter()
    for (state, w), count in dp.items():
        if state in final:
            r = bits(state % 8)[0]
            result[w+r] += count
    return dict(result)


def transfer_poly_circular(n, G):
    result = Counter()
    for initial_state in range(64):
        dp = Counter({(initial_state, 0): 1})
        for _ in range(n):
            out = Counter()
            for (state, w), count in dp.items():
                for next_state in G[state]:
                    out[next_state, w+sum(bits(state % 8))] += count
            dp = out
        for (state, w), count in dp.items():
            if state == initial_state:
                result[w] += count
    return dict(result)


def verify():
    G = automaton()
    assert sum(map(len, G.values())) == 102
    start, finish, act = start_and_terminal(G)
    active_rows = {
        1: [12, 13], 2: [20, 22], 4: [], 5: [40], 6: [48],
        7: [60, 63], 12: [], 13: [40], 20: [], 22: [48],
        40: [2], 48: [1], 60: [], 63: [60, 63],
    }
    assert act == set(active_rows)
    assert {s: [t for t in G[s] if t in act] for s in sorted(act)} == active_rows
    # All strongly connected directed cycles in the full graph consist
    # of this loop and the specified six-cycle. Verify by reachability.
    components = []
    remaining = set(range(64))
    reach = {i: accessible(G, [i]) for i in range(64)}
    while remaining:
        u = min(remaining)
        comp = {v for v in remaining if v in reach[u] and u in reach[v]}
        remaining.difference_update(comp)
        if len(comp)>1 or u in G[u]:
            components.append(comp)
    assert sorted((sorted(c) for c in components)) == [[1,2,13,22,40,48],[63]]
    cycle = [1,13,40,2,22,48]
    assert all([cycle[(i+1)%6]] == [t for t in G[s] if t in components[0]]
               for i,s in enumerate(cycle))
    assert 63 in G[63]
    # Direct enumeration of graph edges, not the transfer states,
    # independently checks every subset for small orders.
    for n in range(1, 8):
        expected = ({1:1} if n == 1 else {n: 4 if n%3==2 else 2, 3*n-2:1})
        actual = transfer_poly_open(n, G)
        assert actual == expected, ('open transfer',n,actual,expected)
        if n<=6:
            brute = exhaustive_poly(n,False)
            assert brute == expected, ('open brute',n,brute,expected)
    for n in range(3, 17):
        expected = {3*n:1}
        if n%6==0:
            expected[n] = 6
        actual = transfer_poly_circular(n,G)
        assert actual == expected, ('circular transfer',n,actual,expected)
        if n<=6:
            brute = exhaustive_poly(n,True)
            assert brute == expected, ('circular brute',n,brute,expected)
    # The 14-state adjacency table above proves the entire parameter range:
    # the terminal-path residues give 2,2,4,2,2,4 nontrivial open states
    # for n modulo 6 = 0,1,2,3,4,5, respectively (n>=2),
    # and the only cyclic paths are one loop and a period-six orbit.
    print('VERIFY_OK active_states=14 directed_transitions=102')
    print('SCC_CYCLES loop=[63] six_cycle=[1,13,40,2,22,48]')
    print('OPEN n>=2: 1 full-edge set plus 2 or 4 weight-n sets (4 iff n mod 3 = 2)')
    print('CIRCULAR n>=3: 1 full-edge set plus 6 weight-n sets iff 6 divides n')
    print('INDEPENDENT_BRUTE open n=1..6, circular n=3..6')
    print('WEIGHTED_TRANSFER open n=1..7, circular n=3..16')

if __name__ == '__main__':
    verify()
