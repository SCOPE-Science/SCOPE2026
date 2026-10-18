import itertools,collections,time
D=[(i,i) for i in range(4)]+list(itertools.combinations(range(4),2))
def sm(q):
 a=[(q>>(4+i))&1 for i in range(6)]
 return a[0]*a[5]^a[1]*a[4]^a[2]*a[3]==1
G=[i for i in range(1024) if sm(i)]
print('smooth',len(G))
# lists all 2spaces canonical tuple from independent pair
pens=set()
for i,p in enumerate(G):
 for r in G[i+1:]:
  if sm(p^r): pens.add(tuple(sorted((p,r,p^r))))
print('pencils',len(pens))

def mon_image(L1,L2):
 poly=0
 for i in range(4):
  if L1>>i&1:
   for j in range(4):
    if L2>>j&1:
     m=(i,j) if i<=j else (j,i)
     poly ^=1<<D.index(m)
 return poly

def gen_map(M):
 basis=[mon_image(M[i],M[j]) for i,j in D]
 def transform(q):
  ans=0
  for k in range(10):
   if q>>k&1:ans ^= basis[k]
  return ans
 return transform
trans=[gen_map(tuple(1<<v for v in perm)) for perm in [(1,0,2,3),(0,2,1,3),(0,1,3,2)]]+[gen_map((3,2,4,8))]

def transform_pencil(p,g):
 q=[g(x) for x in p];return tuple(sorted(q))
remain=set(pens);orbs=[]
while remain:
 rep=min(remain);seen={rep};stk=[rep]
 for p in stk:
  for tr in trans:
   q=transform_pencil(p,tr)
   if q not in seen:seen.add(q);stk.append(q)
 assert seen<=remain,(len(seen),len(seen-remain))
 remain-=seen
 # incidence under GF2 P3 projective = 15 nonzero points
 Q1,Q2,_=rep
 def eval_q(q,x):
  v=0
  for k,(i,j) in enumerate(D):
   if (q>>k)&1 and (x>>i)&1 and (x>>j)&1:v ^=1
  return v
 N1=sum(not eval_q(Q1,x) and not eval_q(Q2,x) for x in range(1,16))
 orbs.append((rep,len(seen),N1))
print('orbits',len(orbs),'sizes',collections.Counter((i[1],i[2]) for i in orbs));print('reps:')
for a in orbs: print(a)
print('done')

# The polar pencil count supplies an independent check on the raw census.
polar_pencils={tuple(sorted((a>>4,b>>4,(a^b)>>4)))
               for a,b,c in pens}
assert len(polar_pencils)==56
# Every polar pencil has exactly 256 quadratic lifts.
assert len(pens)==56*256
assert sorted(size for rep,size,num in orbs)==[336,560,3360,5040,5040]
assert sorted((size,num) for rep,size,num in orbs)==[(336,0),(560,6),(3360,6),(5040,2),(5040,4)]
print('CENSUS_VERIFY_OK')
