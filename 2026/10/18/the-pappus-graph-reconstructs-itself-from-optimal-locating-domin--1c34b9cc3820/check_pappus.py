#!/usr/bin/env python3
"""Standalone exact finite verification of Pappus locating-domination configurations.
Uses only the Python standard library. The small finite-field classification is
also checked independently against all vertex subsets of size at most eight.
"""
from itertools import combinations, product
from collections import deque, Counter

F=range(3); N=18
# Vertices p_(x,y): 0..8; lines l_(m,d): 9..17; incidence y=mx+d in F_3.
adj=[set() for _ in range(N)]
for x,y,m in product(F,F,F):
    p=3*x+y
    d=(y-m*x)%3
    l=9+3*m+d
    adj[p].add(l); adj[l].add(p)
assert sorted(map(len,adj))==[3]*18
masks=[sum(1<<v for v in adj[u]) for u in range(N)]

def ld(S):
    seen={0}
    for u in range(N):
        if (S>>u)&1: continue
        sig=masks[u]&S
        if sig in seen:return False
        seen.add(sig)
    return True

def pol_code(a,b,c):
    assert a in (1,2)
    S=0
    for x in F:
        S |= 1<<(3*x+(a*x*x+b*x+c)%3)
    for m in F:
        intercept=(c-(b-m)**2*pow(a,-1,3)-a)%3
        S |= 1<<(9+3*m+intercept)
    return S

codes={p:pol_code(*p) for p in product((1,2),F,F)}
assert len(set(codes.values()))==18
assert all(ld(s) and s.bit_count()==6 for s in codes.values())
# An exact exhaustive independent check of every possible set <=8.
valid={k:set() for k in range(1,9)}
for k in range(1,9):
    for vertices in combinations(range(N),k):
        S=sum(1<<x for x in vertices)
        if ld(S):valid[k].add(S)
assert [len(valid[k]) for k in range(1,9)]==[0,0,0,0,0,18,540,4869]
assert valid[6]==set(codes.values())
print('LD_MINIMUM 6; MINIMUM_CODES 18')
print('LD_SIZE_COUNTS 1..8:',[len(valid[k]) for k in range(1,9)])

# Intersection graph: adjacent if and only if two minimum codes share 4 vertices.
intersections=Counter(); E=set()
P=list(codes)
for i,p in enumerate(P):
    for j in range(i+1,len(P)):
        q=P[j]
        v=(codes[p]&codes[q]).bit_count()
        intersections[v]+=1
        if v==4:E.add((p,q))
        if p[0]==q[0]:assert v in (0,2)
        else:
            assert v in (1,4)
assert intersections==Counter({4:27,2:54,1:54,0:18})

# Explicit algebraic self-isomorphism. a=1 code -> affine point (b,c+b^2-1),
# a=2 code -> nonvertical line slope -b, intercept c-b^2.
for p,q in combinations(P,2):
    S,T=codes[p],codes[q]
    edge=(S&T).bit_count()==4
    a,b,c=p; aa,bb,cc=q
    if a==aa:assert not edge
    else:
        point=(b,(c+b*b-1)%3) if a==1 else (bb,(cc+bb*bb-1)%3)
        slope=(-bb)%3 if aa==2 else (-b)%3
        intercept=(cc-bb*bb)%3 if aa==2 else (c-b*b)%3
        assert edge==(point[1]==(slope*point[0]+intercept)%3)
print('MIN_INTERSECTIONS:',dict(sorted(intersections.items())))
print('MIN_INTERSECTION_GRAPH: 18 vertices, 27 edges, Pappus incidence graph (explicit affine isomorphism)')

# Enumerate full token-add/remove graphs up to k=7 and k=8.
def build(k):
    V=set().union(*(valid[t] for t in range(1,k+1)))
    nbr={S:[] for S in V}
    for S in V:
        for u in range(N):
            T=S^(1<<u)
            if T in V:nbr[S].append(T)
    return nbr

def comps(nbr):
    seen=set();components=[]
    for s in nbr:
        if s in seen:continue
        c=[s];seen.add(s)
        for u in c:
            for v in nbr[u]:
                if v not in seen:seen.add(v);c.append(v)
        components.append(c)
    return components
G7=build(7);C7=comps(G7)
assert len(G7)==558
assert len(C7)==342
assert Counter(map(len,C7))==Counter({13:18,1:324})
assert all(sum(s in valid[6] for s in c)<=1 for c in C7)
assert sum(map(len,G7.values()))//2==216
print('TAR_LE_7: states 558 edges 216 components 18x13 + 324x1; different optimum codes disconnected')
G8=build(8);C8=comps(G8)
assert len(G8)==5427
assert Counter(map(len,C8))==Counter({4419:1,1:1008})
assert sum(map(len,G8.values()))//2==6156
assert sum(s in valid[6] for s in max(C8,key=len))==18
print('TAR_LE_8: states 5427 edges 6156 components 4419x1 + 1008x1; all minimum codes in large component')

# Exhaustive BFS, checking all 153 unordered pairs of minimum codes.
hist=Counter();intersection_metric=Counter()
for i,s in enumerate(sorted(valid[6])):
    distance={s:0};queue=deque([s])
    while queue:
        u=queue.popleft()
        for v in G8[u]:
            if v not in distance:
                distance[v]=distance[u]+1;queue.append(v)
    for t in sorted(valid[6])[i+1:]:
        d=distance[t]
        assert d==(s^t).bit_count()
        hist[d]+=1
        intersection_metric[((s&t).bit_count(),d)]+=1
assert hist==Counter({4:27,8:54,10:54,12:18})
print('OPTIMUM_CODE_DISTANCES_IN_TAR_LE_8:',dict(sorted(hist.items())))
print('INTERSECTION_DISTANCE:',dict(sorted(intersection_metric.items())))
print('VERIFY_OK')
