"""Exact character and independent chain-Euler checks for the Heawood four-cut complex."""
from itertools import permutations, combinations
from collections import Counter,defaultdict
from math import comb

V=tuple(range(14)); FULL=(1<<14)-1
POINTS=tuple(range(1,8))
def bitdot(a,b):return (a&b).bit_count()%2
LINES={l: frozenset(p for p in POINTS if bitdot(p,l)==0) for l in POINTS}
assert sorted(len(L) for L in LINES.values())==[3]*7
EDGES=set()
for l in POINTS:
 for p in LINES[l]:EDGES.add((p-1,6+l))
N=[set() for _ in V]
for p,l in EDGES:N[p].add(l);N[l].add(p)
assert len(EDGES)==21 and all(len(x)==3 for x in N)
def conn(t):
 t=set(t); seen={next(iter(t))}; frontier=list(seen)
 while frontier:
  a=frontier.pop()
  for b in (N[a]&t)-seen: seen.add(b);frontier.append(b)
 return seen==t
connected4=[sum(1<<x for x in q) for q in combinations(V,4) if conn(q)]
disconnected4=[sum(1<<x for x in q) for q in combinations(V,4) if not conn(q)]
assert len(connected4)==98 and len(disconnected4)==903
# Alexander dual is the complete 2-skeleton plus 98 connected four-subsets.
dual_faces=[set() for d in range(4)]
for k in (1,2,3):dual_faces[k-1]={sum(1<<x for x in q) for q in combinations(V,k)}
dual_faces[3]=set(connected4)
assert [len(x) for x in dual_faces]==[14,91,364,98]
# Each top face has an integral private boundary triangle; this independently
# certifies injectivity and primitivity of the top boundary over Z.
private={}
for q in connected4:
    candidates=[]
    for tri in combinations([i for i in V if q>>i&1],3):
        t=sum(1<<i for i in tri)
        if sum((w&t)==t for w in connected4)==1:candidates.append(t)
    assert candidates,('missing private triangle',q)
    private[q]=min(candidates)
assert len(set(private.values()))==98
# Ordinary cut complex directly from every disconnected-four-set complement.
cut_faces=set()
for q in disconnected4:
 facet=FULL^q
 sub=facet
 while sub:
  cut_faces.add(sub);sub=(sub-1)&facet
assert len(cut_faces)>0
cut_faces_by_dim=[set() for i in range(10)]
for q in cut_faces:cut_faces_by_dim[q.bit_count()-1].add(q)

def lin(a,images):
 r=0
 for i in range(3):
  if a & (1<<i):r^=images[i]
 return r

def maps():
 for ims in permutations(POINTS,3):
  img=[lin(p,ims) for p in POINTS]
  if len(set(img))!=7:continue
  pointperm={p:img[p-1] for p in POINTS}
  lineperm={old:next(lnew for lnew in POINTS if LINES[lnew]==frozenset(pointperm[p] for p in LINES[old])) for old in POINTS}
  col=tuple([pointperm[p]-1 for p in POINTS]+[6+lineperm[l] for l in POINTS])
  dual=tuple([7+p for p in range(7)]+[p for p in range(7)])
  yield col,False
  yield tuple(dual[x] for x in col),True
G=list(maps())
# Independent Fano-plane incidence automorphism census: all 7! point
# permutations that send the seven lines to lines, without matrix algebra.
line_sets=set(LINES.values())
all_fano_collineations=set()
for p in permutations(POINTS):
    if {frozenset(p[x-1] for x in line) for line in LINES.values()}==line_sets:
        all_fano_collineations.add(tuple(x-1 for x in p))
assert len(all_fano_collineations)==168
assert all_fano_collineations=={g[:7] for g,sw in G if not sw}
assert len(G)==336 and len({g for g,b in G})==336
for perm,_ in G:
 assert {tuple(sorted((perm[a],perm[b]))) for a,b in EDGES}==set(tuple(sorted(e)) for e in EDGES)

def sgn_perm(perm):return -1 if sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))%2 else 1
def transform_face(mask,p):
 ids=[i for i in V if mask>>i&1]
 transformed=[p[i] for i in ids]
 out=sum(1<<x for x in transformed)
 if out!=mask:return 0
 return (-1)**(sum(transformed[i]>transformed[j] for i in range(len(transformed)) for j in range(i+1,len(transformed)))%2)
def signed_sum(faces,perm):return sum(transform_face(x,perm) for x in faces)
def cycle_type(perm):
 seen=set();cycles=[]
 for i in V:
  if i in seen:continue
  j=i;m=0
  while j not in seen:seen.add(j);m+=1;j=perm[j]
  cycles.append(m)
 return tuple(sorted(cycles))
def order_perm(p):
 from math import lcm
 return lcm(*cycle_type(p))
character_rows=[]
for g,swap in G:
 traces=[signed_sum(fs,g) for fs in dual_faces]
 tr_dual=-1+traces[0]-traces[1]+traces[2]-traces[3]
 tr_cut_direct=1-sum((-1)**d*signed_sum(fs,g) for d,fs in enumerate(cut_faces_by_dim))
 tr_cut=sgn_perm(g)*tr_dual
 assert tr_cut==tr_cut_direct,(g,tr_dual,tr_cut,tr_cut_direct)
 character_rows.append((g,swap,sgn_perm(g),order_perm(g),cycle_type(g),tr_dual,tr_cut,traces))
assert next(x[-2] for x in character_rows if x[3]==1)==188
sum_cut=sum(x[-2] for x in character_rows)
sum_col=sum(x[-2] for x in character_rows if not x[1])
assert sum_cut%336==0 and sum_col%168==0
print('faces dual',*[len(x) for x in dual_faces],'cut',*[len(x) for x in cut_faces_by_dim], 'total nonempty',len(cut_faces))
print('group size',len(G),'collineation order',168,'private top faces',len(private),'full invariant dimension',sum_cut//336,'collineation invariant dim',sum_col//168)
by=defaultdict(list)
for row in character_rows:
 g,swap,sign,order,ct,dual,ch,traces=row
 by[(swap,order,ct,sign,ch)].append(row)
print('CHARACTER TABLE grouped by split, order, 14-cycle-type, permutation sign, H9 trace:')
for key,vals in sorted(by.items(),key=lambda kv:(kv[0][0],kv[0][1],kv[0][2],kv[0][4])):
 print('group',str(key),'count',len(vals),'dualtrace',vals[0][-3])
print('dual sum',sum(x[-3] for x in character_rows),'cut sum',sum_cut,'collineation sum',sum_col)
print('VERIFY_HEAWOOD_4CUT_FULL_CHARACTER_OK')
