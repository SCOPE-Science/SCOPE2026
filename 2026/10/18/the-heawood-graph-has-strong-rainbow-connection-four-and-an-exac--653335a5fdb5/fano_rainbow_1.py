#!/usr/bin/env python3
"""Exact geodesic-rainbow enumeration on the Fano incidence graph.

Reproduces all labelled proper 3-edge-colourings up to permuting the palette,
their geodesic obstructions, and a proper strong rainbow 4-colouring.
"""
from itertools import combinations
from collections import Counter

# Seven lines obtained from the cyclic (7,3,1) difference set {0,1,3}.
LINES = tuple(frozenset(((i + d) % 7) for d in (0,1,3)) for i in range(7))
E = tuple((p, 7 + l) for p in range(7) for l in range(7) if p in LINES[l])
assert len(E) == 21 and len(set(LINES)) == 7
INC = [tuple(i for i,(p,l) in enumerate(E) if v in (p,l)) for v in range(14)]
assert all(len(x)==3 for x in INC)
ED = {e:i for i,e in enumerate(E)}
ADJ = [set() for _ in range(14)]
for p,l in E:ADJ[p].add(l);ADJ[l].add(p)
# Enumerate geodesics, not arbitrary paths.
PATHS={}
for a in range(14):
 for b in range(a+1,14):
  paths=[(ED[(a,x)],ED[(y,x)],ED[(y,b)]) for x in ADJ[a] for y in ADJ[b] if y in ADJ[x]] if a<7 and b>=7 and b not in ADJ[a] else None
  if paths is None:continue
  assert len(paths)==3,(a,b,paths)
  PATHS[a,b]=tuple(paths)
assert len(PATHS)==28
# Count all 3-colourings. Fix the three colours at point 0 in increasing line order.
START=dict(zip(INC[0],(0,1,2)))
COLOURINGS=[]
def rec(col):
 if len(col)==21:
  COLOURINGS.append(tuple(col[i] for i in range(21)))
  return
 best=None;vals=None
 for i,(p,l) in enumerate(E):
  if i in col:continue
  used={col[j] for v in (p,l) for j in INC[v] if j in col}
  avail=[c for c in (0,1,2) if c not in used]
  if not avail:return
  if best is None or len(avail)<len(vals):best=i;vals=avail
  if len(vals)==1:break
 for v in vals:
  col[best]=v;rec(col);del col[best]
rec(START)
assert len(COLOURINGS)==8,len(COLOURINGS)

def bad_pairs(col):
 return tuple(pair for pair, paths in PATHS.items() if not any(len({col[e] for e in path})==3 for path in paths))

BAD = [bad_pairs(c) for c in COLOURINGS]
assert [len(b) for b in BAD]==[7]*8
assert all(set(a for a,_ in b)==set(range(7)) and set(l for _,l in b)==set(range(7,14)) for b in BAD)
assert set(x for row in BAD for x in row)==set(PATHS)
assert Counter(x for row in BAD for x in row)==Counter({p:2 for p in PATHS})

# Full geometric lower bound: every three-colouring strong on this girth-six graph
# must be proper because every distance-two pair has a unique length-two path.
# Four-colour upper bound: search recolouring a matching in one proper 3-colouring.
C=COLOURINGS[0]
FOUR=None
MATCH_REPAIRS=Counter()
for col in COLOURINGS:
 found=[]
 for k in range(1,8):
  for S in combinations(range(21),k):
   vertices=[v for i in S for v in E[i]]
   if len(set(vertices))!=2*k:continue
   c=list(col)
   for i in S:c[i]=3
   if not bad_pairs(c):found.append(S)
  if found:
   MATCH_REPAIRS[k]+=1
   if col==C:FOUR=tuple(3 if j in found[0] else col[j] for j in range(21));REPAIRS=found
   break
assert MATCH_REPAIRS==Counter({4:8}), MATCH_REPAIRS
assert FOUR is not None and not bad_pairs(FOUR)
assert all(len(set(FOUR[j] for j in INC[v]))==3 for v in range(14))
assert set(FOUR)==set(range(4))
# Check distance-one and distance-two geodesics independently.
for a in range(14):
 for b in range(a+1,14):
  if b in ADJ[a]:continue
  if (a<7 and b>=7):continue
  common=ADJ[a]&ADJ[b]
  assert len(common)==1, (a,b,common)
  mid=next(iter(common))
  def edge(a,b):return ED[(a,b)] if a<7 else ED[(b,a)]
  assert FOUR[edge(a,mid)]!=FOUR[edge(mid,b)]
# Complete one-fresh-color repair spectrum.  A valid repair recolours a
# matching to the fourth colour and leaves the old three colours unchanged.
REPAIR_SPECTRA=[]
MATCHING_COUNTS=[]
for k in range(8):
    matchsets=[frozenset(S) for S in combinations(range(21),k)
               if len({v for j in S for v in E[j]})==2*k]
    MATCHING_COUNTS.append(len(matchsets))
    counts=[]
    for col in COLOURINGS:
        counts.append(sum(not bad_pairs(tuple(3 if j in S else col[j]
                                      for j in range(21))) for S in matchsets))
    assert len(set(counts))==1,counts
    REPAIR_SPECTRA.append(counts[0])
assert REPAIR_SPECTRA==[0,0,0,0,126,84,0,0],REPAIR_SPECTRA
assert MATCHING_COUNTS==[1,21,168,644,1218,1050,336,24],MATCHING_COUNTS
print('GRAPH_VERTICES=14 EDGES=21 DISTANCE3_PAIRS=28')
print('THREE_PALETTE_QUOTIENT_COLORINGS=8 LABELLED_COLORINGS=48')
print('BAD_PER_COLORING=7 PERFECT_MATCHING=True')
print('OBSTRUCTION_MULTIPLICITY_EVERY_NONINCIDENCE=2')
print('MATCHING_COUNTS_BY_SIZE=',MATCHING_COUNTS)
print('FOURTH_COLOR_REPAIR_COUNTS_BY_SIZE=',REPAIR_SPECTRA)
print('MINIMUM_ONE_NEW_COLOR_MATCHING_REPAIR=4 IN_EACH_OF_8_CASES')
print('STRONG_RAINBOW_CONNECTION_NUMBER=4')
print('EDGE_LIST=',E)
print('FOUR_COLOR_WITNESS=',FOUR)
print('FOUR_COLOR_CHANGED_EDGES=',tuple(E[i] for i in range(21) if C[i]!=FOUR[i]))
print('ALL_VERIFY_OK')
