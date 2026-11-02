"""Numerical independent cross-checks for the reflected Gaussian plume inversion.
Requires mpmath. Finite checks do not prove universal uniqueness.
"""
from mpmath import mp
mp.dps=70

def L(z,A,s,t):
    H=t/(2*s)
    return mp.log(2*A)-s*(z*z+H*H)+mp.log(mp.cosh(t*z))
def dd(vals, us):
    return ((vals[2]-vals[1])/(us[2]-us[1])-(vals[1]-vals[0])/(us[1]-us[0]))/(us[2]-us[0])
def F(t, zs):
    return dd([mp.log(mp.cosh(t*z)) for z in zs],[z*z for z in zs])

def inv(zs,ys):
    us=[z*z for z in zs]
    observed=dd(ys,us)
    if observed>0: return None
    lo=mp.mpf('0'); hi=mp.mpf('1')
    while F(hi,zs)>observed:hi*=2
    for _ in range(300):
        mid=(lo+hi)/2
        if F(mid,zs)>observed:lo=mid
        else:hi=mid
    t=(lo+hi)/2
    s=(mp.log(mp.cosh(t*zs[1]))-mp.log(mp.cosh(t*zs[0]))-(ys[1]-ys[0]))/(us[1]-us[0])
    a=ys[0]+s*us[0]-mp.log(mp.cosh(t*zs[0]))
    if s<=0:return None
    H=t/(2*s); A=mp.exp(a+s*H**2)/2
    return (A,(2*s)**(-mp.mpf('0.5')),H,t,s)
for zs in ((mp.mpf(0),mp.mpf(1),mp.mpf(2)),(mp.mpf('0.3'),mp.mpf(2),mp.mpf('4.5'))):
 for A,s,t in [(mp.mpf(3),mp.mpf(1)/8,mp.mpf(1)/4),(mp.mpf('0.34'),mp.mpf('0.2'),mp.mpf('1.25'))]:
  ys=[L(z,A,s,t) for z in zs]
  got=inv(zs,ys)
  print('zs',list(map(str,zs)),'target',float(A),float(s),float(t),'obs_div_diff',mp.nstr(dd(ys,[z*z for z in zs]),22))
  print('inverse',*[mp.nstr(v,21) for v in got])
  assert abs((got[0]-A)/A)<mp.mpf('1e-50')
  assert abs(got[3]-t)<mp.mpf('1e-50')
for t in [mp.mpf('0.04'),mp.mpf('0.02'),mp.mpf('0.01'),mp.mpf('0.005')]:
 zs=[mp.mpf('0.1'),mp.mpf('1.3'),mp.mpf('2.4')];v=F(t,zs)
 print('t',t,'F',mp.nstr(v,30),'F/t^4',mp.nstr(v/t**4,30),'relative quartic residual',mp.nstr((v+t**4/12)/t**6,18))
assert all(F(mp.mpf('0.1')*i,[mp.mpf('0'),mp.mpf('1'),mp.mpf('3')])>F(mp.mpf('0.1')*(i+1),[mp.mpf('0'),mp.mpf('1'),mp.mpf('3')]) for i in range(1,50))
print('TESTS PASS')
