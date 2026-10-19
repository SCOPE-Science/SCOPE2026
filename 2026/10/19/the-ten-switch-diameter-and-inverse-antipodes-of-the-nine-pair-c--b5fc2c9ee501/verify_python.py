#!/usr/bin/env python3
"""Rebuild the crown-graph square-switch distances from derangements.
Python 3 standard library; no external data files.
"""
import itertools, json
from collections import Counter, deque
from math import factorial

def ctype(p):
    seen=set(); lengths=[]
    for v in range(len(p)):
        if v in seen: continue
        w=v; length=0
        while w not in seen:
            seen.add(w);length+=1;w=p[w]
        lengths.append(length)
    return tuple(sorted(lengths))

def analyze(n):
    vertices=[p for p in itertools.permutations(range(n)) if all(p[i]!=i for i in range(n))]
    lookup={p:i for i,p in enumerate(vertices)}
    assert len(lookup)==len(vertices)
    adjacency=[]
    for p in vertices:
        neighbors=[]
        for i in range(n):
            for j in range(i+1,n):
                # A square switch replaces (i,p_i),(j,p_j) by (i,p_j),(j,p_i).
                if p[i] != j and p[j] != i:
                    q=list(p);q[i],q[j]=q[j],q[i]
                    neighbors.append(lookup[tuple(q)])
        adjacency.append(tuple(neighbors))
    assert all(i in adjacency[j] for j,adj in enumerate(adjacency) for i in adj)
    reps={}
    size=Counter()
    for i,p in enumerate(vertices):
        typ=ctype(p);size[typ]+=1;reps.setdefault(typ,i)
    typetable=[]
    for typ,source in sorted(reps.items()):
        distances=[-1]*len(vertices)
        distances[source]=0;queue=deque([source]);hist=Counter()
        while queue:
            v=queue.popleft();hist[distances[v]]+=1
            for w in adjacency[v]:
                if distances[w]<0:
                    distances[w]=distances[v]+1;queue.append(w)
        ecc=max(distances)
        far=[vertices[k] for k,d in enumerate(distances) if d==ecc]
        inverse=tuple(vertices[source].index(i) for i in range(n))
        typetable.append({'cycle_type':list(typ),'count':size[typ],
                         'eccentricity':ecc,'reached':sum(d>=0 for d in distances),
                         'farthest_count':len(far),
                         'inverse_unique_antipode':(len(far)==1 and far[0]==inverse),
                         'distance_counts':[hist[k] for k in range(ecc+1)]})
    assert sum(x['count'] for x in typetable)==len(vertices)
    return {'n':n,'vertices':len(vertices),'edges':sum(map(len,adjacency))//2,
            'connected':all(row['reached']==len(vertices) for row in typetable),
            'radius':min(row['eccentricity'] for row in typetable),
            'diameter':max(row['eccentricity'] for row in typetable),
            'types':typetable}

def main():
    data=[analyze(n) for n in range(4,10)]
    assert [(x['n'],x['vertices'],x['diameter']) for x in data] == [
        (4,9,3),(5,44,4),(6,265,6),(7,1854,7),(8,14833,8),(9,133496,10)]
    t=data[-1]['types']
    assert [r for r in t if r['eccentricity']==10]==[
      next(r for r in t if r['cycle_type']==[3,3,3])]
    assert next(r for r in t if r['cycle_type']==[3,3,3])['inverse_unique_antipode']
    assert next(r for r in t if r['cycle_type']==[3,3,3])['count']==2240
    multiplicities={str(e):sum(row['count'] for row in t if row['eccentricity']==e) for e in sorted({row['eccentricity'] for row in t})}
    antipodal_sources=sum(row['count'] for row in t if row['eccentricity']==10 and row['inverse_unique_antipode'])
    assert multiplicities=={'8':93456,'9':37800,'10':2240} and antipodal_sources==2240
    print(json.dumps({'method':'permutation-enumeration and conjugacy-representative BFS',
      'small_n':[{k:v for k,v in d.items() if k!='types'} for d in data],
      'n9_cycle_type_profiles':data[-1]['types'],
      'n9_eccentricity_multiplicities':multiplicities,
      'n9_unordered_diametral_pairs':antipodal_sources//2},sort_keys=True,indent=2))
if __name__=='__main__':main()
