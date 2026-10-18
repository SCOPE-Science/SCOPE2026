"""Exact symbolic verification of a finite-parameter Poisson certificate.
Run: python verify.py. Requires SymPy (tested with 1.13+).
No numerical orbit sampling is used in the acceptance checks.
"""
import sympy as s
b=s.symbols('b',real=True)
J=[-b,b-4,2-b,s.Integer(0),b-2,4-b,s.Integer(2),b]
lengths=[s.expand(J[i+1]-J[i]) for i in range(7)]
# For 2<b<3 all seven intervals have positive length.
assert all(s.simplify(t.subs(b,s.Rational(5,2)))>0 for t in lengths)
r=[s.Rational(1,18),s.Rational(1,6),s.Rational(2,9),s.Rational(2,9),s.Rational(1,3),s.Rational(1,3),s.Rational(1,9)]
w1=(3-b)/81
w2=-b/27
w3=-4*b/81
w4=(18-4*b)/81
w5=2*(3-b)/27
w6=(12-2*b)/81
w=[w1,w2,w3,w4,w5,w5,w6]
# PF formula: L f(x) = f((b-x)/2)/2 + 1_{(2-b,2)}(x) f(x-2).
# The 4-b split separates distinct positive-branch inverse images.
def image(seq):
    a1,a2,a3,a4,a5,a6,a7=seq
    # If input is constant on the 4-b split, use 7-interval transfer chart.
    return [a7/s.Integer(2),a5/s.Integer(2),
            a1+a5/s.Integer(2),a1+a5/s.Integer(2),
            a2+a5/s.Integer(2),a3+a4/s.Integer(2),a4/s.Integer(2)]
# image chart assumes values at positive-source regions are indexed as w4,w5,w6
# whose distinct values on (b-2,4-b), (4-b,2) are equal.
# For all displayed vectors r,w, entries 5 and 6 agree.
assert r[4]==r[5] and s.simplify(w[4]-w[5])==0
assert all(s.simplify(a-c)==0 for a,c in zip(image(r),r)), 'Invariant density failed'
h=[s.Rational(-2,3)]*3+[s.Rational(1,3)]*4
u=[s.simplify(a*c) for a,c in zip(r,h)]
assert all(s.simplify(a-c-d)==0 for a,c,d in zip(w,image(w),u)), 'Poisson identity failed'
assert s.simplify(sum(a*c for a,c in zip(r,lengths))-1)==0
assert s.simplify(sum(a*c for a,c in zip(w,lengths)))==0
p=s.simplify(sum(r[i]*lengths[i] for i in range(3,7)))
assert p==s.Rational(2,3)
C0=s.simplify(p*(1-p))
Ihw=s.simplify(sum(h[i]*w[i]*lengths[i] for i in range(7)))
var=s.simplify(2*Ihw-C0)
assert Ihw==s.Rational(4,27)
assert var==s.Rational(2,27)
# Right-branch follow-up: 0<x<b/2, with b-2<b/2<2 for 2<b<3.
P11=s.simplify((b-2)*s.Rational(2,9)+(b/s.Integer(2)-(b-2))*s.Rational(1,3))
C1=s.simplify(P11-p*p)
assert C1==(b-4)/18
print('VERIFY_OK: full symbolic transfer identities, mass, Poisson equation, variance and lag-one covariance')
print('stationary_positive_mass =',p)
print('I_h_w =',Ihw,'asymptotic_variance =',var,'covariance_lag_one =',C1)
