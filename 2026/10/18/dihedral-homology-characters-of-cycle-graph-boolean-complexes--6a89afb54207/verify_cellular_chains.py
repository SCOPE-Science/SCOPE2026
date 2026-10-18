"""Exact cellular chains for boolean complexes of small cycles; independent of orbit-count formula."""
import itertools
from sympy import SparseMatrix,Matrix

def cells(n):
 by=[]
 for k in range(1,n+1):
  d={}
  for sub in itertools.combinations(range(n),k):
   S=set(sub)
   ed=[i for i in range(n) if i in S and (i+1)%n in S]
   for choices in itertools.product((0,1),repeat=len(ed)):
    if k==n and (all(c==0 for c in choices) or all(c==1 for c in choices)):
     continue
    arcs=tuple(sorted((i,(i+1)%n) if ch==0 else ((i+1)%n,i) for i,ch in zip(ed,choices)))
    d[(sub,arcs)]=len(d)
  by.append(d)
 return by

def boundary(n,top,bottom):
 Z={}
 for (sub,arcs),j in top.items():
  for h,v in enumerate(sub):
   t=tuple(x for x in sub if x!=v)
   arcs2=tuple(x for x in arcs if v not in x)
   i=bottom[(t,arcs2)]
   Z[(i,j)]=(-1)**h
 return SparseMatrix(len(bottom),len(top),Z)

def group_action(n,top,fun):
 Z={}
 for (sub,arcs),j in top.items():
  t=tuple(sorted(fun(i) for i in sub))
  ordered=[fun(i) for i in sub];parity=(-1)**sum(ordered[a]>ordered[b] for a in range(len(sub)) for b in range(a+1,len(sub)))
  arcs2=tuple(sorted((fun(a),fun(b)) for a,b in arcs))
  i=top[(t,arcs2)]
  Z[(i,j)]=parity
 return SparseMatrix(len(top),len(top),Z)

def char_restrict(T,B):
 K=Matrix.hstack(*B.nullspace())
 idx=[]
 M=B.nullspace()
 # Solve a linearly independent square coordinate restriction of the kernel basis.
 # rref of K.T finds columns that give pivot coordinates.
 _,pivot=K.T.rref(); piv=list(pivot)
 assert len(piv)==K.cols
 Q=K.extract(piv,list(range(K.cols)))
 Qinv=Q.inv()
 W=Qinv*(T*K).extract(piv,list(range(K.cols)))
 assert K*W==T*K
 return int(W.trace()), K.cols

for n in range(3,7):
 levels=cells(n)
 boundary_matrices=[]
 for j in range(1,len(levels)):
  B=boundary(n,levels[j],levels[j-1]); boundary_matrices.append(B)
  if j>1:assert boundary_matrices[j-2]*B==SparseMatrix(boundary_matrices[j-2].rows,B.cols,{})
 ranks=[int(B.rank()) for B in boundary_matrices]
 dim=[len(D) for D in levels]
 betti=[dim[0]-1-ranks[0]]+[dim[k]-ranks[k-1]-(ranks[k] if k<len(ranks) else 0) for k in range(1,n)]
 # The degree-zero formula above includes rank boundary C0 -> reduced C_{-1}; for connected n>2, beta0=0.
 print('n',n,'cells',dim,'boundary_ranks',ranks,'reduced_homology',betti)
 B=boundary_matrices[-1]
 for j in list(range(n))+[-i for i in range(1,n+1)]:
  fun=(lambda i,j=j:(i+j)%n) if j>=0 else (lambda i,j=j:(-j-i)%n)
  T=group_action(n,levels[-1],fun)
  c,rank=char_restrict(T,B)
  print(' ',('rot' if j>=0 else 'ref'),abs(j),c,end=';')
 print()
print('PASS direct exact chain matrices')
