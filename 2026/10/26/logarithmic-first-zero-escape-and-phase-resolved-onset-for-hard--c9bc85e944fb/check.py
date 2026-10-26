import mpmath as mp
import math
mp.mp.dps=75

def F(L,t):
    L=mp.mpf(L);t=mp.mpf(t)
    return mp.sqrt(mp.pi)*mp.exp(-t*t/4)*mp.re(mp.erf(L+1j*t/2))

def Ftail(L,t):
    L=mp.mpf(L);t=mp.mpf(t)
    return mp.sqrt(mp.pi)*mp.exp(-t*t/4)*(1-mp.re(mp.erfc(L-1j*t/2)))

def scaled(L,y):
    L=mp.mpf(L); y=mp.mpf(y)
    t=2*L+(mp.log(L)+y)/L
    return L*mp.exp(L*L)*Ftail(L,t)

def approx(L,y):
    return mp.sqrt(mp.pi)*mp.exp(-y)-mp.cos(2*L*L+mp.log(L)+y+mp.pi/4)/mp.sqrt(2)

for L in [3,5,8,12]:
  lower=2*L+(mp.log(L)-2)/L
  upper=2*L+(mp.log(L)+10)/L
  print('L=',L,'F(lower)=',mp.nstr(Ftail(L,lower)*L*mp.exp(L*L),12))
  roots=[]
  step=mp.pi/(24*L)
  x=lower
  while x<upper:
    y=min(x+step,upper)
    a,b=Ftail(L,x),Ftail(L,y)
    if a*b<0:
      root=mp.findroot(lambda z:Ftail(L,z),(x,y),solver='anderson',verify=True)
      roots.append(root)
    x=y
  if roots:
    first=roots[0]
    param=L*(first-2*L)-mp.log(L)
    print('first_zero',mp.nstr(first,35),'scaled_shift',mp.nstr(param,25))
  else:print('no zeros found')
  for y in [-1,0,1,3,5]:
    err=abs(scaled(L,y)-approx(L,y))
    print('y',y,'limit_resid',mp.nstr(err,12))

for L,t in [(3,2.4),(4,8.5),(7,15.2)]:
  direct=2*mp.quad(lambda x:mp.exp(-x*x)*mp.cos(t*x),[0,L])
  print('quadrature',L,t,'absolute_residual',mp.nstr(abs(direct-Ftail(L,t)),10))

def bisect_root(f,a,b):
    x=mp.mpf(a);y=mp.mpf(b);fx=f(x)
    for i in range(170):
        z=(x+y)/2;fz=f(z)
        if fx*fz>0:x=z;fx=fz
        else:y=z
    return (x+y)/2

def first_from_grid(fun,lo=-2,hi=11,step=mp.mpf('0.025')):
    x=mp.mpf(lo);y=x+step
    while y<=hi:
        if fun(x)*fun(y)<0:return bisect_root(fun,x,y)
        x=y;y+=step
    raise RuntimeError('no root')

theta=mp.mpf('0')
ylim=first_from_grid(lambda y:mp.sqrt(mp.pi)*mp.exp(-y)-mp.cos(theta+y+mp.pi/4)/mp.sqrt(2))
print('generic_phase_theta',mp.nstr(theta,15),'limit_first_y',mp.nstr(ylim,25))
for n in [5,12,30,80]:
    ell=mp.findroot(lambda z:2*z*z+mp.log(z)-2*mp.pi*n, mp.sqrt(mp.pi*n))
    root=first_from_grid(lambda y:scaled(ell,y))
    print('phase_locked_index',n,'L',mp.nstr(ell,16),'y_first',mp.nstr(root,16),'difference',mp.nstr(root-ylim,8))
print('exceptional_theta',mp.nstr((-mp.log(2*mp.sqrt(mp.pi)))%(2*mp.pi),25),'double_limit_y',mp.nstr(mp.log(2*mp.sqrt(mp.pi)),25))
