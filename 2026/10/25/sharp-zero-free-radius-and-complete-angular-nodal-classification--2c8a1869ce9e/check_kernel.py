"""Exact-symbolic and independently summed checks for radial harmonic Bergman kernels."""
import sympy as S
import mpmath as mp

u,t,d=S.symbols('u t d', positive=True, real=True)
D=1-2*u*t+u*u
A=-2*u*u*D+d*u*(1-u*u)*(t-u)
N=S.expand((d*(d+2)*(1-u*u)*D*D+4*(d+1)*A*D+4*u*(S.diff(A,u)*D-(d/2+1)*A*S.diff(D,u))))
P=S.expand(N)
expected=-(d*d*u**6-3*d*d*u**4+3*d*d*u**2-d*d+24*d*t*u**5-24*d*t*u**3-10*d*u**6-6*d*u**4+18*d*u**2-2*d+96*t*t*u**4-96*t*u**5-96*t*u**3+24*u**6+48*u**4+24*u**2)
assert S.expand(P-expected)==0
v=S.symbols('v', nonnegative=True)
H=d*(d+2)-12*(d+2)*v*v-48*v**3
assert S.cancel(N.subs(t,-1)- (1-u*u)**3*H.subs(v,u/(1-u)))==0
assert S.expand(S.diff(N,t,2)+192*u**4)==0
assert S.expand(N.subs(u,1)+96*(t-1)**2)==0

mp.mp.dps=55
for di in [3,4,5,8]:
  a=mp.mpf(di)/2
  for uu,tt in [(mp.mpf('0.1'),mp.mpf('-0.8')),(mp.mpf('0.4'),mp.mpf('0.2')),(mp.mpf('0.58'),mp.mpf('-0.9'))]:
    num=mp.mpf(str(N.subs({d:di,u:S.Rational(str(uu)),t:S.Rational(str(tt))})))
    den=di*(di+2)*(1-2*uu*tt+uu*uu)**(a+2)
    closed=num/den
    total=mp.mpf(0)
    for n in range(150):
      hn=(2*n+di-2)*mp.factorial(n+di-3)/(mp.factorial(n)*mp.factorial(di-2))
      ultrasph=mp.gegenbauer(n,(di-2)/2,tt)/mp.gegenbauer(n,(di-2)/2,1)
      moment=(n+a)*(n+a+1)/(a*(a+1))
      total+=moment*hn*uu**n*ultrasph
    assert abs(total-closed)<mp.mpf('1e-24'),(di,uu,tt,total,closed)
    print('d=',di,'u=',uu,'t=',tt,'absolute_error=',mp.nstr(abs(total-closed),4))
for di in [3,4,5,8,12,32,128]:
    root=mp.findroot(lambda v:48*v**3+12*(di+2)*v**2-di*(di+2),(mp.mpf('0.05'),mp.sqrt(di/12)))
    ucrit=root/(1+root)
    assert 0<ucrit<1
    print('dimension',di,'sharp product radius',mp.nstr(ucrit,24),'residual',mp.nstr(abs(H.subs({d:di,v:S.Rational(str(root))}).evalf(40)),4))
print('SYMBOLIC_AND_SPECTRAL_CHECKS_PASS')
