#!/usr/bin/env python3
"""Exact, independent finite checks of Möbius-ladder independence-complex characters.

Requires only Python >=3.10. No floating-point arithmetic is used.
"""
from collections import defaultdict
from functools import lru_cache


def adjacencies(n):
    N = 2*n
    return [sum(1 << j for j in {(i-1)%N, (i+1)%N, (i+n)%N}) for i in range(N)]


def independent_faces(n):
    adjacency = adjacencies(n)
    N = 2*n
    out = []
    def extend(remaining, chosen):
        if remaining == 0:
            out.append(chosen)
            return
        bit = remaining & -remaining
        i = bit.bit_length()-1
        extend(remaining ^ bit, chosen)
        extend((remaining ^ bit) & ~adjacency[i], chosen | bit)
    extend((1 << N)-1, 0)
    assert len(out) == len(set(out))
    return out


def sign_on_face(mask, permutation):
    ids = [i for i in range(len(permutation)) if (mask >> i) & 1]
    transformed = [permutation[i] for i in ids]
    inversions = sum(transformed[i] > transformed[j]
                     for i in range(len(transformed)) for j in range(i+1,len(transformed)))
    return -1 if inversions & 1 else 1


def direct_reduced_lefschetz(n, faces, p):
    total = 0
    for face in faces:
        image = 0
        for i in range(2*n):
            if (face >> i) & 1:
                image |= 1 << p[i]
        if image == face:
            size = face.bit_count()
            total += (-1 if size%2==0 else 1) * sign_on_face(face,p)
    return total


def orbit_quotient_lefschetz(n, permutation):
    N = 2*n
    used = set()
    orbits = []
    for start in range(N):
        if start in used:
            continue
        o=[]
        i=start
        while i not in used:
            used.add(i)
            o.append(i)
            i=permutation[i]
        orbits.append(o)
    belong={i:k for k,o in enumerate(orbits) for i in o}
    neighbors=[0]*len(orbits)
    adjacency=adjacencies(n)
    for k,o in enumerate(orbits):
        for i in o:
            for j in range(N):
                if (adjacency[i] >> j) & 1:
                    neighbors[k] |= 1 << belong[j]
    @lru_cache(None)
    def independent_euler(available):
        if available == 0:
            return 1
        bit=available & -available
        j=bit.bit_length()-1
        result=independent_euler(available ^ bit)
        if not (neighbors[j] & bit):
            result -= independent_euler(available & ~(bit | neighbors[j]))
        return result
    return -independent_euler((1 << len(orbits))-1)


def expected_character(n, r, reflection):
    if n % 4 == 2:
        k = (n-2)//4
        if reflection:
            return (-1)**(k+r)
        return 3 if r % 4 == 0 else -1
    return (-1)**(n*r+(n//4 if reflection else 0))


def homology_degree(n):
    if n%4 == 0:
        return n//2-1
    if n%4 == 2:
        return (n-2)//2
    return 2*((n-1)//4)


def ranks_mod2(n, faces):
    bysize=defaultdict(list)
    for mask in faces:
        bysize[mask.bit_count()].append(mask)
    boundary_rank={0:0}
    for k in range(1,max(bysize)+1):
        if k == 1:
            boundary_rank[k]=0
            continue
        loc={f:i for i,f in enumerate(bysize[k-1])}
        pivots={}
        for face in bysize[k]:
            col=0
            remain=face
            while remain:
                bit=remain & -remain
                remain ^=bit
                col ^=1 << loc[face ^ bit]
            while col:
                pivot=col.bit_length()-1
                if pivot in pivots:
                    col ^= pivots[pivot]
                else:
                    pivots[pivot]=col
                    break
        boundary_rank[k]=len(pivots)
    betti={k-1:len(bysize[k])-boundary_rank[k]-boundary_rank.get(k+1,0)
           for k in range(1,max(bysize)+1)}
    betti[0] -= 1  # reduced H_0
    return {k:v for k,v in betti.items() if v}


def tests():
    checked=0
    for n in range(2,13):
        N=2*n
        faces=independent_faces(n)
        d=homology_degree(n)
        if n<=9:
            actual=ranks_mod2(n,faces)
            assert actual == {d:(3 if n%4==2 else 1)}, (n,actual,d)
        for r in range(N):
            for reflection in (False,True):
                p = [(r-i)%N if reflection else (r+i)%N for i in range(N)]
                predicted = (-1)**d * expected_character(n,r,reflection)
                result1=direct_reduced_lefschetz(n,faces,p)
                result2=orbit_quotient_lefschetz(n,p)
                assert result1==predicted,(n,r,reflection,result1,predicted)
                assert result2==predicted,(n,r,reflection,result2,predicted)
                checked += 1
        print(f'n={n:2} faces={len(faces):6} homological_degree={d} rank={3 if n%4==2 else 1} group_elements={2*N}',flush=True)
    print(f'VERIFY_OK {checked} character comparisons by two independent methods; 8 exact mod-2 homology checks (n=2,...,9)')

if __name__=='__main__':
    tests()

# An optional larger exact orbit-quotient check (does not enumerate simplices).
def extended_tests():
    count = 0
    for n in range(13,31):
        N = 2*n
        for r in range(N):
            for reflection in (False, True):
                p = [(r-i)%N if reflection else (r+i)%N for i in range(N)]
                actual = orbit_quotient_lefschetz(n,p)
                expected = (-1)**homology_degree(n)*expected_character(n,r,reflection)
                assert actual == expected, (n,r,reflection,actual,expected)
                count += 1
    print(f'EXTENDED_ORBIT_OK {count} additional exact orbit checks, n=13,...,30')

if __name__ == '__main__':
    import sys
    if '--extended' in sys.argv:
        extended_tests()
