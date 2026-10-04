#!/usr/bin/env python3
from itertools import combinations, product
from math import prod


def partitions(n, maxpart=None):
    if n == 0:
        yield ()
        return
    if maxpart is None or maxpart > n:
        maxpart = n
    for a in range(maxpart, 0, -1):
        for rest in partitions(n-a, a):
            yield (a,) + rest


def factor(n):
    out=[]
    p=2
    while p*p<=n:
        if n%p==0:
            e=0
            while n%p==0:
                n//=p; e+=1
            out.append((p,e))
        p+=1
    if n>1: out.append((n,1))
    return out


def abelian_group_types(n):
    choices=[]
    for p,e in factor(n):
        pc=[]
        for lam in partitions(e):
            pc.append(tuple(p**a for a in lam))
        choices.append(pc)
    for pick in product(*choices):
        mods=tuple(m for block in pick for m in block)
        yield mods


def elems(mods):
    return list(product(*[range(m) for m in mods]))


def sub(x,y,mods):
    return tuple((a-b)%m for a,b,m in zip(x,y,mods))


def neg(x,mods):
    return tuple((-a)%m for a,m in zip(x,mods))


def is_embed_K11n(A,z,mods):
    zero=tuple(0 for _ in mods)
    DE=set()
    DN=set()
    # Edges: 0-z, 0-a, z-a.
    for u,v in [(zero,z)]:
        d=sub(v,u,mods); DE.add(d); DE.add(neg(d,mods))
    for a in A:
        for u,v in [(zero,a),(z,a)]:
            d=sub(v,u,mods); DE.add(d); DE.add(neg(d,mods))
    # Nonedges: pairs inside A.
    for a,b in combinations(A,2):
        d=sub(b,a,mods); DN.add(d); DN.add(neg(d,mods))
    return DE.isdisjoint(DN)


def exhaustive_no_smaller(n):
    candidates=0
    group_types=0
    for N in range(n+2,3*n):
        for mods in abelian_group_types(N):
            group_types+=1
            E=elems(mods)
            zero=tuple(0 for _ in mods)
            nz=[x for x in E if x!=zero]
            for At in combinations(nz,n):
                A=set(At)
                for z in nz:
                    if z in A: continue
                    candidates+=1
                    if is_embed_K11n(A,z,mods):
                        raise AssertionError((n,N,mods,A,z))
    return candidates,group_types


def check_construction(n):
    mods=(3,n)
    zero=(0,0)
    z=(1,0)
    A={(2,j) for j in range(n)}
    assert is_embed_K11n(A,z,mods)
    D={sub(a,b,mods) for a in A for b in A}
    B={neg(a,mods) for a in A}
    C={sub(z,a,mods) for a in A}
    assert D.isdisjoint(B) and D.isdisjoint(C) and B.isdisjoint(C)
    assert len(D)>=n and len(B)==n and len(C)==n
    return len(D),len(B),len(C)


def main():
    total_candidates=0
    total_types=0
    for n in range(2,6):
        c,t=exhaustive_no_smaller(n)
        total_candidates+=c; total_types+=t
        check_construction(n)
    for n in range(2,51):
        check_construction(n)
    print(f'ALL CHECKS PASSED; exhaustive_n=2..5; host_types={total_types}; normalized_label_candidates={total_candidates}; constructions_n=2..50')

if __name__=='__main__':
    main()
