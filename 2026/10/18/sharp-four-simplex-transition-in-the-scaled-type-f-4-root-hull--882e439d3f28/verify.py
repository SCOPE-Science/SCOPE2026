from itertools import combinations,product
from functools import lru_cache
from math import comb
from collections import Counter

P=[]
for i,j in combinations(range(4),2):
 for a,b in product((-2,2),repeat=2):
  v=[0]*4;v[i]=a;v[j]=b;P.append((tuple(v),0))
for i in range(4):
 for a in (-2,2):
  v=[0]*4;v[i]=a;P.append((tuple(v),1))
for signs in product((-1,1),repeat=4): P.append((tuple(signs),1))
assert len(P)==48

@lru_cache(maxsize=None)
def det4(idx):
 a,b,c,d=(P[i][0] for i in idx)
 def det3(x,y,z):
  return x[0]*(y[1]*z[2]-y[2]*z[1])-x[1]*(y[0]*z[2]-y[2]*z[0])+x[2]*(y[0]*z[1]-y[1]*z[0])
 res=0
 for j in range(4):
  aa=tuple(a[t] for t in range(4) if t!=j)
  bb=tuple(b[t] for t in range(4) if t!=j)
  cc=tuple(c[t] for t in range(4) if t!=j)
  dd=tuple(d[t] for t in range(4) if t!=j)
  # expand along first row, minor det of rows b,c,d
  res+=(-1 if j%2 else 1)*a[j]*det3(bb,cc,dd)
 return res

def sign_sur(a,b):
 if b==0:return (a>0)-(a<0)
 if a==0:return (b>0)-(b<0)
 if (a>0)==(b>0):return 1 if a>0 else -1
 q=a*a-2*b*b
 assert q!=0
 return (1 if q>0 else -1)*(1 if a>0 else -1)

def bound(u,v,p,q):
 return sign_sur(u*u+2*v*v-p*p-2*q*q,2*(u*v-p*q))<=0

def eval_k(k,A,B):
 return [(A,0),(B,A),(2*A,B),(2*B,2*A),(4*A,2*B)][k]

N=Counter();W=Counter();found=Counter();maxima=Counter()
for sub in combinations(range(1,48),4):
 ids=(0,)+sub
 k=sum(P[i][1] for i in ids)
 cs=[0]*5
 for j in range(5):
  others=ids[:j]+ids[j+1:]
  exp=sum(P[i][1] for i in others)
  cs[exp]+=(-1 if j%2 else 1)*det4(others)
 A,B=cs[k],(cs[k-1] if k else 0)
 u,v=eval_k(k,A,B)
 N[k]+=1
 if k==0:
  assert bound(u,v,192,0)
  if abs(u)==192 and v==0:W[k]+=1
 else:
  assert bound(u,v,0,128)
  if u==0 and abs(v)==128:W[k]+=1
 found[(k,A,B)]+=1
assert N==Counter({0:8855,1:42504,2:69828,3:46552,4:10626}),N
assert W==Counter({0:10,1:24,4:6}), W
# All 24 long-root vertices, and a no-shared-four-face rigidity certificate.
max_sets=[]
for ss in combinations(range(24),5):
    d=sum((-1 if j%2 else 1)*det4(ss[:j]+ss[j+1:]) for j in range(5))
    assert abs(d)<=192
    if abs(d)==192:max_sets.append(ss)
assert len(max_sets)==48
seen=set()
for s in max_sets:
    for face in combinations(s,4):
        assert face not in seen
        seen.add(face)
assert len(seen)==240
# The block-Hadamard orthogonal symmetry maps L to sqrt(2)*S:
# H*u = 2*(2*s), where u=2*v and Q=H/sqrt(2).
L={p[0] for p in P[:24]}
S2={p[0] for p in P[24:]}
H=lambda v:(v[0]+v[1],v[0]-v[1],v[2]+v[3],v[2]-v[3])
assert {H(v) for v in L}=={tuple(2*x for x in w) for w in S2}
# Complete B4-orbit decomposition of pure-short maximizers.
short_index={w:i for i,w in enumerate(P[24:])}
short_max={tuple(sorted(short_index[(tuple(z//2 for z in H(P[i][0])),1)] for i in ss)) for ss in max_sets}
assert len(short_max)==48
left=set(short_max)
short_orbits=[]
for seed in sorted(short_max):
    if seed not in left:continue
    orbit=set()
    for perm in __import__('itertools').permutations(range(4)):
        for signs in product((-1,1),repeat=4):
            orb=tuple(sorted(short_index[(tuple(signs[j]*P[24+i][0][perm[j]] for j in range(4)),1)] for i in seed))
            orbit.add(orb)
    assert orbit<=short_max
    short_orbits.append(orbit)
    left-=orbit
assert not left and sorted(map(len,short_orbits))==[16,16,16]
axial_counts=sorted(next(iter({sum(i<8 for i in ss) for ss in orbit})) for orbit in short_orbits)
assert axial_counts==[0,1,4]
print('PYTHON_VERIFY_OK anchor_sets',sum(N.values()),'minors',det4.cache_info(),
      'classes',len(found),'top',dict(W),'long_max',len(max_sets),'shared_four',0,'Q_duality',24,'short_B4_orbits',[16,16,16])

