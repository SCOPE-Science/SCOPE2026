"""Direct finite checks of a two-prime Pythagorean-pair model."""
from math import isqrt
from itertools import combinations


def predicted_edges(p, q, n):
    if (p, q) != (2, 3):
        return set()
    return {frozenset(((a,b),(a+2,b-1)))
            for a in range(n-2) for b in range(1,n)}


def direct_edges(p, q, n):
    points = [(a, b, p**a*q**b) for a in range(n) for b in range(n)]
    edges = set()
    for (a,b,u),(c,d,v) in combinations(points, 2):
        w2 = u*u + v*v
        if isqrt(w2)**2 == w2:
            edges.add(frozenset(((a,b),(c,d))))
    return edges


def claimed_alpha(n):
    if n % 4 == 0:
        return n*(n+1)//2
    if n % 4 == 2:
        return n*(n+2)//2
    if n % 4 == 1:
        return (2*n*n+3*n-1)//4
    return (2*n*n+3*n+1)//4


def component_lengths(n):
    adj = { (a,b):set() for a in range(n) for b in range(n)}
    for e in predicted_edges(2,3,n):
        v,w = tuple(e)
        adj[v].add(w); adj[w].add(v)
    unseen=set(adj)
    lengths=[]
    while unseen:
        start=unseen.pop()
        stack=[start]
        visited=1
        while stack:
            v=stack.pop()
            for w in adj[v]:
                if w in unseen:
                    unseen.remove(w);stack.append(w);visited+=1
        lengths.append(visited)
    assert sum(lengths)==n*n
    return lengths


def brute_alpha(n):
    vertices=[(a,b) for a in range(n) for b in range(n)]
    ix={v:i for i,v in enumerate(vertices)}
    edges=[(ix[a],ix[b]) for a,b in map(tuple,predicted_edges(2,3,n))]
    best=0
    for bitset in range(1<<(n*n)):
        if bitset.bit_count()<=best:
            continue
        if not any((bitset>>a)&1 and (bitset>>b)&1 for a,b in edges):
            best=bitset.bit_count()
    return best


def main():
    checked=0
    for p,q in combinations((2,3,5,7,11),2):
        for n in range(1,10):
            observed=direct_edges(p,q,n)
            expected=predicted_edges(p,q,n)
            assert observed==expected, (p,q,n,observed^expected)
            checked+=1
    for n in range(1,121):
        actual=sum((length+1)//2 for length in component_lengths(n))
        assert actual==claimed_alpha(n), (n,actual,claimed_alpha(n))
    for n in range(1,5):
        assert brute_alpha(n)==claimed_alpha(n)
    print(f'CERTIFICATE_OK distinct_prime_pairs=10 supports_and_sizes={checked} square_cutoffs=120 brute_independence_cutoffs=4')

if __name__=='__main__':
    main()
