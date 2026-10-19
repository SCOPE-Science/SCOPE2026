#!/usr/bin/env python3
"""Finite consistency checks for constrained cyclic factor covers (stdlib only)."""
from collections import Counter, deque
from itertools import product


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def legal(w):
    return '11' not in w


def index_first_one(w):
    return w.index('1') if '1' in w else 0


def target_edges(k):
    return [''.join(x) for x in product('01', repeat=k) if legal(''.join(x))]


def multiset_edges(k):
    base = target_edges(k)
    doubled = ['0' + ''.join(x) + '0'
               for x in product('01', repeat=k-2)
               if legal(''.join(x)) and '1' in x]
    return base + doubled


def eulerian_word(k):
    edges = multiset_edges(k)
    graph = {}
    indeg, outdeg = Counter(), Counter()
    for edge in edges:
        a, b = edge[:-1], edge[1:]
        graph.setdefault(a, []).append((b, edge[-1]))
        outdeg[a] += 1
        indeg[b] += 1
    nodes = set(indeg) | set(outdeg)
    assert all(indeg[v] == outdeg[v] for v in nodes)
    start = '0' * (k-1)
    stack = [(start, None)]
    reverse_symbols = []
    while stack:
        vertex, incoming = stack[-1]
        if graph.get(vertex):
            nxt, symbol = graph[vertex].pop()
            stack.append((nxt, symbol))
        else:
            stack.pop()
            if incoming is not None:
                reverse_symbols.append(incoming)
    assert len(reverse_symbols) == len(edges)
    cycle = ''.join(reversed(reverse_symbols))
    assert len(cycle) == len(edges)
    return cycle


def bfs_min_length(k):
    """Full directed binary de Bruijn graph, INCLUDING 11-containing windows."""
    targets = {w: i for i, w in enumerate(target_edges(k))}
    goal = (1 << len(targets)) - 1
    mask_v = (1 << (k-1)) - 1
    seen = {(0, 0)}
    queue = deque([(0, 0, 0)])
    while queue:
        state, covered, length = queue.popleft()
        if length and state == 0 and covered == goal:
            return length
        for bit in (0, 1):
            w = (state << 1) | bit
            nxt = w & mask_v
            bits = covered | (1 << targets[format(w, f'0{k}b')]
                              if format(w, f'0{k}b') in targets else 0)
            item = (nxt, bits)
            if item not in seen:
                seen.add(item)
                queue.append((nxt, bits, length+1))
    raise AssertionError('Graph has no feasible covering cycle')


def run():
    for k in range(2, 13):
        required = target_edges(k)
        extras = multiset_edges(k)
        count = fibonacci(k+2)
        overhead = fibonacci(k) - 1
        assert len(required) == count
        assert len(extras) == count + overhead
        # The potential bound holds for all edges, not only permitted edges.
        all_edges = [''.join(x) for x in product('01', repeat=k)]
        assert all(index_first_one(w[:-1]) - index_first_one(w[1:]) <= 1
                   for w in all_edges)
        potential_sum = sum(index_first_one(w[:-1]) - index_first_one(w[1:])
                            for w in required)
        assert potential_sum == -overhead
        cyclic_word = eulerian_word(k)
        observed = [cyclic_word[i:i+k] if i+k <= len(cyclic_word)
                    else (cyclic_word + cyclic_word[:k-1])[i:i+k]
                    for i in range(len(cyclic_word))]
        assert set(required) <= set(observed)
        assert all(legal(w) for w in observed)
        if k <= 5:
            optimum = bfs_min_length(k)
            assert optimum == len(cyclic_word), (k, optimum, len(cyclic_word))
        print(f'k={k:2} required={count:4} repeats={overhead:4} optimum={len(cyclic_word):4} OK')
    print('VERIFICATION_OK')


if __name__ == '__main__':
    run()
