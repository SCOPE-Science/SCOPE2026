#!/usr/bin/env python3
"""Exact identities for two-cycle walks under independently refreshed arrow fields.

Requires Python 3 and SymPy. Run: python check.py
"""
from fractions import Fraction as F
import sympy as sp

a, p, z = sp.symbols('a p z', real=True)
b = 1 - a
c = a*b
R = lambda t: (1 + t*z)/((1 - t*z)*(1 - z*z))
S = lambda t: (1 + t*z)**2/((1 - t*z)**2*(1 - z*z))
H = a*R(a) - b*R(b)
J = a*S(a) + b*S(b)
H_l = H + z*sp.diff(H, z)
v = p*p*H.subs(z, 1-p)
variance = p*p*J.subs(z, 1-p) - 2*p*p*v*H_l.subs(z, 1-p) + (2-p)*v*v/p
checks = 0

def eq(x,y):
    global checks
    assert sp.cancel(x-y) == 0, 'Exact symbolic equality failed'
    checks += 1

speed_simple = (2*a-1)*(1 - 2*c*(1-p)**2 / ((2-p)*(p+c*(1-p)**2)))
eq(v,speed_simple)
eq(sp.diff(speed_simple,p), (2*a-1)*2*c*(1-p)*(2-c*(1-p)**3) /
   ((2-p)**2*(p+c*(1-p)**2)**2))
eq(variance.subs(a, sp.Rational(1,2)), p*(3-p)**2/((2-p)*(1+p)**2))
eq(sp.diff(variance,p).subs(p,1),0)
eq(sp.diff(variance,p,2).subs(p,1),24*c*(2*a-1)**2)
eq(variance.subs(p,1),4*c)
eq(sp.limit(variance,p,0,dir='+'),0)
eq(sp.limit(speed_simple,p,0,dir='+'),0)
eq(sp.diff(p*(3-p)**2/((2-p)*(1+p)**2),p),
   6*(3-p)*(1-p)**2/((2-p)**2*(1+p)**3))

# Independent finite-horizon calculations from the first opposite arrow K.
def raw_moment(t, m, power):
    ans = F(0)
    for k in range(1,m):
        prob = (1-t)*t**(k-1)
        val = k - ((m-k) % 2)
        ans += prob*val**power
    ans += t**(m-1)*m**power
    return ans

for t in (F(1,5),F(1,3),F(1,2),F(3,4),F(9,10)):
    # Coefficients of the rational series are obtained by its own recurrence,
    # independent of the finite-horizon path calculation above.
    den1 = [F(1), -t, F(-1), t]
    num1 = [F(1), t]
    den2 = [F(1), -2*t, t*t]
    den2 = [sum(den2[j]*(F(1) if i-j==0 else (F(-1) if i-j==2 else F(0)))
                for j in range(len(den2)) if 0 <= i-j <= 2)
            for i in range(5)]
    num2 = [F(1),2*t,t*t]
    def coefficients(num,den,n):
        ans=[]
        for i in range(n):
            val = num[i] if i<len(num) else F(0)
            val -= sum(den[j]*ans[i-j] for j in range(1,min(i+1,len(den))))
            ans.append(val)
        return ans
    one=coefficients(num1,den1,16)
    two=coefficients(num2,den2,16)
    for m in range(1,17):
        assert one[m-1] == raw_moment(t,m,1)
        assert two[m-1] == raw_moment(t,m,2)
        checks += 2

# Independent renewal-reward moment calculation by truncating a geometric tail.
# This is a sanity test, not an infinite proof.
for ar in (F(1,5),F(1,2),F(2,3),F(4,5)):
    for pr in (F(1,3),F(1,2),F(3,4)):
        value = {a:sp.Rational(ar.numerator,ar.denominator),
                 p:sp.Rational(pr.numerator,pr.denominator)}
        exact_v=sp.Rational(v.subs(value))
        exact_s=sp.Rational(variance.subs(value))
        mean_d=F(0); second_d=F(0); mean_ld=F(0)
        q = 1-pr
        for m in range(1,111):
            weight=pr*q**(m-1)
            plus=raw_moment(ar,m,1); minus=raw_moment(1-ar,m,1)
            second_plus=raw_moment(ar,m,2); second_minus=raw_moment(1-ar,m,2)
            ed=ar*plus-(1-ar)*minus
            ed2=ar*second_plus+(1-ar)*second_minus
            mean_d+=weight*ed
            second_d+=weight*ed2
            mean_ld+=weight*m*ed
        numeric_v=pr*mean_d
        numeric_s=pr*(second_d-2*F(exact_v)*mean_ld+(2-pr)*F(exact_v)**2/pr**2)
        assert abs(numeric_v-F(exact_v)) < F(1,10**14)
        assert abs(numeric_s-F(exact_s)) < F(1,10**14)
        checks+=2

print(f'PASS: {checks} finite/exact checks; universal signs follow from the proof.')
