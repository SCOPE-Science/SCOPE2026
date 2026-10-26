"""Standalone rational-arithmetic certificate for a four-point toral sign correlation.

The two ingredients are exhaustive parameter knot enumeration using all
hyperplane triple intersections and exact y-slice rational quadrature.
All arithmetic is exact; the code uses Python's standard library only.
"""
from fractions import Fraction as F
from itertools import combinations
C=[0,0,1,3]
BS=[(i,j) for i in range(4) for j in range(2)]
def sign_val(x):return 1 if (x%1)<F(1,2) else -1

def avgx(y,a):
 xs={F(0),F(1)}
 for n,h in BS:xs.add((F(h,2)-n*y-C[n]*a)%1)
 xs=sorted(xs)
 ans=F(0)
 for l,r in zip(xs,xs[1:]):
  xx=(l+r)/2
  ss=1
  for n in range(4):ss*=sign_val(xx+n*y+C[n]*a)
  ans+=ss*(r-l)
 return ans

def exact(a):
 ys={F(0),F(1)}
 for (n,h),(m,k) in combinations(BS,2):
  if n==m:continue
  rhs=F(h-k,2)-(C[n]-C[m])*a
  for ell in range(-20,21):
   y=(rhs-ell)/(n-m)
   if F(0)<y<F(1):ys.add(y)
 for n,h in BS:
  if n==0: continue
  rhs=F(h,2)-C[n]*a
  for ell in range(-20,21):
   y=(rhs-ell)/n
   if F(0)<y<F(1):ys.add(y)
 ys=sorted(ys)
 total=F(0)
 for lo,hi in zip(ys,ys[1:]):
  total+=(hi-lo)*avgx((lo+hi)/2,a)
 return total


def det(a,b,c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])

def breakpoints():
    # Planes of discontinuity in (x,y,alpha) over [0,1]^2 x [0,1/4]
    L=[((1,n,n*(n-1)//2),F(ell,2))
       for n in range(4)
       for ell in range(0, 2*(1+n+3)+2)]
    L.extend([((1,0,0),F(0)),((1,0,0),F(1)),
              ((0,1,0),F(0)),((0,1,0),F(1))])
    # Bounds above are generous; extra half-integer level planes do not matter.
    out={F(0),F(1,4)}
    for (a,aa),(b,bb),(c,cc) in combinations(L,3):
        d=det(a,b,c)
        if d==0:continue
        xx=det((aa,a[1],a[2]),(bb,b[1],b[2]),(cc,c[1],c[2]))/d
        yy=det((a[0],aa,a[2]),(b[0],bb,b[2]),(c[0],cc,c[2]))/d
        alp=det((a[0],a[1],aa),(b[0],b[1],bb),(c[0],c[1],cc))/d
        if F(0)<=xx<=1 and F(0)<=yy<=1 and F(0)<=alp<=F(1,4):out.add(alp)
    return sorted(out)

def predicted(a):
    assert F(0)<=a<=F(1,4)
    return F(1,3)-16*a*a+48*max(F(0),a-F(1,6))**2

def verify():
    knots=breakpoints()
    tested=0
    for lo,hi in zip(knots,knots[1:]):
        assert lo<hi
        for q in (F(1,4),F(1,2),F(3,4)):
            a=lo+(hi-lo)*q
            got=exact(a)
            want=predicted(a)
            assert got==want,(a,got,want)
            tested+=1
    for a in knots:
        assert exact(a)==predicted(a),(a,exact(a),predicted(a))
    print('CERTIFIED_POLYNOMIAL_INTERVALS',len(knots)-1,
          'EXACT_INTERIOR_VALUES',tested,'BOUNDARY_VALUES',len(knots))
    print('KNOTS',','.join(str(x) for x in knots))
    print('VALUE_ALPHA_0',exact(F(0)),'VALUE_ALPHA_1_6',exact(F(1,6)),'VALUE_ALPHA_1_4',exact(F(1,4)))
    print('VERIFY_OK')

if __name__=='__main__':verify()
