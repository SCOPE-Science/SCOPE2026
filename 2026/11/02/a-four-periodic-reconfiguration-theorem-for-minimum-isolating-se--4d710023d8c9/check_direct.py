"""Direct finite checks of minimum isolating-set replacement graphs of cycles.

Run: python3 check_direct.py
Uses no external libraries.
"""
from collections import Counter, deque
from itertools import combinations
from math import comb


def is_isolating(n, selected):
    # Test the graph definition directly: no two adjacent vertices survive N[S].
    covered = set(selected)
    for x in selected:
        covered.add((x - 1) % n)
        covered.add((x + 1) % n)
    return all(i in covered or (i + 1) % n in covered for i in range(n))


def profile(n):
    k = (n + 3) // 4
    family = [frozenset(t) for t in combinations(range(n), k)
              if is_isolating(n, t)]
    family_set = set(family)
    adj = {s: set() for s in family}
    for s in family:
        for removed in s:
            a = s - {removed}
            for inserted in range(n):
                if inserted not in s:
                    t = frozenset(a | {inserted})
                    if t in family_set:
                        adj[s].add(t)
    visited = set()
    parts = []
    for source in family:
        if source in visited:
            continue
        visited.add(source)
        queue = deque([source])
        size = 0
        while queue:
            cur = queue.popleft()
            size += 1
            for nxt in adj[cur]:
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)
        parts.append(size)
    return len(family), Counter(map(len, adj.values())), sorted(parts), sum(map(len,adj.values()))//2


def main():
    for n in range(5, 23):
        k = (n+3)//4
        r = 4*k-n
        expected = n * comb(k+r-1,r)//k
        count, degree_counts, parts, edges = profile(n)
        assert count == expected, (n,count,expected)
        assert degree_counts == Counter({2*r: count}), (n,degree_counts)
        if r:
            assert parts == [count], (n,parts)
        else:
            assert parts == [1,1,1,1], (n,parts)
        assert edges == r*count, (n,edges)
        if r==1:
            assert count==n and degree_counts==Counter({2:n})
        print(f'n={n}: {count} sets; degree {2*r}; components {parts if r==0 else len(parts)}; edges {edges}')
    assert profile(4) == (4,Counter({3:4}),[4],6)
    print('CYCLE_ISOLATION_DIRECT_GRAPH_PASS')

if __name__ == '__main__':
    main()
