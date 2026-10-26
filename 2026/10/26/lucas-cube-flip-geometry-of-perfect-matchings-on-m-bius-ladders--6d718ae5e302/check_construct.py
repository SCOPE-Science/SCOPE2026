"""Independent cyclic-bitword construction and exact flip-distance verifier."""

def ab(a,b): return frozenset((a,b))

def components(n):
    # Distinct from the brute-force vertex-first search: enumerate all length-n
    # independent circular binary words, map occupied bits to parallel links.
    assert n>=4
    def r(i):return ab(i,i+n)
    def face(i):
        j=(i+1)%n
        if j:
            return frozenset([ab(i,j),ab(i+n,j+n)])
        return frozenset([ab(n-1,n),ab(2*n-1,0)])
    canonical=[]
    for b in range(1<<n):
        if any((b>>i)&(b>>((i+1)%n))&1 for i in range(n)):continue
        edges=set()
        touched=set()
        for i in range(n):
            if b>>i&1:
                j=(i+1)%n
                assert not (i in touched or j in touched)
                touched.update((i,j))
                edges.update(face(i))
        for i in range(n):
            if i not in touched:edges.add(r(i))
        assert len(edges)==n and len(set().union(*edges))==2*n
        canonical.append((b,frozenset(edges)))
    assert len({m for b,m in canonical}) == len(canonical)
    for b,m in canonical:
        for i in range(n):
            rr={r(i),r((i+1)%n)}
            hh=set(face(i))
            if rr <= m or hh <= m:
                c=b^(1<<i)
                assert c in {x for x,_ in canonical}
                target=dict(canonical)[c]
                if rr <= m:after=(m-frozenset(rr))|hh
                else:after=(m-frozenset(hh))|rr
                assert after == target
    if n%2:
        # Build the two no-rung boundary cycle perfect matchings by choosing
        # alternating edges on the 2n-cycle in 0,1,...,n-1,2n-1,...,n order.
        ring=list(range(2*n))
        spirals=[]
        for parity in (0,1):
            edges=frozenset(ab(ring[i],ring[(i+1)%(2*n)]) for i in range(parity,2*n+parity,2))
            assert len(edges)==n
            assert len(set().union(*edges))==2*n
            assert edges not in set(x for b,x in canonical)
            assert all(not ({r(i),r((i+1)%n)}<=edges or set(face(i))<=edges) for i in range(n))
            spirals.append(edges)
        assert spirals[0]!=spirals[1]
    count=len(canonical)
    links=0
    diam=0
    for b,_ in canonical:
        for c,_ in canonical:
            dist=(b^c).bit_count()
            diam=max(diam,dist)
            if dist==1:links+=1
    links//=2
    assert diam==2*(n//2)
    return count,links,diam

def lucas(n):
    a,b=2,1
    for j in range(2,n+1):a,b=b,a+b
    return b

def fib(n):
    a,b=0,1
    for _ in range(n):a,b=b,a+b
    return a

if __name__=='__main__':
    for n in range(4,17):
        v,e,d=components(n)
        assert v==lucas(n) and e==n*fib(n-1)
        print(f'n={n:02d} Lucas_vertices={v} Lucas_edges={e} Lucas_diameter={d}')
    print('PASS: explicit correspondence, switches, counts and Hamming diameters verified for n=4..16')
