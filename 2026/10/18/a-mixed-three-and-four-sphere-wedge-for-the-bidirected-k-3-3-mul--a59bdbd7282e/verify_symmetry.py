#!/usr/bin/env python3
"""Exact rational homology character of the bidirected K3,3 multipath complex."""
import itertools,collections
import sympy as sp
import verify_bidirected_k33 as v
faces=sorted(x for x in range(1,1<<18) if v.good(x))
bydim={k:sorted(x for x in faces if x.bit_count()-1==k) for k in range(5)}
idx3={x:i for i,x in enumerate(bydim[3])}
B=sp.MutableSparseMatrix(len(bydim[3]),len(bydim[4]),{})
for j,s in enumerate(bydim[4]):
 for t,c in v.incidence(s):B[idx3[t],j]=c
rref,pivots=B.rref(); assert len(pivots)==60
print('signed_degree_four_boundary_rank=',len(pivots))
free=[j for j in range(B.cols) if j not in pivots]
cycles=[]
for j in free:
 a={j:sp.Integer(1)}
 for r,p in enumerate(pivots):
  c=-rref[r,j]
  if c:a[p]=c
 cycles.append(a)
assert all((B*sp.Matrix([z.get(i,0) for i in range(72)])).is_zero_matrix for z in cycles)
assert len(free)==12 and max(abs(c) for x in cycles for c in x.values())==1
print('kernel_free_columns=',free,'kernel_rank=',len(cycles))

def signed_action(p,s):
 dest=[]
 for i,(u,w) in enumerate(v.ARCS):
  if s>>i&1:dest.append(v.ARCS.index((p[u],p[w])))
 inversions=sum(dest[i]>dest[j] for i in range(len(dest)) for j in range(i+1,len(dest)))
 return sum(1<<x for x in dest),(-1 if inversions%2 else 1)

def chain_trace(p,k):
 return sum(sign for s in bydim[k] for t,sign in [signed_action(p,s)] if t==s)

def top_trace(p):
 tr=0
 for j,z in enumerate(cycles):
  f=bydim[4][free[j]]
  # coefficient of free position j in action of cycle_j
  for i,c in z.items():
   t,sign=signed_action(p,bydim[4][i])
   if t==f:tr+=c*sign
 return tr
perms=list(itertools.permutations(range(3)))
G=[]
for a,b in itertools.product(perms,repeat=2):
 G.append(tuple(a)+tuple(3+x for x in b))
 G.append(tuple(3+x for x in a)+tuple(b))
assert len(set(G))==72
character=[]
for p in G:
 traces=[chain_trace(p,k) for k in range(5)]
 L=sum((-1)**k*t for k,t in enumerate(traces))
 t4=top_trace(p)
 t3=1+t4-L
 character.append((p,tuple(traces),int(t3),int(t4)))
from collections import Counter
print('character_trace_multisets_H3=',sorted(Counter(x[2] for x in character).items()),'H4=',sorted(Counter(x[3] for x in character).items()))
print('trivial-invariant dimension H3',sum(x[2] for x in character)//72,'H4',sum(x[3] for x in character)//72)

# classify cycle shapes for both partitions; choose sorted conjugacy

def ctype(p):
 seen=set();lens=[]
 for i in range(3):
  if i not in seen:
   j=i;k=0
   while j not in seen:seen.add(j);j=p[j];k+=1
   lens.append(k)
 return ''.join(map(str,sorted(lens,reverse=True)))
classes=collections.defaultdict(list)
for p,tr,tt3,tt4 in character:
 if all(p[i]<3 for i in range(3)):
  c=tuple(sorted((ctype(p[:3]),ctype(tuple(p[i]-3 for i in range(3,6))))))
 else:
  # swap type based on product on first part
  perm=tuple(p[p[i]] for i in range(3))
  c=('swap',ctype(perm))
 classes[c].append((tt3,tt4))
expected={
 ("111","111"):(1,19,12),
 ("111","21"):(6,1,0),
 ("111","3"):(4,1,0),
 ("21","21"):(9,3,0),
 ("21","3"):(12,1,0),
 ("3","3"):(4,1,6),
 ("swap","111"):(6,-1,-2),
 ("swap","21"):(18,1,0),
 ("swap","3"):(12,-1,-2),
}
assert len(classes)==9
for c,vals in sorted(classes.items(),key=str):
 size,t3,t4=expected[c]
 assert len(vals)==size and set(vals)=={(t3,t4)},(c,vals)
 print('class=',c,'size=',size,'trace_H3=',t3,'trace_H4=',t4)
assert sum(x[2] for x in character)==72 and sum(x[3] for x in character)==0
print('group_order=',len(G),'conjugacy_classes=',len(classes),'all_exact_checks=passed')
