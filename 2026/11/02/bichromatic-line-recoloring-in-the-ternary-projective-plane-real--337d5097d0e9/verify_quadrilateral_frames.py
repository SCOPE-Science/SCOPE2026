#!/usr/bin/env python3
"""Independent affine model and complete-quadrilateral enumeration of PG(2,3)."""
from itertools import combinations
from collections import Counter,deque
F=range(3)
points=[('a',x,y) for x in F for y in F]+[('d',m) for m in range(4)]
idx={p:i for i,p in enumerate(points)}
lines=[]
for m in F:
    for b in F:
        lines.append({idx[('a',x,(m*x+b)%3)] for x in F}|{idx[('d',m)]})
for x in F:
    lines.append({idx[('a',x,y)] for y in F}|{idx[('d',3)]})
lines.append({idx[('d',m)] for m in range(4)})
assert len(lines)==13 and len(set(map(frozenset,lines)))==13
assert all(len(L)==4 for L in lines)
assert all(sum(p in L for L in lines)==4 for p in range(13))
assert all(len(A&B)==1 for A,B in combinations(lines,2))
assert all(sum((a in L and b in L) for L in lines)==1 for a,b in combinations(range(13),2))
quad={};lineframes={}
for frame in combinations(range(13),4):
    corners={next(iter(lines[i]&lines[j])) for i,j in combinations(frame,2)}
    if len(corners)!=6: continue
    s=sum(1<<v for v in corners)
    assert s not in quad
    quad[s]=frame
    lineframes[frame]=s
assert len(quad)==234
linebits=[sum(1<<p for p in L) for L in lines]
full=(1<<13)-1
# Independently verify that every frame complement and its six corners hit each line.
for s in quad:
    assert all(0<(s&l).bit_count()<4 for l in linebits)
    assert sorted(Counter((s&l).bit_count() for l in linebits).items())==[(1,6),(2,3),(3,4)]
valid=[s for s in range(1<<13) if all(0<(s&l).bit_count()<4 for l in linebits)]
assert len(valid)==468 and {s for s in valid if s.bit_count()==6}==set(quad)
H={s:{t for t in quad if not(s&t)} for s in quad}
assert all(len(v)==3 for v in H.values())
for s,ns in H.items():
    # Four frame-line unused points are forbidden red additions; the 3 leftovers give neighbors.
    frame=quad[s]; forbidden={next(iter(lines[i]-{j for j in range(13) if (s>>j)&1})) for i in frame}
    outside={i for i in range(13) if not(s>>i)&1}
    allowed={i for i in outside if (full^s^(1<<i)) in quad}
    assert len(forbidden)==4 and len(allowed)==3 and allowed==outside-forbidden
    assert ns=={full^s^(1<<i) for i in allowed}
# Check H has no loops, is undirected and odd-cycle (non-bipartite), and is connected.
assert all(s not in ns and all(s in H[t] for t in ns) for s,ns in H.items())
nonbip=False;colors={next(iter(H)):0};q=deque(colors)
while q:
    s=q.popleft()
    for t in H[s]:
        if t not in colors: colors[t]=1-colors[s];q.append(t)
        else:
            if colors[t]==colors[s]: nonbip=True
assert len(colors)==234 and nonbip
# Recoloring graph: 6-subsets vs 7-subsets; adjacency is exactly disjointness.
colorings={s for s in valid}
for s in quad:
    moves={s^(1<<i) for i in range(13) if (s^(1<<i)) in colorings}
    assert moves=={full^t for t in H[s]}
print('QUADRILATERAL_FRAME_GEOMETRY_PASS')
print('ordered_frames',234*24,'unordered_frames',len(quad),'bicolorings',len(valid),'partners_per_frame',3,'nonbipartite_frame_graph',nonbip)
# Construct the projective frame stabilizer without using graph-automorphism software.
from itertools import product
homog=[(x,y,1) for x in F for y in F]+[(1,m,0) for m in F]+[(0,1,0)]
def pn(v):
    first=next(z for z in v if z)
    return tuple((a*first)%3 for a in v)  # first^{-1}=first in F_3
rep={pn(v):i for i,v in enumerate(homog)}
def det3(M):
    a,b,c,d,e,f,g,h,i=M
    return (a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g))%3
base=next(iter(quad));frame=set(quad[base]);neighbors=set()
three={i for i in range(13) if not(base>>i)&1 and (full^base^(1<<i)) in quad}
stabilizer=0
for M in product(F,repeat=9):
    if not det3(M): continue
    if pn(M)!=M: continue  # scalar quotient, first nonzero matrix entry = 1
    pmap={i:rep[pn(tuple(sum(M[3*r+c]*v[c] for c in range(3))%3 for r in range(3)))] for i,v in enumerate(homog)}
    if {frozenset(pmap[p] for p in lines[f]) for f in frame}!={frozenset(lines[f]) for f in frame}:
        continue
    stabilizer+=1
    neighbors|={pmap[i] for i in three}
assert stabilizer==24 and neighbors==three
print('PROJECTIVE_FRAME_STABILIZER_ARC_TRANSITIVITY_PASS',stabilizer,sorted(three))
