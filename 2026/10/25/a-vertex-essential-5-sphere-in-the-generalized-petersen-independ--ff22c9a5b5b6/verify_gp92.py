from itertools import product
from collections import Counter,deque
from functools import lru_cache
N=18;n=9
E=set()
for i in range(n):
 for a,b in ((i,(i+1)%n),(i,n+i),(n+i,n+(i+2)%n)):
  E.add(tuple(sorted((a,b))))
adj=[0]*N
for a,b in E:adj[a]|=1<<b;adj[b]|=1<<a
# enumerate all independent sets (including empty) in deterministic ascending mask order
S=[mask for mask in range(1<<N) if all(not(mask&(1<<i) and mask&adj[i]) for i in range(N))]
K=set(S)
assert len(S)==2461
orders={
 'all':(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17),
 'outer-delete':(17,13,4,3,6,10,11,8,9,16,14,15,1,5,2,0,12,7),
 'inner-delete':(6,14,15,16,9,8,2,17,11,12,5,0,10,1,3,13,4,7),
}

def check(order,removed=None):
 A=[mask for mask in S if removed is None or not(mask>>removed&1)]
 avail=set(A);pairs=[]
 for v in order:
  t=1<<v
  for m in A:
   if (m not in avail or m&t):continue
   if m|t in avail:
    avail.remove(m);avail.remove(m|t);pairs.append((m,m|t))
 mate={pair:1 for pair in pairs}
 assert all(a.bit_count()+1==b.bit_count() for a,b in pairs)
 if removed is None:assert len(avail)==1 and next(iter(avail)).bit_count()==6
 else:assert len(avail)==0
 # Hasse edge orientation: unmatched upwards? usual lower->higher for matched, higher->lower otherwise
 # Graph cycles check with Kahn
 ins={m:0 for m in A};out={m:[] for m in A}
 for b in A:
  v=b
  while v:
   bit=v&-v;v-=bit;a=b^bit
   if (a,b) in mate: u,w=a,b
   else:u,w=b,a
   out[u].append(w);ins[w]+=1
 q=deque(k for k,d in ins.items() if d==0);ordercnt=0
 while q:
  v=q.popleft();ordercnt+=1
  for w in out[v]:
   ins[w]-=1
   if ins[w]==0:q.append(w)
 assert ordercnt==len(A),(removed,ordercnt,len(A))
 assert any(a==0 for a,b in pairs)
 print('verified',removed,len(A),len(pairs),len(avail),len(A)-2*len(pairs),len(out),'acyclic DAG yes')
 return pairs,avail
for kind,removed in [('all',None),('outer-delete',0),('inner-delete',9)]:check(orders[kind],removed)
# canonical dihedral automorphisms rotate indices preserving outer or inner
for r in range(9):
 for s in (1,-1):
  p=list(range(N))
  for i in range(9):p[i]=(s*i+r)%9;p[9+i]=9+(s*i+r)%9
  assert {tuple(sorted((p[a],p[b]))) for a,b in E}==E
print('rotations/reflections',18)
# face vectors and betti from Euler and Morse, order sizes
print('face-vector',tuple(sum(m.bit_count()==j for m in S) for j in range(1,9)))
print('order ALL',orders['all'])
print('order outer-deletion',orders['outer-delete'])
print('order inner-deletion',orders['inner-delete'])
def action_trace(r,s):
 p=[0]*N
 for i in range(9):p[i]=(s*i+r)%9;p[i+9]=9+(s*i+r)%9
 trace={-1:1}
 for k in range(7):trace[k]=0
 for f in S:
  verts=[i for i in range(N) if f>>i&1]
  if not verts:continue
  perm=[p[i] for i in verts]
  if sorted(perm)!=verts:continue
  sign=(-1)**sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))
  trace[len(verts)-1]+=sign
 return sum((1 if j%2==0 else -1)*v for j,v in trace.items()),trace
for r,s in [(1,1),(0,-1),(0,1)]:
 L,t=action_trace(r,s)
 print('character',r,s,'reduced Lefschetz',L,'H5-action',-L,'chain traces',t)

for r in range(9):
 for s in (1,-1):
  L,_=action_trace(r,s)
  assert L==-s,(r,s,L)
print("ALL_DIHEDRAL_CHARACTER_CHECKS",18)
def explicit_collapse(removed,match_pairs):
 surviving={m for m in S if m!=0 and not(m>>removed&1)}
 pairdict={a:b for a,b in match_pairs if a!=0}
 assert len(pairdict)==len(match_pairs)-1
 # all matched nonempty except the vertex paired with empty
 single_vert=next(b for a,b in match_pairs if a==0)
 for a,b in match_pairs:
  if a==0:continue
  assert a in surviving and b in surviving
 count=0
 while pairdict:
  usable=[]
  for a,b in pairdict.items():
   if sum(((a|(1<<v)) in surviving) for v in range(N) if not(a>>v&1))==1:
    usable.append((a,b))
  if not usable:
   print('blocked',removed,len(pairdict));break
  a,b=min(usable)
  assert a in surviving and b in surviving
  surviving.remove(a);surviving.remove(b);pairdict.pop(a);count+=1
 assert surviving=={single_vert}, (removed,sorted(surviving))
 print('ACTUAL_ELEMENTARY_COLLAPSES',removed,count,'remaining_vertex',single_vert.bit_length()-1)
for name,removed in [('outer-delete',0),('inner-delete',9)]:
 pair,_=check(orders[name],removed)
 explicit_collapse(removed,pair)
