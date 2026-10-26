"""Self-contained exact finite-field computation, gf(2), q=2 space-filling CIs.
Reproduces complete quotient search and Jacobian Groebner smoothness checks.
"""
import itertools,json, time, sys
from collections import Counter
import sympy as sp
T0=time.time(); vars_=sp.symbols('x y z w')

def mon(v):
 a=[0]*4;a[v]=1;return {tuple(a)}
def add(*ps):
 out=set()
 for p in ps:out.symmetric_difference_update(p)
 return out
def mul(p,q):
 out=set()
 for a in p:
  for b in q:
   c=tuple(a[i]+b[i] for i in range(4))
   if c in out:out.remove(c)
   else:out.add(c)
 return out
def ph(i,j):
 a=[0]*4;a[i]=2;a[j]+=1
 b=[0]*4;b[j]=2;b[i]+=1
 return {tuple(a),tuple(b)}
def polytobits(p):
 return sum(1<<degree4.index(e) for e in p)
def indep(poly,basis):
 x=polytobits(poly)
 for lead,b in basis.items():
  if (x>>lead)&1:x^=b
 if not x:return False
 lead=x.bit_length()-1
 for k in basis:
  if (basis[k]>>lead)&1:basis[k]^=x
 basis[lead]=x
 return True

g=add(ph(0,1),ph(2,3))
vec=[mul(mon(i),g) for i in range(4)]
degree4=sorted((a,b,c,4-a-b-c) for a in range(5) for b in range(5-a) for c in range(5-a-b))
span={}
for v in vec:assert indep(v,span)
basis=[]
for i in range(4):
 for j in range(i+1,4):
  for k in range(4):
   p=mul(mon(k),ph(i,j))
   if indep(p,span):basis.append(p)
assert len(basis)==16
exprs=[sum(sp.prod(vars_[i]**e[i] for i in range(4)) for e in p) for p in basis]
pointbits=list(range(1,16))

def grad_at(ff, pt):
 return sum(1<<i for i in range(4) if sum((e[i]&1) * int(all(((pt>>j)&1) or e[j]==int(j==i) for j in range(4))) for e in ff)%2)
ggrad={pt:grad_at(g,pt) for pt in pointbits}
# derivative bit masks - allow evaluating f gradient at F2-points by XOR
bg={pt:[grad_at(b,pt) for b in basis] for pt in pointbits}

def f2_local_smooth(mask):
 for pt in pointbits:
  v=0
  for j in range(16):
   if (mask>>j)&1:v^=bg[pt][j]
  if v==0 or v==ggrad[pt]:return False
 return True

def expr_from_mask(mask):
 return sp.Add(*(exprs[j] for j in range(16) if (mask>>j)&1))

def f_from_mask(mask):
 p=set()
 for i in range(16):
  if (mask>>i)&1:p^=basis[i]
 return p

def geom_smooth(ff):
 # Use affine Jacobian ideal and exact Groebner reduction on four standard charts.
 F=sum(sp.prod(vars_[i]**e[i] for i in range(4)) for e in ff)
 G=sum(sp.prod(vars_[i]**e[i] for i in range(4)) for e in g)
 for ch in range(4):
  v=[vars_[i] for i in range(4) if i!=ch]
  gc=sp.expand(G.subs({vars_[ch]:1})); fc=sp.expand(F.subs({vars_[ch]:1}))
  dg=[sp.diff(gc,t) for t in v];df=[sp.diff(fc,t) for t in v]
  minors=[sp.expand(dg[i]*df[j]-dg[j]*df[i]) for i in range(3) for j in range(i+1,3)]
  gb=sp.groebner([gc,fc]+minors,*v,order='grevlex',modulus=2)
  if not (len(gb.polys)==1 and gb.polys[0].is_one):
   return False, ch, [str(z.as_expr()) for z in gb.polys[:4]]
 return True,None,[]

exps=sorted((a,b,c,7-a-b-c) for a in range(1,8) for b in range(1,8-a) for c in range(1,8-a-b) if 7-a-b-c>=1)
L=[int(tuple(t-1 for t in a) in g) for a in exps]
pivot=L.index(1)
Hbase=[(1<<i)|((1<<pivot) if L[i] else 0) for i in range(20) if i!=pivot]

def rank(vecs):
 b={}
 for v in vecs:
  while v:
   p=v.bit_length()-1
   if p in b:v^=b[p]
   else:b[p]=v;break
 return len(b)

def hasse_data(ff):
 gf=mul(g,ff)
 F=[]
 for a in exps:
  out=0
  for j,b in enumerate(exps):
   if tuple(2*ai-bi for ai,bi in zip(a,b)) in gf:out ^=1<<j
  F.append(out)
 def act(vec):
  out=0
  while vec:
   bit=vec&-vec;j=bit.bit_length()-1;out^=F[j];vec^=bit
  return out
 vectors=[act(v) for v in Hbase]
 rank1=rank(vectors)
 for _ in range(19):vectors=[act(v) for v in vectors]
 return rank1,rank(vectors)

if __name__=='__main__':
 local=[]
 for mask in range(65536):
  if f2_local_smooth(mask):local.append(mask)
 print('LOCAL_SMOOTH',len(local),'all_masks',65536,'elapsed',time.time()-T0,flush=True)
 counts=Counter();nonsmooth=[]; smooth=[]
 start=int(sys.argv[1]) if len(sys.argv)>1 else 0
 end=int(sys.argv[2]) if len(sys.argv)>2 else len(local)
 for n,mask in list(enumerate(local))[start:end]:
  ff=f_from_mask(mask)
  ok,ch,gb=geom_smooth(ff)
  if ok:
   r1,stable=hasse_data(ff)
   counts[(r1,stable)]+=1
   smooth.append({'mask':mask,'rank1':r1,'p_rank':stable})
  else:nonsmooth.append({'mask':mask,'chart':ch})
  if n%25==0:print('TESTED',n,'TOTAL',len(local),'SMOOTH',len(smooth),'RANKS',dict(counts),'ELAPSED',round(time.time()-T0,2),flush=True)
 result={'scheme':'V(g,f), g=phi_xy+phi_zw on P3/F2, f in degree-four rational-point ideal modulo g times linear forms','field':2,'basis_dim':len(basis),'total_classes':65536,'local_smooth_classes':len(local),'geometric_smooth_classes':len(smooth),'smooth_rank_counts':{str(k):v for k,v in counts.items()},'smooth':smooth,'nonsmooth':nonsmooth, 'basis_monomials':[[list(e) for e in sorted(b)] for b in basis],'elapsed_seconds':time.time()-T0, 'start':start,'end':end}
 with open(f'space_filling_census_part_{start:03d}_{end:03d}.json','w') as w:json.dump(result,w,sort_keys=True)
 print('END',len(smooth),counts,'nonsmooth',len(nonsmooth),'seconds',time.time()-T0,flush=True)
