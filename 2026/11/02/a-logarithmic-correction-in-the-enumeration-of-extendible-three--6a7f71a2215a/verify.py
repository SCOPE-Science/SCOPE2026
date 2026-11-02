"""Standalone checks for the arithmetic count of extendible three-one prefixes.
No external packages or network access are needed.
"""
from math import gcd


def is_forest_direct(support):
    m = max(support)
    root = list(range(2 * (m + 1)))
    size = [1] * len(root)

    def find(v):
        while root[v] != v:
            root[v] = root[root[v]]
            v = root[v]
        return v

    for t in support:
        for r in range(t + 1):
            u = find(r)
            v = find(m + 1 + t - r)
            if u == v:
                return False
            if size[u] < size[v]:
                u, v = v, u
            root[v] = u
            size[u] += size[v]
    return True


def arithmetic_condition(a,b,c):
    x = c-b
    y = b-a
    return a < x-gcd(x,y)


def exact_count(n):
    return sum(max(0,min(x-gcd(x,y), n-x-y+1))
               for x in range(1,n) for y in range(1,n-x+1))


def direct_count(n):
    return sum(arithmetic_condition(a,b,c)
               for c in range(2,n+1) for b in range(1,c)
               for a in range(b))


def weighted_exclusion(n):
    baseline = sum((s+1)//2 * (n-s) for s in range(1,n))
    core = sum(gcd(x,y) for x in range(1,n+1)
               for y in range(1,n+1-2*x))
    boundary = sum(1 for x in range(1,n+1)
                   for y in range(1,n-x+1)
                   for t in range(1,gcd(x,y)+1)
                   if n < 2*x+y <= n+t)
    return baseline - core - boundary


def totient(n):
    ans = n
    p = 2
    z = n
    while p*p <= z:
        if z % p == 0:
            while z % p == 0:
                z //= p
            ans -= ans // p
        p += 1
    if z > 1:
        ans -= ans // z
    return ans


def core_by_divisors(n):
    return sum(totient(d) * ((n//d -1)**2//4)
               for d in range(1,n//3+1))


def main():
    checked_graph = 0
    for c in range(2,61):
        for b in range(1,c):
            for a in range(b):
                assert is_forest_direct((a,b,c)) == arithmetic_condition(a,b,c), (a,b,c)
                checked_graph += 1
    for n in range(2,91):
        assert exact_count(n) == direct_count(n) == weighted_exclusion(n), n
        assert core_by_divisors(n) == sum(gcd(x,y)
                                           for x in range(1,n+1)
                                           for y in range(1,n+1-2*x))
    samples = ((0,1,3),(0,2,5),(1,3,8),(2,6,14))
    for abc in samples:
        assert arithmetic_condition(*abc)
        support = list(abc)
        for _ in range(5):
            assert is_forest_direct(support)
            support.append(2*max(support)+1)
        assert is_forest_direct(support)
    print('VERIFIED: direct graph-forest vs arithmetic criterion:', checked_graph, 'triples, max index 60')
    print('VERIFIED: independent exact counts, divisor cores and boundary corrections for every N=2,...,90')
    print('VERIFIED: five-stage explicit sparse extensions for four sample triples')
    for n in [10,20,30,50,90]:
        print('T(%d)=%d' %(n,exact_count(n)))

if __name__ == '__main__':
    main()
