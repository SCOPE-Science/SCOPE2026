"""Exact finite-field census of smooth bidegree-(2,3) curves over F2.

The 12 coefficient bits index X0^(2-i) X1^i Y0^(3-j) Y1^j at bit 4*i+j.
No external algebra system is needed. The field modulus z^6+z+1 is irreducible.
"""
import json
from itertools import product
from collections import Counter
# bit i*4+j is coefficient X0**(2-i)*X1**i * Y0**(3-j)*Y1**j
# GF64 with modulus z^6+z+1
MOD=0x43
MUL=[[0]*64 for _ in range(64)]
for a in range(64):
 for b in range(64):
  v=0; w=a; t=b
  while t:
   if t&1:v^=w
   w<<=1
   if w&64:w^=MOD
   t>>=1
  MUL[a][b]=v
SQR=[MUL[a][a] for a in range(64)]
ROOT=[0]*64
for a in range(64):ROOT[SQR[a]]=a
assert set(ROOT)==set(range(64))

def ev(c,t,inf=False):
 # c=4-bit cubic coeff for degree terms t^3, t^2, t^1,1
 if inf:return (c&1)!=0
 r=c&1
 for j in (1,2,3):r=MUL[r][t]^((c>>j)&1)
 return r

def dev(c,t,inf=False):
 # t affine Y0/Y1 (Y1=1). derivative of cubic = (j i) t^i odd: t^3 + t
 if inf:
  # at infinity coordinate Y1/Y0, polynomial c0+c1*s+c2*s²+c3*s³ derivative at s=0 = c1
  return (c>>1)&1
 return MUL[c&1][MUL[t][t]] ^((c>>2)&1)  # derivative t^3 + t

# F=A(Y) X0²+B(Y) X0X1+C(Y) X1²

def smooth(mask):
 A=mask&15;B=(mask>>4)&15;C=(mask>>8)&15
 if not B:return False
 # roots of B homogeneous cubic: t roots incl infinity
 for t in range(64):
  if ev(B,t):continue
  a=ev(A,t);c=ev(C,t)
  if a==0 and c==0:return False
  d=MUL[dev(A,t)][c]^MUL[dev(B,t)][MUL[ROOT[a]][ROOT[c]]]^MUL[dev(C,t)][a]
  if not d:return False
 if (B&1)==0:
  a=ev(A,0,True);c=ev(C,0,True)
  if a==0 and c==0:return False
  d=MUL[dev(A,0,True)][c]^MUL[dev(B,0,True)][MUL[ROOT[a]][ROOT[c]]]^MUL[dev(C,0,True)][a]
  if not d:return False
 return True

# rational pts each factor [1:0],[0:1],[1:1] equivalent affine x infin/0/1
RT=[(1,0),(0,1),(1,1)]
def value(mask,x,y):
 x0,x1=x;y0,y1=y
 out=0
 for i in range(3):
  for j in range(4):
   if (mask>>(4*i+j))&1:
    out^=(x0**(2-i))*(x1**i)*(y0**(3-j))*(y1**j)
 return out

def N1(mask):return sum(not value(mask,x,y) for x in RT for y in RT)

# distinguish number of geometric branch points (distinct roots of B over GF64 incl infinity)
def BR(mask):
 B=(mask>>4)&15
 vals=[t for t in range(64) if ev(B,t)==0]
 if B&1==0:vals.append(64)
 # Frobenius orbits degrees under square
 visited=set();parts=[]
 for t in vals:
  if t not in visited:
   orbit=[];k=t
   while k not in visited:
    visited.add(k);orbit.append(k);k=64 if k==64 else SQR[k]
   parts.append(len(orbit))
 return tuple(sorted(parts))

# transformations SL2(F2) matrices: (a,b,c,d) determinant=1
G=[(a,b,c,d) for a,b,c,d in product(range(2),repeat=4) if a*d^b*c==1]
assert len(G)==6

def poly_pow_lin(a,b,n):
 # homogeneous 2-var linear polynomial (a*z0+b*z1)^n in char2, represented by masks coeff (z0^(n-j)*z1^j)
 z=[1]
 for _ in range(n):
  zz=[0]*(len(z)+1)
  for j,w in enumerate(z):
   zz[j]^=w&a;zz[j+1]^=w&b
  z=zz
 return z

