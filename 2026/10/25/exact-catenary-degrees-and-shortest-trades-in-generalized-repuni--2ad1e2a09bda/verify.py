"""Reproducible finite checks for the catenary formula of generalized repunit monoids.

Uses integer arithmetic and exhaustive factorization enumeration at finite Betti
fibers. The all-parameter theorem requires the separate written proof.
"""
import math
from functools import lru_cache


def repunit(b, n):
    return (b**n - 1) // (b-1)


def generators(a, b, n):
    return tuple(repunit(b, n) + a*repunit(b, i-1) for i in range(1, n+1))


def relations(a, b, n):
    """Every pair of columns in the displayed 2-by-n matrix."""
    out = []
    for i in range(n):
        for j in range(i+1, n):
            x, y = [0]*n, [0]*n
            x[i] += b
            if j < n-1:
                x[j+1] += 1
                y[j] += b
                y[i+1] += 1
            else:
                x[0] += a+1
                y[n-1] += b
                y[i+1] += 1
            out.append((tuple(x), tuple(y)))
    return out


def dot(u, g):
    return sum(x*y for x, y in zip(u, g))


def factorizations(g, m):
    """All nonnegative factorizations of a single element (finite recursion)."""
    @lru_cache(None)
    def rec(j, left):
        if j == len(g)-1:
            if left % g[j]:
                return ()
            return ((left//g[j],),)
        acc = []
        for t in range(left//g[j] + 1):
            for tail in rec(j+1, left-t*g[j]):
                acc.append((t,)+tail)
        return tuple(acc)
    return rec(0, m)


def dist(x,y):
    z = [min(u,v) for u,v in zip(x,y)]
    return max(sum(x)-sum(z),sum(y)-sum(z))


def catenary_fiber(factors):
    """Minimum bottleneck spanning-tree threshold = catenary degree of fiber."""
    if len(factors) <= 1:
        return 0
    parent = list(range(len(factors)))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    ed = sorted((dist(factors[i],factors[j]),i,j)
                for i in range(len(factors)) for j in range(i+1,len(factors)))
    blocks = len(factors)
    for w,i,j in ed:
        u,v = find(i),find(j)
        if u!=v:
            parent[u]=v
            blocks-=1
            if blocks==1:
                return w
    raise AssertionError('disconnected')


def main():
    grid = 0
    exhaustive = 0
    max_fibers = 0
    for b in range(2,6):
        for n in range(2,6):
            for a in range(1,11):
                g = generators(a,b,n)
                if math.gcd(a,g[0])!=1:
                    continue
                N = a+b+1
                assert g[1]+b*g[-1] == N*g[0]
                for x,y in relations(a,b,n):
                    assert dot(x,g) == dot(y,g)
                    assert max(sum(x),sum(y))<=N
                # Finite exhaustive exclusion of a shorter pure-minimum-generator trade.
                limit=N*g[0]
                reachable=bytearray(limit+1)
                reachable[0]=1
                for z in range(1,limit+1):
                    reachable[z] = any(z>=t and reachable[z-t] for t in g[1:])
                assert all(not reachable[k*g[0]] for k in range(1,N))
                assert reachable[N*g[0]]
                grid+=1
                if b<=3 and n<=4 and a<=4:
                    degrees=sorted(set(dot(x,g) for x,_ in relations(a,b,n)))
                    degrees.append(N*g[0])
                    degrees=sorted(set(degrees))
                    c=max(catenary_fiber(factorizations(g,z)) for z in degrees)
                    assert c==N, (a,b,n,c,N)
                    exhaustive+=1
                    max_fibers+=len(degrees)
    print('PASS: generator identities, all minor weights and sharp pure trades,',grid,'triples')
    print('PASS: all factorizations in',max_fibers,'distinct critical fibers across',exhaustive,'triples')


if __name__=='__main__':
    main()
