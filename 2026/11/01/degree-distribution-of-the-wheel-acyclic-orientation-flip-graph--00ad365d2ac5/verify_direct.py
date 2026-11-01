#!/usr/bin/env python3
"""Independent direct orientation/flip census for wheel acyclic-orientation graphs.
Uses only directed-graph topological sorting and reachability, not a degree formula.
"""
from collections import Counter
from itertools import product

def census(m):
    edges = [(i, (i+1) % m) for i in range(m)] + [(m, i) for i in range(m)]
    hist = Counter()
    for bits in product((0, 1), repeat=2*m):
        adj = [[] for _ in range(m+1)]
        indeg = [0]*(m+1)
        for bit, (u, v) in zip(bits, edges):
            if bit: u,v = v,u
            adj[u].append(v)
            indeg[v] += 1
        stack = [i for i,d in enumerate(indeg) if d == 0]
        seen = 0
        while stack:
            u = stack.pop(); seen += 1
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0: stack.append(v)
        if seen < m+1: continue
        flips = 0
        for bit, (u, v) in zip(bits, edges):
            if bit: u,v = v,u
            reached = {u}; stack = [u]
            while stack:
                w = stack.pop()
                for x in adj[w]:
                    if w == u and x == v: continue
                    if x not in reached:
                        reached.add(x); stack.append(x)
            if v not in reached: flips += 1
        hist[flips] += 1
    return hist

expected = {
 3: {3:24},
 4: {4:58,5:16,6:4},
 5: {5:140,6:80,7:20},
 6: {6:344,7:300,8:78,9:4},
 7: {7:868,8:980,9:308,10:28},
 8: {8:2234,9:2992,10:1184,11:144,12:4}
}

def main():
    for m, target in expected.items():
        hist = census(m)
        assert dict(hist) == target, (m,hist,target)
        assert sum(hist.values()) == 3**m - 3
        assert sum(d*n for d,n in hist.items()) == 2*m*(5*3**(m-2)-3)
        print('DIRECT_WHEEL_PASS',m,dict(sorted(hist.items())))
    print('ALL_DIRECT_WHEEL_CHECKS_PASS')

if __name__ == '__main__': main()
