"""Enumerate nonsplit-quadric (3,2) canonical genus-four curves in P3/F2.
A research certificate generator, standard Python plus SymPy for exact smoothness.
"""
import itertools, collections, json, time, os, sympy as S
from functools import reduce
clock=time.monotonic()
x=S.symbols('x0 x1 x2 x3')
Q=x[0]*x[1]+x[2]**2+x[2]*x[3]+x[3]**2
Qeval=lambda v: ((v&1)>0 and (v&2)>0) ^ ((v&4)>0) ^ ((v&4)>0 and (v&8)>0) ^ ((v&8)>0)
P=[v for v in range(1,16) if not Qeval(v)]
assert P==[1,2,7,11,15]
# 16 canonical cubic basis monomials modulo Q*linear
mons=[]
for a in itertools.combinations_with_replacement(range(4),3):
 if not(0 in a and 1 in a):mons.append(a)
assert len(mons)==16
mindex={a:i for i,a in enumerate(mons)}

def mulpoly(A,B):
 C={}
 for aa,va in A.items():
  for bb,vb in B.items():
   cc=tuple(aa[i]+bb[i] for i in range(len(aa)))
   C[cc]=C.get(cc,0)^(va&vb)
 return {k:v for k,v in C.items() if v}

def addpoly(A,B):
 C=A.copy()
 for k,v in B.items():
  C[k]=C.get(k,0)^v
 return {k:v for k,v in C.items() if v}

def poly_pow(A,n):
 C={(0,)*(len(next(iter(A))) if A else 2):1}
 for _ in range(n):C=mulpoly(C,A)
 return C

def cubic_reduce(a):
 if 0 in a and 1 in a:
  r=list(a);r.remove(0);r.remove(1); j=r[0]
  return ( (tuple(sorted((2,2,j))),tuple(sorted((2,3,j))),tuple(sorted((3,3,j)))) )
 return (a,)

def reduce_cubic(p):
 mask=0
 for a,coeff in p.items():
  if not coeff: continue
  for z in cubic_reduce(tuple(sorted(sum(([i]*a[i] for i in range(4)),[])))):
   mask ^=1<<mindex[z]
 return mask

def mat_mulvec(cols, v):
 return reduce(int.__xor__,(cols[j] for j in range(4) if v>>j&1),0)

def basis_matrix_from_values(src,dst):
 # src four independent vectors, dst target images. Solve columns images of standard e_j.
 A=[row for row in src]
 cols=[]
 for jj in range(4):
  t=next((bits for bits in range(16) if reduce(int.__xor__,(src[i] for i in range(4) if bits>>i&1),0)==(1<<jj)),None)
  if t is None:return None
  cols.append(reduce(int.__xor__,(dst[i] for i in range(4) if t>>i&1),0))
 return cols

G=[]
for perm in itertools.permutations(P):
 M=basis_matrix_from_values(P[:4],perm[:4])
 if M is None:continue
 if mat_mulvec(M,P[4])!=perm[4]:continue
 if any(Qeval(mat_mulvec(M,v))!=Qeval(v) for v in range(1,16)):continue
 G.append(M)
assert len(G)==120,len(G)

def action_matrix(M):
 # substitution old x_j = sum_i M_{ji} new x_i
 lin=[]
 for j in range(4):lin.append({tuple(1 if i==k else 0 for i in range(4)):1 for k in range(4) if M[k]>>j&1})
 t=[]
 for aa in mons:
  f={(0,0,0,0):1}
  for i in aa:f=mulpoly(f,lin[i])
  t.append(reduce_cubic(f))
 return t

T=[action_matrix(M) for M in G]
# use two group generators whose induced permutation group is all S5
perms=[]
for M in G: perms.append(tuple(P.index(mat_mulvec(M,v)) for v in P))
gen_perm=[(1,2,3,4,0),(1,0,2,3,4)]
generators=[T[perms.index(p)] for p in gen_perm]

def apply_trans(mask, trans):
 y=0
 while mask:
  bit=mask&-mask
  y^=trans[bit.bit_length()-1]
  mask^=bit
 return y

