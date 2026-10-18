"""Finite independent checks of Kneser-neighborhood equivariant trace identities.

Run: python3 verify.py. Standard library only.
The checks are finite corroboration of the separately stated all-size proof.
"""
from itertools import combinations
from collections import Counter
from array import array
from math import factorial


def partitions(n, high=None):
    if n == 0:
        yield ()
        return
    if high is None:
        high = n
    for a in range(min(n, high), 0, -1):
        for rest in partitions(n-a, a):
            yield (a,) + rest


def representative(lam):
    p=[]; low=0
    for size in lam:
        p.extend([low+i+1 for i in range(size-1)] + [low])
        low+=size
    return tuple(p)


def exact_orbit_sum(n, perm):
    edges=list(combinations(range(n), 2))
    pos={e:k for k,e in enumerate(edges)}
    images=[pos[tuple(sorted((perm[a],perm[b])))] for a,b in edges]
    visited=set(); supports=[]
    for i in range(len(edges)):
        if i in visited:
            continue
        k=i; endpoint_mask=0
        while k not in visited:
            visited.add(k)
            a,b=edges[k]
            endpoint_mask |= (1<<a)|(1<<b)
            k=images[k]
        supports.append(endpoint_mask)
    m=len(supports)
    # Invariant simplex edge sets are precisely unions of edge orbits.
    unions=array('I', [0]) * (1<<m)
    signed=array('b', [0]) * (1<<m)
    signed[0]=1
    index={1<<j:j for j in range(m)}
    alternating=1  # includes the empty edge set, i.e. the augmented chain
    for flags in range(1, 1<<m):
        last=flags & -flags
        prev=flags-last
        unions[flags]=unions[prev] | supports[index[last]]
        signed[flags]=-signed[prev]
        if unions[flags].bit_count()<=n-2:
            alternating+=signed[flags]
    return -alternating, len(visited), m


def predicted(n, lam):
    fixed=lam.count(1)
    trans=lam.count(2)
    sign=(-1)**(n-len(lam))
    formula=sign*(fixed*fixed-3*fixed+1)
    # Young's rule / branching: characters of the two two-row-tail shapes.
    chi_two_row=(fixed*(fixed-3))//2 + trans
    # The fraction is integer for both parity cases.
    chi_two_col=(fixed-1)*(fixed-2)//2 - trans
    assert formula==sign*(chi_two_row+chi_two_col)
    return formula


def main():
    for n in (4,5,6,7):
        count=0
        for lam in partitions(n):
            got, edges, orbits=exact_orbit_sum(n,representative(lam))
            expected_euler=(-1)**(n-4)*predicted(n,lam)
            assert got==expected_euler, (n,lam,got,expected_euler)
            count+=1
        dim=n*n-3*n+1
        assert dim==n*(n-3)//2 +(n-1)*(n-2)//2
        print(f'n={n}; conjugacy classes={count}; identity homology rank={dim}; all traces verified')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
