"""Bidegree (2,3) curves in P1xP1 over F2: projective orbits and smoothness."""
import sympy as sp,collections
mons=[(i,j) for i in range(3) for j in range(4)]
assert len(mons)==12

def substitution(k, which,kind):
  # indices i corresponds u0^(2-i)u1^i, j corresponds v0^(3-j)v1^j
  out=0
  for n,(i,j) in enumerate(mons):
    if not (k>>n)&1:continue
    d=2 if which==0 else 3
    z=i if which==0 else j
    if kind=='swap': dz=d-z
    else:
      # x0 -> x0+x1, x1 unchanged; (x0+x1)^(d-z)x1^z
      dz=None
    if dz is not None:
      b=(dz,j) if which==0 else (i,dz)
      out^=1<<mons.index(b)
    else:
      for h in range(d-z+1):
        if (sp.binomial(d-z,h)%2)==0:continue
        a=z+h
        b=(a,j) if which==0 else (i,a)
        out^=1<<mons.index(b)
  return out

GEN=[[substitution(k,w,kind) for k in range(4096)] for w in range(2) for kind in ('swap','shear')]
unseen=set(range(1,4096)); orbs=[]
while unseen:
 rep=min(unseen); que=[rep];orb={rep}
 for k in que:
  for g in GEN:
   kk=g[k]
   if kk not in orb:orb.add(kk);que.append(kk)
 unseen-=orb; orbs.append((rep,len(orb)))
print('orbits',len(orbs),sum(w for _,w in orbs),flush=True)
u,v=sp.symbols('u v')
@sp.cacheit

def poly(k,chart_u,chart_v):
 terms=[]
 for n,(i,j) in enumerate(mons):
  if (k>>n)&1:
   expu=i if chart_u==0 else 2-i
   expv=j if chart_v==0 else 3-j
   terms.append(u**expu * v**expv)
 return sum(terms)

def smooth(k):
 for cu in range(2):
  for cv in range(2):
   f=poly(k,cu,cv)
   g=sp.groebner([f,sp.diff(f,u),sp.diff(f,v)],u,v,modulus=2)
   if not any(y.as_expr()==1 for y in g.polys):return False
 return True

def count(k):
 # 3 rational points P1(F2): (1,0),(0,1),(1,1)
 ps=[(1,0),(0,1),(1,1)]; total=0
 for a,b in ps:
  for c,d in ps:
   val=0
   for idx,(i,j) in enumerate(mons):
    if (k>>idx)&1:val^=a**(2-i)*b**i*c**(3-j)*d**j
   total+=val==0
 return total

nsm=[];dist=collections.Counter()
for i,(rep,w) in enumerate(orbs):
 if smooth(rep):
  N=count(rep)
  nsm.append((rep,w,N));dist[N]+=w
print('smooth orbits',len(nsm),'smooth',sum(dist.values()),'dist',sorted(dist.items()),flush=True)
print('SMOOTH',nsm,flush=True)
