#!/usr/bin/env python3
"""Independent exhaustive checks for rank-three Eulerian-poset C2 census.
Requires Python 3 standard library only. All numbers are small and exact.
"""
from collections import Counter
from math import isqrt
from itertools import permutations


def partitions(n, low=2):
    if n == 0:
        yield ()
    for a in range(low, n + 1):
        for tail in partitions(n-a, a):
            yield (a,) + tail


def poset(parts):
    r = sum(parts)
    N = 2*r + 2
    lo = 0
    hi = N-1
    out = [[False] * N for _ in range(N)]
    for i in range(1,N-1):
        out[lo][i] = True
        out[i][hi] = True
    out[lo][hi] = True
    pos = 0
    for k in parts:
        for j in range(k):
            x = 1 + pos + j
            for j2 in (j, (j-1)%k):
                y = 1+r+pos+j2
                out[x][y] = True
        pos += k
    return out


def rank(x, n):
    r = (n-2)//2
    return 0 if x==0 else 1 if x<=r else 2 if x<=2*r else 3


def eulerian(E):
    n=len(E)
    ranks=[rank(x,n) for x in range(n)]
    for i in range(n):
        for j in range(n):
            if E[i][j]:
                diff=ranks[j]-ranks[i]
                if diff<=0:
                    return False
                inter=[x for x in range(n) if x==i or x==j or (E[i][x] and E[x][j])]
                odd=sum((ranks[x]-ranks[i])%2 for x in inter)
                if odd*2 != len(inter):
                    return False
    return True


def lattice(E):
    n=len(E)
    le=lambda a,b: a==b or E[a][b]
    for a in range(n):
        for b in range(a+1,n):
            ub=[z for z in range(n) if le(a,z) and le(b,z)]
            lb=[z for z in range(n) if le(z,a) and le(z,b)]
            joins=[z for z in ub if all(le(z,w) for w in ub)]
            meets=[z for z in lb if all(le(w,z) for w in lb)]
            if len(joins)!=1 or len(meets)!=1:
                return False
    return True


def signature(E):
    n=len(E)
    colors=[0]*n
    for _ in range(n+1):
        patterns=[]
        for x in range(n):
            counts=Counter()
            for y in range(n):
                rel=0 if x==y else 1 if E[x][y] else 2 if E[y][x] else 3
                counts[(rel,colors[y])] += 1
            patterns.append((colors[x],tuple(sorted(counts.items()))))
        lookup={s:i for i,s in enumerate(sorted(set(patterns)))}
        updated=[lookup[s] for s in patterns]
        if updated==colors:
            return tuple(sorted(Counter(updated).items())),tuple(sorted(Counter(updated).values()))
        colors=updated
    raise AssertionError('refinement did not stabilize')


def three_variable_witness(E):
    # Models: A(x) = exactly one strict predecessor;
    # C(z) = exactly one strict successor.
    n=len(E)
    atoms=[x for x in range(n) if sum(E[y][x] for y in range(n))==1]
    coatoms=[z for z in range(n) if sum(E[z][w] for w in range(n))==1]
    return any(sum(E[x][z] and E[y][z] for z in coatoms)>=2
               for x in atoms for y in atoms if x!=y)


def direct_orbits(E):
    # Brute-force all atom and coatom permutations to test orbit counts
    # for the small-order examples. Bottom/top have unique ranks.
    n=len(E);r=(n-2)//2
    atom=list(range(1,r+1));coatom=list(range(r+1,2*r+1))
    parent=list(range(n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    for pa in permutations(atom):
        for pc in permutations(coatom):
            p=[0]+list(pa)+list(pc)+[n-1]
            if all(E[a][b]==E[p[a]][p[b]] for a in atom for b in coatom):
                for x,y in enumerate(p):parent[find(x)]=find(y)
    return sorted(Counter(find(x) for x in range(n)).values())

def main():
    total_objects=0
    for r in range(2,17):
        ps=list(partitions(r))
        table=Counter()
        expected_signature=None
        for parts in ps:
            E=poset(parts)
            assert eulerian(E), ('not Eulerian',parts)
            lat=lattice(E)
            assert lat==(2 not in parts), ('bad lattice criterion',parts)
            assert three_variable_witness(E)==(not lat), ('C3 formula mismatch',parts)
            sig=signature(E)
            if expected_signature is None:
                expected_signature=sig
            assert sig==expected_signature,('different C2 profile',r,parts)
            assert sig[1]==(1,1,r,r),('wrong rank cell sizes',r,parts,sig)
            distinct=len(set(parts))
            table['refinable' if distinct==1 else 'nonrefinable']+=1
            if r<=5:
                expected_orbits=sorted([1,1]+[k*parts.count(k) for k in set(parts) for _ in range(2)])
                assert direct_orbits(E)==expected_orbits,('bad automorphism orbit formula',parts)
            table['lattice' if lat else 'nonlattice']+=1
            total_objects+=1
        # Removing one part 2 gives a bijection from nonlattices
        # to unrestricted cycle partitions of r-2.
        assert table['nonlattice']==len(list(partitions(r-2)))
        assert table['lattice']==sum(2 not in p for p in ps)
        assert table['refinable']==sum(r%d==0 for d in range(2,r+1))
        assert table['nonrefinable']==len(ps)-table['refinable']
        dmax=max(len(set(p)) for p in ps)
        assert dmax==(isqrt(8*r+9)-3)//2 or dmax==int(((8*r+9)**0.5-3)//2)

        print(f'r={r:2d} points={2*r+2:2d} types={len(ps):3d} lattices={table["lattice"]:3d} nonlattices={table["nonlattice"]:3d} C2_theories=1 refinable={table["refinable"]:3d} orbit_dmax={dmax}')
    assert lattice(poset((4,)))
    assert not lattice(poset((2,2)))
    assert signature(poset((4,)))==signature(poset((2,2)))
    print('PASS: Eulerian checks, lattice criterion, partitions, C2 classes, 10-point witnesses; cases=',total_objects)

if __name__=='__main__':
    main()
