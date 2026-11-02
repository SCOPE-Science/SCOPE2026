from collections import Counter
import itertools, math
V=[v for v in itertools.product(range(3),repeat=3) if any(v)]
def norm(v):
 for t in v:
  if t:return tuple((x*pow(t,-1,3))%3 for x in v)
P=sorted(set(map(norm,V)))
L=[sum(1<<i for i,p in enumerate(P) if sum(x*y for x,y in zip(a,p))%3==0) for a in P]
assert len(P)==len(L)==13 and len(set(L))==13
ALL=(1<<13)-1
eligible=[0]*(1<<13)
for p in range(1<<13):
 for i,l in enumerate(L):
  if p&l==l:eligible[p]|=1<<i

def step(p,l):
 r=eligible[p]&~l; q=ALL^p
 for i,line in enumerate(L):
  if r>>i&1:q|=line
 return q,r
states=[(p,l) for p in range(1<<13) for l in range(1<<13) if l&~eligible[p]==0]
print('states',len(states))
seen=set();cycles=[]; bylen=Counter(); order=1; loc={}
for s in states:
 if s in seen:continue
 cyc=[]; q=s
 while q not in seen:
  seen.add(q);cyc.append(q);q=step(*q)
 assert q==s,(s,q)
 idx=len(cycles);cycles.append(cyc)
 for t in cyc:loc[t]=idx
 bylen[len(cyc)]+=1;order=math.lcm(order,len(cyc))
print('ncycles',len(cycles),'bylen',sorted(bylen.items()))
print('order',order,'max',max(bylen),'rad',sorted(set(x for x in bylen if x%2)))
print('fixed',bylen[1],'allcovered',sum(k*v for k,v in bylen.items()))
from collections import defaultdict
classes=defaultdict(list)
for cyc in cycles:classes[len(cyc)].append(min(cyc))
print('large',sorted(bylen.items(),key=lambda x:-x[0])[:10])
# Symmetry of rowmotion cycles under generators of GL(3,3)
def act_mat(A,p):return tuple(sum(A[i][j]*p[j] for j in range(3))%3 for i in range(3))
def induced(A):
 pi=[P.index(norm(act_mat(A,p))) for p in P]
 lj=[]
 for line in L:
  new=sum(1<<pi[i] for i in range(13) if line>>i&1)
  lj.append(L.index(new))
 assert sorted(pi)==sorted(lj)==list(range(13))
 return pi,lj
As=[((0,1,0),(1,0,0),(0,0,1)),((2,0,0),(0,1,0),(0,0,1)),((1,1,0),(0,1,0),(0,0,1)),((0,1,0),(0,0,1),(1,0,0))]
gens=[induced(A) for A in As]
def permute(bits,pi):return sum(1<<pi[i] for i in range(len(pi)) if bits>>i&1)
symm=[]
for pi,lj in gens:
 s=[loc[(permute(c[0][0],pi),permute(c[0][1],lj))] for c in cycles]
 assert sorted(s)==list(range(len(cycles)))
 symm.append(s)
seen_orb=set(); classcounts=Counter(); grouped=[]
for i in range(len(cycles)):
 if i in seen_orb: continue
 orb={i};stack=[i]
 while stack:
  v=stack.pop()
  for g in symm:
   u=g[v]
   if u not in orb:orb.add(u);stack.append(u)
 seen_orb|=orb
 classcounts[(len(cycles[i]),len(orb))]+=1
 grouped.append((len(cycles[i]),len(orb),i, min(cycles[i])))
print('cycle_group_orbits',len(grouped),'orbit_len_size_num',sorted(classcounts.items()))
print('sum_check',sum(n*size for (length,size),n in classcounts.items()))
group={tuple(range(13))}; todo=[tuple(range(13))]
while todo:
 s=todo.pop()
 for pi,lj in gens:
  t=tuple(pi[s[i]] for i in range(13))
  if t not in group: group.add(t);todo.append(t)
print('projective_group_order',len(group));assert len(group)==5616
assert len(grouped)==22
assert classcounts==Counter({(2,234):2,(3,1):1,(3,156):2,(3,468):2,(5,13):2,(5,52):1,(5,78):2,(5,234):2,(6,312):2,(7,117):1,(7,468):3,(9,936):1,(11,702):1})
print('LINEAR_COORDINATES_ROW_AND_GROUP_PASS')
