#!/usr/bin/env python3
"""Verify strict rankings of all six nonloop ternary cyclic digram counts.

Uses independent enumeration of arbitrary distinct integer profiles and
reconstruction from the three-interval parameterization. Optionally emit
all shortest-profile witnesses as JSON via --witnesses PATH.
"""
import argparse
import json
from collections import Counter
from itertools import combinations, permutations

EDGES = ((0,1),(1,0),(1,2),(2,1),(2,0),(0,2))
CYCLE = ((0,1),(1,2),(2,0))
REVERSED = ((1,0),(2,1),(0,2))
PATTERNS = {
    'OCOCOC': 21,
    'OCOOCC': 26,
    'OOCCOC': 22,
    'OOCOCC': 27,
    'OOOCCC': 21,
}

def rank_of(v):
    return tuple(EDGES[i] for i in sorted(range(6),key=lambda i:v[i]))

def balanced(v):
    return all(sum(v[i] for i,(u,w) in enumerate(EDGES) if u==s) ==
               sum(v[i] for i,(u,w) in enumerate(EDGES) if w==s)
               for s in range(3))

def direct_enumeration(max_length=27):
    winners={}
    checked=0
    # For six distinct positive numbers with total <=27, largest <=12.
    for values in combinations(range(1,13),6):
        n=sum(values)
        if n>max_length:
            continue
        for v in permutations(values):
            checked+=1
            if balanced(v):
                r=rank_of(v)
                if r not in winners or n<winners[r][0]:
                    winners[r]=(n,v)
    return winners,checked

def structural_enumeration(max_length=27):
    winners={}
    for a in range(1,max_length):
        for p in range(1,max_length):
            for q in range(1,max_length):
                for d in range(1,max_length):
                    if d in (p,q,p+q):
                        continue
                    n=6*a+4*p+2*q+3*d
                    if n>max_length:
                        continue
                    ys=(a,a+p,a+p+q)
                    xs=tuple(y+d for y in ys)
                    for order in permutations(range(3)):
                        for lo,hi in ((CYCLE,REVERSED),(REVERSED,CYCLE)):
                            dic={lo[order[k]]:ys[k] for k in range(3)}
                            dic.update({hi[order[k]]:xs[k] for k in range(3)})
                            v=tuple(dic[e] for e in EDGES)
                            r=rank_of(v)
                            if r not in winners or n<winners[r]:
                                winners[r]=n
    return winners

def type_of(v):
    dic=dict(zip(EDGES,v))
    d=dic[(0,1)]-dic[(1,0)]
    lo=REVERSED if d>0 else CYCLE
    hi=CYCLE if d>0 else REVERSED
    ordered=sorted(lo,key=lambda e:dic[e])
    ys=[dic[e] for e in ordered]
    xs=[dic[(e[1],e[0])] for e in ordered]
    merged=sorted([(x,'O') for x in ys]+[(x,'C') for x in xs])
    return ''.join(flag for _,flag in merged)

def canonical_cycle(profile):
    count=[[0]*3 for _ in range(3)]
    for (u,v),multiplicity in zip(EDGES,profile):
        count[u][v]=multiplicity
    stack=[0]
    end=[]
    while stack:
        v=stack[-1]
        nexts=[j for j in range(3) if count[v][j]]
        if nexts:
            u=min(nexts)
            count[v][u]-=1
            stack.append(u)
        else:
            end.append(stack.pop())
    verts=end[::-1]
    assert verts[0]==verts[-1] and len(verts)==sum(profile)+1
    word=''.join(str(v) for v in verts[:-1])
    assert all(word[i]!=word[(i+1)%len(word)] for i in range(len(word)))
    obs=tuple(sum((word[i]==str(a) and word[(i+1)%len(word)]==str(b))
                  for i in range(len(word))) for a,b in EDGES)
    assert obs==profile
    return word

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--witnesses')
    args=ap.parse_args()
    direct,count=direct_enumeration()
    derived=structural_enumeration()
    assert {r:n for r,(n,_) in direct.items()}==derived
    assert len(direct)==60
    tally=Counter(n for n,_ in direct.values())
    assert tally=={21:24,22:12,26:12,27:12}
    groups=Counter((type_of(profile),n) for n,profile in direct.values())
    assert groups==Counter((p,n) for p,n in PATTERNS.items() for _ in range(12)),groups
    witnesses=[]
    for rank,(n,profile) in sorted(direct.items()):
        witnesses.append({'ranking_low_to_high':[''.join(map(str,e)) for e in rank],
                         'counts_in_edge_order':list(profile),
                         'shortest_length':n,
                         'interleaving':type_of(profile),
                         'circular_word':canonical_cycle(profile)})
    if args.witnesses:
        with open(args.witnesses,'w',encoding='utf-8') as fp:
            json.dump({'edges':[''.join(map(str,e)) for e in EDGES],
                       'meaning':'Cyclic ordered-pair frequencies; every listed word contains each of the six allowed transitions and no equal adjacent symbols.',
                       'rankings':witnesses},fp,indent=2,ensure_ascii=False)
            fp.write('\n')
    print('TERNARY_SIX_RANKS_PASS ranks=60 min_lengths=21:24,22:12,26:12,27:12 maximally_required=27 direct_vectors_checked='+str(count))

if __name__=='__main__':
    main()
