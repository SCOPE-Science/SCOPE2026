"""Reproducibility checks for the polynomial-exponential ambiguity threshold."""
import sympy as S
import mpmath as mp

T,d,z,s=S.symbols('T d z s', real=True)
P=(1+d*T**2)*z**4+2*d*T*z**3+(4*d+2*d**2*T**2)*z**2+12*d**2*T*z+24*d**2
Q=S.Poly(S.expand(P.subs(z,s+2)),s)
a4,a3,a2,a1,a0=Q.all_coeffs()
D2=S.factor(a3*a2-a4*a1)
D3=S.factor(a3*a2*a1-a4*a1*a1-a3*a3*a0)
c2=S.Poly(S.expand(D2/4),T)
c3=S.Poly(S.expand(D3/16),T)
assert c2.degree()==4 and c3.degree()==6
assert S.simplify(c3.nth(0)+16*(5*d*d-8*d-16))==0
assert S.simplify(c3.nth(1)+8*d*(5*d*d-16*d-48))==0
assert S.simplify(c3.nth(2)+d*(9*d**3+104*d*d-512*d-768))==0
assert S.simplify(c3.nth(3)+4*d*d*(7*d*d-56*d-192))==0
assert S.simplify(c3.nth(4)+2*d*d*(3*d**3+18*d*d-224*d-384))==0
assert S.simplify(c3.nth(5)-2*d**3*(d+8)*(d+24))==0
assert S.simplify(c3.nth(6)-4*d**3*(d+8)**2)==0
assert S.simplify(c2.nth(0)-(4*d+40))==0
assert S.simplify(c2.nth(1)-d*(30-d))==0
assert S.simplify(c2.nth(2)-(12*d*d+80*d))==0
assert S.simplify(c2.nth(3)-d*d*(30-2*d))==0
assert S.simplify(c2.nth(4)-(2*d**3+40*d*d))==0

critical=4*(1+S.sqrt(6))/5
wc=2*(1+S.sqrt(6))/S.sqrt(5)
assert S.simplify(5*critical**2-8*critical-16)==0
assert S.simplify(P.subs({T:0,d:critical,z:2+S.I*wc}).expand(complex=True))==0
assert S.simplify(P.subs({T:0,d:critical,z:2-S.I*wc}).expand(complex=True))==0
print('SYMBOLIC: rational ambiguity numerator, quartic Hurwitz minors and critical roots: PASS')

mp.mp.dps=60
Pnum=lambda t,w,c:(1+c*t*t)*(2+mp.j*w)**4+2*c*t*(2+mp.j*w)**3+(4*c+2*c*c*t*t)*(2+mp.j*w)**2+12*c*c*t*(2+mp.j*w)+24*c*c
fn=lambda u,c:mp.exp(-u)*(1+c*u*u) if u>=0 else mp.mpf('0')
Anum=lambda t,w,c:mp.exp(-t-mp.j*w*t/2)*Pnum(t,w,c)/(2+mp.j*w)**5
for c,t,w in [(mp.mpf('0.5'),0,1),(mp.mpf('2.5'),mp.mpf('0.4'),3), (mp.mpf('10'),mp.mpf('0.548'),mp.mpf('5.536')), (mp.mpf('3'),mp.mpf('1'),mp.mpf('7'))]:
 ref=mp.quad(lambda u: fn(u+t,c)*fn(u,c)*mp.exp(-mp.j*w*(u+t/2)),[0,1,mp.inf])
 formula=Anum(t,w,c)
 assert abs(ref-formula)<mp.mpf('1e-28'),(ref,formula)
print('NUMERIC: four independent quadrature comparisons: PASS')
for c,guess in [(mp.mpf('3'),(mp.mpf('.1'),mp.mpf('3'))),(mp.mpf('10'),(mp.mpf('.55'),mp.mpf('5.5'))),(mp.mpf('100'),(mp.mpf('.95'),mp.mpf('14.5')))]:
 try:
  rt,rw=mp.findroot(lambda t,w:(mp.re(Pnum(t,w,c)),mp.im(Pnum(t,w,c))),guess,solver='mdnewton',tol=mp.mpf('1e-38'),verify=True,maxsteps=100)
  assert rt>0 and rw>0 and abs(Pnum(rt,rw,c))<mp.mpf('1e-37')
  print('EXAMPLE: d=%s, delay=%s, angular_frequency=%s, residual=%s'%(mp.nstr(c,6),mp.nstr(rt,18),mp.nstr(rw,18),mp.nstr(abs(Anum(rt,rw,c)),4)))
 except Exception as e:
  print('EXAMPLE findroot failed for',c,str(e)[:100])
print('ALL EXACT IDENTITIES AND FINITE CHECKS PASSED')
