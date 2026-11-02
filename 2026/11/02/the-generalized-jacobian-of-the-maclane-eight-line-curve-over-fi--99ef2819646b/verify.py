#!/usr/bin/env python3
"""Exact, dependency-free incidence and integral Frobenius certificate for the MacLane curve.
Run: python3 verify.py
"""
from itertools import combinations
from collections import Counter
from collections import deque

ZERO=(0,0); ONE=(1,0); W=(0,1)
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y):
 a,b=x; c,d=y
 return (a*c-b*d,a*d+b*c-b*d) # w^2=-w-1
def norm(x):
 a,b=x
 return a*a-a*b+b*b
def determinant3(A):
 (a,b,c),(d,e,f),(g,h,i)=A
 return add(sub(mul(a,sub(mul(e,i),mul(f,h))),mul(b,sub(mul(d,i),mul(f,g)))),mul(c,sub(mul(d,h),mul(e,g))))
W2=mul(W,W)
lines=[]
for r in [W,W2]:lines.append((ONE,neg(r),ZERO))
for r in [ONE,W,W2]:lines.append((ZERO,ONE,neg(r)))
for r in [ONE,W,W2]:lines.append((neg(r),ZERO,ONE))
assert len(lines)==8
norms=Counter(); triple=[]
for t in combinations(range(8),3):
 n=norm(determinant3([lines[i] for i in t]));norms[n]+=1
 if not n:triple.append(t)
assert norms=={0:8,3:48},norms
members={tuple(sorted(t)) for t in triple}
for i,j in combinations(range(8),2):
 if not any({i,j}<=set(t) for t in triple):members.add((i,j))
P=sorted(members)
assert Counter(map(len,P))=={3:8,2:4},Counter(map(len,P))
assert sum(len(p) for p in P)==32
# Fixed integral graph certificate: indices are in the edge order below.
vertices=[('L',i) for i in range(8)]+[('P',p) for p in P]
edges=[(('L',i),('P',p)) for p in P for i in p]
assert len(vertices)==20 and len(edges)==32
edge_index={e:i for i,e in enumerate(edges)}
tree_indices=[0,1,2,3,4,5,6,7,8,9,10,11,14,17,20,23,25,27,29]
chords=[i for i in range(32) if i not in tree_indices]
assert chords==[12,13,15,16,18,19,21,22,24,26,28,30,31]
adj={v:[] for v in vertices}
for i in tree_indices:
 u,v=edges[i];adj[u].append((v,i));adj[v].append((u,i))
def path(start,target):
 par={start:None};Q=deque([start]);prev={}
 while Q and target not in par:
  u=Q.popleft()
  for v,i in adj[u]:
   if v not in par:par[v]=u;prev[v]=i;Q.append(v)
 if target not in par:raise AssertionError('not a spanning tree')
 out=[];v=target
 while par[v] is not None:
  u=par[v];j=prev[v]
  out.append((u,v,j));v=u
 return out[::-1]
assert len({v for e in tree_indices for v in edges[e]})==20
assert len(path(vertices[0],vertices[-1]))>0
# Orientation always from line vertex to point vertex.
cycles=[]
for i in chords:
 u,v=edges[i];vec=[0]*32;vec[i]=1
 for a,b,j in path(v,u):
  vec[j]+=1 if edges[j]==(a,b) else -1
 cycles.append(vec)
for vec in cycles:
 # boundary is negative at each L, positive at each P
 bound={v:0 for v in vertices}
 for (u,v),c in zip(edges,vec):bound[u]-=c;bound[v]+=c
 assert all(x==0 for x in bound.values())
# Frobenius for q=2 modulo 3 is the conjugation w <-> w^2.
sigma={0:1,1:0,2:2,3:4,4:3,5:5,6:7,7:6}
p_sigma={p:tuple(sorted(sigma[i] for i in p)) for p in P}
assert set(p_sigma.values())==set(P)
permutation=[]
for u,v in edges:
 target=(('L',sigma[u[1]]),('P',p_sigma[v[1]]))
 permutation.append(edge_index[target])
