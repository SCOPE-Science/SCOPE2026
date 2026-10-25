"""Finite independent checks of a theorem on Kneser-neighborhood homology.
No external packages or external data. This is a finite check, not proof for all n.
"""
from itertools import combinations
from math import factorial


def partitions(n, bound=None):
    if n == 0:
        yield ()
    else:
        for i in range(min(bound or n,n), 1-1, -1):
            for p in partitions(n-i, i):
                yield (i,)+p


def representative(parts):
    g=[]; off=0
    for q in parts:
        g += [off + (i+1)%q for i in range(q)]
        off+=q
    return tuple(g)


def sign_perm(g):
    inv=sum(g[i]>g[j] for i in range(len(g)) for j in range(i+1,len(g)))
    return -1 if inv%2 else 1


def edge_orbit_masks(g):
    n=len(g)
    edges=list(combinations(range(n),2)); ed_id={e:i for i,e in enumerate(edges)}
    unseen=set(range(len(edges))); masks=[]
    while unseen:
        i=next(iter(unseen)); orb=[]
        while i in unseen:
            unseen.remove(i); orb.append(i)
            a,b=edges[i]
            i=ed_id[tuple(sorted((g[a],g[b])))]
        mask=0
        for j in orb:
            a,b=edges[j]
            mask|=(1<<a)|(1<<b)
        masks.append(mask)
    return masks


def direct_reduced_lefschetz(g):
    n=len(g)
    # Each invariant edge subset is a union of complete edge orbits.
    # Its signed augmented-chain contribution equals (-1)^orbit_count.
    orbits=edge_orbit_masks(g)
    total=0
    def recurse(k, support, parity):
        nonlocal total
        if support.bit_count()>n-2:return
        if k==len(orbits):
            total+=parity
            return
        recurse(k+1,support,parity)
        recurse(k+1,support|orbits[k],-parity)
    recurse(0,0,1)
    return -total


def independent_simplex_trace(g):
    n=len(g)
    edges=list(combinations(range(n),2))
    eid={e:i for i,e in enumerate(edges)}
    induced=[eid[tuple(sorted((g[a],g[b])))] for a,b in edges]
    total=0
    # Independent simplicial Lefschetz computation (not the edge-orbit recursion).
    for face in range(1<<len(edges)):
        used=0; chosen=[]; mapped=0
        for i,(a,b) in enumerate(edges):
            if face>>i&1:
                used |= (1<<a)|(1<<b)
                chosen.append(i)
                mapped |=1<<induced[i]
        if used.bit_count()>n-2 or mapped!=face:continue
        order=[induced[i] for i in chosen]
        parity=sum(order[i]>order[j] for i in range(len(order)) for j in range(i+1,len(order)))%2
        total += (-1)**(len(chosen)-1+parity)
    return total


def expected_homology_character(g):
    n=len(g); f=sum(i==g[i] for i in range(n))
    return sign_perm(g)*(f*f-3*f+1)


def main():
    count=0
    for n in range(4,8):
        for part in partitions(n):
            g=representative(part)
            lhs=direct_reduced_lefschetz(g)
            rhs=(-1)**(n-4)*expected_homology_character(g)
            assert lhs==rhs,(n,part,lhs,rhs)
            if n<=6:
                direct=independent_simplex_trace(g)
                assert direct==lhs,(n,part,'simplicial_trace',direct,lhs)
            f=sum(i==g[i] for i in range(n))
            t=sum(i<g[i] and g[g[i]]==i for i in range(n))
            ext2=((f-1)**2-(f+2*t-1))//2
            twobox=((f*(f-1)//2)+t)-f
            assert ext2+twobox==f*f-3*f+1
            count+=1
        print(f'n={n} conjugacy_class_trace_checks={count}')
    # Irreducible-dimension check for sign-twisted S^(n-2,2) plus exterior-square standard.
    for n in range(4,13):
        dimA=(n-1)*(n-2)//2
        dimB=n*(n-3)//2
        assert dimA+dimB==n*n-3*n+1
    print('KNESER_NEIGHBORHOOD_SYMMETRY_CHARACTER_VERIFIED',count,'orbit_trace_conjugacy_classes','direct_simplicial_to_n6','specht_trace_identity')

if __name__=='__main__':main()
