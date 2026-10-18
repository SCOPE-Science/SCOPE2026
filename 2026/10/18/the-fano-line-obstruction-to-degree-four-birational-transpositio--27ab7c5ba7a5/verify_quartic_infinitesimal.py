exec(open('verify_quartic_proper.py').read().split('info=[]')[0])
from collections import Counter,defaultdict
# quadratic Hasse jet evaluation at B in affine chart excluding coordinate j
def quadjet(P,ix,iy,u,v):
 vals=[]
 for m in mons:
  r=0
  for aa in range(3):
   bb=2-aa
   if aa>m[ix] or bb>m[iy]:continue
   import math
   if math.comb(m[ix],aa)%2 and math.comb(m[iy],bb)%2:
    mm=list(m);mm[ix]-=aa;mm[iy]-=bb
    term=point_eval(P,mm)
    term=mult(term,mult(pow8[u][aa],pow8[v][bb]))
    r^=term
  vals.append(r)
 return [sum(((z>>bit)&1)<<k for k,z in enumerate(vals)) for bit in range(3)]
trans=[tuple(j if k==i else i if k==j else k for k in range(7)) for i in range(7) for j in range(i+1,7)]
count=Counter();examples=[]
for B in Blist:
 b=B[0];j=next(i for i in range(3) if b[i]); ix,iy=[i for i in range(3) if i!=j]
 rows=getrows(b)+getrows(b,ix+1)+getrows(b,iy+1)
 for uv in [(1,k) for k in range(8)]+[(0,1)]:
  bas=ker(rows+quadjet(b,ix,iy,*uv));count['total']+=1
  count['dim '+str(len(bas))]+=1
  if len(bas)!=3:continue
  p=[]
  for v in pts:
   w=tuple(f_eval(v,s) for s in bas)
   if w==(0,0,0):break
   p.append(idx[w])
  if len(p)!=7 or len(set(p))!=7:count['nonbijection']+=1;continue
  p=tuple(p)
  count['bijection']+=1;count[cyc(p)]+=1
  if any(compose(g,p) in trans for g in G):
   count['transposition']+=1
   examples.append((B,uv,bas,p))
print(count)
print('first transposition',examples[:1])
assert count['total']==72 and count['dim 3']==72 and count['bijection']==16
assert not examples
print('quartic_infinitesimal_certificate PASS; 72 systems; 16 rational permutations, all even')
