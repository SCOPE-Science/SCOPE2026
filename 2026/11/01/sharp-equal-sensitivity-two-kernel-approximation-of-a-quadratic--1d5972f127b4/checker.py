#!/usr/bin/env python3
"""Exact polynomial certificate for the equal-radius Bergman two-kernel problem.

Requirements: Python 3 and SymPy >= 1.12 (see requirements.txt).
All algebraic identities and root counts below are exact over the rationals.
Numerical values printed at the end are supplementary only.
"""
import sympy as s

t, c, u = s.symbols('t c u')
q = 1 - 2*t*c + t*t
P = (s.chebyshevt(2,c) - 2*t*s.chebyshevt(3,c)
     + t*t*s.chebyshevt(4,c))
raw = 2*t*t*(1-t)**2*(q*q - (1-t)**2*P)/(q*q - (1-t)**4)
F = s.cancel(raw)
A, B = s.fraction(F)
Q = (4*t**4-8*t**3+4*t**2)*c**3 + (4*t**4-12*t**3+12*t**2-4*t)*c**2 + (-4*t**3+7*t**2-6*t+1)*c + t**3+t**2-t+1
assert s.cancel(F - t*(1-t)**2*Q/(t*t-t+1-c*t)) == 0
# Independent 2-by-2 kernel-Gram calculation using e^{i theta}=u.
A0 = (1-t)**(-2)
B0 = (1-t/u)**(-2)
BC = (1-t*u)**(-2)
Fgram = t*t*(2*A0 - B0*u*u - BC/u**2)/(A0**2-B0*BC)
assert s.cancel(Fgram - F.subs(c,(u+1/u)/2)) == 0

D_c = s.factor(s.diff(A,c)*B-A*s.diff(B,c))
D_t = s.factor(s.diff(A,t)*B-A*s.diff(B,t))
U = s.cancel(D_c/(t*(t-1)**4))
V = s.cancel(D_t/(t-1))
assert s.factor(D_c-t*(t-1)**4*U)==0
assert s.factor(D_t-(t-1)*V)==0
p4 = 5*t**4-9*t**3+9*t*t-5*t+1
p3 = 2*t**3-2*t*t+2*t-1
p2 = 2*t*t-1
pout = 4*t*t-4*t-1
res = s.resultant(U,V,c)
assert s.expand(res + 4096*t**15*p2*pout*p3**4*p4)==0

# Exact elimination certificates (Groebner reduction over Q).
g4=s.groebner([U,V,p4],c,t,order='lex',domain=s.QQ)
g3=s.groebner([U,V,p3],c,t,order='lex',domain=s.QQ)
g2=s.groebner([U,V,p2],c,t,order='lex',domain=s.QQ)
h4=(15*t**3-17*t*t+14*t-4)/2
h3=2*t*t-t+1
assert s.expand(g4.reduce(c-h4)[1])==0
assert s.expand(g3.reduce((c-h3)**2)[1])==0
assert s.expand(g2.reduce(c-3*t/2)[1])==0
assert s.rem(s.together(U.subs(c,h4)),p4,t)==0
assert s.rem(s.together(V.subs(c,h4)),p4,t)==0
assert s.rem(s.together(h3*h3-t*t-1),p3,t)==0

# Exact real-root isolation by Sturm counts, plus rational sign brackets.
assert s.Poly(p4,t).count_roots(0,1)==2
assert s.Poly(p3,t).count_roots(0,1)==1
assert s.Poly(p2,t).count_roots(0,1)==1
assert s.Poly(pout,t).count_roots(0,1)==0
lo0,hi0=s.Rational(39078,100000),s.Rational(39079,100000)
lo1,hi1=s.Rational(67924,100000),s.Rational(67926,100000)
assert p4.subs(t,lo0)*p4.subs(t,hi0)<0
assert p4.subs(t,lo1)*p4.subs(t,hi1)<0
assert -1<h4.subs(t,lo0)<h4.subs(t,hi0)<1
assert h4.subs(t,lo1)>1
# h4 is strictly increasing since 45t^2-34t+14 has negative discriminant.
assert 34**2-4*45*14<0
assert p3.subs(t,s.Rational(1,2))<0<p3.subs(t,1)
assert s.discriminant(p3,t)<0
assert h3.subs(t,s.Rational(1,2))==1
assert s.simplify(F.subs(c,1)-t*(1-t)**2*(8*t*t-7*t+2))==0
assert s.simplify(F.subs(c,-1)-t*t*(1-t*t)**2/(1+t*t))==0
# Boundary extrema are < 1/8, while the rational interior test exceeds 1/8.
rfirst=(4-s.sqrt(6))/10
rsecond=(4+s.sqrt(6))/10
fplus=t*(1-t)**2*(8*t*t-7*t+2)
assert s.expand(s.diff(fplus,t)-2*(t-1)*(2*t-1)*(10*t*t-8*t+1))==0
assert s.simplify(fplus.subs(t,rfirst)-(1179+144*s.sqrt(6))/12500)==0
assert s.simplify(fplus.subs(t,rsecond)-(1179-144*s.sqrt(6))/12500)==0
assert s.simplify(fplus.subs(t,s.Rational(1,2))-s.Rational(1,16))==0
assert (1179+144*s.Rational(5,2))/12500 < s.Rational(1,8)
y=s.symbols('y')
fminus=y*(1-y)**2/(1+y)
y_star=(s.sqrt(17)-3)/4
assert s.cancel(s.diff(fminus,y)-(y-1)*(2*y*y+3*y-1)/(y+1)**2)==0
assert s.simplify(fminus.subs(y,y_star)-(71-17*s.sqrt(17))/8)==0
assert 17**3>70**2
assert s.simplify(F.subs({t:s.Rational(2,5),c:-s.Rational(1,8)})-s.Rational(1967,12500))==0
assert s.Rational(1967,12500)>s.Rational(1,8)

root=s.nroots(p4,n=40,maxsteps=100)[0]
# Sorting in nroots is not a theorem; use a bracket to select the isolated root.
root=next(z for z in s.nroots(p4,n=40,maxsteps=100) if abs(s.im(z))<s.Rational(1,10**20) and lo0<s.re(z)<hi0)
cc=h4.subs(t,root)
value=F.subs({t:root,c:cc})
assert abs(complex(root).real-0.3907807203191816)<1e-12
assert abs(complex(cc).real+0.11499664218141443)<1e-12
assert abs(complex(value).real-0.15741816657239726)<1e-12
print('All exact identities, elimination, root counts, boundary comparisons and numerical checks passed.')
print('t*=',s.N(root,25))
print('cos(theta*)=',s.N(cc,25))
print('squared projection=',s.N(value,25))
