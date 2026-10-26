"""Exact algebra and finite numerical cross-checks for a spherical Legendre criterion."""
import sympy as s
import mpmath as mp
n,a=s.symbols('n a', positive=True)
num=(a*a+n*n)*(a*a+(n+4)**2)*(a*a+n*n+n+1)
den=(a*a+(n+3)**2)*(a*a+(n-1)**2)*(a*a+n*n+5*n+7)
assert s.simplify(num-den-3*(2*n+3)*(3*n*n+9*n-7-7*a*a))==0
mp.mp.dps=35
for av in (mp.mpf('0.1'),mp.mpf('1'),mp.mpf('2'),mp.mpf('5')):
 A=[(1+mp.exp(-mp.pi*av))/(1+av*av),(1-mp.exp(-mp.pi*av))/(4+av*av)]
 for k in range(16):
  A.append(A[k]*(av*av+k*k)/(av*av+(k+3)**2))
 for k in range(7):
  m=mp.quad(lambda t:mp.exp(-av*t)*mp.legendre(k,mp.cos(t))*mp.sin(t),[0,mp.pi])
  assert abs(m-A[k])<mp.mpf('1e-28'), (av,k,m,A[k])
 print('a=',av,'recurrence check passed')
print('all finite checks passed')
