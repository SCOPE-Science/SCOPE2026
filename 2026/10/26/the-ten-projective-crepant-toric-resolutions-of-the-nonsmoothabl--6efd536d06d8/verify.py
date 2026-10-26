#!/usr/bin/env python3
"""Exact exhaustive triangulation/coherence/flop check for an explicit lattice pentagon."""
from itertools import combinations
from collections import Counter, deque, defaultdict

P = ((0,0),(-2,-1),(-3,-2),(-2,-3),(-1,-2),(-2,-2),(-1,-1))
HEIGHTS = (
 (0,0,0,9,9,3,1),
 (0,0,0,10,7,3,1),
 (0,0,0,12,10,4,1),
 (0,0,0,0,3,-3,-2),
 (0,0,0,-2,5,-3,-5),
 (0,0,0,11,-11,-6,-4),
 (0,0,0,3,0,-3,-2),
 (0,0,0,0,2,-4,-3),
 (0,0,0,5,-1,-2,-5),
 (0,0,0,4,4,-1,-4),
)

def cross(a,b,c):
    (x,y),(u,v),(s,t) = (P[i] for i in (a,b,c))
    return (u-x)*(t-y)-(v-y)*(s-x)

def edges(t):
    return tuple(tuple(sorted(e)) for e in combinations(t,2))

def proper_cross(a,b,c,d):
    return (cross(a,b,c)*cross(a,b,d)<0 and cross(c,d,a)*cross(c,d,b)<0)

def compatible(t,s):
    for a,b in edges(t):
        for c,d in edges(s):
            if proper_cross(a,b,c,d): return False
            if (a,b)==(c,d):
                v=next(x for x in t if x not in (a,b))
                w=next(x for x in s if x not in (a,b))
                if cross(a,b,v)*cross(a,b,w)>0: return False
    return True

def enumeration():
    unit=tuple(t for t in combinations(range(7),3) if abs(cross(*t))==1)
    assert len(unit)==17
    comp={(i,j):compatible(unit[i],unit[j]) for i in range(len(unit)) for j in range(i+1,len(unit))}
    def search(chosen,cands):
        if len(chosen)==7:
            yield tuple(chosen)
        elif len(chosen)+len(cands)>=7:
            for k,v in enumerate(cands):
                yield from search(chosen+[v],[w for w in cands[k+1:] if comp[v,w]])
    out=tuple(search([],list(range(len(unit)))))
    assert len(out)==10
    assert len(set(out))==10
    return unit,out

def laplace(h,u,v,w,z):
    # Strict convexity condition at z for plane through u,v,w.
    d=cross(u,v,w)
    assert abs(d)==1
    numerator = cross(z,v,w)*h[u]+cross(u,z,w)*h[v]+cross(u,v,z)*h[w]
    return d*h[z]-numerator if d>0 else numerator-d*h[z]

def verify_height(unit,tri,h):
    incid=defaultdict(list)
    for k in tri:
        for edge in edges(unit[k]): incid[edge].append(k)
    assert sum(len(fs)==1 for fs in incid.values())==5
    assert sum(len(fs)==2 for fs in incid.values())==8
    assert all(1<=len(fs)<=2 for fs in incid.values())
    margins=[]
    for (u,v),fs in incid.items():
        if len(fs)!=2: continue
        w=next(q for q in unit[fs[0]] if q not in (u,v))
        z=next(q for q in unit[fs[1]] if q not in (u,v))
        assert cross(u,v,w)*cross(u,v,z)<0
        margins.append(laplace(h,u,v,w,z))
    assert len(margins)==8 and min(margins)>0, (min(margins),margins)
    return min(margins)

def main():
    unit,trs=enumeration()
    print('Unimodular triangle list:',list(enumerate(unit)))
    print('Triangulation index sets:',trs)
    margins=[verify_height(unit,tri,h) for tri,h in zip(trs,HEIGHTS)]
    graph=[set() for _ in trs]
    for i,j in combinations(range(len(trs)),2):
        ri,rj=set(trs[i]),set(trs[j]); old=ri-rj;new=rj-ri
        if len(old)==len(new)==2:
            oldT=[unit[k] for k in old];newT=[unit[k] for k in new]
            assert set().union(*map(set,oldT))==set().union(*map(set,newT))
            assert len(set().union(*map(set,oldT)))==4
            graph[i].add(j);graph[j].add(i)
    assert all(j in graph[i] for i in range(len(graph)) for j in graph[i])
    dist_counter=Counter(); ecc=[];max_pairs=[]; diam=-1
    for s in range(len(graph)):
        dist={s:0};q=deque([s])
        while q:
            u=q.popleft()
            for v in graph[u]:
                if v not in dist: dist[v]=dist[u]+1;q.append(v)
        assert len(dist)==len(graph)
        ecc.append(max(dist.values()))
        for t in range(s+1,len(graph)):
            d=dist[t];dist_counter[d]+=1
            if d>diam:diam=d;max_pairs=[(s,t)]
            elif d==diam:max_pairs.append((s,t))
    degree_hist=Counter(map(len,graph))
    assert sum(map(len,graph))//2==13
    assert degree_hist=={1:1,2:3,3:5,4:1}
    assert min(ecc)==3 and diam==5 and len(max_pairs)==1
    assert dist_counter=={1:13,2:16,3:11,4:4,5:1}
    print('Integer coherence height certificates:',HEIGHTS)
    print('Minimum convexity margins:',margins)
    print('Flop adjacency:',[sorted(g) for g in graph])
    print('Number of phases:',len(trs),'flops:',sum(map(len,graph))//2)
    print('Degree histogram:',dict(sorted(degree_hist.items())))
    print('Distance histogram:',dict(sorted(dist_counter.items())))
    print('Radius:',min(ecc),'diameter:',diam,'unique antipodal pair:',max_pairs)
    print('QB_EXACT_VERIFICATION_OK')
if __name__=='__main__':main()
