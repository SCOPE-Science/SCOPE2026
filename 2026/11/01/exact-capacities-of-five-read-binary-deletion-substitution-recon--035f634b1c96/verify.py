"""Exact finite five-read deletion/substitution reconstruction-code census.

Run: python3 verify.py
Requires only the Python 3 standard library. Every upper bound follows
from a complete branch-and-bound clique enumeration with a sound coloring bound.
"""
from collections import Counter

EXPECTED = {3: 8, 4: 5, 5: 5, 6: 6, 7: 8, 8: 12, 9: 16}
WITNESSES = {
    3: tuple(range(8)),
    4: (0, 3, 8, 14, 15),
    5: (0, 7, 17, 28, 31),
    6: (0, 3, 15, 28, 49, 63),
    7: (127, 124, 115, 96, 79, 24, 3, 0),
    8: (255, 248, 243, 224, 207, 129, 126, 50, 31, 76, 7, 0),
    9: (511, 508, 499, 455, 480, 385, 415, 294, 204, 280, 181, 126, 112, 15, 3, 0),
}

def outputs(x, n):
    """Distinct results of exactly one deletion and at most one substitution."""
    bits = tuple((x >> (n - i - 1)) & 1 for i in range(n))
    result = set()
    for removed in range(n):
        shortened = bits[:removed] + bits[removed + 1:]
        result.add(shortened)
        for flipped in range(n - 1):
            result.add(shortened[:flipped] + (1-shortened[flipped],) + shortened[flipped+1:])
    return frozenset(result)

def independent_ball_check(x,n):
    """Independent Hamming-neighborhood membership test."""
    d = set()
    for i in range(n):
        low_mask=(1 << (n-i-1))-1
        d.add(((x >> (n-i)) << (n-i-1)) | (x & low_mask))
    return frozenset(tuple((y >> (n-i-2)) & 1 for i in range(n-1))
                     for y in range(1 << (n-1))
                     if any((y ^ z).bit_count() <= 1 for z in d))

def compatibility(n):
    m = 1 << n
    balls = [outputs(x,n) for x in range(m)]
    adj = [0] * m
    edge_count = 0
    for x in range(m):
        for y in range(x+1,m):
            if len(balls[x].intersection(balls[y])) < 5:
                adj[x] |= 1 << y
                adj[y] |= 1 << x
                edge_count += 1
    return adj,balls,edge_count

def maximum_clique(adj):
    """Exhaustive exact maximum clique, with provably safe greedy-color bounds.

    At every invocation P contains precisely the vertices compatible with
    every vertex in `current`. Each color class produced by color_sort is
    an independent set, so a clique may use at most one vertex per class.
    The descending-color branch explores every surviving first choice.
    """
    best=[]
    current=[]
    nodes=0

    def color_sort(P):
        order=[]
        color_bounds=[]
        color=0
        while P:
            color+=1
            independent=P
            while independent:
                v=(independent & -independent).bit_length()-1
                bit=1<<v
                order.append(v)
                color_bounds.append(color)
                P &= ~bit
                independent &= ~bit
                independent &= ~adj[v]
        return order,color_bounds

    def expand(P):
        nonlocal best,nodes
        nodes+=1
        if not P:
            if len(current)>len(best):
                best=current.copy()
            return
        order,bounds=color_sort(P)
        for i in range(len(order)-1,-1,-1):
            if len(current)+bounds[i]<=len(best):
                return
            v=order[i]
            current.append(v)
            expand(P & adj[v])
            current.pop()
            P &= ~(1<<v)

    expand((1<<len(adj))-1)
    return best,nodes

def verify():
    for n in EXPECTED:
        adj,balls,edge_count=compatibility(n)
        assert all(outputs(x,n)==independent_ball_check(x,n) for x in range(1<<n)), ('ball',n)
        witness=WITNESSES[n]
        assert len(witness)==EXPECTED[n] and len(set(witness))==len(witness)
        assert all(0<=x<(1<<n) for x in witness)
        assert all((adj[x]>>y)&1 for i,x in enumerate(witness) for y in witness[i+1:]), ('witness',n)
        best,nodes=maximum_clique(adj)
        assert len(best)==EXPECTED[n], ('upper',n,len(best),EXPECTED[n])
        print('n=%d; M=%d; compatible_edges=%d; maximum=%d; search_nodes=%d' %
              (n,1<<n,edge_count,len(best),nodes),flush=True)
    print('EXACT_CERTIFICATE_OK',flush=True)

if __name__=='__main__':
    verify()
