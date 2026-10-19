#!/usr/bin/env python3
"""Independent projection-merger enumeration and distance certification for bootstrap seeds.
Public mathematical definitions only."""
from collections import Counter,deque
from itertools import combinations,permutations
import json,hashlib

def spans_by_boxes(seed,d):
    full=(1<<d)-1
    boxes=[(full,v) for v in seed]
    while len(boxes)>1:
        changed=False
        for i in range(len(boxes)):
            if changed:break
            a,x=boxes[i]
            for j in range(i+1,len(boxes)):
                b,y=boxes[j]
                if ((x^y)&a&b).bit_count()<=2:
                    common=a&b&~(x^y)
                    boxes=[q for k,q in enumerate(boxes) if k not in (i,j)]+[(common,x&common)]
                    changed=True
                    break
        if not changed:break
    return len(boxes)==1 and boxes[0][0]==0

def main(d):
    n=1<<d; k=(d+1)//2+1
    assert not any(spans_by_boxes(x,d) for x in combinations(range(n),k-1))
    states=[t for t in combinations(range(n),k) if spans_by_boxes(t,d)]
    st=set(states)
    print('d',d,'seeds',len(states),flush=True)
    digest=hashlib.sha256((''.join(','.join(map(str,s))+'\n' for s in states)).encode()).hexdigest()
    print('SEED_SHA256',d,digest,flush=True)
    def neighbours(t,slide):
        members=set(t)
        for x in t:
            for y in ( (x^(1<<j) for j in range(d)) if slide else range(n)):
                if y not in members:
                    u=tuple(sorted((members-{x})|{y}))
                    if u in st:yield u
    # Full Hamming cube isometry group, not generator-orbit BFS.
    orbit_reps=[];unseen=set(states)
    perm_maps=[]
    for p in permutations(range(d)):
        perm_maps.append([sum(((x>>i)&1)<<p[i] for i in range(d)) for x in range(n)])
    while unseen:
        t=min(unseen); orbit_reps.append(t)
        orbit=set()
        for m in perm_maps:
            base=[m[x] for x in t]
            for shift in range(n):orbit.add(tuple(sorted(v^shift for v in base)))
        assert orbit<=st
        unseen-=orbit
    print('orbits',len(orbit_reps),flush=True)
    results={}
    for label,slide in [('jump',False),('slide',True)]:
        graph={t:tuple(set(neighbours(t,slide))) for t in states}
        records=[]
        for rep in orbit_reps:
            dist={rep:0};q=deque([rep])
            while q:
                t=q.popleft()
                for u in graph[t]:
                    if u not in dist:dist[u]=dist[t]+1;q.append(u)
            assert len(dist)==len(states)
            # no cross-use of previous computation
            counts=Counter(dist.values())
            r={'rep':rep,'degree':len(graph[rep]),
               'eccentricity':max(dist.values()),'layers':[counts[i] for i in range(max(dist.values())+1)]}
            records.append(r)
            print(' ',label,rep,'ecc',r['eccentricity'],'degree',r['degree'],flush=True)
        degree_hist=Counter()
        ecc_hist=Counter()
        for record in records:
            rep=record['rep'];orbit=set()
            for m in perm_maps:
                base=[m[x] for x in rep]
                for shift in range(n):orbit.add(tuple(sorted(v^shift for v in base)))
            assert len(orbit) and (len(orbit)+sum(ecc_hist.values())<=len(states))
            degree_hist[record['degree']]+=len(orbit)
            ecc_hist[record['eccentricity']]+=len(orbit)
        results[label]={'radius':min(ecc_hist),'diameter':max(ecc_hist),'ecc_hist':dict(sorted(ecc_hist.items())),'degree_hist':dict(sorted(degree_hist.items())),'edges':sum(k*v for k,v in degree_hist.items())//2,'reps':records}
        print(label,results[label]['radius'],results[label]['diameter'],results[label]['ecc_hist'],results[label]['edges'],flush=True)
    print('VERIFIED',d)
    print('MACHINE_SUMMARY',d,json.dumps(results,sort_keys=True))
if __name__=='__main__':
    for d in (4,5):main(d)
