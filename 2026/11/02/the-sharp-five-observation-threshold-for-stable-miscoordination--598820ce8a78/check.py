"""Reproduce symbolic identities and finite sample-size tests for the stated game."""
import math
from fractions import Fraction
import sympy as s

p, q = s.symbols('p q', real=True)

def tail(k, threshold):
    return s.expand(sum(s.binomial(k, j)*p**j*(1-p)**(k-j)
                        for j in range(threshold, k+1)))

def selected_count(k, u):
    # The four test payoffs below have no integer threshold ties.
    return next(j for j in range(k+1) if (u+1)*j > k)

regions = [
    (s.Rational(6, 5), [0, 1, 2*p-1, -3*p*p+5*p-1]),
    (s.Rational(5, 2), [0, 1, 2-p, -3*p*p+5*p-1]),
    (s.Integer(4), [0, 1, 2-p, p*p-3*p+3]),
]
checks = 0
for u, expected in regions:
    for k in range(1, 5):
        r = s.cancel((tail(k,selected_count(k,u))-p)/(p*(1-p)))
        assert s.simplify(r-expected[k-1]) == 0
        checks += 1

u=s.Rational(6,5)
assert [selected_count(k,u) for k in (2,5)] == [1,3]
w2=tail(2,1)
w5=tail(5,3)
h=-p+9*p*p-6*p**3
Q=(2*q-1)+(1-q)*h
assert s.factor(q*w2+(1-q)*w5-p) == s.factor(p*(1-p)*Q)
checks+=1
pm=(3-s.sqrt(7))/6
pp=(3+s.sqrt(7))/6
assert s.simplify(s.diff(h,p).subs(p,pm))==0
assert s.simplify(s.diff(h,p).subs(p,pp))==0
assert s.simplify(h.subs(p,pm)-(1-s.Rational(7,18)*s.sqrt(7)))==0
qstar=s.simplify((1-h.subs(p,pm))/(2-h.subs(p,pm)))
assert s.simplify(qstar-(343-126*s.sqrt(7))/19)==0
assert s.simplify(Q.subs(p,1)-1)==0
checks+=6

q0=s.Rational(101,200)
roots=sorted(float(s.re(z)) for z in s.nroots(Q.subs(q,q0)) if abs(float(s.im(z)))<1e-11)
assert len(roots)==3 and 0<roots[0]<float(pm)<roots[1]<1<roots[2]
assert float(s.diff(Q,p).subs({q:q0,p:roots[0]}))<0
assert float(s.diff(Q,p).subs({q:q0,p:roots[1]}))>0
checks+=3

# Exact rational sign sampling of the flow, and the predicted phase portrait.
for r in [s.Rational(i,1000) for i in range(1,1000)]:
    val=s.sign(Q.subs({q:q0,p:r}))
    assert (r < roots[0] and val==1) or (roots[0] < r < roots[1] and val==-1) or (r > roots[1] and val==1)
    checks+=1

print('PASS',checks,'symbolic/finite sign checks')
print('critical q:',str(qstar), 'approx',float(qstar))
print('q=101/200 interior equilibria:',roots[0],roots[1])
print('Sign and stability classification verified at 999 rational states; infinite statements use the analytic proof.')
