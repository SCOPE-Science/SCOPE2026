
from fractions import Fraction as F
from itertools import combinations, product
import json, hashlib

def tree_paths(n, edges):
    adj=[[] for _ in range(n)]
    for j,(a,b,t) in enumerate(edges):
        adj[a].append((b,j)); adj[b].append((a,j))
    paths={}
    for source in range(n):
        seen={source:([],[source])}; queue=[source]
        for x in queue:
            for y,i in adj[x]:
                if y not in seen:
                    pe,pv=seen[x];seen[y]=(pe+[i],pv+[y]); queue.append(y)
        assert len(seen)==n
        for d,x in seen.items(): paths[source,d]=x
    return paths

def check(n,edges,prior):
    paths=tree_paths(n,edges); weights=[e[2] for e in edges]
    b=[]
    for v in range(n):
        b.append(sum((prior[s]*__import__('math').prod(weights[j] for j in paths[s,v][0]) for s in range(n)),F(0)))
    runs=0
    for a,bv in combinations(range(n),2):
        P=paths[a,bv][1]; pind=set(paths[a,bv][0])
        rho=__import__('math').prod(weights[j] for j in pind)
        coefs={v:F(1)-sum((weights[j]/(1+weights[j]) for j in pind if v in edges[j][:2]),F(0)) for v in P}
        rhs=rho*sum((coefs[v]*b[v] for v in P),F(0))
        lhs=F(0)
        # direct edge-config and source weighted sum
        for mask in range(1<<len(edges)):
            probability=F(1)
            for j,t in enumerate(weights): probability *= t if mask&(1<<j) else (1-t)
            for s in range(n):
                if all(mask&(1<<j) for j in paths[s,a][0]+paths[s,bv][0]):
                    lhs+=probability*prior[s]
        assert lhs==rhs, (n,edges,prior,a,bv,lhs,rhs)
        runs+=1
    return runs

def prufer_tree(seq,n):
    degree=[1]*n
    for x in seq:degree[x]+=1
    es=[]
    for x in seq:
        leaf=min(i for i in range(n) if degree[i]==1)
        es.append((leaf,x));degree[leaf]-=1;degree[x]-=1
    x,y=[i for i in range(n) if degree[i]==1]
    es.append((x,y))
    return es

count=0; comparisons=0; configs=0
for n in range(2,6):
    seqs=product(range(n),repeat=n-2)
    for seq in seqs:
        e=prufer_tree(seq,n)
        for tset in (tuple(F(i+1,i+3) for i in range(n-1)), tuple(F(1,2) for i in range(n-1))):
            edges=[(*edge,t) for edge,t in zip(e,tset)]
            prior=[F(i+1,n*(n+1)//2) for i in range(n)]
            comparisons+=check(n,edges,prior)
            count+=1
            configs+= (1<<(n-1))*n*(n*(n-1)//2)
cert={"status":"passed","tree_weight_scenarios":count,"pair_comparisons":comparisons,"enumerated_source_edge_pair_configurations":configs,"n_range":[2,5],"arithmetic":"exact fractions", "checks":"joint outbreak monitor probability equals weighted path-local linear combination of single monitor marginals for every unordered monitor pair"}
print(json.dumps(cert,sort_keys=True))
