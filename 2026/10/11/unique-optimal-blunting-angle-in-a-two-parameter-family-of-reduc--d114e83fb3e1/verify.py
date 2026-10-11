from fractions import Fraction as F
from functools import lru_cache
from math import factorial
from time import monotonic
S=10**40
class Iv:
 __slots__=('lo','hi')
 def __init__(self,x,y=None,raw=False):
  if isinstance(x,Iv):self.lo,self.hi=x.lo,x.hi;return
  if y is not None:
   if raw:self.lo,self.hi=x,y
   else:self.lo,self.hi=Iv(x).lo,Iv(y).hi
   assert self.lo<=self.hi
  elif isinstance(x,F):
   self.lo=x.numerator*S//x.denominator
   self.hi=-((-x.numerator*S)//x.denominator)
  elif isinstance(x,str):
   return self.__init__(F(x))
  else:
   self.lo=self.hi=int(x) if raw else int(x)*S
 def __add__(a,b):
  b=Iv(b);return Iv(a.lo+b.lo,a.hi+b.hi,True)
 __radd__=__add__
 def __neg__(a):return Iv(-a.hi,-a.lo,True)
 def __sub__(a,b):return a+-Iv(b)
 def __rsub__(a,b):return Iv(b)+-a
 def __mul__(a,b):
  b=Iv(b)
  v=(a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi);mn,mx=min(v),max(v)
  return Iv(mn//S,-((-mx)//S),True)
 __rmul__=__mul__
 def inv(a):
  assert a.lo*a.hi>0,(a.lo/S,a.hi/S)
  v=[(S*S)//n for n in (a.lo,a.hi)]
  u=[-((-S*S)//n) for n in (a.lo,a.hi)]
  return Iv(min(v),max(u),True)
 def __truediv__(a,b):return a*Iv(b).inv()
 def __rtruediv__(a,b):return Iv(b)*a.inv()
 def __pow__(a,k):
  assert k>=0 and isinstance(k,int)
  z=Iv(1)
  while k:
   if k&1:z=z*a
   a=a*a;k//=2
  return z
 def __repr__(a):return f'[{a.lo/S:.12g},{a.hi/S:.12g}]'

@lru_cache(maxsize=20000)
def scpoint(xlo,xhi):
 x=Iv(xlo,xhi,True)
 assert x.lo>=0 and x.hi<2*S
 x2=x*x
 pow_s=x;pow_c=Iv(1)
 sin=Iv(0);cos=Iv(0)
 for j in range(18):
  term_s=pow_s/factorial(2*j+1)
  term_c=pow_c/factorial(2*j)
  if j%2:
   sin=sin-term_s;cos=cos-term_c
  else:
   sin=sin+term_s;cos=cos+term_c
  pow_s=pow_s*x2;pow_c=pow_c*x2
 # next j=18 term is positive, so add [0, upper term]
 rems=pow_s/factorial(37);remc=pow_c/factorial(36)
 return Iv(sin.lo,sin.hi+max(0,rems.hi),True),Iv(cos.lo,cos.hi+max(0,remc.hi),True)

def sc(x):
 assert isinstance(x,Iv) and 0<=x.lo<=x.hi<2*S
 slo,_=scpoint(x.lo,x.lo);shi,_=scpoint(x.hi,x.hi)
 _,clo=scpoint(x.hi,x.hi);_,chi=scpoint(x.lo,x.lo)
 return Iv(min(slo.lo,shi.lo), max(slo.hi,shi.hi,S if x.hi>=F("1.5707963")*S else 0), True),Iv(clo.lo,chi.hi,True)

class Jet:
 __slots__=('v','d','dd')
 def __init__(self,v,d=0,dd=0):self.v,self.d,self.dd=Iv(v),Iv(d),Iv(dd)
 def __add__(a,b):
  b=jet(b);return Jet(a.v+b.v,a.d+b.d,a.dd+b.dd)
 __radd__=__add__
 def __neg__(a):return Jet(-a.v,-a.d,-a.dd)
 def __sub__(a,b):return a+-jet(b)
 def __rsub__(a,b):return jet(b)+-a
 def __mul__(a,b):
  b=jet(b);return Jet(a.v*b.v,a.d*b.v+a.v*b.d,a.dd*b.v+2*a.d*b.d+a.v*b.dd)
 __rmul__=__mul__
 def inv(a):
  i=a.v.inv();return Jet(i,-a.d*i*i,(2*a.d*a.d-a.v*a.dd)*i*i*i)
 def __truediv__(a,b):return a*jet(b).inv()
 def __rtruediv__(a,b):return jet(b)*a.inv()
 def __pow__(a,n):
  if n==0:return Jet(1)
  if n==1:return a
  if n<0:return (a**(-n)).inv()
  out=Jet(1)
  for _ in range(n):out=out*a
  return out

def jet(x):return x if isinstance(x,Jet) else Jet(x)

def data(iv):
 m=Jet(iv,1,0)
 s0,c0=sc(iv)
 s=Jet(s0,c0,-s0);c=Jet(c0,-s0,-c0)
 k=c*c/(2*s*s);q=2*s/(m+s*c)
 eb=(Jet(F(1,2))-k)/(1-q*c)
 I0=2*m-2*s*c
 I1=2*m*c-2*s-2*s*s*s
 I2=m*(s*s-F(1,4))+s*c*(1+2*s*s)/4
 C0=k*k*I0+m/2+s*c/2
 B=k*(2*I0+q*I1)
 C=I0+q*I1+q*q*I2
 E=B+2*C*eb
 beta=(s*s-c*c)/(s*(m-s*c))
 J1=3*m*c-3*s+s*s*s
 J2=m*(F(15,4)-3*s*s)+s*c*(2*s*s-15)/4
 FF=m+beta*J1+beta*beta*J2
 U=C0-B*B/(4*C) if C.v.hi<0 else None
 return {'FF':FF,'B':B,'C':C,'E':E,'eb':eb,'U':U}

def bounds(v,der,half):
 d=max(abs(der.lo),abs(der.hi))*half
 # half is rational F; using ceil scaled
 diff=(d.numerator+d.denominator-1)//d.denominator if isinstance(d,F) else d
 return v.lo-diff,v.hi+diff

def segments(start,end,N):
 start,end=F(start),F(end)
 for j in range(N):
  a=start+(end-start)*j/N;b=start+(end-start)*(j+1)/N
  yield a,b

def run(N1=235,N2=300,N3=401):
 t=monotonic()
 global_summary={}
 for block,st,en,num in [('low','0.785398','1.02',N1),('mid','1.02','1.17',N2),('high','1.17','1.570797',N3)]:
  lowE=10*S;lowB=10*S;maxCap=-10*S;maxF=-10*S;maxU=-10*S;maxD2=-10*S;maxC=-10*S
  for i,(a,b) in enumerate(segments(st,en,num)):
   mid=(a+b)/2;half=(b-a)/2
   d=data(Iv(F(a),F(b)));p=data(Iv(mid))
   _,Bup=bounds(p['B'].v,d['B'].d,half);Blow,_=bounds(p['B'].v,d['B'].d,half)
   Elow,_=bounds(p['E'].v,d['E'].d,half)
   _,capmax=bounds(p['eb'].v,d['eb'].d,half)
   lowB=min(lowB,Blow);lowE=min(lowE,Elow);maxCap=max(maxCap,capmax)
   if block!='high':
    _,fmax=bounds(p['FF'].v,d['FF'].d,half);maxF=max(maxF,fmax)
   if block=='mid':maxD2=max(maxD2,d['FF'].dd.hi)
   if block=='high':
    if d['C'].v.hi>=0:print('C FAIL',float(a),d['C'].v);return False
    _,cmax=bounds(p['C'].v,d['C'].d,half);maxC=max(maxC,cmax)
    _,umax=bounds(p['U'].v,d['U'].d,half);maxU=max(maxU,umax)
  print(block,'N',num,'sec',round(monotonic()-t,1),'min B/E',round(lowB/S,9),round(lowE/S,9),'maxCap',round(maxCap/S,9),'max F',round(maxF/S,9),'max U',round(maxU/S,9),'max Fdd',round(maxD2/S,9),'max C',round(maxC/S,9),flush=True)
  global_summary[block]={'Bmin':lowB,'Emin':lowE,'capmax':maxCap,'Fmax':maxF,'Umax':maxU,'Fddmax':maxD2,'Cmax':maxC}
 return global_summary
if __name__=='__main__':
 # All displayed tests are exact integer/rational inequalities. No random sampling.
 out=run(1000,3000,10000)
 assert out and out['low']['Bmin']>0 and out['low']['Emin']>0
 assert out['mid']['Bmin']>0 and out['mid']['Emin']>0
 assert out['low']['Fmax'] < F('0.7887')*S
 assert out['mid']['Fddmax']< F('-0.1303')*S
 assert out['high']['Cmax']<F('-0.01135')*S
 assert out['high']['Umax']<F('0.7887')*S
 assert max(out[k]['capmax'] for k in ('low','mid','high')) < F('0.81')*S
 def ev(z):return data(Iv(z))['FF']
 assert ev('1.02').d.lo>0 and ev('1.17').d.hi<0
 assert ev('1.0783169').d.lo>0 and ev('1.0783171').d.hi<0
 u=ev('1.07831698').v
 assert u.lo>F('0.78884378')*S
 # Concavity bounds the derivative between its values at bracket endpoints.
 l=ev('1.0783169').d;r=ev('1.0783171').d
 derivative_bound=max(abs(l.lo),abs(l.hi),abs(r.lo),abs(r.hi))
 bracket_width=F('1.0783171')-F('1.0783169')
 upper_gain=derivative_bound*bracket_width
 upper_gain=(upper_gain.numerator+upper_gain.denominator-1)//upper_gain.denominator
 assert u.hi+upper_gain<F('0.78884380')*S
 # Independent numerical check of the source boundary integral (not a proof).
 import math
 z=1.07831698; sn=math.sin(z);co=math.cos(z)
 k=co*co/(2*sn*sn);q=2*sn/(z+sn*co)
 eps=(0.5-k)/(1-q*co);alpha=k+eps;beta=q*eps
 n=8192;step=2*z/n;total=0.0
 for j in range(n):
  th=(j+0.5)*step
  rr=alpha-beta*math.cos(th-z)
  pp=alpha*(1-math.cos(th))-0.5*beta*(th*math.sin(th-z)+sn*math.sin(th))
  total+=rr*pp
 area_integral=total*step+z/2+math.sin(2*z)/4
 assert abs(area_integral-(u.lo/S+u.hi/S)/2)<3e-9
 print('VERIFY_OK')
