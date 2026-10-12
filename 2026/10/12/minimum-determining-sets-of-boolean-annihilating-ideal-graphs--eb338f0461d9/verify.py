from itertools import combinations, permutations
from math import ceil, log2, perm, factorial

def vertices(n):
    return list(range(1, (1 << n) - 1))

def adjacent(a,b):
    return a != b and (a & b) == 0

def popcount(x):
    return x.bit_count()

def degree(n,a):
    return sum(1 for b in vertices(n) if adjacent(a,b))

def signatures(n,D):
    return [tuple((m >> i) & 1 for m in D) for i in range(n)]

def determining(n,D):
    return len(set(signatures(n,D))) == n

def explicit_basis(n):
    k=ceil(log2(n))
    D=[]
    for j in range(k):
        m=0
        for i in range(n):
            if (i >> j) & 1:
                m |= 1 << i
        assert 0 < m < (1 << n)-1
        D.append(m)
    assert len(set(D)) == k
    assert determining(n,D)
    return D

def coordinate_image(mask,p):
    out=0
    for i in range(len(p)):
        if (mask >> i) & 1:
            out |= 1 << p[i]
    return out

def verify_graph_structure(n):
    V=vertices(n)
    degs={a:degree(n,a) for a in V}
    for a,d in degs.items():
        assert d == (1 << (n-popcount(a))) - 1
    maxd=max(degs.values())
    singles={1<<i for i in range(n)}
    assert {a for a,d in degs.items() if d==maxd} == singles
    # Each vertex is recovered from which singleton vertices are nonadjacent to it.
    for a in V:
        recovered=0
        for i in range(n):
            s=1<<i
            if not adjacent(s,a):
                recovered |= s
        assert recovered == a
    # All coordinate permutations are graph automorphisms.
    if n <= 5:
        for p in permutations(range(n)):
            for a in V:
                aa=coordinate_image(a,p)
                assert aa in V
            for a in V:
                aa=coordinate_image(a,p)
                for b in V:
                    bb=coordinate_image(b,p)
                    assert adjacent(a,b)==adjacent(aa,bb)

def verify_minimum_count(n):
    V=vertices(n)
    k=ceil(log2(n))
    assert n > (1 << (k-1))
    for j in range(k):
        pass
    D=explicit_basis(n)
    assert len(D)==k and determining(n,D)
    # Exhaustive count at the minimum size.
    count=0
    for Dtuple in combinations(V,k):
        if determining(n,Dtuple):
            count += 1
    expected=perm(1<<k,n)//factorial(k)
    assert count==expected,(n,count,expected)
    # Exhaustive failure one size below when feasible.
    if k>1:
        assert all(not determining(n,Dtuple) for Dtuple in combinations(V,k-1))
    return k,count

def main():
    rows=[]
    for n in range(2,8):
        verify_graph_structure(n)
        k,c=verify_minimum_count(n)
        rows.append((n,k,c))
    # Formula-only checks beyond exhaustive range.
    for n in [8,9,10,16,17,31,32,33]:
        k=ceil(log2(n))
        D=explicit_basis(n)
        assert determining(n,D)
        expected=perm(1<<k,n)//factorial(k)
        assert expected>0
    print('n k minimum_set_count')
    for n,k,c in rows:
        print(n,k,c)
    print('published_n5_two_set_obstruction', max(len(set(signatures(5,D))) for D in combinations(vertices(5),2)))
    print('VERIFY_OK')

if __name__=='__main__':
    main()
