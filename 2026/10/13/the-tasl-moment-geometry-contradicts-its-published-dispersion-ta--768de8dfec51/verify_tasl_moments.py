"""Symbolic and independent quadrature checks for the TASL moment classification."""
import sympy as s
import mpmath as mp
A,t,x,u=s.symbols('A t x u',real=True)
pi=s.pi
c0=(98*pi**4-140*pi**2+630)/105
c2=(155*pi**6-98*pi**4+105*pi**2)/105
d2=(889*pi**8-310*pi**6+147*pi**4)/105
moms={0:s.Integer(1),2:pi**2/3,4:7*pi**4/15,6:31*pi**6/21,8:127*pi**8/15}
poly=s.expand(((1-A*x)**2+1)*((x**2-1)**2+2))
def expectation_power(k):
 return s.expand(sum(s.expand(poly*x**k).coeff(x,i)*moms.get(i,s.Integer(0)) for i in range(0,9) if i%2==0))
normal=expectation_power(0)
first=expectation_power(1)
second=expectation_power(2)
assert s.simplify(normal-(c0+c2*A*A))==0
assert s.simplify(first+2*c2*A)==0
assert s.simplify(second-(2*c2+d2*A*A))==0
mu=-2*c2*A/(c0+c2*A*A)
variance=(2*c2+d2*u)/(c0+c2*u)-4*c2*c2*u/(c0+c2*u)**2
Delta=d2*c0-2*c2*c2
expected_derivative=(c0*(Delta-4*c2*c2)+c2*u*(Delta+4*c2*c2))/(c0+c2*u)**3
assert s.simplify(s.diff(variance,u)-expected_derivative)==0
polyDelta=s.expand(32*t**2*(407*t**4-980*t**3+5558*t**2-1820*t+735)/3675)
polyGap=s.expand(4*t**2*(14257*t**4-6860*t**3-91238*t**2+23100*t-6615)/11025)
assert s.simplify(Delta-polyDelta.subs(t,pi*pi))==0
assert s.simplify(4*c2*c2-Delta-polyGap.subs(t,pi*pi))==0
# For t>=9: displayed grouping into positive cubic/quadratic and quartic/linear terms.
assert 407*9-980>0
assert 5558*9**2-1820*9+735>0
assert 14257*9**2-6860*9-91238>0
assert 23100*9-6615>0
mp.mp.dps=45
c0m=mp.mpf(str(s.N(c0,55)));c2m=mp.mpf(str(s.N(c2,55)));d2m=mp.mpf(str(s.N(d2,55)))
def moments(a):
 a=mp.mpf(str(a)); den=c0m+c2m*a*a
 mean=-2*c2m*a/den
 var=(2*c2m+d2m*a*a)/den-mean**2
 return mean,var
am=mp.sqrt(c0m/c2m)
delt=d2m*c0m-2*c2m*c2m
av=mp.sqrt(c0m*(4*c2m*c2m-delt)/(c2m*(delt+4*c2m*c2m)))
assert mp.mpf('.249')<am<mp.mpf('.251')
assert mp.mpf('.161')<av<mp.mpf('.164')
assert delt>0 and 4*c2m*c2m-delt>0
assert abs(moments(am)[0]+mp.sqrt(c2m/c0m))<mp.mpf('1e-40')
assert 26<moments(av)[1]<27
samples=[(-2,mp.mpf('.984593392007'),mp.mpf('56.645203975384')),
 (-1,mp.mpf('1.882192192199'),mp.mpf('52.938329930080')),
 (-.5,mp.mpf('3.199071061301'),mp.mpf('42.563544077327')),
 (.5,mp.mpf('-3.199071061301'),mp.mpf('42.563544077327')),
 (1,mp.mpf('-1.882192192199'),mp.mpf('52.938329930080')),
 (2,mp.mpf('-.984593392007'),mp.mpf('56.645203975384')),
 (3,mp.mpf('-.662062336273'),mp.mpf('57.397836247981')),
 (5,mp.mpf('-.399001049115'),mp.mpf('57.791873846003'))]
for alpha,mwant,vwant in samples:
 m,v=moments(alpha)
 assert abs(m-mwant)<mp.mpf('1e-9'),(alpha,m,mwant)
 assert abs(v-vwant)<mp.mpf('1e-9'),(alpha,v,vwant)
# Quadrature independently verifies the true density and moments.
def kernel(xx):
 return 1/(4*mp.cosh(xx/2)**2)
def quad(alpha,k):
 a=mp.mpf(str(alpha));den=c0m+c2m*a*a
 f=lambda xx:(xx**k)*(((1-a*xx)**2+1)*((xx**2-1)**2+2))*kernel(xx)/den
 return mp.quad(f,[-mp.inf,0,mp.inf])
for a in (-1,0,.5,2):
 m,v=moments(a)
 assert abs(quad(a,0)-1)<mp.mpf('1e-33')
 assert abs(quad(a,1)-m)<mp.mpf('1e-33')
 assert abs(quad(a,2)-(v+m*m))<mp.mpf('1e-32')
assert moments(-.5)[0]==-moments(.5)[0]
print('VERIFY_OK')
print('alpha_mean_peak',mp.nstr(am,18),'max_abs_mean',mp.nstr(mp.sqrt(c2m/c0m),18))
print('alpha_variance_min',mp.nstr(av,18),'variance_min',mp.nstr(moments(av)[1],18))
print('variance_large_parameter_limit',mp.nstr(d2m/c2m,18))
for a,m,v in samples:
 print('parameter',a,'mean',mp.nstr(moments(a)[0],16),'variance',mp.nstr(moments(a)[1],16))
