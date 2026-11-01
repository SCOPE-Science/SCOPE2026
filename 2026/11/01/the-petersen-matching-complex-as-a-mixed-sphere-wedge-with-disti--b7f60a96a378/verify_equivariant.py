#!/usr/bin/env python3
"""Independent exact cellular computations for the matching complex of the Petersen graph."""
import itertools as it
from collections import Counter
import numpy as np
from sympy import Matrix
P=101
N=5
V=list(it.combinations(range(5),2)); graph_edges=[(i,j) for i,j in it.combinations(range(10),2) if set(V[i]).isdisjoint(V[j])]
edge_lookup={e:i for i,e in enumerate(graph_edges)}
faces={k: [t for t in it.combinations(range(15),k) if len({z for i in t for z in graph_edges[i]})==2*k] for k in range(1,6)}
idx={k:{f:i for i,f in enumerate(faces[k])} for k in faces}
matrices={}
for k in range(2,6):
 D=np.zeros((len(faces[k-1]),len(faces[k])),dtype=np.int64)
 for j,f in enumerate(faces[k]):
  for i in range(k):D[idx[k-1][f[:i]+f[i+1:]],j]=(-1)**i
 matrices[k]=D
assert all(not np.any(matrices[k-1]@matrices[k]) for k in range(3,6))
print('counts', [len(faces[k]) for k in range(1,6)],flush=True)
print('rational_ranks', {k: Matrix(matrices[k].tolist()).rank() for k in range(2,6)},flush=True)

def pivots(A,p=P):
 B=(A.copy()%p).astype(np.int64); n,m=B.shape; r=0; cols=[]
 for j in range(m):
  nz=np.where(B[r:,j]%p!=0)[0]
  if len(nz)==0:continue
  i=r+int(nz[0]);B[[r,i]]=B[[i,r]];B[r]=(B[r]*pow(int(B[r,j]),-1,p))%p
  for ii in range(r+1,n):
   if B[ii,j]: B[ii]=(B[ii]-int(B[ii,j])*B[r])%p
  cols.append(j);r+=1
  if r==n:break
 return cols

def inv_mod(M,p=P):
 n=len(M);A=np.hstack([M.copy()%p,np.eye(n,dtype=np.int64)])
 for i in range(n):
  nz=np.where(A[i:,i]%p!=0)[0]
  assert len(nz)>0
  j=i+int(nz[0]); A[[i,j]]=A[[j,i]]
  A[i]=(A[i]*pow(int(A[i,i]),-1,p))%p
  for j in range(n):
   if j!=i and A[j,i]:A[j]=(A[j]-int(A[j,i])*A[i])%p
 return A[:,n:]%p

basis={}
for k,D in matrices.items():
 pcs=pivots(D)
 assert len(pcs)==[0,0,14,61,79,6][k]
 A=D[:,pcs]
 prs=pivots(A.T)
 U=A[np.ix_(prs,range(len(pcs)))]%P
 Uinv=inv_mod(U)
 basis[k]=(pcs,prs,Uinv)
 assert np.array_equal((U@Uinv)%P,np.eye(len(pcs),dtype=int)%P)

def vertex_map(perm):
 vid={v:i for i,v in enumerate(V)}
 return [vid[tuple(sorted((perm[a],perm[b])))] for a,b in V]

def edge_map(perm):
 v=vertex_map(perm)
 return [edge_lookup[tuple(sorted((v[a],v[b])))] for a,b in graph_edges]

def induced(k,edgemap):
 fs=faces[k];ind=idx[k]
 dest=[];sgn=[]
 for f in fs:
  x=[edgemap[i] for i in f]
  inv=sum(x[i]>x[j] for i in range(k) for j in range(i+1,k))
  sg=(-1)**inv
  dest.append(ind[tuple(sorted(x))]);sgn.append(sg)
 return np.array(dest),np.array(sgn)

def imtrace(k,edgemap):
 # Boundary image in chains of cardinality k-1, from cardinality k.
 D=matrices[k];pcs,prs,Uinv=basis[k]
 dst,sgn=induced(k-1,edgemap)
 inv_dst=np.empty_like(dst);inv_dst[dst]=np.arange(len(dst))
 # Ux has rows prs. transformed basis columns after chain permutation: at row r,
 # sign of source index whose destination is r times its original entry.
 sub=((D[np.ix_(inv_dst[prs],pcs)]*sgn[inv_dst[prs],None])%P)
 T=(Uinv@sub)%P
 return int(np.trace(T)%P)

def chtrace(k,edgemap):
 d,s=induced(k,edgemap)
 return int(sum(s[i] for i in range(len(d)) if d[i]==i))

def cyc_perm(parts):
 p=list(range(5)); start=0
 for s in parts:
  if s>1:
   for j in range(s):p[start+j]=start+(j+1)%s
  start+=s
 return tuple(p)

allchars={}
for part in [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,)]:
 e=edge_map(cyc_perm(part))
 t={k:chtrace(k,e) for k in range(1,6)}
 a={k:imtrace(k,e) for k in range(2,6)}
 def center(v): return v if v<=P//2 else v-P
 h2=center((t[3]-a[3]-a[4])%P)
 h3=center((t[4]-a[4]-a[5])%P)
 h1=center((t[2]-a[2]-a[3])%P)
 h0=center((t[1]-a[2])%P)
 allchars[part]=(h0,h1,h2,h3)
 print('part',part,'face_traces',t,'boundary_image_traces',a,'homology',(h0,h1,h2,h3),flush=True)

# Independent character table by permutations on standard Young tableaux via Murnaghan-Nakayama from symmetric function power sums.
# For 5D Specht modules distinguish S^(3,2) and its sign twist S^(2,2,1).
# character of S^(3,2) from action on 2-subsets minus permutation on points (the 2-subset module = 1 + standard + (3,2)).
for part in allchars:
 perm=cyc_perm(part)
 fix_vertices=sum(perm[i]==i for i in range(5))
 fix_pairs=sum({perm[a],perm[b]}=={a,b} for a,b in it.combinations(range(5),2))
 spec=fix_pairs-fix_vertices # perm on 2-subsets - perm on points -> (3,2)
 sign=(-1)**(5-len(part))
 print('Specht (3,2)',part,spec,'sign twist',sign*spec,flush=True)
for part, (h0, h1, h2, h3) in allchars.items():
    assert h0 == 1 and h1 == 0
    perm = cyc_perm(part)
    fixed_points = sum(perm[i] == i for i in range(5))
    fixed_pairs = sum({perm[a],perm[b]} == {a,b} for a,b in it.combinations(range(5),2))
    sign = (-1)**(5-len(part))
    assert h2 == sign * fixed_points
    assert h3 == fixed_pairs - fixed_points
print('H2=sign_tensor_permutation_on_five_points')
print('H3=Specht(3,2)')
print('VERIFY_EQUIVARIANT_OK')
