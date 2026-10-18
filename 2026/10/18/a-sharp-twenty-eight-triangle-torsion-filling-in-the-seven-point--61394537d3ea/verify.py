#!/usr/bin/env python3
"""Exact finite verification of a sharp 3-torsion filling in M_7.

Run: python3 verify.py
Only Python standard-library modules are used.
"""
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'certificates/m7_filling.json').read_text(encoding='utf-8'))
V=list(combinations(range(7),2));vi={e:i for i,e in enumerate(V)}
E=[e for e in combinations(range(len(V)),2) if set(V[e[0]]).isdisjoint(V[e[1]])]
ei={e:i for i,e in enumerate(E)}
T=[t for t in combinations(range(len(V)),3) if len(set().union(*(set(V[i]) for i in t)))==6]
assert (len(V),len(E),len(T))==(21,105,105)
# Sparse signed boundary columns; oriented simplices are increasing vertex tuples.
columns=[]
for t in T:
 columns.append({ei[(t[1],t[2])]:1, ei[(t[0],t[2])]:-1, ei[(t[0],t[1])]:1})
z=[0]*len(E)
a,b,c,d=(vi[e] for e in [(0,1),(0,2),(3,4),(3,5)])
for u,v,sgn in [(a,c,1),(a,d,-1),(b,c,-1),(b,d,1)]:
 assert u!=v
 z[ei[tuple(sorted((u,v)))]]+=sgn*(1 if u<v else -1)
assert sum(abs(w) for w in z)==4
# Check that z is a cycle, using the first simplicial boundary.
vertex_boundary=[0]*len(V)
for (u,v),k in zip(E,z):
 vertex_boundary[u]-=k; vertex_boundary[v]+=k
assert not any(vertex_boundary)
x=D['primal_coefficients']; y=D['dual_thirds']
assert len(x)==len(T) and len(y)==len(E)
assert all(isinstance(w,int) and not isinstance(w,bool) for w in x+y)
primal=[0]*len(E)
for j,w in enumerate(x):
 for i,s in columns[j].items():primal[i]+=s*w
assert primal==[3*t for t in z]
assert sum(abs(w) for w in x)==28
# The rational cochain y/3 has infinity coboundary norm <= 1.
# Pairing 3z with y/3 is 28, proving the lower bound for ALL
# integral or real 2-chains with boundary 3z by l1/l-infinity duality.
assert max(abs(sum(y[i]*sgn for i,sgn in col.items())) for col in columns)<=3
assert sum(3*z[i]*y[i] for i in range(len(E)))==84
# For the mod-three obstruction, produce a full column echelon basis.
piv={}
for col in columns:
 w={i:val%3 for i,val in col.items() if val%3}
 while w:
  p=min(w)
  if p not in piv:
   inv=pow(w[p],-1,3)
   piv[p]={i:(val*inv)%3 for i,val in w.items() if val%3}
   break
  k=w[p]
  for i,val in piv[p].items():
   tmp=(w.get(i,0)-k*val)%3
   if tmp:w[i]=tmp
   else:w.pop(i,None)
assert len(piv)==84
r={i:t%3 for i,t in enumerate(z) if t%3}
while r and min(r) in piv:
 p=min(r);k=r[p]
 for i,val in piv[p].items():
  tmp=(r.get(i,0)-k*val)%3
  if tmp:r[i]=tmp
  else:r.pop(i,None)
assert r,'The canonical 4-cycle is not a boundary modulo three.'
# Every 4-cycle is an unoriented graph cycle on M7's 1-skeleton.
adj=[set() for _ in V]
for u,v in E:adj[u].add(v);adj[v].add(u)
cycles=set()
for u in range(len(V)):
 for v in adj[u]:
  for w in adj[v]-{u}:
   for t in adj[w]&adj[u]:
    if len({u,v,w,t})!=4:continue
    q=(u,v,w,t)
    cycles.add(min(tuple(h[i:]+h[:i]) for h in (q,tuple(reversed(q))) for i in range(4)))
assert len(cycles)==945
classes={6:0,7:0}
for cycle in cycles:
 m=len(set().union(*(set(V[v]) for v in cycle)))
 assert m in classes
 classes[m]+=1
 # The chord is either opposite pair of cycle vertices: present
 # exactly in the 7-label class. All 7-label cycles bound two faces.
 has_chord=any(tuple(sorted((cycle[i],cycle[i+2]))) in ei for i in (0,1))
 assert has_chord==(m==7)
assert classes=={6:630,7:315}
# Formula for the S7 orbit of six-label chordless 4-cycles:
# unused label x; partition other six into unordered triples A,B;
# choose one center in each block -> 7*10*3*3=630.
assert 7*(20//2)*3*3==classes[6]
print('VERIFY_OK 945_FOUR_CYCLES 630_TORSION_GENERATORS 315_BOUNDARIES SHARP_FILLING_28')
