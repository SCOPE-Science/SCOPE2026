#!/usr/bin/env python3
"""Independent check via Kneser KG(5,2) and modular simplicial homology.
No output from the other verifier is used.
"""
from itertools import combinations
from collections import defaultdict

P = list(combinations(range(5),2))
G = [tuple(x) for x in combinations(range(10),2) if set(P[x[0]]).isdisjoint(P[x[1]])]
assert len(G)==15
# In the line graph of KG(5,2), vertices represent the 15 Petersen edges.
F=defaultdict(list)
for k in range(1,6):
    for chosen in combinations(range(15),k):
        endpoints = [i for e in chosen for i in G[e]]
        if len(set(endpoints))==2*k:F[k-1].append(chosen)
assert {d:len(v) for d,v in F.items()}=={0:15,1:75,2:145,3:90,4:6}

def rank_mod_p(columns,p):
    pivot={};rank=0
    for col in columns:
        x=dict(col)
        while x:
            j=max(x)
            if j not in pivot:
                c=x[j]
                inv=pow(c,-1,p)
                pivot[j]={a:(b*inv)%p for a,b in x.items()}
                rank+=1
                break
            mul=x[j];v=pivot[j]
            for a,b in v.items():
                z=(x.get(a,0)-mul*b)%p
                if z:x[a]=z
                else:x.pop(a,None)
    return rank

for p in (2,3,5,7,11):
    ranks={0:0}
    for d in range(1,5):
        idx={a:i for i,a in enumerate(F[d-1])}
        cols=[]
        for s in F[d]:
            col={}
            for i in range(d+1):col[idx[s[:i]+s[i+1:]]]=(1 if i%2==0 else -1)%p
            cols.append(col)
        ranks[d]=rank_mod_p(cols,p)
    betti={d:len(F[d])-ranks[d]-ranks.get(d+1,0) for d in range(5)}
    betti[0]-=1
    assert [betti[d] for d in range(5)]==[0,0,5,5,0]
    print('CHARACTERISTIC',p,'RANKS',[ranks[d] for d in range(5)],'REDUCED_BETTI',[betti[d] for d in range(5)])
print('KNESER_EDGE_COUNT',len(G),'FACE_VECTOR',[len(F[d]) for d in range(5)])
