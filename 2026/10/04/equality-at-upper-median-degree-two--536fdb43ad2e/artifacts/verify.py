#!/usr/bin/env python3
from itertools import combinations


def edges_of(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]


def adjacency(n, mask, edges):
    a=[0]*n
    for k,(i,j) in enumerate(edges):
        if (mask>>k)&1:
            a[i] |= 1<<j
            a[j] |= 1<<i
    return a


def connected(a):
    n=len(a)
    seen=1
    frontier=1
    while frontier:
        vbit=frontier & -frontier
        frontier-=vbit
        v=vbit.bit_length()-1
        new=a[v] & ~seen
        seen |= new
        frontier |= new
    return seen == (1<<n)-1


def upper_median(a):
    ds=sorted(x.bit_count() for x in a)
    return ds[len(ds)//2]


def is_2dom(a, D):
    n=len(a)
    full=(1<<n)-1
    outside=full ^ D
    x=outside
    while x:
        b=x & -x; x-=b
        v=b.bit_length()-1
        if (a[v] & D).bit_count() < 2:
            return False
    return True


def gamma2(a):
    n=len(a)
    verts=range(n)
    for k in range(n+1):
        for C in combinations(verts,k):
            D=0
            for v in C: D |= 1<<v
            if is_2dom(a,D):
                return k
    raise AssertionError


def predicted_equality(a):
    n=len(a)
    deg=[x.bit_count() for x in a]
    H=[v for v,d in enumerate(deg) if d>=2]
    # P4 case: two degree-1 and two degree-2 vertices.
    if n==4 and sorted(deg)==[1,1,2,2]:
        return True
    # Triangle with k=0,1,2,3 leaves all attached to at most one triangle vertex.
    if 3 <= n <= 6 and len(H)==3:
        if all(((a[u]>>v)&1) for i,u in enumerate(H) for v in H[i+1:]):
            high=[v for v in H if deg[v]>=3]
            if len(high)<=1 and all(deg[v]==1 for v in range(n) if v not in H):
                return True
    return False


def structural_nminus1(a):
    deg=[x.bit_count() for x in a]
    H=[v for v,d in enumerate(deg) if d>=2]
    if not H:
        return False
    clique=all(((a[u]>>v)&1) for i,u in enumerate(H) for v in H[i+1:])
    at_most_one_high=sum(d>=3 for d in deg) <= 1
    return clique and at_most_one_high


def main():
    total_masks=0
    connected_graphs=0
    m2_graphs=0
    m2_equalities=0
    structural_checks=0
    equality_signatures=set()
    for n in range(2,7):
        E=edges_of(n)
        for mask in range(1<<len(E)):
            total_masks += 1
            a=adjacency(n,mask,E)
            if not connected(a):
                continue
            connected_graphs += 1
            g=gamma2(a)
            # Independently check the structural lemma gamma_2=n-1.
            lhs=(g==n-1)
            rhs=structural_nminus1(a)
            assert lhs==rhs, (n,mask,g,[x.bit_count() for x in a])
            structural_checks += 1
            m=upper_median(a)
            if m==2:
                m2_graphs += 1
                eq=(g==n-m+1)
                pred=predicted_equality(a)
                assert eq==pred, (n,mask,g,m,[x.bit_count() for x in a])
                if eq:
                    m2_equalities += 1
                    equality_signatures.add((n,tuple(sorted(x.bit_count() for x in a))))
    expected={(3,(2,2,2)),(4,(1,1,2,2)),(4,(1,2,2,3)),(5,(1,1,2,2,4)),(6,(1,1,1,2,2,5))}
    assert equality_signatures==expected, equality_signatures
    print(f"ALL CHECKS PASSED; graph_masks={total_masks}; connected_graphs={connected_graphs}; structural_checks={structural_checks}; m2_graphs={m2_graphs}; m2_equalities={m2_equalities}; max_order=6")

if __name__=='__main__': main()
