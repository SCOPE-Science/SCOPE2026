#!/usr/bin/env python3
"""Exact exhaustive evidence for a rooted voter-copying network theorem.
Run with Python 3. No optional dependencies or external input.
"""
from fractions import Fraction as F
from itertools import combinations
import json

def solve(mat, rhs):
    n=len(rhs)
    a=[[F(x) for x in row]+[F(rhs[i])] for i,row in enumerate(mat)]
    for j in range(n):
        k=next((k for k in range(j,n) if a[k][j]),None)
        assert k is not None, ('singular',j)
        a[j],a[k]=a[k],a[j]
        pivot=a[j][j]
        a[j]=[u/pivot for u in a[j]]
        for i in range(n):
            if i!=j and a[i][j]:
                f=a[i][j]; a[i]=[u-f*v for u,v in zip(a[i],a[j])]
    return [row[-1] for row in a]

def adj(n,edges):
    out=[set() for _ in range(n)]
    for u,v in edges:out[u].add(v);out[v].add(u)
    return out

def connected(n,edges):
    a=adj(n,edges);seen={0};q=[0]
    for v in q:
        for w in a[v]:
            if w not in seen:seen.add(w);q.append(w)
    return len(seen)==n

def dissent(n,edges,root):
    a=adj(n,edges);V=[v for v in range(n) if v!=root];index={v:i for i,v in enumerate(V)}
    mat=[[F(0) for _ in V] for _ in V]
    rhs=[]
    for v in V:
        i=index[v];mat[i][i]=len(a[v]);rhs.append(len(a[v]))
        for w in a[v]:
            if w!=root:mat[i][index[w]]-=1
    h=solve(mat,rhs)
    return sum(h,F(0)),{v:h[index[v]] for v in V}

def dissent_direct(n,edges,root):
    # State-space expectation of total cumulative negative opinions; root positive.
    a=adj(n,edges);V=[i for i in range(n) if i!=root]
    M=1<<len(V);Q=[[F(0) for _ in range(M-1)] for _ in range(M-1)]
    R=[]
    for s in range(M-1):
        R.append(len(V)-s.bit_count())
        for idx,v in enumerate(V):
            for w in a[v]:
                prob=F(1,len(a[v]))
                new=(s>>V.index(w))&1 if w!=root else 1
                snew=(s&~(1<<idx)) | (new<<idx)
                if snew!=s:
                    Q[s][s]-=prob
                    if snew<M-1:Q[s][snew]+=prob
    x=solve([[-u for u in row] for row in Q],R)
    return x[0]

def fraction(x):return str(x)

def main():
    record={};total_tests=0
    for n in range(2,5):
        possible=list(combinations(range(n),2));counts={'rooted_connected_graphs':0,'eligible_additions':0,'positive_change':0,'negative_change':0,'zero_change':0}
        mn=None;mx=None
        for bit in range(1<<len(possible)):
            E=tuple(possible[k] for k in range(len(possible)) if (bit>>k)&1)
            if not connected(n,E):continue
            for root in range(n):
                counts['rooted_connected_graphs']+=1
                missing=[p for p in possible if p not in E and root not in p]
                if not missing:continue
                old,_=dissent(n,E,root)
                for edge in missing:
                    new,_=dissent(n,E+(edge,),root)
                    delta=new-old
                    counts['eligible_additions']+=1;total_tests+=1
                    key='positive_change' if delta>0 else 'negative_change' if delta<0 else 'zero_change'
                    counts[key]+=1
                    mn=delta if mn is None else min(mn,delta)
                    mx=delta if mx is None else max(mx,delta)
        counts['minimum_delta']=fraction(mn) if mn is not None else None
        counts['maximum_delta']=fraction(mx) if mx is not None else None
        record[str(n)]=counts
        assert not counts['negative_change']
    n=5;root=0;E=((0,1),(0,4),(1,2),(2,3));add=(2,4)
    old,h=dissent(n,E,root);new,h2=dissent(n,E+(add,),root)
    direct_old=dissent_direct(n,E,root);direct_new=dissent_direct(n,E+(add,),root)
    assert (old,new)==(F(23),F(21))
    assert (direct_old,direct_new)==(old,new)
    three=((0,1),(0,2)); old3,_=dissent(3,three,0);new3,_=dissent(3,three+((1,2),),0)
    assert (old3,new3)==(F(2),F(4))
    out={'method':'exact rational grounded-Laplacian linear solves over all labeled connected simple graphs; independently checked witness by full 16-state voter Markov generator','n2_to_n4':record,'total_addition_tests':total_tests,'five_vertex_witness':{'root':root,'before_edges':[list(e) for e in E],'added_edge':list(add),'before_integrated_dissent':fraction(old),'after_integrated_dissent':fraction(new),'change':fraction(new-old),'before_hitting_times':{str(k):fraction(v) for k,v in h.items()},'after_hitting_times':{str(k):fraction(v) for k,v in h2.items()},'direct_markov_before':fraction(direct_old),'direct_markov_after':fraction(direct_new)},'three_vertex_worsening':{'before':fraction(old3),'after':fraction(new3)}}
    print(json.dumps(out,sort_keys=True,separators=(',',':')))

if __name__=='__main__': main()
