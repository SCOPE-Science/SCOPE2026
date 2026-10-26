"""Direct graph-theoretic exhaustive check for independent domination on C_n square K_2."""
from collections import deque
from math import comb


def graph(n):
    adj = [0] * (2 * n)
    for i in range(n):
        for a in (0, 1):
            x = 2 * i + a
            for y in (2 * ((i - 1) % n) + a, 2 * ((i + 1) % n) + a, 2 * i + 1 - a):
                adj[x] |= 1 << y
    return adj


def independent_dominating_sets(n):
    adj = graph(n)
    full = (1 << (2*n)) - 1
    best = 2*n+1
    sets = []
    for s in range(1, 1 << (2*n)):
        k = s.bit_count()
        if k > best:
            continue
        b = s
        d = s
        good = True
        while b:
            u = (b & -b).bit_length() - 1
            if adj[u] & s:
                good = False
                break
            d |= adj[u]
            b &= b-1
        if not good or d != full:
            continue
        if k < best:
            best = k
            sets = []
        sets.append(s)
    return best, sets, adj


def components(N, edges):
    unseen = set(range(N))
    out = []
    while unseen:
        u = unseen.pop()
        q = [u]
        for v in q:
            for w in edges[v]:
                if w in unseen:
                    unseen.remove(w)
                    q.append(w)
        out.append(len(q))
    return sorted(out, reverse=True)


def main():
    for n in range(3, 11):
        k, sets, adj = independent_dominating_sets(n)
        index = {s:i for i,s in enumerate(sets)}
        neighbors = [set() for _ in sets]
        jump_neighbors = [set() for _ in sets]
        for a,s in enumerate(sets):
            b = s
            while b:
                u = (b & -b).bit_length()-1
                remaining = s ^ (1 << u)
                for v in range(2*n):
                    if remaining & (1<<v):
                        continue
                    t = remaining | (1<<v)
                    j = index.get(t)
                    if j is not None and j != a:
                        jump_neighbors[a].add(j)
                        if adj[u] & (1<<v):
                            neighbors[a].add(j)
                b &= b-1
        z = n-k
        expectation = (2*n*comb(k,z)//k, 2*n*comb(k-2,z-1) if z<=k-1 else 0)
        E = sum(map(len, neighbors))//2
        EJ = sum(map(len, jump_neighbors))//2
        cc = components(len(sets), neighbors)
        expected_cc = [1,1,1,1] if n%4==0 else [len(sets)]
        assert k == 2*((n+3)//4)
        assert (len(sets),E)==expectation, (n,len(sets),E,expectation)
        assert all(a==b for a,b in zip(neighbors,jump_neighbors))
        assert cc==expected_cc,(n,cc)
        if n%4==3:
            assert all(len(t)==2 for t in neighbors)
        print(f'n={n} i={k} sets={len(sets)} edges={E} jump_edges={EJ} components={cc} PASS')
    print('DIRECT BITMASK GRAPH CHECK PASS')

if __name__=='__main__':
    main()
