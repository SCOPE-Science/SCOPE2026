#!/usr/bin/env python3
"""Exact reproducible Morse-chain computation for the snub cubical graph."""
from itertools import permutations, product
from collections import Counter, defaultdict, deque
from functools import lru_cache

# Arithmetic in Z[t]/(t^3-t^2-t-1): a+b*t+c*t^2.
ONE=(1,0,0); T=(0,1,0); RECIP=(-1,-1,1)
def minus(x,y): return tuple(a-b for a,b in zip(x,y))
def square(x):
 a,b,c=x
 return (a*a+2*b*c+c*c,
         2*a*b+2*b*c+2*c*c,
         b*b+2*a*c+2*b*c+2*c*c)
def dotnorm(x):
 out=(0,0,0)
 for z in x:
  w=square(z)
  out=tuple(a+b for a,b in zip(out,w))
 return out

def graph():
 base=(ONE,RECIP,T)
 verts=[]
 for p in permutations(range(3)):
  parity=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2
  for signs in product((-1,1),repeat=3):
   if sum(a==1 for a in signs)%2 != parity: continue
   verts.append(tuple(tuple(signs[i]*z for z in base[p[i]]) for i in range(3)))
 assert len(verts)==24 and len(set(verts))==24
 goal=(2,4,-2)
 edges=[(i,j) for i in range(24) for j in range(i+1,24)
        if dotnorm(tuple(minus(a,b) for a,b in zip(verts[i],verts[j])))==goal]
 assert len(edges)==60
 adj=[0]*24
 for i,j in edges: adj[i]|=1<<j;adj[j]|=1<<i
 assert all(a.bit_count()==5 for a in adj)
 # Exact distance equality is not a floating point comparison.
 return verts,edges,adj

def faces_of(adj):
 output=[]
 def rec(first,bits):
  if bits: output.append(bits)
  for j in range(first,len(adj)):
   if not bits & adj[j]:rec(j+1,bits|(1<<j))
 rec(0,0)
 assert len(output)==len(set(output))
 return output

def matching(faces):
 unmatched=set(faces)
 # Fixed full ordering, expressed independently of the graph vertex labelling.
 order=sorted(range(24),key=lambda v:(13*v+22)%24)
 pairs=[]
 for v in order:
  b=1<<v
  for f in sorted(unmatched):
   if f not in unmatched or f&b:continue
   g=f|b
   if g in unmatched:
    unmatched.remove(f);unmatched.remove(g);pairs.append((f,g))
 return order,pairs,unmatched

def faces_boundary(f):
 for i,v in enumerate(j for j in range(24) if f>>j &1):
  yield (f^(1<<v),(-1)**i)

def verify_acyclic(faces,pairs):
 lower={f:g for f,g in pairs}
 index={f:i for i,f in enumerate(faces)}
 indeg=[0]*len(faces); out=[[] for f in faces]
 count=0
 for f in faces:
  for s,_ in faces_boundary(f):
   if not s:continue
   a,b=(f,s) if lower.get(s)==f else (s,f)
   out[index[a]].append(index[b]);indeg[index[b]]+=1;count+=1
 queue=deque(i for i,d in enumerate(indeg) if d==0);visited=0
 while queue:
  i=queue.popleft();visited+=1
  for j in out[i]:
   indeg[j]-=1
   if indeg[j]==0:queue.append(j)
 assert visited==len(faces),(visited,len(faces))
 return count

def determinant(a):
 # Integer-preserving Bareiss elimination, including pivot row swaps.
 a=[list(map(int,row)) for row in a];n=len(a)
 assert all(len(row)==n for row in a)
 if n==0:return 1
 sign=1;prev=1
 for k in range(n-1):
  if a[k][k]==0:
   j=next((j for j in range(k+1,n) if a[j][k]),None)
   if j is None:return 0
   a[k],a[j]=a[j],a[k];sign=-sign
  piv=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    value=piv*a[i][j]-a[i][k]*a[k][j]
    assert value%prev==0
    a[i][j]=value//prev
  for i in range(k+1,n):a[i][k]=0
  prev=piv
 return sign*a[-1][-1]

def main():
 _,edges,adj=graph(); faces=faces_of(adj);F=set(faces)
 counts=Counter(f.bit_count()-1 for f in faces)
 assert counts=={0:24,1:216,2:912,3:1854,4:1680,5:564,6:48,7:3},counts
 order,pairs,crit=matching(faces)
 critical_counts=Counter(f.bit_count()-1 for f in crit)
 assert critical_counts=={0:1,3:9,4:35},critical_counts
 assert len(pairs)==2628
 inc=verify_acyclic(faces,pairs)
 assert inc==22728,inc
 lower=dict(pairs);upper={g for _,g in pairs}
 @lru_cache(None)
 def reduced(f):
  if f in crit:return {f:1}
  if f in upper:return {}
  g=lower[f]
  coefficient=next(c for s,c in faces_boundary(g) if s==f)
  tally=defaultdict(int)
  for s,c in faces_boundary(g):
   if s==f:continue
   for u,z in reduced(s).items():tally[u]-=coefficient*c*z
  return {u:z for u,z in tally.items() if z}
 c3=sorted(f for f in crit if f.bit_count()==4)
 c4=sorted(f for f in crit if f.bit_count()==5)
 D=[]
 for f in c4:
  row=defaultdict(int)
  for s,c in faces_boundary(f):
   for u,z in reduced(s).items():row[u]+=c*z
  D.append([row[u] for u in c3])
 matrix=[[D[j][i] for j in range(len(D))] for i in range(9)]
 indices=[7,19,20,26,28,1,18,29,10]
 minor=[[matrix[i][j] for j in indices] for i in range(9)]
 det=determinant(minor)
 assert det==-1,det
 print('exact_vertices=24 edges=60 nonempty_faces=5301')
 print('f_vector=',[counts[k] for k in range(8)])
 print('morse_pairs=2628 critical_cells=',dict(sorted(critical_counts.items())))
 print('directed_hasse_incidences=',inc,'acyclic=yes')
 print('signed_boundary_shape=9x35; unit_minor_columns=',indices,'determinant=',det)
 print('integral_homotopy=wedge_of_26_S4')

if __name__=='__main__':main()
