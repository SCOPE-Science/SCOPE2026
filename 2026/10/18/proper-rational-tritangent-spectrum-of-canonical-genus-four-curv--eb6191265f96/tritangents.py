from nonsplit_genus4 import BASIS, PTS, EVALS,qpoint
import json,collections
# GF2 binary homogeneous forms as int bits exponent t=i

def mulbits(a,b):
 out=0
 while a:
  j=(a&-a).bit_length()-1
  out^=b<<j;a&=a-1
 return out

def bival(a):return [(a&1)!=0,(a>>2&1)!=0,a.bit_count()%2!=0]

def q2(b):
 return mulbits(b[0],b[1])^mulbits(b[2],b[2])^mulbits(b[2],b[3])^mulbits(b[3],b[3])

def dot(h,v):return (h&v).bit_count()&1

def conic_param(h):
 rational={v for v in PTS if not dot(h,v)}
 assert len(rational) in (1,3)
 if len(rational)==1:return None
 results=[]
 for mask in range(1<<12):
  b=[(mask>>(3*j))&7 for j in range(4)]
  if any(sum((int((b[i]>>k)&1) for i in range(4) if h>>i&1))%2 for k in range(3)):continue
  if q2(b):continue
  images=[]
  for coord in range(3):
   if coord==0:v=sum((b[i]&1)<<i for i in range(4))
   elif coord==1:v=sum((b[i]>>2&1)<<i for i in range(4))
   else:v=sum((b[i].bit_count()&1)<<i for i in range(4))
   images.append(v)
  if set(images)==rational:
   results.append(b)
 assert len(results)==6,(h,len(results))
 return min(results)

HPLANES=list(range(1,16))
CONIC={h:conic_param(h) for h in HPLANES if len([v for v in PTS if not dot(h,v)])==3}
assert len(CONIC)==10

def eval_cubic_on_conic(b):
 basis=[]
 for m in BASIS:
  val=1
  for j in range(4):
   for _ in range(m[j]):val=mulbits(val,b[j])
  basis.append(val)
 return basis
CONIC_RESTR={h:eval_cubic_on_conic(b) for h,b in CONIC.items()}

def conic_tritangent(mask,h):
 row=CONIC_RESTR[h]
 f=0
 for i in range(16):
  if mask>>i&1:f^=row[i]
 if f&0b0101010:return False
 # half-cubic coefficients
 a,b,c,d=[f>>i&1 for i in (0,2,4,6)]
 return (a*d^b*c)==1

# GF4 F2[w]/w^2+w+1
F4M=[[0]*4 for _ in range(4)]
for a in range(4):
 for b in range(4):
  z=0
  for i in range(2):
   for j in range(2):
    if a>>i&1 and b>>j&1:
     if i+j==0:z^=1
     elif i+j==1:z^=2
     else:z^=3
  F4M[a][b]=z

def mul4(a,b):return F4M[a][b]
def q4(v):
 a,b,c,d=v
 return mul4(a,b)^mul4(c,c)^mul4(c,d)^mul4(d,d)

def add4(a,b):return [x^y for x,y in zip(a,b)]
def smul4(x,v):return [mul4(x,z) for z in v]

def all_projp4():
 out=[]
 for nn in range(1,4**4):
  v=[];w=nn
  for i in range(4):v.append(w%4);w//=4
  idx=next(i for i,k in enumerate(v) if k)
  inv=next(k for k in range(1,4) if mul4(k,v[idx])==1)
  normalized=tuple(smul4(inv,v))
  if normalized not in out:out.append(normalized)
 return out

PROJP4=all_projp4()
assert len(PROJP4)==85

def line_restriction(p,v):
 arr=[]
 for m in BASIS:
  # binary homogeneous polynomial degree3 with GF4 coefficients, coeff of t^k
  val=[1]
  for j in range(4):
   for _ in range(m[j]):
    nxt=[0]*(len(val)+1)
    for i,a in enumerate(val):
     nxt[i]^=mul4(a,p[j]);nxt[i+1]^=mul4(a,v[j])
    val=nxt
  arr.append(val)
 return arr

TANGENT_RESTR={}
for h in HPLANES:
 if h in CONIC:continue
 rational=[v for v in PTS if not dot(h,v)]
 assert len(rational)==1
 p=tuple((rational[0]>>i)&1 for i in range(4))
 # H-plane equation over F4
 off=[v for v in PROJP4 if not __import__('functools').reduce(int.__xor__,(v[i] for i in range(4) if h>>i&1),0) and q4(v)==0 and v!=p]
 assert len(off)==8,(h,len(off))
 v=off[0]
 # chosen v not on F2 point, span line in Q
 assert all(q4(add4(smul4(s,p),smul4(t,v)))==0 for s in range(4) for t in range(4))
 TANGENT_RESTR[h]=line_restriction(p,v)
assert len(TANGENT_RESTR)==5

def tangent_tritangent(mask,h):
 f=[0,0,0,0]
 row=TANGENT_RESTR[h]
 for i in range(16):
  if mask>>i&1:
   for k in range(4):f[k]^=row[i][k]
 return f[0]==0 and f[1]!=0 and f[2]==0

def rtritangents(mask):
 good=[h for h in CONIC if conic_tritangent(mask,h)]
 good2=[h for h in TANGENT_RESTR if tangent_tritangent(mask,h)]
 return good,good2
