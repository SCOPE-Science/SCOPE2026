"""Enumerate every optimal labelled Kneser coloring, and compute Kempe-swap connectivity.
Independent of formula for Kempe chains, using induced bichromatic components.
Run: python3 verify_kempe.py
"""
from itertools import combinations,permutations
from collections import deque
from math import factorial,comb

def solve(n):
    edges=tuple(combinations(range(n),2)); idx={e:i for i,e in enumerate(edges)}
    k=n-2; states=set()
    for Q in combinations(range(n),3):
        S=tuple(v for v in range(n) if v not in Q)
        for colors in permutations(range(k)):
            colors_of=dict(zip(S,colors[1:])); pairs=tuple(combinations(S,2))
            for mask in range(1<<len(pairs)):
                c=[-1]*len(edges)
                for e in combinations(Q,2):c[idx[e]]=colors[0]
                for s in S:
                    for q in Q:c[idx[tuple(sorted((s,q)))]]=colors_of[s]
                for b,(s,t) in enumerate(pairs):c[idx[(s,t)]]=colors_of[t if (mask>>b)&1 else s]
                states.add(tuple(c))
    expect=comb(n,3)*factorial(k)*2**comb(n-3,2)
    assert len(states)==expect
    root=next(iter(states)); seen={root}; queue=deque([root]); moves=0
    non_disjoint=[tuple(j for j,f in enumerate(edges) if not(set(e)&set(f))) for e in edges]
    while queue:
        c=queue.popleft()
        for a,b in combinations(range(k),2):
            induced={i for i,x in enumerate(c) if x==a or x==b}
            while induced:
                st=[induced.pop()]; comp=set(st)
                while st:
                    i=st.pop()
                    for j in non_disjoint[i]:
                        if j in induced:
                            induced.remove(j);comp.add(j);st.append(j)
                w=list(c)
                for i in comp:w[i]=b if c[i]==a else a
                w=tuple(w); moves+=1
                assert w in states,(n,c,a,b,comp)
                if w not in seen:seen.add(w);queue.append(w)
    assert len(seen)==len(states),(n,len(seen),len(states))
    print(f'KEMPE_PASS n={n} optimal_colorings={len(states)} reachable={len(seen)} checked_moves={moves}',flush=True)
for n in (4,5,6):solve(n)
print('ALL_KEMPE_PASS')
