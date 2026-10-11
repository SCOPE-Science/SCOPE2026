#!/usr/bin/env python3
"""Exact integer checks for cyclic edge/triple Minkowski polytopes.
Standard library only; full-dimensional theorem is proved separately.
"""
import itertools
from collections import Counter


def pell_lucas(n):
    a, b = 2, 2
    for _ in range(n):
        a, b = b, 2*b+a
    return a


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a+b
    return a


def polytope_hyperedges(n):
    return ([tuple(sorted((i, (i+1) % n))) for i in range(n)]
            + [tuple(sorted((i, (i+1) % n, (i+2) % n))) for i in range(n)])


def wins_to_vector(n, h, wins):
    return tuple(sum(v == i for v in wins) for i in range(n))


def covers(n, h, wins):
    edges={(i, winner) for H,winner in zip(h,wins) for i in H if i != winner}
    reach=set(edges)
    for k in range(n):
        reach |= {(i,j) for i in range(n) for j in range(n)
                  if (i,k) in reach and (k,j) in reach}
    assert all((j,i) not in reach for i,j in edges)
    return {(i,j) for i,j in edges if not any((i,k) in reach and (k,j) in reach
                                                     for k in range(n) if k != i and k != j)}


def brute_vertices(n):
    H=polytope_hyperedges(n)
    chosen={}
    for perm in itertools.permutations(range(n)):
        rank={x:i for i,x in enumerate(perm)}
        wins=tuple(max(e,key=rank.__getitem__) for e in H)
        vector=wins_to_vector(n,H,wins)
        if vector in chosen:
            assert chosen[vector][0] == wins
        else:
            chosen[vector]=(wins,perm)
    degrees=Counter(len(covers(n,H,wins)) for wins,_ in chosen.values())
    return len(chosen),degrees


def has_directed_cycle(n, arcs):
    deg=[0]*n
    out=[[] for _ in range(n)]
    for u,v in arcs:
        out[u].append(v)
        deg[v]+=1
    seen=0
    stack=[x for x in range(n) if deg[x]==0]
    while stack:
        u=stack.pop(); seen+=1
        for v in out[u]:
            deg[v]-=1
            if deg[v]==0:stack.append(v)
    return seen<n


def enumerate_signs(n):
    raw=good=bad=bad_pred=0
    for s in itertools.product((0,1),repeat=n):
        # bit 1 means rank(i) < rank(i+1), i.e. increasing clockwise.
        valleys=[i for i in range(n) if s[(i-1)%n]==0 and s[i]==1]
        minus_positions={i for i,x in enumerate(s) if not x}
        plus_positions=set(range(n))-minus_positions
        chord_positions=[((i-1)%n,(i+1)%n) for i in valleys]
        cycle_edges=[(i,(i+1)%n) if bit else ((i+1)%n,i)
                     for i,bit in enumerate(s)]
        current_bad=0
        for choice in itertools.product((0,1),repeat=len(valleys)):
            raw+=1
            arcs=cycle_edges+[(u,v) if b else (v,u)
                               for (u,v),b in zip(chord_positions,choice)]
            if has_directed_cycle(n,arcs):
                bad+=1; current_bad+=1
            else:good+=1
        def independent(q):
            return all((i+1)%n not in q for i in q)
        predicted=int(independent(minus_positions))+int(independent(plus_positions))
        assert current_bad==predicted,(n,s,current_bad,predicted)
        bad_pred+=predicted
    return raw,good,bad,bad_pred


def witness_nonsimple(n):
    w=list(range(n));w[-2],w[-1]=w[-1],w[-2]
    H=polytope_hyperedges(n)
    wins=[max(e,key=w.__getitem__) for e in H]
    cv=covers(n,H,wins)
    expect={(i,i+1) for i in range(n-2)}|{(1,n-1),(n-1,n-2)}
    assert cv==expect,(n,cv,expect)
    return len(cv)


def main():
    for n in range(4,13):
        raw,good,bad,bad_pred=enumerate_signs(n)
        formula=pell_lucas(n)-2*lucas(n)
        assert raw==pell_lucas(n),(n,raw,pell_lucas(n))
        assert good==formula,(n,good,formula)
        assert bad==2*lucas(n)==bad_pred
        print('orientation',n,'raw',raw,'vertices',good,'forbidden',bad)
    for n in range(4,9):
        num,deg=brute_vertices(n)
        assert num==pell_lucas(n)-2*lucas(n)
        assert sum(deg.values())==num
        if n==4: assert deg=={3:20}
        else:assert any(k>n-1 for k in deg)
        print('direct vertices',n,num,'normal-cone facet profile',dict(sorted(deg.items())))
    for n in range(5,41):
        assert witness_nonsimple(n)==n
    print('ALL_CYCLE_POLYTOPE_CHECKS_PASS')

if __name__ == '__main__':
    main()
