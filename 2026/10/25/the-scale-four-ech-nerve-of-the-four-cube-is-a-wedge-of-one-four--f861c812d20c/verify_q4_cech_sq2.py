"""Reproducible GF(2) certificate for the four-cube scale-four Cech nerve.
Uses only the Python standard library; run from directory with q4_cech_sq2_certificate.json.
"""
from itertools import combinations
from pathlib import Path
import json
V=range(16)
facets=[sum(1<<v for v in V if (u^v).bit_count()<=2) for u in V]
fs={}
for m in facets:
 vertices=[v for v in V if m>>v&1]
 for k in range(1,12):
  fs.setdefault(k,set()).update(sum(1<<v for v in t) for t in combinations(vertices,k))
faces={k:sorted(s) for k,s in fs.items()}
pos={k:{m:i for i,m in enumerate(s)} for k,s in faces.items()}
assert [len(faces[k]) for k in range(1,12)]==[16,120,560,1780,3808,5272,4640,2560,880,176,16]

def bits(mask):
 while mask:
  low=mask&-mask
  yield low.bit_length()-1
  mask^=low

def boundary(mask,k):
 return sum(1<<pos[k-1][mask^(1<<v)] for v in bits(mask))

def reduce_col(x,pivots):
 while x:
  p=x.bit_length()-1
  if p in pivots:x^=pivots[p]
  else:pivots[p]=x;return True
 return False
ranks={1:15}
for k in range(2,12):
 pivots={}
 for m in faces[k]:reduce_col(boundary(m,k),pivots)
 ranks[k-1]=len(pivots)
assert ranks=={1:15,2:105,3:455,4:1325,5:2482,6:2790,7:1840,8:720,9:160,10:16},ranks
betti=[len(faces[d+1])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(11)]
assert betti==[1,0,0,0,1,0,10,0,0,0,0],betti
c=json.loads((Path(__file__).parent/'q4_cech_sq2_certificate.json').read_text())
a=sum(1<<i for i in c['cocycle_4_indices'])
b=sum(1<<i for i in c['primitive_5_indices'])
z=sum(1<<i for i in c['nonboundary_cycle_4_indices'])
sq_certificate=sum(1<<i for i in c['square_support_6_indices'])
assert len(c['cocycle_4_indices'])==108
assert len(c['primitive_5_indices'])==116
assert len(c['nonboundary_cycle_4_indices'])==24
assert len(c['square_support_6_indices'])==81
assert all((a&boundary(m,6)).bit_count()%2==0 for m in faces[6])
assert (a&z).bit_count()%2==1
# z is a mod-2 cycle in degree 4
for i in range(len(faces[4])):
 assert sum(bool(z>>j&1 and faces[4][i]&faces[5][j]==faces[4][i]) for j in range(len(faces[5])))%2==0
# Independent normalized cup-2 formula from Medina-Mardones: for n=6, i=2,
# split each 4-element U subset of {0,..,6} into U0 and U1 by u_j+j parity.
# Only summands leaving 5-vertex factors are relevant for a degree-four cochain.
sq=0
for i,m in enumerate(faces[7]):
 vv=list(bits(m));val=0
 for U in combinations(range(7),4):
  U0=[u for j,u in enumerate(U,1) if (u+j)%2==0]
  U1=[u for j,u in enumerate(U,1) if (u+j)%2==1]
  if len(U0)!=2 or len(U1)!=2:continue
  m0=sum(1<<vv[j] for j in range(7) if j not in U0)
  m1=sum(1<<vv[j] for j in range(7) if j not in U1)
  val^=((a>>pos[5][m0])&1)&((a>>pos[5][m1])&1)
 if val:sq|=1<<i
assert sq==sq_certificate
# δb = a cup_2 a, verified independently by adjacency of six- and seven-vertex faces.
for i,m in enumerate(faces[7]):
 val=sum((b>>pos[6][m^(1<<v)])&1 for v in bits(m))%2
 assert val==(sq>>i)&1
assert all((sq&boundary(m,8)).bit_count()%2==0 for m in faces[8])
print('Q4_CECH_SQ2_CERTIFICATE_OK')
print('betti_F2',betti,'cochain_supports',(108,116,24,81))
