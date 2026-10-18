#!/usr/bin/env python3
"""Independent projective-binary-plane model and 1-factorization test."""
from itertools import combinations,permutations
from collections import Counter,deque

# Projective plane PG(2,2) represented by nonzero vectors 1..7 in F_2^3;
# lines are 2D subspaces, with third nonzero vector equal to xor of the other two.
TRIPLES={frozenset((a,b,a^b)) for a in range(1,8) for b in range(a+1,8)}
LINES=sorted(TRIPLES, key=lambda s:tuple(sorted(s)))
assert len(LINES)==7 and all(len(x)==3 for x in LINES)
# Points 0..6 stand for binary vectors 1..7, lines 7..13.
G={v:set() for v in range(14)}
for l, triple in enumerate(LINES):
 for x in triple:
  a=x-1;b=l+7
  G[a].add(b);G[b].add(a)
E=sorted((p,l) for p in range(7) for l in G[p])
assert len(E)==21 and all(len(G[v])==3 for v in G)

def dist(a,b):
 q=deque([(a,0)]);visited={a}
 while q:
  v,d=q.popleft()
  if v==b:return d
  for w in G[v]-visited:visited.add(w);q.append((w,d+1))
 raise AssertionError('Disconnected')

# All 3-edge-colourings via 1-factorizations: enumerate matchings M0 by assigning
# an incident line to each point and requiring all seven chosen lines distinct;
# G-M0 is a single cycle of length 14, then alternate the two other colors.
PERFECT=[]
for t in permutations(range(7)):
 if all((t[p]+7) in G[p] for p in range(7)):
  PERFECT.append({(p,t[p]+7) for p in range(7)})
assert len(PERFECT)==24,len(PERFECT)
COLORS=set()
for m in PERFECT:
 rem=set(E)-m
 N={v:set() for v in G}
 for a,b in rem:N[a].add(b);N[b].add(a)
 assert all(len(N[v])==2 for v in N)
 # Cycle walk starting at 0 and either neighbor.
 prev=0;cur=min(N[0]);walk=[0]
 while cur!=0:
  assert cur not in walk
  walk.append(cur)
  prev,cur=cur,next(z for z in N[cur] if z!=prev)
 assert len(walk)==14
 cycle=[(min(a,b),max(a,b)) for a,b in zip(walk,walk[1:]+walk[:1])]
 assert len(set(cycle))==14
 for phase in (0,1):
  c={edge:0 for edge in m}
  for i,edge in enumerate(cycle):c[edge]=1+((i+phase)%2)
  assert all({c[(min(v,w),max(v,w))] for w in G[v]}=={0,1,2} for v in G)
  COLORS.add(tuple(c[e] for e in E))
assert len(COLORS)==48,len(COLORS)

# Independent distance-three check: enumerate all shortest 3-edge walks by
# intersection and inspect first/last colors (middle differs by properness).
OBSTRUCTIONS=[]
NONINC=[(p,l) for p in range(7) for l in range(7,14) if l not in G[p]]
assert len(NONINC)==28
for cvals in sorted(COLORS):
 c=dict(zip(E,cvals));bad=[]
 for p,l in NONINC:
  good=False;paths=0
  for q in G[l]:
   common=G[p]&G[q]
   assert len(common)==1
   h=next(iter(common))
   cols=(c[(p,h)],c[(q,h)],c[(q,l)])
   paths+=1
   if len(set(cols))==3:good=True
  assert paths==3
  if not good:bad.append((p,l))
 assert len(bad)==7 and len(set(p for p,l in bad))==7 and len(set(l for p,l in bad))==7
 OBSTRUCTIONS.append(tuple(bad))
# All color names give same sets six times each.
assert len(set(OBSTRUCTIONS))==8
assert Counter(x for B in set(OBSTRUCTIONS) for x in B)==Counter({pair:2 for pair in NONINC})

# Strong four-colouring: start from a 3-colouring and recolour a matching;
# independently validate ALL vertex pairs by BFS distances and enumerate
# paths of precisely the shortest possible length.
WITNESS=None
for cvals in sorted(COLORS):
 c=dict(zip(E,cvals))
 for S in combinations(E,4):
  if len({v for e in S for v in e})<8:continue
  d=dict(c)
  for e in S:d[e]=3
  def exists_geodesic(start,goal):
   DD=dist(start,goal)
   def walk(v,depth,used):
    if depth==DD:return v==goal
    for w in G[v]:
     e=(min(v,w),max(v,w));colour=d[e]
     if colour not in used and walk(w,depth+1,used|{colour}):return True
    return False
   return walk(start,0,set())
  if all(exists_geodesic(a,b) for a in G for b in range(a+1,14)):
   WITNESS=d;CHANGED=S;break
 if WITNESS is not None:break
assert WITNESS is not None
assert len({v for e in CHANGED for v in e})==8
# Independently count the complete fresh-colour matching repair spectrum
# for every labelled factorization, not merely the selected witness.
MM=[]
for k in range(8):
    MM.append([S for S in combinations(E,k)
               if len({v for e in S for v in e})==2*k])
HIST=set()
for cv in COLORS:
    c=dict(zip(E,cv))
    row=[]
    for Slist in MM:
        good_count=0
        for S in Slist:
            new=c.copy()
            for e in S:new[e]=3
            if all(any(len({new[(p,h)],new[(q,h)],new[(q,l)]})==3
                           for q in G[l] for h in (next(iter(G[p]&G[q])),))
                       for p,l in NONINC):
                good_count+=1
        row.append(good_count)
    HIST.add(tuple(row))
assert HIST=={(0,0,0,0,126,84,0,0)},HIST
print('PG22_LINES=',tuple(tuple(sorted(x)) for x in LINES))
print('PERFECT_MATCHINGS=24 COMPLEMENTS_ARE_HAMILTON_CYCLES=True')
print('LABELLED_THREE_EDGE_COLORINGS=48')
print('THREE_EDGE_COLORING_BAD_PAIRS=7 MATCHING_ON_NONINCIDENCES=True')
print('EIGHT_UNLABELLED_OBSTRUCTION_SETS DOUBLE_COVER_OF_28_NONINCIDENCES=True')
print('DISTANCE_CHECK_ALL_91_VERTEX_PAIRS=True')
print('INDEPENDENT_REPAIR_MATCHING_COUNTS=',tuple(map(len,MM)))
print('INDEPENDENT_REPAIR_SPECTRUM=',next(iter(HIST)))
print('STRONG_FOUR_COLOR_REPAIR_MATCHING=',CHANGED)
print('FOUR_COLOR_WITNESS=',tuple(WITNESS[e] for e in E))
print('INDEPENDENT_VERIFY_OK')
