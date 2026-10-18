#!/usr/bin/env python3
"""Exact integral cellular and cycle-lattice verification for K_(3,3,3).
Run: python verify_k333.py (from a directory containing basis_indices.json).
Requires sympy==1.14.0; uses no network access or external mathematical data.
"""
from collections import defaultdict
from itertools import combinations, permutations
import json
from pathlib import Path
from sympy import Matrix, ZZ, zeros
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

V=tuple(range(9))
parts=(V[0:3],V[3:6],V[6:9])
group={v:k for k,P in enumerate(parts) for v in P}
E=tuple((a,b) for a,b in combinations(V,2) if group[a]!=group[b])
Eset=set(E)
C0=tuple(combinations(V,2))
C1=tuple((e,v) for e in E for v in V if v not in e)
C2=tuple((e,f) for e,f in combinations(E,2) if len(set(e+f))==4)
idx1={c:i for i,c in enumerate(C1)}
idx2={c:i for i,c in enumerate(C2)}
assert (len(E),len(C0),len(C1),len(C2))==(27,36,189,216)

# Boundary conventions: edge (a,b), a<b, oriented a->b;
# 1-cell (edge,vertex) follows the edge; 2-cell (e,f),e<f,
# oriented in product order e x f.
D2cols=[]
for e,f in C2:
 a,b=e;c,d=f
 D2cols.append({idx1[(e,c)]:1,idx1[(e,d)]:-1,
                idx1[(f,a)]:-1,idx1[(f,b)]:1})
# Chain condition ∂1 ∂2 = 0 checked without any homology package.
def bdry1(row):
 e,v=C1[row];a,b=e
 return {tuple(sorted((b,v))):1,tuple(sorted((a,v))):-1}
for col in D2cols:
 acc=defaultdict(int)
 for row,x in col.items():
  for vertex_pair,v in bdry1(row).items():acc[vertex_pair]+=x*v
 assert all(x==0 for x in acc.values())

def rank_mod(cols,p):
 basis={}
 for col in cols:
  a={i:int(v)%p for i,v in col.items() if int(v)%p}
  while a:
   i=min(a);c=a[i]
   if i not in basis:
    ci=pow(c,-1,p)
    basis[i]={r:v*ci%p for r,v in a.items()}
    break
   for r,v in basis[i].items():
    w=(a.get(r,0)-c*v)%p
    if w:a[r]=w
    else:a.pop(r,None)
 return len(basis)
assert rank_mod(D2cols,3)==135

# Exhaustive simple undirected graph cycles: smallest vertex first,
# second vertex smaller than last (one orientation per unoriented cycle).
cycles=[]
for n in range(3,10):
 for vertices in combinations(V,n):
  start,*others=vertices
  for order in permutations(others):
   c=(start,)+order
   if c[1]>c[-1]:continue
   if all(tuple(sorted((c[i],c[(i+1)%n]))) in Eset for i in range(n)):
    cycles.append(c)
cycles.sort()
assert len(cycles)==6705

def oriented_cycle(c):
 out=[]
 for i in range(len(c)):
  a,b=c[i],c[(i+1)%len(c)]
  out.append((tuple(sorted((a,b))),1 if a<b else -1))
 return out

T=defaultdict(list)
for i,a in enumerate(cycles):
 aset=set(a)
 for b in cycles[i+1:]:
  if aset.intersection(b):continue
  vals={}
  for e,sgne in oriented_cycle(a):
   for f,sgnf in oriented_cycle(b):
    face=tuple(sorted((e,f)))
    vals[idx2[face]]=sgne*sgnf*(1 if e<f else -1)
  # Check each fundamental torus is a signed 2-cycle.
  d=defaultdict(int)
  for face,x in vals.items():
   for row,v in D2cols[face].items():d[row]+=x*v
  assert all(x==0 for x in d.values())
  T[tuple(sorted((len(a),len(b))))].append(vals)
expected={(3,3):(108,81,1,()),(3,4):(405,81,2,(2,)),
          (3,5):(648,81,1,()),(3,6):(432,81,4,(4,)),
          (4,4):(243,60,None,None),(4,5):(324,81,2,(2,))}
assert set(T)==set(expected)
assert sum(map(len,T.values()))==2160

# Explicit certificate consists of indices into lexicographic lists above.
cert=json.loads((Path(__file__).resolve().parent/'basis_indices.json').read_text())
cols=cert['triangle_pair_column_indices_zero_based']
rows=cert['two_edge_cell_row_indices_zero_based']
assert len(cols)==len(rows)==81
assert len(set(cols))==len(set(rows))==81
assert all(0<=c<108 for c in cols) and all(0<=r<216 for r in rows)
A=Matrix(216,81,lambda i,j:T[(3,3)][cols[j]].get(i,0))
P=A[rows,:]
assert P.det(method='domain-ge')==1
# The rank 81 unimodular 2-cycle minor forces all 81 columns to
# generate the complete integer kernel of ∂2:
# dim ker(∂2)_Q = 216-135 = 81, and projection to these 81 rows
# sends this kernel injectively to Z^81 while our selected cycles
# surject onto Z^81.
Pinv=P.inv()
assert all(v==int(v) for v in Pinv)

print('CELLULAR_COMPLEX 36 189 216 BOUNDARY_SQUARED_ZERO')
print('RANK_D2_MOD_3 135 EXACT_RANK_D2 135')
print('SIMPLE_CYCLES',len(cycles),'DISJOINT_CYCLE_PAIR_TORI',sum(map(len,T.values())))
print('TRIANGLE_TRIANGLE_UNIT_DETERMINANT 1 BASIS_SIZE 81')
print('H2_INTEGER_RANK_81_TRIANGLE_TRIANGLE_TORI_GENERATE_INTEGRALLY')
for typ in sorted(T):
 columns=T[typ]
 projected=Matrix(81,len(columns),lambda i,j:columns[j].get(rows[i],0))
 coords=Pinv*projected
 assert all(v==int(v) for v in coords)
 h=hermite_normal_form(coords)
 assert h.rows==81
 r=h.cols
 exp_count,exp_rank,exp_index,exp_snf=expected[typ]
 assert len(columns)==exp_count and r==exp_rank
 if r==81:
  index=abs(int(h.det(method='domain-ge')))
  snf=smith_normal_form(h,domain=ZZ)
  torsion=tuple(abs(int(snf[i,i])) for i in range(81) if abs(snf[i,i])!=1)
  assert index==exp_index and torsion==exp_snf
  print('TYPE',typ,'COUNT',len(columns),'RANK',r,'INDEX',index,'FINITE_QUOTIENT',torsion)
 else:
  snf=smith_normal_form(h,domain=ZZ)
  torsion=tuple(abs(int(snf[i,i])) for i in range(r) if abs(snf[i,i])!=1)
  assert typ==(4,4) and r==60 and torsion==()
  print('TYPE',typ,'COUNT',len(columns),'RANK',r,'FREE_QUOTIENT_RANK',81-r,'TORSION',torsion)
print('VERIFY_OK_K333_INTEGRAL_LENGTH_RESTRICTED_TORUS_LATTICES')
