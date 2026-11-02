#!/usr/bin/env python3
"""Exhaustive independent two-method DSC census for four-element meet-semilattices.

All 2^6 directed comparabilities on the three elements above the bottom
are tested as posets and for existence of unique pairwise meets. All
2^12 reflexive relations are then checked for each isomorphism class.
"""
from collections import Counter
from itertools import permutations
from fractions import Fraction

N=4
ARCS=[(a,b) for a in range(1,N) for b in range(1,N) if a!=b]
RELS=[(a,b) for a in range(N) for b in range(N) if a!=b]
DIAG=frozenset((i,i) for i in range(N))


def order_to_meet(mask):
    le={(i,i) for i in range(N)}|{(0,i) for i in range(N)}
    le|={edge for k,edge in enumerate(ARCS) if mask>>k&1}
    if any(a!=b and (b,a) in le for a,b in le):return None
    if any((a,d) not in le for a,b in le for c,d in le if b==c):return None
    rows=[]
    for a in range(N):
        row=[]
        for b in range(N):
            common=[v for v in range(N) if (v,a) in le and (v,b) in le]
            tops=[v for v in common if all((w,v) in le for w in common)]
            if len(tops)!=1:return None
            row.append(tops[0])
        rows.append(tuple(row))
    return tuple(rows)


def equiv(m,n):
    for perm in permutations((1,2,3)):
        q=(0,)+perm
        if all(q[m[i][j]]==n[q[i]][q[j]] for i in range(N) for j in range(N)):
            return True
    return False


def meet(a,b,m):
    return (m[a[0]][b[0]],m[a[1]][b[1]])


def closed(r,m):
    return all(meet(x,y,m) in r for x in r for y in r)


def is_equivalence(r):
    return all((b,a) in r for a,b in r) and all((a,d) in r
        for a,b in r for c,d in r if b==c)


def closure(initial,m):
    r=set(initial)
    while True:
        grown=r|{meet(x,y,m) for x in r for y in r}
        if grown==r:return frozenset(r)
        r=grown


def main():
    classes=[]
    for mask in range(1<<6):
        m=order_to_meet(mask)
        if m is not None and not any(equiv(m,k) for k in classes):classes.append(m)
    assert len(classes)==5
    vals=[]
    for m in classes:
        dist=Counter();all_closed=set();closed_cong=0
        generated=set()
        for mask in range(1<<12):
            r=DIAG|frozenset(RELS[k] for k in range(12) if mask>>k&1)
            if closed(r,m):
                all_closed.add(r)
                dist[len(r)-4]+=1
                if is_equivalence(r):closed_cong+=1
            generated.add(closure(r,m))
        assert generated==all_closed  # independent closure-generation engine
        values=(len(all_closed),closed_cong)
        vals.append(values)
        print('CLASS',m, 'D,C',values,'PROFILE',tuple(dist[j] for j in range(13)))
    assert sorted(vals)==[(306,7),(322,8),(400,8),(576,8),(625,8)],vals
    assert len({Fraction(c,d) for d,c in vals})==5
    print('VERIFY_OK')

if __name__=='__main__':main()
