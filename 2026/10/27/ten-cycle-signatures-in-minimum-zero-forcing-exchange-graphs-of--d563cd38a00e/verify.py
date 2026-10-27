"""Independent exact checks of minimum zero forcing on complements of long-cycle 2-factors."""
from collections import Counter, deque
from itertools import combinations
from math import comb


def graph(lengths):
    n = sum(lengths)
    h = [set() for _ in range(n)]
    offset = 0
    for ell in lengths:
        for j in range(ell):
            v = offset + j
            h[v].update((offset + (j-1)%ell, offset + (j+1)%ell))
        offset += ell
    assert all(len(s) == 2 for s in h)
    g = [set(range(n)) - {v} - h[v] for v in range(n)]
    return h, g


def forces(g, whites):
    w = set(whites)
    n = len(g)
    while w:
        changes = [(v, list(g[v] & w)) for v in range(n) if v not in w]
        one = [x[1][0] for x in changes if len(x[1]) == 1]
        if not one:
            return False
        w.remove(one[0])
    return True


def structural(h, whites):
    w = set(whites)
    return any(h[v].issubset(w) for v in range(len(h)) if v not in w)


def check(lengths):
    n = sum(lengths)
    c10 = lengths.count(10)
    h, g = graph(lengths)
    states = [frozenset(w) for w in combinations(range(n),3) if forces(g, w)]
    good = set(states)
    assert good == {frozenset(w) for w in combinations(range(n),3) if structural(h,w)}
    assert len(good) == n*(n-4)
    edges = set()
    nbrs = {a:set() for a in good}
    for a in good:
        for drop in a:
            for add in range(n):
                if add in a:
                    continue
                b = (a-{drop})|{add}
                if b in good:
                    nbrs[a].add(b)
                    edges.add(frozenset((a,b)))
    assert len(edges) == n*(comb(n,2)-11)
    expected = {n:2*n+10*c10,n+1:2*n-20*c10,n+2:n*(n-9)+10*c10,2*n-6:n}
    assert Counter(map(len,nbrs.values())) == Counter({k:v for k,v in expected.items() if v>0})
    if n <= 20:
        for start in good:
            distances={start:0}
            todo=deque([start])
            while todo:
                a=todo.popleft()
                for b in nbrs[a]:
                    if b not in distances:
                        distances[b]=distances[a]+1
                        todo.append(b)
            assert len(distances)==len(good)
            assert max(distances.values())<=3
        assert any(len(a-b)==3 for a,b in combinations(good,2))
    else:
        start=next(iter(good))
        seen={start}
        todo=[start]
        for a in todo:
            for b in nbrs[a]:
                if b not in seen:
                    seen.add(b);todo.append(b)
        assert seen==good
    print('CHECK_OK', lengths, 'N', n, 'states',len(good),'edges',len(edges), 'degree_spectrum',sorted(Counter(map(len,nbrs.values())).items()))


if __name__ == '__main__':
    for partition in ((9,),(10,),(11,),(12,),(13,),(18,),(19,),(20,),(9,9),(9,10),(9,11),(10,10),(9,9,9),(9,10,11)):
        check(partition)
    print('VERIFY_OK')
