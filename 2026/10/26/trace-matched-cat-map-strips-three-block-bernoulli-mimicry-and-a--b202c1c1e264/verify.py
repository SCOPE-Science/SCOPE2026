from fractions import Fraction as F
from itertools import product

def polygon_area(p):
 if len(p)<3:return F(0)
 return abs(sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(p,p[1:]+p[:1]))/2)

def chop(poly,A,B,C,positive):
 if not poly:return []
 def f(pt):return A*pt[0]+B*pt[1]-C
 out=[]
 for P,Q in zip(poly,poly[1:]+poly[:1]):
  p=f(P);q=f(Q)
  insidep=p>=0 if positive else p<=0
  insideq=q>=0 if positive else q<=0
  if insidep and insideq:out.append(Q)
  elif insidep!=insideq:
   t=p/(p-q);R=(P[0]+t*(Q[0]-P[0]),P[1]+t*(Q[1]-P[1]))
   if insidep:out.append(R)
   else:out.extend([R,Q])
 return out

def box(a,b,q):
 x=F(a,q); xx=F(a+1,q);y=F(b,q);yy=F(b+1,q)
 return [(x,y),(xx,y),(xx,yy),(x,yy)]

def P3(q,a,b,c):
 ans=F(0)
 for k in range(-1,q+1):
  p=box(a,b,q)
  p=chop(p,-1,q,F(c,q)+k,True)
  p=chop(p,-1,q,F(c+1,q)+k,False)
  ans+=polygon_area(p)
 return ans

def P4(q,a,b,c,d):
 ans=F(0)
 for k in range(-1,q+1):
  p=box(a,b,q)
  p=chop(p,-1,q,F(c,q)+k,True)
  p=chop(p,-1,q,F(c+1,q)+k,False)
  # x3 = q*x2 - x1 modulo 1, x2=q*v-u-k
  # x3 = (q*q-1)*v -q*u -q*k
  for ell in range(-2,q*q+1):
   pp=chop(p,-q,q*q-1,F(d,q)+ell+q*k,True)
   pp=chop(pp,-q,q*q-1,F(d+1,q)+ell+q*k,False)
   ans+=polygon_area(pp)
 return ans

if __name__=='__main__':
 for q in (3,4,5,7):
  assert (q-1)*1-(q-2)*1==1  # [[q-1,1],[q-2,1]]
  assert (q-1)+1==q
 for q in (3,4,5):
  failures=[]
  for a,b,c in product(range(q),repeat=3):
   z=P3(q,a,b,c)
   if z!=F(1,q**3):failures.append((a,b,c,z))
  print('TRIPLE',q,'tested',q**3,'failures',len(failures));assert not failures
 for q in (3,4,5):
  got=[P4(q,0,0,0,d) for d in range(q)]
  expected=[F(1,q*q*(q*q-1)) for _ in range(q-1)]+[F(1,q**3*(q+1))]
  print('FOUR',q,'got',got,'expected',expected)
  assert got==expected
 print('VERIFY_OK: exact all-symbol three-block and zero-prefix four-block checks')