orbit_id=[-1]*65536
orbits=[]
for v in range(1,65536):
 if orbit_id[v]>=0:continue
 idx=len(orbits);visited=[v];orbit_id[v]=idx
 for w in visited:
  for gen in generators:
   z=apply_trans(w,gen)
   if orbit_id[z]==-1:
    orbit_id[z]=idx;visited.append(z)
 assert all(orbit_id[w]==idx for w in visited)
 orbits.append((v,len(visited)))
print('orbits',len(orbits),'sizes',collections.Counter(n for v,n in orbits),'clock',round(time.monotonic()-clock,2),flush=True)

# Exact F2-extension Jacobian algebra via Gröbner bases, chartwise no singular points over algebraic closure.
qs=[S.diff(Q,t) for t in x]


def is_smooth(mask):
 F=sum((S.prod(x[j] for j in aa) for i,aa in enumerate(mons) if mask>>i&1),S.Integer(0))
 fs=[F.diff(t) for t in x]
 minor=[qs[i]*fs[j]+qs[j]*fs[i] for i in range(4) for j in range(i+1,4)]
 for k in range(4):
  variables=[x[j] for j in range(4) if j!=k]
  gens=[S.Poly(p.subs({x[k]:1}),*variables,modulus=2).as_expr() for p in (Q,F,*minor)]
  gb=S.groebner(gens,*variables,order='grevlex',modulus=2)
  if not(len(gb.polys)==1 and gb.polys[0].is_one):return False
 return True

# Theta-syndromes via projective plane sections; one 3-bit syndrome per H.
def polar(u,v):return Qeval(u^v)^Qeval(u)^Qeval(v)

def coords_monomial_product(L,aa):
 out={(0,0):1}
 for k in aa:out=mulpoly(out,L[k])
 return out

# GF4 repr: a+b*omega as 2-bit; omega^2=omega+1
def gf4mul(a,b):
 a0=a&1;a1=(a>>1)&1;b0=b&1;b1=(b>>1)&1
 return (a0*b0 ^ a1*b1) | ((a0*b1 ^a1*b0 ^a1*b1)<<1)

def gf4poly_mul(A,B):
 C={}
 for a,v in A.items():
  for b,w in B.items():
   k=(a[0]+b[0],a[1]+b[1]);C[k]=C.get(k,0)^gf4mul(v,w)
 return {k:v for k,v in C.items() if v}

def planebasis(h):
 V=[v for v in range(1,16) if (v&h).bit_count()%2==0]
 for u,w,z in itertools.combinations(V,3):
  if len({u,w,z,u^w,u^z,w^z,u^w^z})==7:return (u,w,z)
 raise ValueError(h)

