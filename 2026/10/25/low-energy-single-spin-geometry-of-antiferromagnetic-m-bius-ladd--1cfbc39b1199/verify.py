#!/usr/bin/env python3
"""Independent exhaustive finite checks for low-energy cuts in Mobius ladders.

Run: python3 mobius_low_energy_verify.py
No third-party modules are needed.
"""
from collections import Counter, defaultdict, deque


def graph(n):
    N = 2*n
    E = [(i, (i+1) % N) for i in range(N)]
    E += [(i, i+n) for i in range(n)]
    return E


def defects(mask, edges):
    return sum(1 - (((mask >> a) ^ (mask >> b)) & 1) for a, b in edges)


def components(vertices, N):
    pool = set(vertices)
    sizes = []
    while pool:
        start = pool.pop()
        todo = [start]
        for mask in todo:
            for v in range(N):
                nxt = mask ^ (1 << v)
                if nxt in pool:
                    pool.remove(nxt)
                    todo.append(nxt)
        sizes.append(len(todo))
    return sorted(sizes)


def run(n):
    N = 2*n
    E = graph(n)
    bound = 5 if n % 2 else 3
    levels = defaultdict(set)
    for state in range(1 << N):
        d = defects(state, E)
        if d <= bound:
            levels[d].add(state)
    ground = 0 if n % 2 else 2
    assert all(not levels[d] for d in range(ground))
    if n % 2:
        assert len(levels[0]) == 2
        assert len(levels[3]) == 4*n
        assert len(levels[4]) == n*(n+3)
        small = set().union(*(levels[d] for d in range(5)))
        assert components(small, N) == sorted([1]*(n*(n-3)) + [5*n+1]*2)
        assert components(set().union(*levels.values()), N) == [sum(map(len, levels.values()))]
        ref = next(iter(levels[0]))
        ordering = [k for pair in zip(range(n), range(n, 2*n)) for k in pair]
        mask = ref
        for v in ordering:
            mask ^= 1 << v
            assert defects(mask, E) <= 5
        assert mask == (ref ^ ((1 << N) - 1))
        print(f"ODD_OK n={n} ground=2 at3={len(levels[3])} at4={len(levels[4])} isolations={n*(n-3)} barrier=5")
    else:
        assert len(levels[2]) == 2*n
        assert len(levels[3]) == 4*n
        states = levels[2] | levels[3]
        assert components(states, N) == [6*n]
        for mask in levels[2]:
            assert sum((mask ^ (1 << v)) in levels[3] for v in range(N)) == 4
        shared = Counter()
        for mask in levels[3]:
            neighbors = [mask ^ (1 << v) for v in range(N) if (mask ^ (1 << v)) in levels[2]]
            assert len(neighbors) == 2
            shared[frozenset(neighbors)] += 1
        assert len(shared) == 2*n and set(shared.values()) == {2}
        simple = defaultdict(set)
        for e in shared:
            a,b=tuple(e)
            simple[a].add(b)
            simple[b].add(a)
        assert len(simple) == 2*n and all(len(nei) == 2 for nei in simple.values())
        print(f"EVEN_OK n={n} ground={2*n} one_excitation={4*n} cyclic_diamonds={2*n}")


def main():
    for n in range(3, 11):
        run(n)
    print('ALL_VERIFY_OK')


if __name__ == '__main__':
    main()
