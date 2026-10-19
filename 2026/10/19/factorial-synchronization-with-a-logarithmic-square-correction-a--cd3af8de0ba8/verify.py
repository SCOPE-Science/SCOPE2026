"""Exact and numerical checks for critical diffusive logistic synchronization."""
from fractions import Fraction
from math import log, lgamma, exp
import sympy as sp

x,y,u,v,e=sp.symbols('x y u v e', real=True)
X=x*(1-x)+e*(y-x)
Y=y*(1-y)+e*(x-y)
assert sp.simplify(((X+Y)/2-(u-u**2-v**2)).subs({x:u+v,y:u-v}))==0
assert sp.simplify(((X-Y)/2-(1-2*e-2*u)*v).subs({x:u+v,y:u-v}))==0
J=sp.Matrix([X,Y]).jacobian([x,y]).subs({x:0,y:0})
assert sp.simplify(J.det()-(1-2*e))==0
assert sp.simplify(J.trace()-(2-2*e))==0

for a,b,ee in [(Fraction(1,5),Fraction(3,10),Fraction(0)),
               (Fraction(1,5),Fraction(3,10),Fraction(1,10)),
               (Fraction(1,30),Fraction(2,5),Fraction(9,20)),
               (Fraction(1,30),Fraction(2,5),Fraction(1,2))]:
 xx,yy=a,b
 for n in range(5):
  uu=(xx+yy)/2; vv=(xx-yy)/2
  xx2=xx*(1-xx)+ee*(yy-xx)
  yy2=yy*(1-yy)+ee*(xx-yy)
  assert 0<xx2<Fraction(1,2) and 0<yy2<Fraction(1,2)
  assert (xx2+yy2)/2==uu-uu**2-vv**2
  assert (xx2-yy2)/2==(1-2*ee-2*uu)*vv
  xx,yy=xx2,yy2

def numerical(x0,y0,eps,nmax=500000):
 w=2/(x0+y0); lnd=log(abs((x0-y0)/2)); lam=1-2*eps
 results={}
 for n in range(nmax+1):
  if n in (1000,10000,100000,250000,500000):
   c=(w-n-log(n)-(log(n)-0.5)/n)/(1+1/n)
   if lam==0:
    q=lnd+lgamma(n)-n*log(2)+0.5*log(n)**2+c*log(n)
   else:
    q=lnd-n*log(lam)+2/lam*log(n)
   results[n]=(c,q)
  if n==nmax:break
  t2=exp(2*(lnd+log(w))) if lnd+log(w)>-350 else 0.0
  s=1+t2
  fac=lam-2/w
  assert fac!=0
  lnd+=log(abs(fac))
  w+=s/(1-s/w)
 return results

for e0 in (0.0,0.1,0.45,0.5):
 res=numerical(0.2,0.3,e0)
 a=res[250000][1];b=res[500000][1]
 print('eps',e0,'C/Q:',[(n,round(c,8),round(q,8)) for n,(c,q) in res.items()])
 assert abs(a-b)<0.004, (e0,a,b)
print('VERIFY_OK')
