import math
from scipy.integrate import quad
from scipy.special import gamma

def predicted(a):
 d=len(a);A=math.sqrt(sum(x*x for x in a))
 return 2**(1-d)*A**(d+1)*gamma((d+1)/2)/(math.pi**((d-1)/2)*math.factorial(2*d-2)*math.prod(a)**3*sum(1/x for x in a))

def exact2(a,eps):
 p,q=a; ell=2*math.hypot(*a)-eps
 lo=math.acos(min(1,2*p/ell));hi=math.asin(min(1,2*q/ell))
 def f(theta):
  x=math.cos(theta);y=math.sin(theta)
  h=max(0,2*p-ell*x);v=max(0,2*q-ell*y)
  return x*v+y*h
 return quad(f,lo,hi,epsabs=1e-14)[0]/(2*(p+q))

def exact3(a,eps):
 p,q,r=a; A=math.sqrt(sum(t*t for t in a)); ell=2*A-eps
 b=[2*t/ell for t in a]
 xl=math.sqrt(max(0,1-b[1]**2-b[2]**2));xh=min(1,b[0])
 def f(x):
  yl=math.sqrt(max(0,1-x*x-b[2]**2));yh=min(b[1],math.sqrt(max(0,1-x*x)))
  if yh<=yl:return 0
  def g(y):
   z=math.sqrt(max(0,1-x*x-y*y))
   ts=[max(0,2*t-ell*u) for t,u in zip(a,[x,y,z])]
   return (x*ts[1]*ts[2]+y*ts[0]*ts[2]+z*ts[0]*ts[1])/z
  return quad(g,yl,yh,epsabs=1e-13,epsrel=1e-10)[0]
 numerator=(2/math.pi)*quad(f,xl,xh,epsabs=1e-12,epsrel=1e-10)[0]
 denominator=2*(p*q+p*r+q*r)
 return numerator/denominator

for a in [(1.,1.),(1.,2.),(1.,1.,1.),(1.,2.,3.)]:
 C=predicted(a);print('A',a,'predicted',C)
 for eps in [0.2,0.1,0.05,0.02]:
  f=(exact2 if len(a)==2 else exact3)(a,eps)
  print(eps,'tail',f,'ratio',f/(eps**(2*len(a)-2)*C))
