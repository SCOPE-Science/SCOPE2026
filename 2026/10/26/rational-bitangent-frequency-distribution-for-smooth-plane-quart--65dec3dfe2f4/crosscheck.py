"""A separate full-matrix enumeration and direct binary restriction check."""
import csv,itertools,collections
import sympy as sy
from functools import reduce
E=[(a,b,4-a-b) for a in range(5) for b in range(5-a)]
IX={e:i for i,e in enumerate(E)}
X,Y,Z=sy.symbols('X Y Z')

def p_mul(P,Q):
 R={}
 for e in P:
  for f in Q:
   h=tuple(e[i]+f[i] for i in range(len(e)))
   if h in R:del R[h]
   else:R[h]=1
 return R

def p_power_product(exp,forms,n):
 P={(0,)*n:1}
 for k,m in enumerate(exp):
  for _ in range(m):P=p_mul(P,forms[k])
 return P

def polynomial_transform(m,precomputed):
 output=0
 for i in range(15):
  if m>>i&1:output^=precomputed[i]
 return output

def rank_three(rows):
 im={0}
 for r in rows:im|={u^r for u in list(im)}
 return len(im)==8

# Exhaust the 168 invertible 3x3 matrices, no generator reliance.
matrices=[(a,b,c) for a,b,c in itertools.product(range(1,8),repeat=3) if rank_three((a,b,c))]
assert len(matrices)==168
T=[]
for rows in matrices:
 # Correct representation of each linear polynomial as unit coordinate monomials.
 forms=[{tuple(int(k==i) for k in range(3)):1 for i in range(3) if rows[j]>>i&1} for j in range(3)]
 T.append([sum(1<<IX[g] for g in p_power_product(e,forms,3)) for e in E])

def transverse_coeff_mask(e,v,w):
 Fs=[]
 for i in range(3):
  A={}
  if v>>i&1:A[(1,0)]=1
  if w>>i&1:A[(0,1)]=1
  Fs.append(A)
 P=p_power_product(e,Fs,2)
 return sum(1<<j for j in range(5) if (4-j,j) in P)

L=[]
for a in range(1,8):
 ker=[p for p in range(1,8) if ((p&a).bit_count()&1)==0]
 assert len(ker)==3
 v,w=ker[:2]
 L.append([transverse_coeff_mask(e,v,w) for e in E])

def line_bitangents(m):
 total=0
 for restriction in L:
  mask=polynomial_transform(m,restriction)
  if (mask&10)==0:total+=1
 return total

def smooth(m):
 polys=[]
 F=sum(sy.prod(t**e[i] for i,t in enumerate((X,Y,Z))) for k,e in enumerate(E) if m>>k&1)
 Ds=[sy.diff(F,t) for t in (X,Y,Z)]
 for v in (X,Y,Z):
  q=[q for q in (X,Y,Z) if q!=v]
  ideal=[sy.Poly(p.subs(v,1),*q,modulus=2).as_expr() for p in [F]+Ds]
  if not sy.groebner(ideal,*q,order='grevlex',modulus=2).contains(sy.Integer(1)):
   return False
 return True

with open('all_orbits.csv',newline='') as f:
 records=list(csv.DictReader(f))
assert len(records)==279
seen=set(); distro=collections.Counter();smoothcount=0
for row in records:
 m=int(row['mask']);sz=int(row['orbit_size']);flag=(row['smooth']=='1')
 orb={polynomial_transform(m,t) for t in T}
 assert 0 not in orb and len(orb)==sz and not(seen&orb),m
 seen.update(orb)
 assert smooth(m)==flag,m
 if flag:
  count=line_bitangents(m)
  assert count==int(row['bitangents']),m
  # All 168 coordinate images have the same line-bitangent count.
  assert all(line_bitangents(y)==count for y in orb)
  distro[count]+=len(orb);smoothcount+=len(orb)
assert len(seen)==32767
assert smoothcount==10920
assert dict(distro)=={0:3072,1:5278,2:2352,3:105,4:112,7:1},distro
print('CROSSCHECK_OK; matrices=168; forms=32767; orbit_representatives=279; smooth_forms=10920; distribution='+repr(sorted(distro.items())))
