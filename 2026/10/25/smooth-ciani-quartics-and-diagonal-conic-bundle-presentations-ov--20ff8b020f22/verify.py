from itertools import product
from collections import Counter

def norm(t,p):
 for x in t:
  if x%p:
   inv=pow(x,-1,p)
   return tuple((a*inv)%p for a in t)
 return None

def det3(a,b,c,p):
 return (a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]))%p

def proj_forms(p):
 return sorted({norm(t,p) for t in product(range(p),repeat=3)}-{None})

def resnonzero(a,b,p):
 i=(b[1]*b[1]-b[0]*b[2])%p
 j=(a[1]*a[1]-a[0]*a[2])%p
 h=(2*a[1]*b[1]-a[0]*b[2]-a[2]*b[0])%p
 return (h*h-4*i*j)%p !=0

for q in [3,5,7,11]:
 smooth_quadratics=[a for a in proj_forms(q) if (a[1]*a[1]-a[0]*a[2])%q]
 compatible={a:[b for b in smooth_quadratics if resnonzero(a,b,q)] for a in smooth_quadratics}
 count=sum(det3(a,b,c,q)!=0 and c in compatible[a] and c in compatible[b] for a in smooth_quadratics for b in compatible[a] for c in smooth_quadratics)
 pred=q*(q-1)*(q+1)*(q**3-4*q*q+6*q-5)
 print('basis',q,count,pred, count==pred)
 if q>7: continue
 # Independent count of the projective Ciani sextuples through geometric smoothness of F(x,y,z)=g(x^2,y^2,z^2)
 # Coeff order: X4,Y4,Z4,X2Y2,X2Z2,Y2Z2
 count_ciani=0
 for v in product(range(q),repeat=6):
  if not any(v):continue
  if norm(v,q)!=v:continue
  a,b,c,d,e,f=v
  if not all([a,b,c]):continue
  if (d*d-4*a*b)%q==0 or (e*e-4*a*c)%q==0 or (f*f-4*b*c)%q==0:continue
  if (4*a*b*c + d*e*f - a*f*f-b*e*e-c*d*d)%q==0:continue
  count_ciani+=1
 predc=(q-1)**2*(q**3-4*q*q+6*q-5)
 print('ciani',q,count_ciani,predc,count_ciani==predc)

# Independently enumerate all nonzero diagonal (2,2)-forms over F3,
# and check uniform fibers over smooth Ciani coefficient classes.
from collections import Counter
p=3
fibers=Counter()
for coeff in product(range(p), repeat=9):
 forms=[(coeff[j],coeff[3+j],coeff[6+j]) for j in range(3)]
 if any((f[1]*f[1]-f[0]*f[2])%p==0 for f in forms):
  continue
 if det3(*forms,p)==0:
  continue
 if any(not resnonzero(forms[i], forms[j], p)
        for i,j in ((0,1),(0,2),(1,2))):
  continue
 diag=[(f[1]*f[1]-f[0]*f[2])%p for f in forms]
 cross=[(2*forms[i][1]*forms[j][1]-forms[i][0]*forms[j][2]-forms[i][2]*forms[j][0])%p
        for i,j in ((0,1),(0,2),(1,2))]
 fibers[norm(diag+cross,p)]+=1
assert len(fibers)==16
assert set(fibers.values())=={48}
assert sum(fibers.values())==768
assert 48//2==24 # presentations modulo common nonzero scalar
print('F3_FIBERS_OK: 16 quartics, 48 forms each (24 projective presentations)')
print('VERIFY_OK')