syndromes=[];types=[];detail=[]
for h in range(1,16):
 V=planebasis(h)
 Cpts=[v for v in range(1,16) if (v&h).bit_count()%2==0 and not Qeval(v)]
 if len(Cpts)==3:
  # smooth conic, parametrized by projection from P0; A B complement
  p0=Cpts[0];other=[v for v in V if v!=p0]
  for a,b in itertools.combinations([v for v in range(1,16) if (v&h).bit_count()%2==0],2):
   if len({p0,a,b,p0^a,p0^b,a^b,p0^a^b})==7:break
  # P(s,t)=Q(sA+tB)*P0 + B(P0,sA+tB)*(sA+tB)
  quad={(2,0):int(Qeval(a)),(1,1):polar(a,b),(0,2):int(Qeval(b))}
  dot={(1,0):polar(p0,a),(0,1):polar(p0,b)}
  lin=[{(1,0):int(a>>j&1),(0,1):int(b>>j&1)} for j in range(4)]
  L=[addpoly(({k:v for k,v in quad.items()} if p0>>j&1 else {}),mulpoly(dot,lin[j])) for j in range(4)]
  assert not addpoly(mulpoly(L[0],L[1]),addpoly(poly_pow(L[2],2),addpoly(mulpoly(L[2],L[3]),poly_pow(L[3],2))))
  coeff=[]
  for aa in mons:
   poly=coords_monomial_product(L,aa)
   value=sum((1<<j if poly.get((5-2*j,1+2*j),0) else 0 for j in range(3)))
   coeff.append(value)
  types.append('smooth')
 else:
  assert len(Cpts)==1,(h,Cpts)
  p=Cpts[0]
  for a,b in itertools.combinations([v for v in range(1,16) if (v&h).bit_count()%2==0],2):
   if len({p,a,b,p^a,p^b,a^b,p^a^b})==7:break
  # all values Q(s a +t b) nonzero => Q(a)=Q(b)=polar(a,b)=1
  assert (Qeval(a),Qeval(b),polar(a,b))==(1,1,1),(h,p,a,b)
  # line vector t*(omega*a+b)+w*p in GF4
  # omega=2, 1=1
  L=[]
  for j in range(4):
   d=(2 if a>>j&1 else 0)^(1 if b>>j&1 else 0)
   L.append({(1,0):d,(0,1):(1 if p>>j&1 else 0)})
  coeff=[]
  for aa in mons:
   poly={(0,0):1}
   for k in aa:poly=gf4poly_mul(poly,L[k])
   coeff.append((poly.get((0,3),0)&1)|((poly.get((2,1),0)&1)<<1)|((poly.get((2,1),0)>>1)<<2))
  types.append('tangent')
 syndromes.append(coeff)
 detail.append({'plane':h,'type':types[-1],'basis':list(V),'points':Cpts})
assert collections.Counter(types)=={'smooth':10,'tangent':5}
print('theta section types',collections.Counter(types),'clock',round(time.monotonic()-clock,2),flush=True)

def theta_mask(mask):
 out=0
 for h,cols in enumerate(syndromes):
  val=0;z=mask
  while z:
   bit=z&-z;val^=cols[bit.bit_length()-1];z^=bit
  if val==0:out|=1<<h
 return out

# theta-count invariance across all 120 automorphisms (up to orbit reps) tests generic
for z in [3,0xffff,0x77a9,0x3bee,0x45e1]:
 assert len({theta_mask(apply_trans(z,t)).bit_count() for t in T})==1,z
print('theta invariance sample passed',round(time.monotonic()-clock,2),flush=True)

smooth_orbits=[];dist=collections.Counter();theta_orbitstats=collections.Counter()
for i,(v,n) in enumerate(orbits):
 if is_smooth(v):
  mask=theta_mask(v);count=mask.bit_count();dist[count]+=n
  smooth_orbits.append({'mask':v,'size':n,'theta_count':count,'theta_planes':mask, 'pts':sum(1 for p in P if sum( ((all((p>>j)&1 for j in aa))) for ii,aa in enumerate(mons) if v>>ii&1)%2==0)})
  theta_orbitstats[count]+=1
 if i%100==0:print('progress',i,'clock',round(time.monotonic()-clock,2),flush=True)
print('smooth orbits',len(smooth_orbits),'smooth eqs',sum(z['size'] for z in smooth_orbits),'dist',sorted(dist.items()),'orbit theta',sorted(theta_orbitstats.items()),'elapsed',round(time.monotonic()-clock,2),flush=True)
# matrix of all values theta => independent weighted full eq count check by linear algebra all forms
all_theta=collections.Counter(theta_mask(m).bit_count() for m in range(1,65536))
print('all theta dist',sorted(all_theta.items()),'clock',round(time.monotonic()-clock,2),flush=True)
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/qminus_genus4_results.json'),'w') as f:json.dump({'Q':'x0*x1+x2^2+x2*x3+x3^2','basis':['*'.join('x%d'%j for j in aa) for aa in mons], 'automorphism_group_order':len(G),'total_orbits':len(orbits),'smooth_orbits':smooth_orbits,'smooth_equation_distribution':sorted(dist.items()),'smooth_orbit_distribution':sorted(theta_orbitstats.items()),'all_equation_distribution':sorted(all_theta.items()),'plane_details':detail,'theta_syndrome_columns':syndromes},f,indent=2)
