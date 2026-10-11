"""Exact finite checks for transposition Fourier concentration and graph spectral transfer."""
from itertools import combinations
from math import factorial
from random import Random


def edges(n):
    return list(combinations(range(n), 2))


def incidence(n, ee):
    return [[int(v in e) for e in ee] for v in range(n)]


def hh(n, ee):
    b = incidence(n, ee)
    m = len(ee)
    return [[(n-5) + sum(b[v][i]*b[v][j] for v in range(n)) + 2*(i == j)
             for j in range(m)] for i in range(m)]


def char_gram(n, ee):
    # Each product of transpositions has n, n-3, or n-4 fixed points.
    return [[n-1 if e == f else n-4 if len(set(e)&set(f)) == 1 else n-5
             for f in ee] for e in ee]


def irank(a):
    """Integer-preserving exact fraction-free row elimination, returning rank."""
    if not a:
        return 0
    a = [list(row) for row in a]
    h, w, rr = len(a), len(a[0]), 0
    for c in range(w):
        z = next((i for i in range(rr,h) if a[i][c]), None)
        if z is None:
            continue
        a[rr],a[z] = a[z],a[rr]
        pivot = a[rr][c]
        for i in range(rr+1,h):
            coef = a[i][c]
            if not coef:
                continue
            a[i] = [pivot*a[i][j] - coef*a[rr][j] for j in range(w)]
            from math import gcd
            g = 0
            for val in a[i]:
                g = gcd(g, val)
            if g > 1:
                a[i] = [v//g for v in a[i]]
        rr += 1
        if rr == h:
            break
    return rr


def bipartite_components(n, ee):
    """Return number of bipartite components, including isolated vertices."""
    adj = [[] for _ in range(n)]
    for u,v in ee:
        adj[u].append(v)
        adj[v].append(u)
    colors = {}
    good = 0
    for root in range(n):
        if root in colors:
            continue
        colors[root] = 0
        queue = [root]
        bip = True
        for u in queue:
            for v in adj[u]:
                if v not in colors:
                    colors[v] = 1-colors[u]
                    queue.append(v)
                elif colors[v] == colors[u]:
                    bip = False
        good += int(bip)
    return good


def is_regular(n, ee):
    degrees = [sum(v in e for e in ee) for v in range(n)]
    return len(set(degrees)) == 1 and degrees[0] >= 2


def regular_checks(n, ee):
    assert is_regular(n, ee)
    r = 2*len(ee)//n
    m = len(ee)
    b = incidence(n, ee)
    h = hh(n, ee)
    top = (n-5)*m + 2*r + 2
    assert all(sum(row) == top for row in h)
    # BB^T = rI + vertex adjacency; exact identity underlying the
    # regular-graph characteristic polynomial and multiplicity transfer.
    for u in range(n):
        for v in range(n):
            z = sum(b[u][j]*b[v][j] for j in range(m))
            assert z == (r if u == v else int(tuple(sorted((u,v))) in ee))


def complete_checks(n):
    ee = edges(n)
    h = hh(n, ee)
    b = incidence(n, ee)
    m = len(ee)
    top = n*(n-3)**2//2
    assert all(sum(row) == top for row in h)
    for v in range(n-1):
        y = [b[v][i] - b[n-1][i] for i in range(m)]
        assert [sum(row[j]*y[j] for j in range(m)) for row in h] == [n*z for z in y]
    assert irank(b) == n
    assert m == (n-1)*n//2


def cycle(n, offset=0):
    return [(offset+i, offset+((i+1)%n)) for i in range(n)]


def main():
    full=0
    for n in range(4,10):
        ee = edges(n)
        assert hh(n,ee)==char_gram(n,ee)
        complete_checks(n)
        full += 1
    rng=Random(20261008)
    subsets=0
    for n in range(4,9):
        ee=edges(n)
        masks = list(range(1<<len(ee))) if n==4 else []
        cases = ([tuple(ee[i] for i in range(len(ee)) if mask>>i &1) for mask in masks]
                 if n==4 else [tuple(e for e in ee if rng.randrange(2)) for _ in range(90)])
        for ss in cases:
            assert hh(n,ss)==char_gram(n,ss)
            rank = irank(incidence(n, ss))
            assert rank == n - bipartite_components(n, ss)
            assert len(ss)-rank == len(ss)-n+bipartite_components(n, ss)
            subsets+=1
        # Full Gram positive-definite implies every principal sub-Gram is positive-definite.
    regular=[]
    for n in range(4,10):
        regular.append((n,cycle(n)))
        if n<=8:
            regular.append((n,edges(n)))
    regular += [(6, cycle(3,0)+cycle(3,3)),
                (8,cycle(4,0)+cycle(4,4)),
                (9,cycle(3,0)+cycle(3,3)+cycle(3,6)),
                (6,[(i,j) for i in range(3) for j in range(3,6)]),
                (6,[(0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(0,3),(1,4),(2,5)]),
                (8,[(i,j) for i in range(8) for j in range(i+1,8)
                    if bin(i^j).count('1') == 1])]
    for n,e in regular:
        regular_checks(n,[tuple(sorted(x)) for x in e])
    # Confirm the singular exceptional rank at n=3, without extending the theorem to it.
    assert irank(hh(3, edges(3))) == 2
    print(f'VERIFY_OK complete_n=4..9 ({full}) arbitrary_edge_masks={subsets} regular_graphs={len(regular)} exceptional_n3_rank=2')

if __name__=='__main__':
    main()
