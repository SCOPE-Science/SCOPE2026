"""Reproducible computations for an asymmetric variable-power copula."""
import math
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 70

def cdf(u,v,s,a,b):
    if u == 0 or v == 0: return mp.mpf('0')
    return mp.exp((1+a*(v**(-s)-1))*mp.log(u) + (1+b*(u**(-s)-1))*mp.log(v))

def density_direct(u,v,s,a,b):
    U,V=u**(-s),v**(-s)
    P=1+a*(V-1)+s*b*U*(-mp.log(v))
    Q=1+b*(U-1)+s*a*V*(-mp.log(u))
    return cdf(u,v,s,a,b)/(u*v)*(P*Q-s*(a*V+b*U))

def tail_ul(t,s,a,b):
    # Positive opposite-corner probability divided by t
    return 1-cdf(t,1-t,s,a,b)/t

def tail_lr(t,s,a,b):
    return 1-cdf(1-t,t,s,a,b)/t

def p_ur(t,s,a,b):
    return 2*t-1+cdf(1-t,1-t,s,a,b)

samples=[(1,mp.mpf('0.7'),mp.mpf('0.3')),
         (1,mp.mpf('0.2'),mp.mpf('0.7')),
         (mp.mpf('0.5'),mp.mpf('0.4'),mp.mpf('0.6')),
         (mp.mpf('0.5'),1,1),
         (1,mp.mpf('0'),mp.mpf('1')),
         (1,mp.mpf('0.5'),mp.mpf('0.5'))]
for s,a,b in samples:
    assert s*(a+b)<=1
    for u in map(mp.mpf,['0.005','0.05','0.33','0.65','0.98']):
      for v in map(mp.mpf,['0.01','0.07','0.39','0.75','0.95']):
        c=density_direct(u,v,s,a,b)
        assert c>=0, (s,a,b,u,v,c)
        with mp.workdps(45):
          h=mp.mpf('1e-10')
          c_fd=(cdf(u+h,v+h,s,a,b)-cdf(u+h,v-h,s,a,b)-cdf(u-h,v+h,s,a,b)+cdf(u-h,v-h,s,a,b))/(4*h*h)
        assert abs(c-c_fd)<mp.mpf('1e-12'),(s,a,b,u,v,c,c_fd)
for s,a,b in samples:
    t=mp.mpf('1e-20')
    target_ul=1-mp.exp(-b) if s==1 else mp.mpf('0')
    target_lr=1-mp.exp(-a) if s==1 else mp.mpf('0')
    err_ul=abs(tail_ul(t,s,a,b)-target_ul)
    err_lr=abs(tail_lr(t,s,a,b)-target_lr)
    assert err_ul<mp.mpf('2e-8') and err_lr<mp.mpf('2e-8'),(s,a,b,err_ul,err_lr)
    if abs(s*(a+b)-1)<mp.mpf('1e-30'):
      est=p_ur(mp.mpf('1e-12'),s,a,b)/mp.mpf('1e-36')
      assert abs(est-(1-s/2))<mp.mpf('1e-9'),(s,a,b,est)
    else:
      est=p_ur(mp.mpf('1e-12'),s,a,b)/mp.mpf('1e-24')
      assert abs(est-(1-s*(a+b)))<mp.mpf('1e-9'),(s,a,b,est)
# Density negative near upper-right if coefficient sum is outside the simplex.
s,a,b=mp.mpf('1'),mp.mpf('0.72'),mp.mpf('0.6')
assert density_direct(mp.mpf('0.99999'),mp.mpf('0.99999'),s,a,b)<0
# Same diagonal for asymmetrically allocated coefficients.
for u in map(mp.mpf,['0.05','0.25','0.7','0.99']):
    assert abs(cdf(u,u,1,mp.mpf('0.1'),mp.mpf('0.9'))-cdf(u,u,1,mp.mpf('0.5'),mp.mpf('0.5')))<mp.mpf('1e-55')
print('PASS: 150 density/central-difference checks, 6 opposite-tail regimes, 6 upper-right asymptotic checks, inadmissibility witness, diagonal degeneracy.')
for s,a,b in samples[:3]:
 print('s,a,b =',*[mp.nstr(x,10) for x in (s,a,b)],'tails UL/LR =',*[mp.nstr(x,12) for x in (tail_ul(mp.mpf('1e-20'),s,a,b),tail_lr(mp.mpf('1e-20'),s,a,b))])
