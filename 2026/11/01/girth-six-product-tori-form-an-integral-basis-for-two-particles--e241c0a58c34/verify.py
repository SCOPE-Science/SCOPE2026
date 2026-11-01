#!/usr/bin/env python3
"""Exact integral chain calculation for two points on the Moebius-Kantor graph.
Run with Python >=3.10 and sympy >=1.12. No external data files needed.
"""
from itertools import combinations
from collections import Counter
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

N=8
E=sorted({tuple(sorted((a,b))) for i in range(N)
          for a,b in ((i,(i+1)%N),(i,8+i),(8+i,8+(i+3)%N))})
assert len(E)==24
adj={i:sorted(v for e in E if i in e for v in e if v!=i) for i in range(16)}
C0=list(combinations(range(16),2))
C1=[(v,e) for v in range(16) for e in E if v not in e]
C2=[(e,f) for e,f in combinations(E,2) if set(e).isdisjoint(f)]
i0={c:i for i,c in enumerate(C0)}
i1={c:i for i,c in enumerate(C1)}
i2={c:i for i,c in enumerate(C2)}
assert (len(C0),len(C1),len(C2))==(120,336,228)

D1=[]
for v,(a,b) in C1:
 D1.append({i0[tuple(sorted((v,a)))]:-1,i0[tuple(sorted((v,b)))]:1})
D2=[]
for (a,b),(c,d) in C2:
 D2.append({i1[(b,(c,d))]:1,i1[(a,(c,d))]:-1,
            i1[(d,(a,b))]:-1,i1[(c,(a,b))]:1})
for col in D2:
 b={}
 for row,coeff in col.items():
  for v,z in D1[row].items():b[v]=b.get(v,0)+coeff*z
 assert all(z==0 for z in b.values())

def rank_mod(columns,p):
 pivot={};nr=0
 for c in columns:
  vec={i:(v%p) for i,v in c.items() if v%p}
  while vec:
   j=min(vec)
   if j not in pivot:
    v=pow(vec[j],-1,p)
    pivot[j]={i:(x*v)%p for i,x in vec.items()}
    nr+=1;break
   c0=vec[j]
   for i,x in pivot[j].items():
    nv=(vec.get(i,0)-c0*x)%p
    if nv:vec[i]=nv
    else:vec.pop(i,None)
 return nr

R1=rank_mod(D1,3)
R2=rank_mod(D2,3)
R2MOD2=rank_mod(D2,2)
assert (R1,R2,R2MOD2)==(119,208,207)

# Canonical simple 6-cycles: smallest vertex first and second vertex < last.
cycles=set()
CYCLE_LENGTH=6
def extend(path,start):
 if len(path)==CYCLE_LENGTH:
  if start in adj[path[-1]] and path[1]<path[-1]:
   cycles.add(tuple(path))
  return
 for y in adj[path[-1]]:
  if y>start and y not in path:extend(path+[y],start)
for k in (3,4,5,6):
 CYCLE_LENGTH=k
 cycles.clear()
 for i in range(16):extend([i],i)
 if k<6:assert not cycles
 else:cycles=sorted(cycles)

assert len(cycles)==24

def signed_cycle(c):
 out={}
 for u,v in zip(c,c[1:]+c[:1]):
  e=tuple(sorted((u,v)))
  out[e]=1 if (u,v)==e else -1
 return out

tori=[];pairs=[]
for a,b in combinations(range(len(cycles)),2):
 if not set(cycles[a]).isdisjoint(cycles[b]):continue
 v={}
 for e,ce in signed_cycle(cycles[a]).items():
  for f,cf in signed_cycle(cycles[b]).items():
   v[i2[tuple(sorted((e,f)))]]=ce*cf*(1 if e<f else -1)
 tori.append(v)
 pairs.append((a,b))
assert len(tori)==60
for z in tori:
 bd={}
 for c,coeff in z.items():
  for r,d in D2[c].items():bd[r]=bd.get(r,0)+coeff*d
 assert all(x==0 for x in bd.values())
assert rank_mod(tori,2)==20 and rank_mod(tori,3)==20

# A displayable, EXACT 20-by-20 unimodular minor of the 228-by-60
# matrix with the product-torus vectors as columns (0-based indices).
basis_torus_indices=[0,1,2,5,6,7,10,11,12,15,16,17,20,21,25,26,27,30,31,32]
minor_square_indices=[0,2,4,6,8,11,19,21,23,25,27,57,59,61,63,91,93,95,121,123]
A=Matrix([[tori[t][i] if i in tori[t] else 0 for t in basis_torus_indices]
          for i in minor_square_indices])
assert A.det()==-1

# Integral Smith calculation independently checks the torsion component.
B=Matrix.zeros(len(C1),len(C2))
for j,co in enumerate(D2):
 for i,x in co.items():B[i,j]=x
s=smith_normal_form(B,domain=ZZ)
nonzero=[abs(int(s[i,i])) for i in range(min(s.shape)) if s[i,i]]
assert len(nonzero)==208 and Counter(nonzero)==Counter({1:207,2:1})

print('VERTICES 16 EDGES 24; CELLS 120,336,228; EULER 12')
print('RANKS d1=119 d2_Q=208 d2_F2=207')
print('SIX_CYCLES 24; DISJOINT_HEXAGON_PAIRS 60')
print('GIRTH_SIX_TORI_RANK 20; BASIS_SIZE 20; MINOR_DET -1')
print('SMITH_d2 1^207,2^1; H1 Z^9 + Z/2; H2 Z^20')
print('BASIS_PAIR_INDICES', [pairs[i] for i in basis_torus_indices])
print('MINOR_SQUARE_INDICES',minor_square_indices)
print('VERIFY_OK')
