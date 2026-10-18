"""Independent graph construction and exact 1-WL comparisons for cycle roses."""
from collections import Counter

def rose(lengths):
    assert lengths and all(L>=3 for L in lengths)
    adj=[set()]
    for L in lengths:
        ids=list(range(len(adj),len(adj)+L-1))
        adj.extend(set() for _ in ids)
        chain=[0]+ids+[0]
        for u,v in zip(chain,chain[1:]):
            adj[u].add(v);adj[v].add(u)
    return adj

def colors_joint(G,H,rounds):
    ns=(len(G),len(H)); nodes=G+[{len(G)+v for v in a} for a in H]
    c=[0]*sum(ns)
    signatures=[]
    for step in range(rounds+1):
        signatures.append((tuple(sorted(c[:ns[0]])),tuple(sorted(c[ns[0]:]))))
        keys=[(c[u],tuple(sorted(c[v] for v in adj))) for u,adj in enumerate(nodes)]
        enc={key:j for j,key in enumerate(sorted(set(keys)))}
        c=[enc[key] for key in keys]
    return signatures

def refined_length_spectrum(adj):
    root=next(i for i,a in enumerate(adj) if len(a)>2)
    dist=[-1]*len(adj); dist[root]=0;todo=[root]
    for u in todo:
        for v in adj[u]:
            if dist[v]<0:dist[v]=dist[u]+1;todo.append(v)
    assert len(todo)==len(adj)
    even,odd=Counter(),Counter()
    for u in range(len(adj)):
        d=dist[u]
        if d==0:continue
        if sum(dist[v]==d-1 for v in adj[u])==2:even[2*d]+=1
        if sum(dist[v]==d for v in adj[u])==1:odd[2*d+1]+=1
    assert all(v%2==0 for v in odd.values())
    result=even+Counter({length:k//2 for length,k in odd.items()})
    return result

if __name__ == "__main__":
 for lengths in ((3,3),(4,5,7),(3,3,8),(5,6,6,11)):
     G=rose(lengths)
     got=refined_length_spectrum(G)
     assert got==Counter(lengths),(lengths,got)
     print('recovered',len(G),dict(sorted(got.items())))
 for r in range(1,31):
     A=rose((2*r+3,2*r+7));B=rose((2*r+5,2*r+5))
     sigs=colors_joint(A,B,r+4)
     assert all(a==b for a,b in sigs[:r+1]),r
     first=next((j for j,(a,b) in enumerate(sigs) if a!=b),None)
     print('r=',r,'n=',len(A),'first_WL_distinguishing_round=',first)
