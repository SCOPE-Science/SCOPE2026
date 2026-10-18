"""Exact free-face checks for graph-Morse bipartite patch collapses.

Requires verify_faces.py alongside this file and Python standard library.
The theoretical proof gives the finite-independent collapse schedule.
"""
from collections import Counter
from verify_faces import all_faces, proposed_generators
from itertools import combinations

def nonempty_subsets(seq, min_size=1):
 seq=sorted(seq)
 for t in range(len(seq),min_size-1,-1):
  for sub in combinations(seq,t): yield frozenset(sub)

def sim_collapse(sizes):
 labels=[i for i,n in enumerate(sizes) for _ in range(n)]
 group={i:[a for a,p in enumerate(labels) if p==i] for i in range(len(sizes))}
 faces=all_faces(proposed_generators(labels)) - {frozenset()}
 before=len(faces);num=0
 def remove(lo,hi):
  nonlocal num
  assert lo in faces and hi in faces, (sizes,'absent',lo,hi)
  assert len(hi)==len(lo)+1
  cofaces=[f for f in faces if f>lo]
  assert cofaces==[hi], (sizes,'not free',lo,hi,cofaces)
  faces.remove(lo);faces.remove(hi);num+=1
 def flap(tip,base,chosen):
  for subset in nonempty_subsets(set(base)-{chosen}):
   lo=subset|{tip}
   remove(lo,lo|{chosen})
 def base_collapse(base,root):
  for subset in nonempty_subsets(set(base)-{root},2):
   remove(subset,subset|{root})
 for i,j in combinations(group,2):
  A,B=group[i],group[j]
  if len(A)>=2 and len(B)>=2:
   for b in B:
    X={(a,b) for a in A}
    for a in A:
     tip=(b,a); x=(a,b); other=sorted(X-{x}); flap(tip,X-{x},other[0])
    base_collapse(X,sorted(X)[0])
   for a in A:
    Y={(b,a) for b in B}
    for b in B:
     tip=(a,b); y=(b,a); other=sorted(Y-{y}); flap(tip,Y-{y},other[0])
    base_collapse(Y,sorted(Y)[0])
  elif len(A)==1 and len(B)==1:
   pass
  else:
   # directly single contractible patch: when |A|=1, choose V_a; otherwise choose U_b
   if len(A)==1:
    a=A[0]; base={(b,a) for b in B}
    for b in B:
     y=(b,a); tip=(a,b); other=sorted(base-{y}); flap(tip,base-{y},other[0])
   else:
    b=B[0]; base={(a,b) for a in A}
    for a in A:
     x=(a,b); tip=(b,a); other=sorted(base-{x}); flap(tip,base-{x},other[0])
   base_collapse(base,sorted(base)[0])
   # entire component is now a tree; contract it by leaf removal (preserving one vertex)
   while True:
    vs={next(iter(f)) for f in faces if len(f)==1 and all((z[0] in A and z[1] in B) or (z[0] in B and z[1] in A) for z in f)}
    edges=[f for f in faces if len(f)==2 and all((z[0] in A and z[1] in B) or (z[0] in B and z[1] in A) for z in f)]
    deg=Counter(v for e in edges for v in e)
    leaf=next((v for v in sorted(vs) if deg[v]==1), None)
    if leaf is None: break
    edge=next(e for e in edges if leaf in e)
    remove(frozenset((leaf,)), edge)
 assert all(len(f)<=2 for f in faces)
 print(sizes,'before',before,'pairs',num,'final V/E',sum(len(f)==1 for f in faces),sum(len(f)==2 for f in faces),'Euler',sum(len(f)==1 for f in faces)-sum(len(f)==2 for f in faces))
 return num,faces
if __name__ == "__main__":
 for c in ((2,2,2),(1,2,2),(1,1,2),(1,1,1,1),(2,3,2),(2,2,1,1),(3,3),(1,4),(2,3),(1,1)):
  sim_collapse(c)
 print("ALL COMPLETE: every removal was a certified free-face elementary collapse.")
