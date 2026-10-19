#!/usr/bin/env python3
"""Exact symbolic and finite independent checks for a degree-five harmonic sampling result."""
import itertools
from math import comb
import sympy as s

m, r, t = s.symbols('m r t', integer=True)
P = s.factor(s.gegenbauer(5, (m-3)/2, t)/s.gegenbauer(5, (m-3)/2, 1))
t_r = (m*r - 9)/(3*(m-3))
values = [s.factor(P.subs(t, t_r.subs(r,h))) for h in range(4)]
a = [s.factor(sum((-1)**(j-h)*s.binomial(j,h)*values[h] for h in range(j+1))) for j in range(4)]
eigen = [s.factor(s.expand_func(sum(a[j]*s.binomial(3-i,j-i)*s.binomial(m-j-i,3-j) for j in range(i,4)))) for i in range(4)]
P1 = m**7-12*m**6+1241*m**5-30837*m**4+272970*m**3-880875*m**2+131220*m+2755620
P2 = m**4-27*m**3+254*m**2-594*m-648
P3 = 5*m**3-47*m**2+648
want = [
 m*(m-27)**2*(m-6)**2*(m-4)*(m+3)/(162*(m-3)**4*(m-2)),
 m*P1/(486*(m-3)**5*(m-2)),
 10*m*(m-6)*(m+3)*P2/(81*(m-3)**5*(m-2)),
 10*m**2*(m+3)*P3/(81*(m-3)**5*(m-2))]
assert all(s.cancel(v-w)==0 for v,w in zip(eigen,want))
assert s.factor(P-t*((m+3)*(m+5)*t**4-10*(m+3)*t**2+15)/(m*(m-2)))==0
for poly,q in [(P1,13),(P2,7),(P3,11)]:
 assert all(int(poly.subs(m,k)) % q != 0 for k in range(q))

# Independently check the Johnson eigendecomposition using exact rational Gram matrices.
for mm in range(6,12):
 sets = list(itertools.combinations(range(mm),3))
 N=len(sets)
 vals=[s.Rational(v.subs(m,mm)) for v in values]
 K=s.Matrix(N,N,lambda i,j: vals[len(set(sets[i]).intersection(sets[j]))])
 actual={}
 for i in range(4):
  eig=s.Rational(eigen[i].subs(m,mm))
  actual[eig]=actual.get(eig,0)+comb(mm,i)-(comb(mm,i-1) if i else 0)
 # characteristic polynomial is equivalent to an exact eigenspectrum certificate.
 v=s.symbols('v')
 char=s.factor(K.charpoly(v).as_expr())
 expected=s.prod((v-ev)**mul for ev,mul in actual.items())
 assert s.factor(char-expected)==0
 print('exact finite Gram spectrum:',mm,N,'OK')

vals27=[s.Rational(v.subs(m,27)) for v in values]
assert vals27==[-s.Rational(1,512),s.Rational(0),s.Rational(21,512),s.Rational(1)]
assert [s.Rational(ev.subs(m,27)) for ev in eigen]==[0,s.Rational(855,256),s.Rational(455,256),s.Rational(225,256)]
assert 26*s.Rational(855,256)+324*s.Rational(455,256)+2574*s.Rational(225,256)==2925
assert 1+72*s.Rational(21,512)-comb(24,3)*s.Rational(1,512)==0

# On the standard-coordinate zero-sum hyperplane, harmonicity is checked from
# the tangent Laplacian; the vertex and triangle evaluations are independent checks.
k=s.symbols('k',integer=True)
q3=s.factor(k*(1-k/m)**3+(m-k)*(-k/m)**3)
q5=s.factor(k*(1-k/m)**5+(m-k)*(-k/m)**5)
r2=k*(m-k)/m
alpha=10*(m-1)/(m*(m+5))
H=s.factor(q5-alpha*r2*q3)
assert s.cancel(H-k*(k-m)*(2*k-m)*(12*k*k-12*k*m+m*m+5*m)/(m**3*(m+5)))==0
assert H.subs({m:27,k:3})==0
assert H.subs({m:27,k:1})==s.Rational(7475,13122)
print('symbolic four-sector identities, three modular exclusions, exceptional kernel and harmonic repair: OK')
