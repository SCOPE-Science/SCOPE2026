#!/usr/bin/env python3
"""Independent fixed-variable logical type refinement for rooted ancestry trees.
Model-checks arbitrary quantifier depth up to the exact finite fixed point.
"""
from itertools import product


def vertices(branch):
    a=[()]; lev=[()]
    for b in branch:
        lev=[x+(v,) for x in lev for v in range(b)]
        a.extend(lev)
    return a


def atom(t,V):
    k=len(t); n=len(V)
    # -1 represents unassigned pebbles; no false equalities are introduced.
    return tuple(v>=0 for v in t)+tuple(
        (0 if t[i]==t[j] else 1 if V[t[i]]==V[t[j]][:len(V[t[i]])]
         else 2 if V[t[j]]==V[t[i]][:len(V[t[j]])] else 3)
        if t[i]>=0 and t[j]>=0 else 4
        for i in range(k) for j in range(i+1,k))


def same_theory(branch1,branch2,k,max_rounds=100):
    Vs=[vertices(branch1),vertices(branch2)]
    states=[list(product(range(-1,len(V)),repeat=k)) for V in Vs]
    ats=[[atom(s,V) for s in S] for S,V in zip(states,Vs)]
    # index of any tuple is its lexicographic position in cartesian product
    def make_colors(sigs):
        d={s:i for i,s in enumerate(sorted({x for group in sigs for x in group}))}
        return [[d[s] for s in group] for group in sigs]
    colors=make_colors(ats)
    empty=[S.index((-1,)*k) for S in states]
    for q in range(max_rounds):
        nxt=[]
        for V,S,C in zip(Vs,states,colors):
            n=len(V); base=n+1
            # product(range(-1,n),repeat=k) has positional digits t_i+1.
            strides=[base**(k-1-i) for i in range(k)]
            ns=[]
            for idx,t in enumerate(S):
                reach=[]
                for i in range(k):
                    idx0=idx-(t[i]+1)*strides[i]
                    reach.append(tuple(sorted({C[idx0+(v+1)*strides[i]] for v in range(n)})))
                ns.append((C[idx], tuple(reach)))
            nxt.append(ns)
        new_colors=make_colors(nxt)
        old_types=len(set(colors[0]+colors[1])); new_types=len(set(new_colors[0]+new_colors[1]))
        colors=new_colors
        if old_types==new_types:
            return colors[0][empty[0]]==colors[1][empty[1]],q+1,new_types
    raise RuntimeError('No finite fixed point within the iteration budget')


def main():
    tests=[
        ((2,1,2),(2,3,4),2,True),
        ((1,2,2),(1,3,4),2,True),
        ((1,1,2),(1,2,1),2,False),
        ((2,2),(2,3),2,True),
        ((2,2),(2,3),3,False),
        ((3,2),(4,2),3,True),
        ((2,3),(2,4),3,True),
        ((1,2,2),(1,2,3),3,False),
        ((2,2),(2,2,1),3,False),
    ]
    for a,b,k,want in tests:
        got,rounds,types=same_theory(a,b,k)
        assert got==want,(a,b,k,got,want)
        print(f'PASS FO^{k}: {a} versus {b}; equivalent={got}; stable_after={rounds}; types={types}')
    print('PASS exact finite-depth logical fixed points')

if __name__=='__main__':main()
