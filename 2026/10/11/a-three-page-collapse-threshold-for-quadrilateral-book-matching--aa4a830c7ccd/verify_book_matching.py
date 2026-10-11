#!/usr/bin/env python3
"""Exact finite checks for matching complexes of quadrilateral book graphs."""
from collections import defaultdict, deque


def book_edges(n):
    E=[('u','v','c')]
    for i in range(1,n+1):
        E.extend([
            ('u',f'a{i}',f'p{i}'),
            (f'a{i}',f'b{i}',f'q{i}'),
            (f'b{i}','v',f'r{i}')])
    return E


def all_faces(n):
    E=book_edges(n)
    out=[]
    for mask in range(1<<len(E)):
        used=set(); ok=True
        for j,(a,b,_) in enumerate(E):
            if (mask>>j)&1:
                if a in used or b in used:
                    ok=False; break
                used.add(a); used.add(b)
        if ok: out.append(mask)
    return out,E


def gf2_rank(cols):
    piv={}
    for x in cols:
        while x:
            p=x.bit_length()-1
            if p in piv: x ^= piv[p]
            else:
                piv[p]=x
                break
    return len(piv)


def reduced_betti(faces):
    by=defaultdict(list)
    for m in faces:
        if m:
            by[m.bit_count()-1].append(m)
    maxd=max(by, default=-1)
    ranks={}
    for d in range(1,maxd+1):
        low={s:i for i,s in enumerate(by[d-1])}
        cols=[]
        for s in by[d]:
            x=0; t=s
            while t:
                b=t & -t; t-=b
                x ^= 1<<low[s^b]
            cols.append(x)
        ranks[d]=gf2_rank(cols)
    bet=[]
    for d in range(maxd+1):
        b=len(by[d])-ranks.get(d,0)-ranks.get(d+1,0)
        if d==0: b-=1
        bet.append(b)
    return [len(by[d]) for d in range(maxd+1)],bet


def labels(mask,E):
    return frozenset(E[j][2] for j in range(len(E)) if (mask>>j)&1)


def compatible_with_q(face,k):
    return (f'p{k}' not in face and f'r{k}' not in face)


def star_cluster_check(n,faces,E):
    outside=[]
    for m in faces:
        F=labels(m,E)
        if not any(compatible_with_q(F,k) for k in range(1,n+1)):
            outside.append(F)
    return sorted(outside,key=lambda s:(len(s),sorted(s)))


def main():
    expected={1:[1,0],2:[0,2,0]}
    print('n | f-vector | reduced mod-2 Betti | faces outside SC({q_i})')
    for n in range(1,8):
        faces,E=all_faces(n)
        f,b=reduced_betti(faces)
        outside=star_cluster_check(n,faces,E)
        print(n,f,b,[sorted(x) for x in outside])
        if n==1:
            assert b==expected[1]
            assert set(outside)=={frozenset({'p1'}),frozenset({'r1'}),frozenset({'p1','r1'})}
        elif n==2:
            assert b==expected[2]
            assert set(outside)=={frozenset({'p1','r2'}),frozenset({'p2','r1'})}
        else:
            assert all(x==0 for x in b)
            assert outside==[]
    print('VERIFY_OK')

if __name__=='__main__':
    main()
