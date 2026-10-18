import itertools, sympy as S
from functools import reduce
X0,X1,Y0,Y1=S.symbols('X0 X1 Y0 Y1');vv=[X0,X1,Y0,Y1]
mons=[(4-a,a,3-b,b) for a in range(5) for b in range(4)]
rat=[(1,0),(0,1),(1,1)]
pts=[p+q for p in rat for q in rat]
row=[sum(int(all((not e or p[i]) for i,e in enumerate(m)))<<j for j,m in enumerate(mons)) for p in pts]
rr=[];piv=[]
for r in row:
 for p,u in zip(piv,rr):
  if r>>p&1:r^=u
 if r:
  p=(r&-r).bit_length()-1;ind=sum(v<p for v in piv);piv.insert(ind,p);rr.insert(ind,r)
free=[j for j in range(len(mons)) if j not in piv];basis=[]
for j in free:
 m=1<<j
 for p,r in reversed(list(zip(piv,rr))):
  if (m&r).bit_count()%2:m^=1<<p
 assert all((m&r).bit_count()%2==0 for r in row)
 basis.append(m)
assert len(piv) == 9 and len(basis) == 11

def poly(mask):return sum(S.prod(t**e for t,e in zip(vv,m)) for j,m in enumerate(mons) if mask>>j&1)
def smooth(mask):
 f=poly(mask)
 for a,b in itertools.product([0,1],repeat=2):
  sub={vv[a]:1,vv[2+b]:1};other=[vv[1-a],vv[3-b]]
  bb=S.groebner([f.subs(sub),*[S.diff(f,u).subs(sub) for u in vv]],*other,modulus=2)
  if not(len(bb.polys)==1 and bb.polys[0].is_one):return False
 return True
from functools import lru_cache
@lru_cache(None)
def terms(mask):return [mon for i,mon in enumerate(mons) if mask>>i&1]

def ratgrad(mask,p):
 for k in range(4):
  ss=0
  for m in terms(mask):
   if m[k]%2 and all(p[i] or e-(i==k)==0 for i,e in enumerate(m)):ss^=1
  if ss:return True
 return False
goods=[];smoothr=0
for t in range(1,1<<len(basis)):
 mask=0
 for j,u in enumerate(basis):
  if t>>j&1:mask^=u
 if all(ratgrad(mask,p) for p in pts):
  smoothr+=1
  if smooth(mask):goods.append(mask)
assert smoothr == 364
assert len(goods) == 66

# PGL2 F2 elements 6 matricies and transformations
mats=[]
for a,b,c,d in itertools.product(range(2),repeat=4):
 if a*d^b*c:mats.append((a,b,c,d))
assert len(mats)==6
mon_to_bit={m:1<<i for i,m in enumerate(mons)}
def pmul(p,q):
 o={}
 for i,a in p.items():
  for j,b in q.items():
   k=tuple(i[t]+j[t] for t in range(4));o[k]=o.get(k,0)^(a*b)
 return {k:v for k,v in o.items() if v}
def ppow(p,n):
 r={(0,0,0,0):1}
 for _ in range(n):r=pmul(r,p)
 return r
trans=[]
for A,B in itertools.product(mats,repeat=2):
  fx=[{(1,0,0,0):A[0],(0,1,0,0):A[1]}, {(1,0,0,0):A[2],(0,1,0,0):A[3]}, {(0,0,1,0):B[0],(0,0,0,1):B[1]}, {(0,0,1,0):B[2],(0,0,0,1):B[3]}]
  fx=[{k:v for k,v in u.items() if v} for u in fx]
  mapping=[]
  for m in mons:
   p={(0,0,0,0):1}
   for i,e in enumerate(m):p=pmul(p,ppow(fx[i],e))
   mapping.append(sum(mon_to_bit[k] for k in p))
  trans.append(mapping)
def act(mask,trans):
 out=0
 for i in range(20):
  if mask>>i&1:out^=trans[i]
 return out
left=set(goods);orbits=[]
while left:
 v=min(left);orbit={act(v,t) for t in trans};assert orbit<=set(goods)
 left-=orbit;orbits.append((v,len(orbit)))
assert orbits == [(396246, 6), (399606, 18), (404886, 36), (420790, 6)]


polys={1:0b11,2:0b111,3:0b1011,4:0b10011,5:0b100101,6:0b1000011}
def field(n):
 P=polys[n];q=1<<n
 def mul(a,b):
  out=0
  while b:
   if b&1:out^=a
   b>>=1;a<<=1
   if a&q:a^=P
  return out
 T=[[mul(a,b) for b in range(q)] for a in range(q)]
 return q,T

def count(mask,n):
 q,T=field(n);R=[(1,t) for t in range(q)]+[(0,1)]
 powers=[[1]*5 for _ in range(q)]
 for t in range(q):
  for e in range(1,5):powers[t][e]=T[powers[t][e-1]][t]
 terms=[m for i,m in enumerate(mons) if mask>>i&1]
 count=0
 for x0,x1 in R:
  for y0,y1 in R:
   t=0
   for a,b,c,d in terms:
    t^=T[T[T[powers[x0][a]][powers[x1][b]]][powers[y0][c]]][powers[y1][d]]
   count+=not t
 return count

def Lpoly(N):
 C=[1]
 for n in range(1,7):
  s=sum((N[k-1]-(2**k+1))*C[n-k] for k in range(1,n+1))
  assert s%n==0,(n,s,N,C)
  C.append(s//n)
 return C+[C[6-j]*2**j for j in range(1,7)]


ijs=[(i,j) for i in range(3) for j in range(2)]

def mat(mask):
 terms={(m[1],m[3]) for n,m in enumerate(mons) if mask>>n&1}
 return [sum((int((2*i+1-k,2*j+1-l) in terms)<<n) for n,(k,l) in enumerate(ijs)) for i,j in ijs]
def mult(A,B):return [reduce(lambda a,b:a^b,(B[i] for i in range(6) if row>>i&1),0) for row in A]
def rank(A):
 piv={}
 for row in A:
  while row:
   p=row.bit_length()-1
   if p in piv:row^=piv[p]
   else:piv[p]=row;break
 return len(piv)

# Exhaustion and exact genus-six Weil numerators. All arithmetic is integral.
expected = {
 396246:(6,[9,9,9,9,69,51],[1,6,20,48,90,144,211,288,360,384,320,192,64],6),
 399606:(18,[9,9,9,21,39,39],[1,6,20,48,93,156,233,312,372,384,320,192,64],6),
 404886:(36,[9,9,12,17,24,78],[1,6,20,49,98,167,250,334,392,392,320,192,64],5),
 420790:(6,[9,11,9,23,9,53],[1,6,21,54,114,204,313,408,456,432,336,192,64],6),
}
assert sum(size for _,size in orbits)==len(goods)==66
for v,size in orbits:
 E_size,E_N,E_L,E_prank=expected[v]
 N=[count(v,n) for n in range(1,7)]
 L=Lpoly(N)
 H=mat(v)
 B=H
 for _ in range(5):B=mult(H,B)
 assert (size,N,L,rank(B))==(E_size,E_N,E_L,E_prank)
 assert rank(H)==E_prank
 assert max(i for i in range(7) if L[i]%2)==E_prank
 assert len(L)==13 and L[-1]==64
 print('mask',v,'orbit_size',size,'points',N,'L_coefficients',L,'p_rank',E_prank,'a_number',6-rank(H))
print('PASS: 2047 candidate equations, 364 rationally nonsingular, 66 geometrically smooth; 4 distinct zeta functions')
