#!/usr/bin/env python3
"""Independent complete finite k-variable non-counting type refinement.
Each round computes possible replacement types as SETS, not multisets.
No use is made of the theorem's component strategy or length formulas.
"""
from itertools import product
from collections import Counter

def graph(parts):
    a=[]
    for n in parts:
        s=len(a)
        for i in range(n):a.append({s+(i-1)%n,s+(i+1)%n})
    return a

def canonical_pair_class(a,b,k=3,max_rounds=100):
    graphs=[a,b]
    seqs=[[t for t in product(range(len(g)), repeat=k)] for g in graphs]
    lookups=[{t:i for i,t in enumerate(tt)} for tt in seqs]
    at=[]
    for g,tt in zip(graphs,seqs):
        at.append([tuple((t[i]==t[j], t[j] in g[t[i]]) for i in range(k) for j in range(i+1,k)) for t in tt])
    pool=sorted(set(at[0])|set(at[1]))
    ids={v:i for i,v in enumerate(pool)}
    colors=[[ids[v] for v in aa] for aa in at]
    for r in range(max_rounds):
        sigs=[]
        for g,tt,lookup,c in zip(graphs,seqs,lookups,colors):
            row=[]
            for t in tt:
                rep=[]
                for j in range(k):
                    rep.append(tuple(sorted({c[lookup[t[:j]+(v,)+t[j+1:]]] for v in range(len(g))})))
                row.append((c[lookup[t]],)+tuple(rep))
            sigs.append(row)
        uniq={s:i for i,s in enumerate(sorted(set(sigs[0])|set(sigs[1])))}
        newer=[[uniq[s] for s in rows] for rows in sigs]
        # The joint partition across both graphs is stable iff the number
        # of joint types has stopped increasing under refinement.
        same=(len(uniq)==len(set(colors[0])|set(colors[1])))
        colors=newer
        if same:
            return set(colors[0])==set(colors[1]),r+1,len(uniq)
    raise RuntimeError('no fixed point after %d rounds'%max_rounds)

def main():
    comparisons=[
        ((3,), (4,),3,False),
        ((5,), (6,),3,False),
        ((3,), (3,3),3,False),
        ((3,3),(3,3,3),3,False),
        ((3,3,3),(3,3,3,3),3,True),
        ((4,4,4),(4,4,4,4),3,True),
        ((3,4),(3,4,4),3,False),
        ((3,3,3,4),(3,3,3,3,4),3,True),
        ((3,5),(3,6),3,False),
        ((3,3,3),(3,3,3,3),4,False),
    ]
    checked=0
    for left,right,k,want in comparisons:
        got,rounds,num=canonical_pair_class(graph(left),graph(right),k)
        assert got==want,(left,right,k,got,want)
        print('PEBBLE_OK k=%d G=%s H=%s equivalent=%s rounds=%d colors=%d' % (k,left,right,got,rounds,num))
        checked+=1
    print('PEBBLE_SUITE_OK comparisons=%d'%checked)
if __name__=='__main__':main()
