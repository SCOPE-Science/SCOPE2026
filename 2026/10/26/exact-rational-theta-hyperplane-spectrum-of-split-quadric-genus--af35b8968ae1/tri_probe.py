import itertools, collections, time
from functools import lru_cache
pts=((1,0),(0,1),(1,1))
# Binary homogeneous polynomials represented as coefficient arrays in powers of T.
def mul(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]^=x&y
 return out

def powpoly(a,n):
 y=[1]
 for _ in range(n):y=mul(y,a)
 return y

def hpoly(a,b):return [a,b]

def vals_deg3_at(pt):return [(pt[0]**(3-i)*pt[1]**i)&1 for i in range(4)]
val=[vals_deg3_at(p) for p in pts]
# all planes on P3 as nonzero linear form h, each plane contains projective points z dot h =0
seg=[]
for u in pts:
 for v in pts:
  seg.append((u[0]*v[0],u[0]*v[1],u[1]*v[0],u[1]*v[1]))

monexp=[]
for i in range(4):
 for j in range(4):
  t=min(i,j);monexp.append((3-max(i,j),j-t,i-t,t))

rulings=[]
for i,u in enumerate(pts):
 for j,v in enumerate(pts):
  # first v variable with u fixed, then u variable with v fixed
  first=[]; second=[]
  for a in range(4):
   for b in range(4):
    first.append((val[i][a]<<b))
    second.append((val[j][b]<<a))
  rulings.append((i,j,first,second))

lin=[[1,0],[0,1],[1,1]]
allowed=[]
for idx in range(3):
 L=[lin[(idx+1)%3][0]^lin[(idx+2)%3][0],lin[(idx+1)%3][1]^lin[(idx+2)%3][1]] # careful L vanishes at point idx ; another use direct: for point (u,v), L=[v,u]
 p=pts[idx];L=[p[1],p[0]]
 poss=set()
 for Q in lin:
  b=mul(L,powpoly(Q,2));poss.add(sum(x<<k for k,x in enumerate(b)))
 allowed.append(poss)
assert all(len(x)==3 for x in allowed), allowed

smoothplanes=[]
tangent=[]
for h in range(1,16):
 conic=[idx for idx,z in enumerate(seg) if sum((h>>k&1)*z[k] for k in range(4))%2==0]
 if len(conic)==3:
  P=[seg[t] for t in conic]
  Z=[]
  for k in range(4):Z.append([P[0][k],P[0][k]^P[1][k]^P[2][k],P[1][k]])
  # verify on Q: z0*z3+z1*z2 ==0 polynomials
  assert mul(Z[0],Z[3])==mul(Z[1],Z[2]), (h,Z)
  basis=[]
  for ex in monexp:
   q=[1]
   for k,e in enumerate(ex):
    for t in range(e):q=mul(q,Z[k])
   basis.append(sum((x&1)<<ind for ind,x in enumerate(q)))
  smoothplanes.append((h,basis))
 else:
  assert len(conic)==5,(h,len(conic))
  pid=[k for k,p in enumerate(seg) if  p in [seg[idx] for idx in conic] and sum(1 for j in conic if j//3==k//3)>1 and sum(1 for j in conic if j%3==k%3)>1]
  assert len(pid)==1,(h,pid)
  tangent.append((h,pid[0]))
assert (len(smoothplanes),len(tangent))==(6,9)

def form_test(f):
 tc=0; m=0
 for h, basis in smoothplanes:
  sextic=0
  for k in range(16):
   if f>>k&1:sextic^=basis[k]
  if sextic&0b0101010==0:
   tc+=1;m|=1<<h
 for h,pid in tangent:
  i,j,basis1,basis2=rulings[pid]
  c1=0;c2=0
  for k in range(16):
   if f>>k&1:
    c1^=basis1[k];c2^=basis2[k]
  if c1 in allowed[j] and c2 in allowed[i]:
   tc+=1;m|=1<<h
 return tc,m

if __name__=='__main__':
 print('conic planes', [x[0] for x in smoothplanes]);print('tangent planes',tangent);print('allowed',allowed)
 t=time.monotonic()
 d=collections.Counter();maxd=[]
 for f in range(1,65536):
  n,m=form_test(f);d[n]+=1
  if n>=5:maxd.append((f,n,m))
 print('distribution all',sorted(d.items()),' >=5',len(maxd),'time',time.monotonic()-t)
 print('max',sorted(maxd,key=lambda x:-x[1])[:20])
