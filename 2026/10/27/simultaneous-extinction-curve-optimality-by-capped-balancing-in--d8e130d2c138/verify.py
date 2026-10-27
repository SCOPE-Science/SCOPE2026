#!/usr/bin/env python3
"""Exact finite checks for a plant-pollinator extinction-area theorem."""
from itertools import combinations, permutations
from functools import lru_cache
import json

def opt_area_by_caps(caps):
    n=sum(caps)
    profile=[0]*len(caps)
    area=0
    prefix=[]
    for t in range(1,n+1):
        eligible=[j for j in range(len(caps)) if profile[j]<caps[j]]
        j=min(eligible,key=lambda j: (profile[j],j))
        profile[j]+=1
        prod=1
        for value in profile: prod*=value
        prefix.append(prod)
        area+=prod
    return area,prefix

def enumerate_group_sequences(caps):
    k=len(caps); n=sum(caps)
    best=-1; count=0
    def rec(profile,score):
        nonlocal best,count
        if sum(profile)==n:
            count+=1
            best=max(best,score)
            return
        for j in range(k):
            if profile[j]<caps[j]:
                profile[j]+=1
                p=1
                for v in profile: p*=v
                rec(profile,score+p)
                profile[j]-=1
    rec([0]*k,0)
    return best,count

def degree_prefix_max(H,n):
    full=(1<<n)-1
    deg=[v.bit_count() for v in H]
    edges=[0]*(full+1)
    for m in range(1,full+1):
        bit=m&-m
        i=bit.bit_length()-1
        edges[m]=edges[m^bit]+(H[i]&(m^bit)).bit_count()
    opt=[0]*(full+1)
    heuristic=[0]*(full+1)
    for m in range(1,full+1):
        vs=[i for i in range(n) if (m>>i)&1]
        opt[m]=edges[m]+max(opt[m^(1<<i)] for i in vs)
        d=min(deg[i] for i in vs)
        heuristic[m]=edges[m]+max(heuristic[m^(1<<i)] for i in vs if deg[i]==d)
    return opt[full],heuristic[full]

def census(n):
    pairs=list(combinations(range(n),2))
    fails=[]
    for bits in range(1<<len(pairs)):
        H=[0]*n
        for k,(i,j) in enumerate(pairs):
            if bits&(1<<k):
                H[i]|=1<<j
                H[j]|=1<<i
        opt,heur=degree_prefix_max(H,n)
        if opt>heur:
            fails.append({"edge_pairs":[list(pairs[k]) for k in range(len(pairs)) if bits&(1<<k)],"optimal_area":opt,"best_degree_area":heur})
    return fails

def run():
    caps_tests=[(2,3),(1,2,3),(2,2,2),(2,3,3),(1,2,4),(3,4),(1,1,1,3),(2,2,3)]
    seq=[]
    for caps in caps_tests:
        candidate,prefix=opt_area_by_caps(caps)
        maximum,orders=enumerate_group_sequences(caps)
        assert candidate==maximum,(caps,candidate,maximum)
        if len(caps)==2 and caps[0]<=caps[1]:
            a,b=caps
            assert 6*candidate==a*(a*a+3*b*b+3*b-1)
        seq.append({"caps":caps,"group_words_checked":orders,"optimum_area":maximum})
    checks={}
    for n in range(1,6):
        fails=census(n)
        checks[str(n)]={"graphs_examined":2**(n*(n-1)//2),"degree_failures":len(fails)}
        if n<=4:assert not fails
        else:
            assert len(fails)==10
            for f in fails:
                edges=f["edge_pairs"]
                deg=[sum(i in e for e in edges) for i in range(n)]
                assert sorted(deg)==[2,2,2,3,3]
                hubs=[i for i in range(n) if deg[i]==3]
                leaves=[i for i in range(n) if deg[i]==2]
                actual={tuple(sorted(e)) for e in edges}
                expected={tuple(sorted((u,v))) for u in hubs for v in leaves}
                assert actual==expected
                assert f["optimal_area"]==13 and f["best_degree_area"]==12
    out={"version":1,"cap_tests":seq,"all_graph_census":checks,"first_bad_graph_class":"K_2,3","result":"OK"}
    print(json.dumps(out,sort_keys=True,separators=(',',':')))

if __name__=="__main__":run()
