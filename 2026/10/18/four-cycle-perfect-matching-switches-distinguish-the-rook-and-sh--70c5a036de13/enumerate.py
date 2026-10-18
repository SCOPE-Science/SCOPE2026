#!/usr/bin/env python3
"""Exhaustive four-cycle matching-switch census on two sixteen-vertex graphs.

Run: python3 enumerate.py certificate.json
Only standard-library modules are required.
"""
import itertools, json, sys
from collections import Counter, deque

SH_STEPS={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}

def build_graph(name):
    E=[]
    for u in range(16):
        a,b=divmod(u,4)
        for v in range(u+1,16):
            c,d=divmod(v,4)
            good=(a==c or b==d) if name=='rook' else (((a-c)%4,(b-d)%4) in SH_STEPS)
            if good:E.append((u,v))
    assert len(E)==48
    N=[set() for _ in range(16)]
    for u,v in E:N[u].add(v);N[v].add(u)
    assert all(len(x)==6 for x in N)
    assert all(len(N[u]&N[v])==2 for u,v in itertools.combinations(range(16),2))
    return E,N

def all_matchings(E,N):
    ix={e:i for i,e in enumerate(E)}
    out=[]
    def rec(unused,choices):
        if not unused:
            out.append(tuple(sorted(choices)))
            return
        u=min(unused)
        for v in sorted(N[u]&unused):
            rec(unused-{u,v},choices+(ix[min(u,v),max(u,v)],))
    rec(set(range(16)),())
    out.sort()
    assert len(set(out))==len(out)
    return out,ix

def flip_neighbors(E,N,states,ix):
    where={m:i for i,m in enumerate(states)}
    adj=[set() for _ in states]
    for i,m in enumerate(states):
        for e,f in itertools.combinations(m,2):
            a,b=E[e];c,d=E[f]
            for (u,v),(w,x) in (((a,c),(b,d)),((a,d),(b,c))):
                if v in N[u] and x in N[w]:
                    new=tuple(sorted((set(m)-{e,f})|{ix[(min(u,v),max(u,v))],ix[(min(w,x),max(w,x))]}))
                    assert len(new)==8 and new in where
                    j=where[new]
                    assert j!=i
                    adj[i].add(j)
    assert all(i in adj[j] for i,a in enumerate(adj) for j in a)
    return [sorted(a) for a in adj]

def component_stats(adj):
    remaining=set(range(len(adj)))
    cc=[]
    while remaining:
        start=min(remaining);remaining.remove(start)
        todo=[start]
        for u in todo:
            for v in adj[u]:
                if v in remaining:
                    remaining.remove(v);todo.append(v)
        cc.append(sorted(todo))
    cc.sort(key=lambda c:(-len(c),c[0]))
    entries=[]
    for comp in cc:
        eccentricity=[]
        for src in comp:
            dist={src:0};todo=deque([src])
            while todo:
                u=todo.popleft()
                for v in adj[u]:
                    if v not in dist:
                        dist[v]=dist[u]+1;todo.append(v)
            assert len(dist)==len(comp)
            eccentricity.append(max(dist.values()))
        entries.append({'size':len(comp), 'radius':min(eccentricity), 'diameter':max(eccentricity),
                        'eccentricity_histogram':dict(sorted(Counter(eccentricity).items())),
                        'degree_histogram':dict(sorted(Counter(len(adj[x]) for x in comp).items()))})
    return entries

def main():
    dest=sys.argv[1] if len(sys.argv)>1 else 'certificate.json'
    data={'schema':1,'vertex_labels':'u=4*a+b, a,b in {0,1,2,3}',
          'switch_rule':'symmetric difference is one alternating four-cycle', 'graphs':{}}
    for kind in ('rook','shrikhande'):
        E,N=build_graph(kind)
        states,ix=all_matchings(E,N)
        adj=flip_neighbors(E,N,states,ix)
        comps=component_stats(adj)
        summary={'perfect_matchings':len(states),'switch_edges':sum(map(len,adj))//2,
                 'component_size_histogram':dict(sorted(Counter(c['size'] for c in comps).items())),
                 'components':len(comps), 'isolated':sum(len(a)==0 for a in adj),
                 'nontrivial_component_stats':[c for c in comps if c['size']>1]}
        data['graphs'][kind]={'edges':E,'matchings':states,'adjacency':adj,'summary':summary}
        print(kind,json.dumps(summary,sort_keys=True,separators=(',',':')))
    with open(dest,'w',encoding='utf-8',newline='\n') as f:
        json.dump(data,f,sort_keys=True,separators=(',',':'));f.write('\n')
if __name__=='__main__':main()
