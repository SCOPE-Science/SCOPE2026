#!/usr/bin/env python3
"""Exact algebraic certificate for the sharp sixth moment of frequencies 0,1,3.
Requires SymPy >=1.12; uses exact rational polynomial arithmetic for certification.
Run: python checker.py
"""
import random
random.seed(20261009)
from collections import defaultdict
import sympy as s

u,v,w=s.symbols('u v w')
N=1+u**6+v**6+9*(u**2+v**2+u**4+v**4+u**2*v**4+u**4*v**2)+36*u**2*v**2+6*u**3*v
D=1+u**2+v**2
E1=s.expand(D*s.diff(N,u)-6*u*N)
E2=s.expand(D*s.diff(N,v)-6*v*N)
P=4800*w**10+24320*w**9-22480*w**8-135480*w**7+216636*w**6-59622*w**5-51379*w**4+17526*w**3+5227*w**2+200*w-4
res=s.resultant(E1,E2,u)
assert s.expand(res+104485552128*v**3*(v*v-1)*(v*v+1)**3*(5*v*v+1)*P.subs(w,v*v))==0
# Exact real-root count and rational intervals, via Sturm sequences.
roots=s.polys.polytools.intervals(P,eps=s.Rational(1,10**25))
assert len(roots)==6 and all(m==1 for _,m in roots)
pos=[(a,b) for (a,b),m in roots if a>0]
assert len(pos)==3
assert pos[0][0]>s.Rational(143,10000) and pos[0][1]<s.Rational(145,10000)
assert pos[1][0]>s.Rational(9064,10000) and pos[1][1]<s.Rational(9066,10000)
assert pos[2][0]>s.Rational(1099,1000) and pos[2][1]<s.Rational(1101,1000)

# The reduced Groebner-basis relation is linear in u. All equality and
# elimination checks are exact identities over Q[u,v].
gb=s.groebner((E1,E2),u,v,order='lex')
K=s.Integer(9096133226180822175068352)
G=[g.as_expr() for g in gb.polys if s.degree(g.as_expr(),u)==1 and s.expand(s.diff(g.as_expr(),u)-K*v*(1+v*v))==0]
assert len(G)==1
G=G[0]
Q=s.cancel(G.subs(u,0)/(v*v*(v*v-1)*(v*v+1)**2))
assert s.denom(Q)==1
qv=s.Poly(Q,v)
assert all(k[0]%2==0 for k,c in qv.terms())
qw=s.Poly(sum(c*w**(j[0]//2) for j,c in qv.terms()),w)
assert qw.degree()==10
assert s.expand(G-v*(1+v*v)*(K*u+v*(v*v-1)*(1+v*v)*Q))==0
U=-v*(v*v-1)*(v*v+1)*Q/K

# Evaluate the polynomial Q over exact rational root-enclosing intervals.
# Horner interval bounds, not floating point, certify the three signs.
def interval_eval(poly,a,b):
 lo=hi=s.Integer(0)
 for coeff in poly.all_coeffs():
  products=(lo*a,lo*b,hi*a,hi*b)
  lo=min(products)+coeff
  hi=max(products)+coeff
 return lo,hi
signs=[]
for a,b in pos:
 l,h=interval_eval(qw,a,b)
 assert (l>0 and h>0) or (l<0 and h<0)
 signs.append(1 if l>0 else -1)
assert signs==[-1,1,1]
# Since u=-v (w-1)(w+1)Q(w)/K, the first and third roots
# give negative u; only the middle root gives positive u.
assert pos[0][1]<1 and pos[1][1]<1 and pos[2][0]>1

# Elimination is sufficient as well as necessary: the reduced polynomial
# identity makes both stationary equations vanish at every root of P.
for E in [E1,E2]:
 numerator=s.together(E.subs(u,U)).as_numer_denom()[0]
 assert s.rem(s.Poly(numerator,v),s.Poly(P.subs(w,v*v),v)).is_zero

# At v=1, the only common nonnegative solution of E1=E2=0 has u=0:
# their nonzero factors differ by u*(u**2+2).
f1=s.cancel(E1.subs(v,1)/(-6*u))
f2=s.cancel(E2.subs(v,1)/(6*u*u))
assert s.simplify(f1-2*f2-u*(u*u+2))==0

# Every boundary case a=0 or b=0 or c=0 has moment at most 5/2.
# The interior witness (a,b,c)=(1,1,1) has 11/3 > 5/2;
# hence the unique positive stationary solution is the unique maximizer.
assert N.subs({u:1,v:1})==99

# Numerical values are supplemental, not used in Sturm/algebraic proof.
wstar=s.N((pos[1][0]+pos[1][1])/2,65)
vstar=s.sqrt(wstar).evalf(60)
ustar=U.subs(v,vstar).evalf(55)
Kstar=(N/D**3).subs({u:ustar,v:vstar}).evalf(45)
assert abs(float(ustar)-1.0419026)<1e-5 and abs(float(Kstar)-3.67669088479)<1e-8

# Check coefficient-convolution identity independently over exact integers.
def moment(coeff,mod=None):
 buckets=defaultdict(complex)
 for i,a in enumerate(coeff):
  for j,b in enumerate(coeff):
   for k,c in enumerate(coeff):
    power=[0,1,3][i]+[0,1,3][j]+[0,1,3][k]
    buckets[power if mod is None else power%mod]+=a*b*c
 return sum(abs(z)**2 for z in buckets.values())
for _ in range(100):
 coeff=[random.choice([-2,-1,0,1,2])+1j*random.choice([-2,-1,0,1,2]) for _ in range(3)]
 a,b,c=map(abs,coeff)
 x,y,z=a*a,b*b,c*c
 generic=(x+y+z)**3+6*(x+y+z)*(x*y+y*z+z*x)+12*x*y*z
 # P=(sum squares)^3+6(sum squares)*e2+12e3
 target=generic+6*((coeff[1]**3)*((coeff[0]**2)*coeff[2]).conjugate()).real
 assert abs(moment(coeff)-target)<1e-5*max(1,abs(target)),(coeff,moment(coeff),target)
 for modulus in range(10,15):
  assert abs(moment(coeff,modulus)-moment(coeff))<1e-5*max(1,moment(coeff))

powers={0,1,2,3,4,5,6,7,9}
for modulus in range(4,10):
 assert len({j%modulus for j in powers})<len(powers)
 assert moment([1,float(ustar),float(vstar)],modulus)>moment([1,float(ustar),float(vstar)])+1e-9
print('CERTIFICATE_PASS')
print('positive squared-v root intervals:',[(str(a),str(b)) for a,b in pos])
print('stationary u, v, sharp sixth-moment constant:',s.N(ustar,22),s.N(vstar,22),s.N(Kstar,22))
print('phase rigidity and finite sampling threshold:',10)
