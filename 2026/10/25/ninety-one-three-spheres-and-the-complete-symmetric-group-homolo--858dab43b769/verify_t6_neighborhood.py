#!/usr/bin/env python3
"""Exact independent certificate for the six-label triangular-graph neighborhood complex.
Only Python 3 standard library is required; no external data files.
"""
from itertools import combinations,permutations
from collections import Counter,defaultdict,deque
LABELS=list(combinations(range(6),2));assert len(LABELS)==15
N=[sum(1<<j for j,b in enumerate(LABELS) if j!=i and bool(set(a)&set(b))) for i,a in enumerate(LABELS)]
assert all(nb.bit_count()==8 for nb in N)
F={0}
for nb in N:
 s=nb
 while s:
  F.add(s);s=(s-1)&nb
assert len(F)==2881
FV=Counter(f.bit_count()-1 for f in F)
assert FV=={-1:1,0:15,1:105,2:420,3:945,4:840,5:420,6:120,7:15}
print('EXACT_FACE_VECTOR',dict(sorted(FV.items())))
ORDER=(2,11,3,4,1,0,9,12,6,10,14,5,7,13,8)
remaining=set(F);pairs=set()
for i in ORDER:
 bit=1<<i
 for x in sorted(remaining):
  y=x|bit
  if not x&bit and x in remaining and y in remaining:
   pairs.add((x,y));remaining.remove(x);remaining.remove(y)
assert len(pairs)==1395 and len(remaining)==91
assert all(v.bit_count()==4 for v in remaining)
assert sum(lo==0 for lo,hi in pairs)==1
D=defaultdict(list);indeg={f:0 for f in F};arrow_count=0
for hi in F:
 for i in range(15):
  if hi&(1<<i):
   lo=hi^(1<<i);assert lo in F
   u,v=((lo,hi) if (lo,hi) in pairs else (hi,lo))
   D[u].append(v);indeg[v]+=1;arrow_count+=1
q=deque(v for v in F if indeg[v]==0);ct=0
while q:
 u=q.popleft();ct+=1
 for v in D[u]:
  indeg[v]-=1
  if indeg[v]==0:q.append(v)
assert ct==len(F)
print('ALL_MORSE_ARROWS_ACYCLIC',len(F),arrow_count,len(pairs),'CRITICAL_3CELLS',len(remaining))

def sign(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def cyc(p):
 seen=set();out=[]
 for v in range(len(p)):
  if v in seen:continue
  j=v;k=0
  while j not in seen:
   seen.add(j);k+=1;j=p[j]
  out.append(k)
 return tuple(sorted(out,reverse=True))

def gverts(p):return tuple(LABELS.index(tuple(sorted((p[a],p[b])))) for a,b in LABELS)

def redtrace(g):
 out=-1
 for f in F:
  if not f:continue
  old=[j for j in range(15) if f>>j&1];new=[g[j] for j in old]
  if set(old)==set(new):out+=(-1)**(len(old)-1)*sign(new)
 return out
chars=defaultdict(set);counts=Counter()
for p in permutations(range(6)):
 c=cyc(p);counts[c]+=1;g=gverts(p)
 assert {sum(1<<g[i] for i in range(15) if nb>>i&1) for nb in N} == set(N)
 chars[c].add(redtrace(g))
assert len(chars)==11 and all(len(vals)==1 for vals in chars.values())
print('S6_CLASS_TRACES')
for c in sorted(chars):print(c,counts[c],next(iter(chars[c])))
# Murnaghan--Nakayama character recursion, independently of the face traces.
from functools import lru_cache

def partitions(n, ceiling=None):
    if n==0:
        yield ()
        return
    for a in range(min(ceiling or n,n),0,-1):
        for rest in partitions(n-a,a):
            yield (a,)+rest

def cells(shape):
    return {(i,j) for i,a in enumerate(shape) for j in range(a)}

@lru_cache(None)
def specht_character(shape,cycle_shape):
    if not cycle_shape:
        return int(not shape)
    k=cycle_shape[0]; old=cells(shape); value=0
    for shorter in partitions(sum(shape)-k):
        if any(i>=len(shape) or a>shape[i] for i,a in enumerate(shorter)):
            continue
        skew=old-cells(shorter)
        if len(skew)!=k:
            continue
        if any((i+1,j) in skew and (i,j+1) in skew and (i+1,j+1) in skew for i,j in skew):
            continue
        connected={next(iter(skew))};stack=list(connected)
        while stack:
            i,j=stack.pop()
            for nxt in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if nxt in skew and nxt not in connected:
                    connected.add(nxt);stack.append(nxt)
        if len(connected)!=k:
            continue
        height=len({i for i,j in skew})
        value+=(-1)**(height-1)*specht_character(shorter,cycle_shape[1:])
    return value
expected_mult={(6,):0,(5,1):0,(4,2):1,(4,1,1):0,(3,3):1,
    (3,2,1):2,(3,1,1,1):1,(2,2,2):2,(2,2,1,1):1,
    (2,1,1,1,1):3,(1,1,1,1,1,1):1}
assert sum(specht_character(sh,(1,)*6)*mul for sh,mul in expected_mult.items())==91
for sh,multiplicity in expected_mult.items():
    numerator=sum(counts[ct]*(-next(iter(vals)))*specht_character(sh,ct)
        for ct,vals in chars.items())
    assert numerator==720*multiplicity,(sh,numerator)
print('S6_IRREDUCIBLE_DECOMPOSITION_VERIFIED',expected_mult)
print('FULL_S6_NEIGHBORHOOD_CHARACTER_VERIFIED')
