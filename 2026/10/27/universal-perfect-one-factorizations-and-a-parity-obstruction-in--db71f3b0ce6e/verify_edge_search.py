"""Exhaustive labelled edge-colouring search for GP(3k,k).

Builds all three-edge-colourings with the three edges at the first vertex
fixed to colours 0, 1, 2, one representative per permutation of colours.
Each two-colour spanning subgraph is examined by graph traversal.
"""
from collections import Counter
from itertools import combinations


def graph(k):
    n = 3*k
    edges = [tuple(sorted((i, (i+1) % n))) for i in range(n)]
    edges += [tuple(sorted((n+i, n+(i+k) % n))) for i in range(n)]
    edges += [(i, n+i) for i in range(n)]
    assert len(edges) == 3*n and len(set(edges)) == 3*n
    incidence = [[] for _ in range(2*n)]
    for j, (a,b) in enumerate(edges):
        incidence[a].append(j); incidence[b].append(j)
    assert all(len(x)==3 for x in incidence)
    return edges, incidence


def enumerate_colourings(k):
    edges, inc = graph(k)
    colors = [-1]*len(edges)
    for c, edge in enumerate(inc[0]):
        colors[edge] = c
    solutions = []
    def recurse(arr):
        # Propagate the only missing colour at any vertex.
        while True:
            new = []
            for star in inc:
                used = [arr[e] for e in star if arr[e] != -1]
                if len(used) != len(set(used)):
                    return
                missing = [e for e in star if arr[e] == -1]
                if len(missing) == 1:
                    new.append((missing[0], next(c for c in range(3) if c not in used)))
            if not new:
                break
            for edge, col in new:
                if arr[edge] != -1 and arr[edge] != col:
                    return
                arr[edge] = col
        if -1 not in arr:
            solutions.append(tuple(arr))
            return
        choice = None
        for e,(a,b) in enumerate(edges):
            if arr[e] != -1:
                continue
            forbidden = {arr[f] for v in (a,b) for f in inc[v] if arr[f]!=-1}
            available = tuple(set(range(3))-forbidden)
            if not available:
                return
            if choice is None or len(available)<len(choice[1]):
                choice=(e,available)
        e, options = choice
        for c in options:
            next_arr=arr.copy();next_arr[e]=c
            recurse(next_arr)
    recurse(colors)
    return edges,inc,solutions


def component_count(pair, edges, inc, col):
    seen=set(); count=0
    for seed in range(len(edges)):
        if seed in seen or col[seed] not in pair: continue
        count+=1; seen.add(seed); todo=[seed]
        while todo:
            e=todo.pop()
            for v in edges[e]:
                for f in inc[v]:
                    if f not in seen and col[f] in pair:
                        seen.add(f);todo.append(f)
    return count


def check(k):
    edges,inc,solutions=enumerate_colourings(k)
    patterns=Counter()
    for colors in solutions:
        assert all(set(colors[e] for e in star)==set(range(3)) for star in inc)
        cycles=tuple(component_count(pair,edges,inc,colors) for pair in ((0,1),(0,2),(1,2)))
        patterns[tuple(sorted(cycles))]+=1
    J=(2**k-(-1)**k)//3
    expected=J*(1 if k%2 else 4)
    assert len(solutions)==expected,(k,len(solutions),expected)
    perfect=patterns.get((1,1,1),0)
    assert perfect==(J if k%2 else 0),(k,perfect)
    return f"k={k} factors={len(solutions)} perfect={perfect} cycle_profiles={dict(sorted(patterns.items()))}"

if __name__=='__main__':
    for k in range(1,9):
        print(check(k),flush=True)
    print('ALL_EDGE_SEARCH_CHECKS_PASS')
