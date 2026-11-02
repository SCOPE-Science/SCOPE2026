"""Finite corroboration of labelled counting and graph-incidence automorphism encoding.
Run with Python 3 standard library: python checker.py.
"""
from itertools import product, permutations
from math import factorial


def predicted(n):
    total = 0
    for a in range(n):
        for b in range(n-a):
            c = n - 1 - a - b
            total += (n * factorial(n - 1) // (factorial(a) * factorial(b) * factorial(c))) * ((a + 1) * (b + 1)) ** c
    return total


def accepted(f, g):
    n = len(f)
    if any(f[f[i]] != f[i] or g[g[i]] != g[i] for i in range(n)):
        return False
    h = [f[g[i]] for i in range(n)]
    return len(set(h)) == 1 and all(g[f[i]] == h[i] for i in range(n))


def brute(n):
    maps = [t for t in product(range(n), repeat=n) if all(t[t[i]] == t[i] for i in range(n))]
    return sum(accepted(f, g) for f in maps for g in maps)


def incidence_ops(vertices, edges):
    # Root zero, A vertices, B edges, C incidence nodes.
    m = len(vertices)
    e = len(edges)
    n = 1 + m + e + 2*e
    f = list(range(n))
    g = list(range(n))
    f[0] = g[0] = 0
    for j in range(m):
        g[1+j] = 0
    for j in range(e):
        f[1+m+j] = 0
    idx = 1+m+e
    for j, (u,v) in enumerate(edges):
        for node in (u,v):
            f[idx] = 1 + node
            g[idx] = 1 + m + j
            idx += 1
    return f,g


def graph_aut_count(vertices,edges):
    es = {tuple(sorted(t)) for t in edges}
    ans = 0
    for p in permutations(vertices):
        if {tuple(sorted((p[u],p[v]))) for u,v in edges} == es:
            ans += 1
    return ans


def direct_aut_count(f,g):
    n=len(f)
    ans=0
    for p in permutations(range(n)):
        if all(p[f[i]]==f[p[i]] and p[g[i]]==g[p[i]] for i in range(n)):
            ans+=1
    return ans


if __name__ == '__main__':
    for n in range(1,5):
        p, b = predicted(n), brute(n)
        print('n',n,'predicted',p,'direct',b)
        assert p == b
    # Tiny graphs keep total carrier <= 10 for brute permutation testing.
    for verts, edges in [([0],[]), ([0,1], [(0,1)]), ([0,1,2],[(0,1),(1,2)])]:
        f,g=incidence_ops(verts,edges)
        assert accepted(f,g)
        ga=graph_aut_count(verts,edges)
        fa=direct_aut_count(f,g)
        print('graph',len(verts),len(edges),'aut',ga,fa)
        assert ga==fa
    print('ALL_CHECKS_OK')
