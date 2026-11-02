"""Exact, dependency-free checks of a three-vertex coordination game's asymptotics."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from heapq import heappush, heappop

S = [(k, c) for c in (0, 1) for k in range(3)]
IDX = {s: i for i, s in enumerate(S)}

def changes(s, theta):
    k, c = s
    delta_leaf = F(c) - theta / 3
    delta_hub = F(k, 2) - 2 * theta / 3
    out = []
    if k < 2:
        out.append((IDX[k+1, c], max(F(0), -delta_leaf), 2-k))
    if k > 0:
        out.append((IDX[k-1, c], max(F(0), delta_leaf), k))
    if c == 0:
        out.append((IDX[k, 1], max(F(0), -delta_hub), 1))
    else:
        out.append((IDX[k, 0], max(F(0), delta_hub), 1))
    return out

def shortest(source, target, theta):
    dist = [None] * 6
    dist[source] = F(0)
    heap = [(F(0), source)]
    while heap:
        weight, u = heappop(heap)
        if weight != dist[u]: continue
        if u == target: return weight
        for v, cost, _ in changes(S[u], theta):
            d = weight + cost
            if dist[v] is None or d < dist[v]:
                dist[v] = d
                heappush(heap, (d, v))
    raise AssertionError('unreachable')

def trees(theta):
    edges = {u: changes(S[u], theta) for u in range(6)}
    answer = {}
    for root in range(6):
        others = [u for u in range(6) if u != root]
        best, coefficient, ways = None, 0, 0
        for chosen in product(*(edges[u] for u in others)):
            destinations = {u: ch[0] for u, ch in zip(others, chosen)}
            valid = True
            for start in others:
                u, visited = start, set()
                while u != root:
                    if u in visited:
                        valid = False
                        break
                    visited.add(u)
                    u = destinations[u]
                if not valid: break
            if not valid: continue
            cost = sum((edge[1] for edge in chosen), F(0))
            prefactor = 1
            for edge in chosen: prefactor *= edge[2]
            if best is None or cost < best:
                best, coefficient, ways = cost, prefactor, 1
            elif cost == best:
                coefficient += prefactor
                ways += 1
        answer[S[root]] = (best, coefficient, ways)
    return answer

def check():
    # Both strict equilibria and weighted-potential differences.
    for theta in (F(4,5), F(9,10), F(19,20), F(11,10), F(7,5)):
        assert shortest(IDX[0,0], IDX[2,1], theta) == theta-F(1,2)
        assert shortest(IDX[2,1], IDX[0,0], theta) == 1-2*theta/3
        for leaf_a, centre, leaf_b in product((0,1), repeat=3):
            a = (leaf_a, centre, leaf_b)
            phi = leaf_a*centre + centre*leaf_b - theta*(leaf_a + 4*centre + leaf_b)/3
            for i, deg, nbrs in ((0,1,[1]), (1,2,[0,2]), (2,1,[1])):
                b = list(a); b[i] ^= 1
                psi = b[0]*b[1] + b[1]*b[2] - theta*(b[0] + 4*b[1] + b[2])/3
                utility_change = (b[i]-a[i])*(F(sum(a[j] for j in nbrs),deg) - deg*theta/3)
                assert psi - phi == deg*utility_change
    exact = trees(F(9,10))
    expected = {
        (0,0):(F(2,5),12,4), (1,0):(F(7,10),24,4),
        (2,0):(F(4,5),6,2), (0,1):(F(1),4,2),
        (1,1):(F(4,5),12,2), (2,1):(F(2,5),18,4),
    }
    assert exact == expected, (exact, expected)
    assert F(exact[0,0][1],exact[0,0][1]+exact[2,1][1]) == F(2,5)
    assert F(exact[2,1][1],exact[0,0][1]+exact[2,1][1]) == F(3,5)
    print('EXACT_VERIFY_OK: five rational parameter tests; all 24 single-player transitions per parameter')
    print('SIX_ROOT_TREE_MINIMA:')
    for s in S: print(s, exact[s])
    print('CRITICAL_LIMIT 000=2/5, 111=3/5; THRESHOLD=9/10')

if __name__ == '__main__': check()
