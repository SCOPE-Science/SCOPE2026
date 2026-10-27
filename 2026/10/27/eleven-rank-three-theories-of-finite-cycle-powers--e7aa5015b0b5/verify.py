"""Independent executable checks for rank-three theories of finite cycle powers.

Standard-library Python. No external files or packages are needed.
The infinite part is proved algebraically in RESULT.md, not inferred from tests.
"""


def regime(n, k):
    assert k >= 1 and n >= 2*k+1
    if n == 2*k+1:
        return 'clique'
    if k == 1:
        return 'cycle4' if n == 4 else 'cycle5' if n == 5 else 'cycle6' if n == 6 else 'long_cycle'
    if n == 2*k+2:
        return 'co_matching'
    if n <= 3*k+1:
        return 'low_overlap'
    if n == 3*k+2:
        return 'first_boundary'
    if n <= 4*k+1:
        return 'middle_overlap'
    if n == 4*k+2:
        return 'second_boundary'
    return 'long_power'

# Each value is (diagonal-pattern, adjacent pair-patterns, nonadjacent pair-patterns).
# Pattern mask: bit 1=neither adjacent, bits 2 and 4=mixed, bit 8=both adjacent.
TABLE = {
    'clique': (8, (8,), ()),
    'cycle4': (9, (6,), (8,)),
    'cycle5': (9, (7,), (14,)),
    'cycle6': (9, (7,), (6, 15)),
    'long_cycle': (9, (7,), (7, 15)),
    'co_matching': (9, (14,), (8,)),
    'low_overlap': (9, (14, 15), (14,)),
    'first_boundary': (9, (15,), (14,)),
    'middle_overlap': (9, (15,), (14, 15)),
    'second_boundary': (9, (15,), (6, 15)),
    'long_power': (9, (15,), (7, 15)),
}


def arithmetic_signature(n, k):
    L = 2*k+1
    diagonal = 8 if n == L else 9
    adjacent, nonadjacent = set(), set()
    for d in range(1, n//2+1):
        a = int(d <= k)
        overlap = max(0, L-d)+max(0, L-(n-d))
        c = overlap-2*a
        u = 2*k+a-overlap
        w = n-2-4*k+overlap
        assert min(c,u,w)>=0, (n,k,d,c,u,w)
        mask = (8 if c else 0) | (6 if u else 0) | (1 if w else 0)
        (adjacent if a else nonadjacent).add(mask)
    return (diagonal, tuple(sorted(adjacent)), tuple(sorted(nonadjacent)))


def direct_signature(n, k):
    def edge(x,y):
        d = (x-y) % n
        return x!=y and min(d, n-d)<=k
    results = []
    for x in range(n):
        pointed = set()
        for y in range(n):
            ext = set()
            for z in range(n):
                # Ordered triple atomic diagram, including equality patterns.
                ext.add((x==y,x==z,y==z,edge(x,y),edge(x,z),edge(y,z)))
            pointed.add((x==y,edge(x,y),frozenset(ext)))
        results.append(frozenset(pointed))
    return frozenset(results)


def direct_pair_masks(n,k):
    def e(x,y):
        d=(x-y)%n
        return x!=y and min(d,n-d)<=k
    diag=0;adj=set();non=set()
    for y in range(n):
        mask=0
        for z in range(n):
            if z==0 or z==y:
                continue
            mask |= 1 << (2*int(e(0,z))+int(e(y,z)))
        if y==0:diag=mask
        elif e(0,y):adj.add(mask)
        else:non.add(mask)
    return(diag,tuple(sorted(adj)),tuple(sorted(non)))


def main():
    assert len(TABLE)==11 and len(set(TABLE.values()))==11
    count=0
    for k in range(1,101):
        for n in range(2*k+1, min(8*k+42,800)):
            value=arithmetic_signature(n,k)
            expected=TABLE[regime(n,k)]
            assert value==expected,(n,k,regime(n,k),value,expected)
            count+=1
    print('ARITHMETIC_TABLE_OK classes=11 checked_parameter_pairs='+str(count))
    pairs=0
    for n in range(3,25):
        for k in range(1,(n-1)//2+1):
            assert arithmetic_signature(n,k)==direct_pair_masks(n,k), (n,k)
            pairs+=1
    print('DIRECT_PAIR_COUNTS_OK graphs='+str(pairs))
    classes={}
    for name in TABLE:
        choices=[(n,k) for n in range(3,25) for k in range(1,(n-1)//2+1) if regime(n,k)==name]
        assert choices, name
        n,k=min(choices)
        signature=direct_signature(n,k)
        assert signature not in classes.values(),(name,n,k)
        classes[name]=signature
    # Pairwise comparison of eleven exact 3-round types, with no use of arithmetic TABLE.
    assert len(classes)==11
    for n,k in [(3,1),(4,1),(5,1),(6,1),(7,1),(6,2),(7,2),(8,2),(9,2),(10,2),(11,2),(15,3),(19,4)]:
        assert direct_signature(n,k)==classes[regime(n,k)]
    print('FULL_ATOMIC_GAME_OK representatives=11 pairwise_distinctions=55 supplemental_graphs=13')
    minima={name:min(n for n in range(3,30) for k in range(1,(n-1)//2+1) if regime(n,k)==name) for name in TABLE}
    assert max(minima.values())==11 and sum(x==11 for x in minima.values())==1
    print('SHARP_BOUND_OK largest_smallest_representative=11 regime=long_power')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
