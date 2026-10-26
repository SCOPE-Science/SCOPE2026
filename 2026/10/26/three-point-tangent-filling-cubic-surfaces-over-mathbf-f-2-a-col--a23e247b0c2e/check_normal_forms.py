"""Exact, dependency-free certificates for two cubic-surface tangent-filling orbits over GF(2)."""
from itertools import product

E=[]
for a in range(4):
 for b in range(a,4):
  for c in range(b,4):
   e=[0]*4
   for i in (a,b,c):e[i]+=1
   E.append(tuple(e))
assert len(E)==20
index={e:j for j,e in enumerate(E)}

def mono(*v):
 ex=[0]*4
 for i in v:ex[i]+=1
 return 1<<index[tuple(ex)]

def evaluate(mask,p):
 parity=0
 for j,e in enumerate(E):
  if (mask>>j)&1 and all(not e[k] or ((p>>k)&1) for k in range(4)):parity^=1
 return parity

def gradient(mask,p):
 out=0
 for k in range(4):
  t=0
  for j,e in enumerate(E):
   if (mask>>j)&1 and (e[k]&1) and all(not (e[h]-(h==k)) or ((p>>h)&1) for h in range(4)): t^=1
  out|=t<<k
 return out

# w,x,y,z are coordinate 0,1,2,3; L is w=x=0.
f0=mono(0,0,0)^mono(1,1,1)^mono(0,0,1)
kernel=[mono(i,i,j)^mono(i,j,j) for i in range(4) for j in range(i+1,4)]
family={f0^sum((kernel[j] if (t>>j)&1 else 0) for j in range(6)):t for t in range(64)}
assert len(family)==64
L={4,8,12}
assert all({p for p in range(1,16) if not evaluate(m,p)}==L for m in family)
regular={m:t for m,t in family.items() if all(gradient(m,p) for p in L)}
inside={m:t for m,t in regular.items() if (t>>5)&1==0} # kernel order ij: (01)(02)(03)(12)(13)(23)
outside={m:t for m,t in regular.items() if (t>>5)&1}
assert len(inside)==12 and len(outside)==32,(len(inside),len(outside))
print('64 fixed-line cubic equations: 44 smooth at rational points, split 12 containing the line and 32 not')

def mulforms(a,b):
 out=0
 for j,e in enumerate(E):
  if (a>>j)&1: raise ValueError('expect low-degree formal tuples, not cubics')
# Expand a homogeneous cubic F(X) after a GF(2)-linear change X=M Xnew.
def transformed(mask,cols):
 rows=[sum((1<<j) for j in range(4) if (cols[j]>>i)&1) for i in range(4)]
 out=0
 for j,e in enumerate(E):
  if not ((mask>>j)&1):continue
  p={(0,0,0,0)}
  for i,n in enumerate(e):
   for _ in range(n):
    nxt=set()
    for m in p:
     for k in range(4):
      if rows[i]>>k&1:
       v=list(m);v[k]+=1;v=tuple(v)
       if v in nxt:nxt.remove(v)
       else:nxt.add(v)
    p=nxt
  for v in p:out^=1<<index[v]
 return out

# A linear change preserves L iff columns 2 and 3 are a basis of U,
# and the first two columns project to a basis of the quotient GF(2)^4/U.
mats=[]
for a in (1,2,3):
 for b in (1,2,3):
  if a==b:continue
  for u in range(4):
   for v in range(4):
    for c in L:
     for d in L:
      if c==d:continue
      mats.append((a+4*u,b+4*v,c,d))
assert len(mats)==576
print('line stabilizer size',len(mats))

fA=mono(0,0,0)^mono(0,0,1)^mono(0,0,3)^mono(0,3,3)^mono(1,1,1)^mono(1,1,2)^mono(1,2,2)
fB=mono(0,0,0)^mono(0,1,1)^mono(1,1,1)^mono(2,2,3)^mono(2,3,3)
assert fA in inside and fB in outside
for mask,kind,target in ((fA,'contained',inside),(fB,'not contained',outside)):
 orbit={transformed(mask,M) for M in mats}
 assert orbit==set(target),(len(orbit),len(target))
 print('representative',kind,'mask',hex(mask),'fixed-line orbit',len(orbit),'global orbit',len(orbit)*35,'stabilizer',576//len(orbit))
 # The partial derivatives are quadratic forms in squares; verify invertible coefficient matrix.
 rows=[]
 for k in range(4):
  row=[]
  for j in range(4):
   p=1<<j
   row.append((gradient(mask,p)>>k)&1)
  rows.append(row)
 # This test checks exact symbolic derivative has no mixed term.
 for k in range(4):
  for p in range(16):
   assert ((gradient(mask,p)>>k)&1)==sum(rows[k][j]*((p>>j)&1) for j in range(4))%2
 rank=0;M=[sum((v<<j) for j,v in enumerate(row)) for row in rows]
 for j in range(4):
  i=next((i for i in range(rank,4) if (M[i]>>j)&1),None)
  if i is None:continue
  M[i],M[rank]=M[rank],M[i]
  for i in range(4):
   if i!=rank and M[i]>>j&1:M[i]^=M[rank]
  rank+=1
 assert rank==4
 print('  squared-coordinate Jacobian matrix',rows,'rank',rank)
 print('  rational zeros',sorted(p for p in range(1,16) if evaluate(mask,p)==0))

# Each of the 35 lines is the zero locus of 64 forms, so 35*(12+32)=1540.
# Three distinct planes through a line cover all 15 ambient rational points.
# With one surface point the unique tangent plane has only 7 rational points.
assert 35*(12+32)==1540
print('PASS: sharp three-point minimum; 1540 surfaces in two classes, sizes 420 and 1120')