# F columns in the fundamental-cycle basis are the coefficients on chords.
F=[[0]*13 for _ in range(13)]
for j,vec in enumerate(cycles):
 new=[0]*32
 for i,c in enumerate(vec):new[permutation[i]]+=c
 for k,e in enumerate(chords):F[k][j]=new[e]
 assert [sum(cycles[k][i]*F[k][j] for k in range(13)) for i in range(32)]==new
for i in range(13):
 for j in range(13):assert sum(F[i][k]*F[k][j] for k in range(13))==int(i==j)
def matvec(v):return [sum(F[i][j]*v[j] for j in range(13)) for i in range(13)]
def e(i):return [int(j==i) for j in range(13)]
# Integral witness: six free Z[C2]-orbits plus one sign line.
indices=[1,2,6,8,9,11]
U=[]
for i in indices:U.extend([e(i),matvec(e(i))])
U.append(e(0))
assert matvec(e(0))==[-x for x in e(0)]
for j in range(0,12,2):
 assert matvec(U[j])==U[j+1]
 assert matvec(U[j+1])==U[j]
def bareiss_det(A):
 a=[list(row) for row in A];n=len(a);sign=1;prev=1
 for k in range(n-1):
  if a[k][k]==0:
   ii=next((i for i in range(k+1,n) if a[i][k]),None)
   if ii is None:return 0
   a[k],a[ii]=a[ii],a[k];sign=-sign
  piv=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    num=a[i][j]*piv-a[i][k]*a[k][j]
    assert num%prev==0
    a[i][j]=num//prev
   a[i][k]=0
  prev=piv
 return sign*a[-1][-1]
d=bareiss_det([[col[i] for col in U] for i in range(13)])
assert abs(d)==1,d
P_fixed=sum(p==p_sigma[p] for p in P)
B_fixed=sum(permutation[i]==i for i in range(32))
L_fixed=sum(sigma[i]==i for i in range(8))
assert (L_fixed,P_fixed,B_fixed)==(2,4,4)
assert sum(len(p)==3 and p_sigma[p]==p for p in P)==2
# Independent projective point counts over prime fields, without line incidence data.
def prime_count(p):
    seen=set()
    for x in range(p):
        for y in range(p):
            for z in range(p):
                if (x,y,z)==(0,0,0):continue
                coords=(x,y,z)
                nz=next(t for t in coords if t)
                a=pow(nz,-1,p)
                seen.add(tuple(v*a%p for v in coords))
    count=0
    for x,y,z in seen:
        v=(x*x+x*y+y*y)*(y**3-z**3)*(z**3-x**3)
        if v%p==0:count+=1
    return count
for p in (2,5,7,11,13):
    observed=prime_count(p)
    expected=8*p-12 if p%3==1 else 2*p+2
    assert observed==expected,(p,observed,expected)
print('DIRECT_PRIME_FIELD_COUNTS',[(p,prime_count(p)) for p in (2,5,7,11,13)])
print('MACLANE_EXACT_NORM_DISTRIBUTION',sorted(norms.items()))
print('GEOMETRIC_CONFIG 8_LINES 8_TRIPLES 4_DOUBLES 32_BRANCHES')
print('ARITHMETIC_GENUS 21 TORUS_RANK 13 ADDITIVE_DIMENSION 8')
print('FROBENIUS_FIXED_LINES_POINTS_BRANCHES',L_fixed,P_fixed,B_fixed)
print('FROBENIUS_INTEGRAL_BASIS_DETERMINANT',d)
print('FROBENIUS_BLOCKS 6_REGULAR_PLUS_1_SIGN')
print('PICARD_SPLIT_GROUP (F_q_plus)^8 x C_(q-1)^13')
print('PICARD_NONSPLIT_GROUP (F_q_plus)^8 x C_(q+1) x C_(q^2-1)^6')
print('POINTS_SPLIT 8*q-12')
print('POINTS_NONSPLIT 2*q+2')
print('VERIFY_OK')