def transform_cols(gx,gy):
 a,b,c,d=gx;e,f,g,h=gy
 cols=[]
 for i in range(3):
  xp=poly_pow_lin(a,b,2-i); xq=poly_pow_lin(c,d,i)
  X=[0]*3
  for ii,p in enumerate(xp):
   for jj,q in enumerate(xq):X[ii+jj]^=p&q
  # next per monomial j
  for j in range(4):
   yp=poly_pow_lin(e,f,3-j); yq=poly_pow_lin(g,h,j)
   Y=[0]*4
   for ii,p in enumerate(yp):
    for jj,q in enumerate(yq):Y[ii+jj]^=p&q
   im=0
   for ii,xv in enumerate(X):
    for jj,yv in enumerate(Y):
     if xv&yv:im^=1<<(ii*4+jj)
   cols.append(im)
 return cols

TRANS=[transform_cols(gx,gy) for gx in G for gy in G]
assert len(set(map(tuple,TRANS)))==36

def act(mask,cols):
 r=0
 while mask:
  b=mask & -mask;r^=cols[b.bit_length()-1];mask^=b
 return r

# extra invariants
CUBES={1,8,15}
def totally_ramified_x(mask):
 out=0
 for x in RT:
  x0,x1=x
  c=0
  for j in range(4):
   a=0
   for i in range(3):a^=((mask>>(4*i+j))&1)*(x0**(2-i))*(x1**i)
   c|=a<<j
  if c in CUBES:out+=1
 return out

def kpower(a,n):
 v=1
 for _ in range(n):v=MUL[v][a]
 return v

def points_degree(n):
 k=[a for a in range(64) if kpower(a,2**n)==a]
 assert len(k)==2**n
 return [(1,0)]+[(t,1) for t in k]

def vextension(mask,x,y):
 x0,x1=x;y0,y1=y
 powx0=[1,x0,SQR[x0]];powx1=[1,x1,SQR[x1]]
 powy0=[1,y0,SQR[y0],MUL[SQR[y0]][y0]]
 powy1=[1,y1,SQR[y1],MUL[SQR[y1]][y1]]
 v=0
 for i in range(3):
  for j in range(4):
   if (mask>>(4*i+j))&1:
    v^=MUL[MUL[powx0[2-i]][powx1[i]]][MUL[powy0[3-j]][powy1[j]]]
 return v

def Nn(mask,n):
 P=points_degree(n)
 return sum(vextension(mask,x,y)==0 for x in P for y in P)



def enumerate_curves():
    smooth_masks = [mask for mask in range(1, 4096) if smooth(mask)]
    smooth_set = set(smooth_masks)
    checked = set()
    orbit_rows = []
    for mask in smooth_masks:
        if mask in checked:
            continue
        orbit = {act(mask, transform) for transform in TRANS}
        assert orbit.issubset(smooth_set)
        checked.update(orbit)
        r = min(orbit)
        n = N1(r)
        branch = BR(r)
        assert all(N1(m) == n and BR(m) == branch for m in orbit)
        n2 = Nn(r, 2)
        n3 = Nn(r, 3)
        a1 = n - 3
        assert (a1*a1 - (5-n2)) % 2 == 0
        a2 = (a1*a1 - (5-n2)) // 2
        assert n3 == 9 + a1**3 - 3*a1*a2 + 6*a1
        tr = totally_ramified_x(r)
        assert all(totally_ramified_x(m) == tr for m in orbit)
        orbit_rows.append({
            'rep': r, 'size': len(orbit), 'N1': n, 'N2': n2, 'N3': n3,
            'a1': a1, 'a2': a2, 'branch': list(branch),
            'totally_ramified_x': tr
        })
    assert sum(row['size'] for row in orbit_rows) == len(smooth_masks)
    assert checked == smooth_set
    strata = Counter()
    for row in orbit_rows:
        strata[(row['N1'], row['N2'], tuple(row['branch']))] += row['size']
    return {
        'total_nonzero_forms': 4095,
        'smooth_forms': len(smooth_masks),
        'orbit_count': len(orbit_rows),
        'distinct_weil_polynomials': len({(r['a1'],r['a2']) for r in orbit_rows}),
        'branch_point_count_strata': len({(r['N1'],tuple(r['branch'])) for r in orbit_rows}),
        'joint_strata': [
            {'N1': n, 'N2': n2, 'branch': list(b), 'equations': v,
             'orbits': sum(r['N1']==n and r['N2']==n2 and tuple(r['branch'])==b for r in orbit_rows)}
            for (n,n2,b),v in sorted(strata.items())
        ],
        'orbits': orbit_rows,
    }

if __name__ == '__main__':
    print(json.dumps(enumerate_curves(), sort_keys=True, indent=2))
