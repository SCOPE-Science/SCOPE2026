#!/usr/bin/env python3
"""Replay all transitions and all-source BFS distances in certificate.json.

Run: python3 verify_certificate.py certificate.json
This certificate checker does not rely on cached experiment output.
"""
import sys,json,itertools,collections,hashlib
from collections import deque

def verify(name,D):
    edges=[tuple(e) for e in D['edges']]
    states=[tuple(m) for m in D['matchings']]
    adj=[set(xs) for xs in D['adjacency']]
    assert len(edges)==48 and len(set(edges))==48 and edges==sorted(edges)
    N=[set() for _ in range(16)]
    for u,v in edges:
        assert 0<=u<v<16
        N[u].add(v);N[v].add(u)
    assert all(len(x)==6 for x in N)
    assert all(len(N[u]&N[v])==2 for u,v in itertools.combinations(range(16),2))
    assert len(set(states))==len(states)
    for m in states:
        assert len(m)==8 and tuple(sorted(m))==m and len(set(m))==8
        ends=[v for e in m for v in edges[e]]
        assert sorted(ends)==list(range(16))
    # Independent recurrence exhaustively generates all perfect matchings.
    Elookup={e:i for i,e in enumerate(edges)}
    found=set()
    def rec(remaining,selected):
        if not remaining:
            found.add(tuple(sorted(selected)));return
        u=min(remaining)
        for v in N[u]&remaining:
            rec(remaining-{u,v},selected+[Elookup[(u,v) if u<v else (v,u)]])
    rec(set(range(16)),[])
    assert found==set(states)
    assert len(adj)==len(states)
    index={m:i for i,m in enumerate(states)}
    total=0
    for i,m in enumerate(states):
        legal=set()
        for e,f in itertools.combinations(m,2):
            a,b=edges[e];c,d=edges[f]
            for ((u,v),(w,x)) in (((a,c),(b,d)),((a,d),(b,c))):
                if v in N[u] and x in N[w]:
                    alt=tuple(sorted((set(m)-{e,f}) | {Elookup[min(u,v),max(u,v)],Elookup[min(w,x),max(w,x)]}))
                    legal.add(index[alt])
        assert legal==adj[i]
        assert i not in legal
        for j in legal:
            assert i in adj[j]
            A=set(m);B=set(states[j]);
            assert len(A-B)==len(B-A)==2
            four=list(A^B); endpoints=[w for k in four for w in edges[k]]
            assert len(set(endpoints))==4 and all(endpoints.count(w)==2 for w in set(endpoints))
        total+=len(legal)
    assert total%2==0
    leftover=set(range(len(states)))
    stats=[]
    while leftover:
        source=min(leftover);queue=[source];leftover.remove(source)
        for u in queue:
            for v in adj[u]:
                if v in leftover:leftover.remove(v);queue.append(v)
        ecc=[]
        for src in queue:
            ds={src:0};q=deque([src])
            while q:
                u=q.popleft()
                for v in adj[u]:
                    if v not in ds:ds[v]=ds[u]+1;q.append(v)
            assert len(ds)==len(queue)
            ecc.append(max(ds.values()))
        stats.append({'size':len(queue),'radius':min(ecc),'diameter':max(ecc),
                      'eccentricity_histogram':dict(sorted(collections.Counter(ecc).items())),
                      'degree_histogram':dict(sorted(collections.Counter(len(adj[i]) for i in queue).items()))})
    nontrivial=[x for x in stats if x['size']>1]
    nontrivial.sort(key=lambda x:(-x['size'],x['radius'],x['diameter']))
    summary={'perfect_matchings':len(states),'switch_edges':total//2,
             'component_size_histogram':dict(sorted(collections.Counter(x['size'] for x in stats).items())),
             'components':len(stats),'isolated':sum(not a for a in adj),
             'nontrivial_component_stats':nontrivial}
    # Object keys from JSON must be converted back from strings where appropriate.
    
    assert json.loads(json.dumps(summary))==D['summary']
    if name=='rook':
        freeze=[states[i] for i,a in enumerate(adj) if not a]
        assert len(freeze)==72
        for m in freeze:
            horizontal=[e for e in m if edges[e][0]//4==edges[e][1]//4]
            vertical=[e for e in m if edges[e][0]%4==edges[e][1]%4]
            assert len(horizontal)==len(vertical)==4
            column_pairs=[tuple(sorted((edges[e][0]%4,edges[e][1]%4))) for e in horizontal]
            assert len(set(column_pairs))==4
            assert all(sum(c in pair for pair in column_pairs)==2 for c in range(4))
    print(name,'certificate_OK','states=',len(states),'switches=',total//2,'components=',len(stats),'isolated=',sum(not a for a in adj))

def main():
    raw=open(sys.argv[1],'rb').read()
    D=json.loads(raw)
    assert D['schema']==1 and set(D['graphs'])=={'rook','shrikhande'}
    for name,g in D['graphs'].items():verify(name,g)
    print('CERTIFICATE_OK sha256=',hashlib.sha256(raw).hexdigest())
if __name__=='__main__':main()
