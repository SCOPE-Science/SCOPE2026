"""Exhaustive one-root colour-refinement orbit certificates for abelian Cayley graphs of order <16.

Run: python enumerate_cayley.py [output certificate JSON]
Requires networkx 3.x. The certificate itself is verified without networkx.
"""
import itertools, json, sys
from collections import Counter, defaultdict
import networkx as nx

GROUPS=[(1,), (2,), (3,), (4,), (2,2), (5,), (6,), (7,),
        (8,), (4,2), (2,2,2), (9,), (3,3), (10,), (11,),
        (12,), (6,2), (13,), (14,), (15,)]

def group(factors):
    points=list(itertools.product(*[range(x) for x in factors]))
    idof={p:i for i,p in enumerate(points)}
    add=lambda x,y:idof[tuple((a+b)%k for a,b,k in zip(x,y,factors))]
    seen={points[0]};pairs=[]
    for x in points[1:]:
        if x in seen:continue
        inv=tuple((-a)%k for a,k in zip(x,factors))
        seen|={x,inv};pairs.append([x] if x==inv else [x,inv])
    return points,add,pairs

def stable(adj):
    n=len(adj); colors=[1]+[0]*(n-1)
    for r in range(n):
        sig=[(colors[i], tuple(sorted(Counter(colors[j] for j in adj[i]).items()))) for i in range(n)]
        cv={v:k for k,v in enumerate(sorted(set(sig)))}
        nxt=[cv[x] for x in sig]
        if len(set(nxt))==len(set(colors)):return colors,r
        colors=nxt
    raise AssertionError('rounds did not stabilize')

def valid(adj,p,root,source,target):
    n=len(adj)
    return sorted(p)==list(range(n)) and p[root]==root and p[source]==target and all(
       (j in adj[i])==(p[j] in adj[p[i]]) for i in range(n) for j in range(n))

def run(path):
    result={'version':1,'scope':'undirected simple Cayley graphs of all abelian groups of order less than 16', 'cases':[]}
    counts=defaultdict(int);required=0
    for fac in GROUPS:
        points,add,invclasses=group(fac);n=len(points);m=len(invclasses)
        for mask in range(1<<m):
            chosen=[x for k,pair in enumerate(invclasses) if mask>>k&1 for x in pair]
            adj=[sorted(add(a,x) for x in chosen) for a in points]
            col,rounds=stable(adj)
            cls=defaultdict(list)
            for i,c in enumerate(col):cls[c].append(i)
            g=nx.Graph();g.add_nodes_from(range(n));g.add_edges_from((i,j) for i in range(n) for j in adj[i] if j>i)
            cert=[]
            for cell in cls.values():
                for target in cell[1:]:
                    source=cell[0]
                    a=g.copy();b=g.copy()
                    for i in range(n):
                        a.nodes[i]['mark']=2 if i==0 else 1 if i==source else 0
                        b.nodes[i]['mark']=2 if i==0 else 1 if i==target else 0
                    gm=nx.algorithms.isomorphism.GraphMatcher(a,b,node_match=lambda x,y:x['mark']==y['mark'])
                    mapping=next(gm.isomorphisms_iter(),None)
                    if mapping is None:raise AssertionError(('counterexample',fac,mask,source,target))
                    perm=[mapping[i] for i in range(n)]
                    assert valid(adj,perm,0,source,target)
                    cert.append([source,target,perm]);required+=1
            result['cases'].append({'factors':list(fac),'mask':mask,'colour_classes':len(cls),'rounds':rounds,'witnesses':cert})
            counts[n]+=1
    result['case_counts']={str(x):counts[x] for x in sorted(counts)}
    result['total_cases']=len(result['cases'])
    result['total_witnesses']=required
    with open(path,'w',encoding='utf-8',newline='\n') as f:json.dump(result,f,separators=(',',':'));f.write('\n')
    print(json.dumps({'case_counts':result['case_counts'],'total_cases':len(result['cases']),'total_witnesses':required},sort_keys=True))

if __name__=='__main__':run(sys.argv[1] if len(sys.argv)>1 else 'cayley_certificates.json')
