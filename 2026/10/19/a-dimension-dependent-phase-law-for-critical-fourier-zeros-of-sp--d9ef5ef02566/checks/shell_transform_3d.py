"""Independent normalization test: 3D shell Fourier integral versus Bessel formula.
Uses SciPy quadrature and special functions; finite numerical check only.
"""
import math
from scipy import integrate,special,optimize

def via_integral(q,x):
    return 4*math.pi*integrate.quad(
        lambda r:r*math.sin(x*r)/x,q,1.,epsabs=1e-12)[0]

def via_bessel(q,x):
    nu=1.5
    f=lambda t:t**nu*special.jv(nu,t)
    return (2*math.pi)**nu*(f(x)-f(q*x))/x**3

count=0
for q in (.13,.29,.56,.88):
 for x in (.3,1.5,3.2,7.2,19.4):
  a,b=via_integral(q,x),via_bessel(q,x)
  assert abs(a-b)<3e-11,(q,x,a,b)
  count+=1
for q in (.15,.4,.75):
 alpha=special.jn_zeros(0,6) # only used as an auxiliary check of Bessel functions
 # In 3D, J_{1/2} zeros are n*pi, and every shell zero lies between adjacent values.
 for n in (1,2,4,5):
  lo=n*math.pi;hi=(n+1)*math.pi
  f=lambda x:math.sin(x)-x*math.cos(x)
  x=optimize.brentq(lambda x:f(x)-f(q*x),lo,hi)
  assert abs(via_integral(q,x))<2e-11
  count+=1
print('DIRECT_INTEGRAL_CHECKS_PASSED',count)
