# Independent enumeration/rank/alternating-Lefschetz verifier for the bidirected 3-rung ladder.
from collections import defaultdict
A=[(0,1),(1,2),(3,4),(4,5),(0,3),(1,4),(2,5)];A+= [(y,x) for x,y in A]

def admissible(indices):
 inn=set();out=set();arcs=[]
 for i in indices:
  u,v=A[i]
  if u in out or v in inn:return False
  out.add(u);inn.add(v);arcs.append((u,v))
 nxt=dict(arcs)
 for x in range(6):
  z=x;S=set()
  while z in nxt:
   if z in S:return False
   S.add(z);z=nxt[z]
 return True

F=defaultdict(list)
for mask in range(1,1<<14):
 sub=[i for i in range(14) if mask>>i&1]
 if admissible(sub):F[len(sub)-1].append(mask)

ranks={}
for k in range(1,5):
 lower={m:i for i,m in enumerate(F[k-1])};basis={}
 for m in F[k]:
  b=0
  for i in range(14):
   if m>>i&1:b^=1<<lower[m^(1<<i)]
  while b:
   top=b.bit_length()-1
   if top in basis:b^=basis[top]
   else:basis[top]=b;break
 ranks[k]=len(basis)
print('f-vector',[len(F[k]) for k in range(5)])
print('mod2_boundary_ranks',[ranks[k] for k in range(1,5)])
print('reduced_mod2_betti',[len(F[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in range(1,5)])

index={x:i for i,x in enumerate(A)}
perms={'identity':[0,1,2,3,4,5], 'row_swap':[3,4,5,0,1,2], 'column_reversal':[2,1,0,5,4,3], 'half_turn':[5,4,3,2,1,0]}
for name,p in perms.items():
 total=-1
 for k in range(5):
  trace=0
  for mask in F[k]:
   perm=[index[(p[A[j][0]],p[A[j][1]])] for j in range(14) if mask>>j&1]
   if sum(1<<j for j in perm)!=mask:continue
   inv=sum(a>b for i,a in enumerate(perm) for b in perm[i+1:])
   trace+=-1 if inv%2 else 1
  total+=(-1)**k*trace
 print('reduced_lefschetz',name,total)
