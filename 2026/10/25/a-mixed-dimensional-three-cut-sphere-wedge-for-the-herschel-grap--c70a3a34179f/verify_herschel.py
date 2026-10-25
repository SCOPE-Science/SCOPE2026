#!/usr/bin/env python3
"""Recompute the 3-cut complex of an explicitly defined 11-vertex graph.

A face is a subset of a complementary disconnected triple.
All integer boundary signs use increasing vertex order.
Requires only Python 3 standard library.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

N = 11
ORDER = (0, 3, 1, 7, 8, 5, 4, 2, 9, 6, 10)
EDGES = tuple(sorted(tuple(sorted((x,y))) for ab,pairs in [((0,1),(5,6)), ((1,2),(7,8)), ((2,0),(9,10))] for a,b in [ab] for z in pairs for x,y in [(z,a),(z,b),(z,3+(z%2==0))]))
# Explicit choice of terminal attachments: odd red labels go to 3, even to 4.
# This parity convention is equivalent to interchanging the two terminals.
ADJ = [0]*N
for a,b in EDGES:
    ADJ[a] |= 1<<b
    ADJ[b] |= 1<<a
ALL=(1<<N)-1

def connected(mask):
    if not mask: return False
    reached=mask&-mask
    while True:
        new=reached
        for v in range(N):
            if reached>>v&1: new |= ADJ[v]&mask
        if new == reached: break
        reached=new
    return reached==mask

def boundary(mask):
    vertices=[v for v in range(N) if mask>>v&1]
    return {mask^(1<<v):(1 if i%2==0 else -1) for i,v in enumerate(vertices)}

assert len(EDGES)==18 and sorted(x.bit_count() for x in ADJ)==[3]*8+[4]*3
assert all(connected(ALL^a) for a in (0,))
for s in combinations(range(N),2):
    assert connected(ALL^sum(1<<v for v in s))
for s in combinations(range(N),1):
    assert connected(ALL^(1<<s[0]))

facets={ALL^sum(1<<v for v in triple) for triple in combinations(range(N),3)
        if not connected(sum(1<<v for v in triple))}
faces={0}
for f in facets:
    x=f
    while x:
        faces.add(x)
        x=(x-1)&f
nonempty=faces-{0}
face_counts=Counter(x.bit_count()-1 for x in faces)
assert len(facets)==123 and len(faces)==1930
assert tuple(face_counts[k] for k in range(-1,8))==(1,11,55,165,330,462,462,321,123)

unmatched=set(nonempty)
pairs=[]
for v in ORDER:
    b=1<<v
    for low in sorted(tuple(unmatched)):
        high=low|b
        if not low&b and low in unmatched and high in unmatched:
            unmatched.remove(low); unmatched.remove(high)
            pairs.append((low,high))
assert len(pairs)==957 and len(unmatched)==15
critical_counts=Counter(x.bit_count()-1 for x in unmatched)
assert critical_counts==Counter({0:1,6:1,7:13})

# Acyclic Morse matching: unmatched incidences run high->low;
# paired incidences run low->high.
paired={(low,high) for low,high in pairs}
out={f:[] for f in nonempty}
indegree={f:0 for f in nonempty}
for high in nonempty:
    if high.bit_count()==1: continue
    for low in boundary(high):
        if (low,high) in paired:
            u,v=low,high
        else:
            u,v=high,low
        out[u].append(v)
        indegree[v]+=1
queue=deque(x for x in nonempty if indegree[x]==0)
visited=0
while queue:
    u=queue.popleft();visited+=1
    for v in out[u]:
        indegree[v]-=1
        if indegree[v]==0:queue.append(v)
assert visited==len(nonempty)

# The incidence vector of the signed Morse differential C_7 -> C_6.
low_to_high={low:high for low,high in pairs}
@lru_cache(None)
def collapse_chain(s):
    if s in unmatched: return {s:1}
    if s not in low_to_high: return {}
    h=low_to_high[s]; full_boundary=boundary(h); pivot=full_boundary[s]
    result=defaultdict(int)
    for other,c in full_boundary.items():
        if other==s: continue
        for base,coef in collapse_chain(other).items():
            result[base] -= pivot*c*coef
    return {k:v for k,v in result.items() if v}

c6=sorted(x for x in unmatched if x.bit_count()==7)
c7=sorted(x for x in unmatched if x.bit_count()==8)
assert len(c6)==1 and len(c7)==13
morse=[]
for h in c7:
    integer=sum(sgn*collapse_chain(low).get(c6[0],0)
                for low,sgn in boundary(h).items())
    morse.append(integer)
assert morse==[0]*13

# Independent ordinary simplicial-boundary calculation over small fields.
bydim={d:sorted(x for x in nonempty if x.bit_count()-1==d) for d in range(8)}
def rank_mod2(d):
    lower={s:i for i,s in enumerate(bydim[d-1])}
    pivots={}
    for face in bydim[d]:
        v=0
        for s in boundary(face):v ^=1<<lower[s]
        while v:
            pivot=v.bit_length()-1
            if pivot not in pivots:
                pivots[pivot]=v
                break
            v ^=pivots[pivot]
    return len(pivots)

ranks={d:rank_mod2(d) for d in range(1,8)}
assert tuple(ranks[d] for d in range(1,8))==(10,45,120,210,252,210,110)

# Independent random-field rank check in the top two boundary degrees.
def rank_modp(d,p):
    lower={s:i for i,s in enumerate(bydim[d-1])}
    pivots={}
    for face in bydim[d]:
        v={lower[s]:c%p for s,c in boundary(face).items()}
        while v:
            row=max(v)
            if row not in pivots:
                u=pow(v[row],-1,p)
                pivots[row]={k:(val*u)%p for k,val in v.items()}
                break
            fac=v[row]
            for k,c in pivots[row].items():
                z=(v.get(k,0)-fac*c)%p
                if z:v[k]=z
                elif k in v:del v[k]
    return len(pivots)
for p in (3,5):
    assert rank_modp(6,p)==210 and rank_modp(7,p)==110

print('graph: 11 vertices, 18 edges, degrees 3^8 4^3, three-connected')
print('cut facets:',len(facets),'faces:',len(faces),'f(-1..7):',tuple(face_counts[k] for k in range(-1,8)))
print('Morse: pairs',len(pairs),'critical:',dict(sorted(critical_counts.items())), 'acyclic incidences:',sum(map(len,out.values())))
print('critical 6-face:',c6,'critical 7-faces:',c7)
print('integer Morse boundary:',morse)
print('mod2 boundary ranks:',tuple(ranks[d] for d in range(1,8)))
print('mod3,mod5 ranks at degrees 6 and 7: (210,110) each')
print('reduced homology Z in degree 6 and Z^13 in degree 7; sphere-wedge via simply-connected Morse CW')
print('VERIFY_OK')
