#!/usr/bin/env python3
"""Exact symbolic checks for a trapped three-state active particle.
Requires SymPy. The calculations supplement, not replace, the analytic proof.
"""
import sympy as sp

a, c, s, y = sp.symbols('a c s y', positive=True)


def moment_even(k, aa, cc):
    out = sp.Integer(1)
    for j in range(1, k + 1):
        out *= (2*j-1)*(2*j-2+cc)/((2*j-1+aa)*(2*j-2+aa+cc))
    return sp.factor(out)


def fold_curve(ss, aa):
    cc = ss*aa*(aa+1)/(1-ss*(aa+1))
    return sp.factor((cc+2)/((aa+cc+2)*(aa+3)))


# Independent moment formulations, including beta-product Pochhammer moments.
for k in range(1, 8):
    beta = sp.rf(c/2,k)*sp.rf(sp.Rational(1,2),k) / (sp.rf((a+c)/2,k)*sp.rf((a+1)/2,k))
    assert sp.cancel(moment_even(k,a,c)-beta) == 0

ss = c/((a+c)*(a+1))
assert sp.cancel(moment_even(1,a,c)-ss) == 0
assert sp.cancel(moment_even(2,a,c)/(3*ss)-(c+2)/((a+c+2)*(a+3))) == 0

cc_s = s*a*(a+1)/(1-s*(a+1))
t = fold_curve(s,a)
P = s*(5*s-3)*a**2 + 2*(5*s-1)*(s-1)*a + 5*(s-1)**2
Den = (a+3)**2*(2*a*s-a+2*s-2)**2
assert sp.cancel(sp.diff(t,a)+2*P/Den) == 0
assert sp.simplify(P.subs(a,y*(1-s)/s)*s/(1-s)**2 - ((5*s-3)*y**2-2*(5*s-1)*y+5*s)) == 0
assert sp.limit(t,a,0,dir='+') == sp.Rational(1,3)
assert sp.simplify(sp.limit(t,a,(1-s)/s,dir='-')-s/(1+2*s)) == 0
rho = sp.sqrt(1+5*s)
a_star = 5*(1-s)/(5*s-1+rho)
t_min = (rho-1)*(3*rho+7)/(2*rho+3)**2
assert sp.simplify(sp.radsimp(t.subs(a,a_star)-t_min)) == 0
assert sp.simplify(P.subs(a,a_star)) == 0

# Exact pair of indistinguishable second- and fourth-moment statistics.
pairs = [(sp.Rational(7,5),sp.Rational(28,5)),
         (sp.Rational(3,2),sp.Rational(15,2))]
assert all(moment_even(1,aa,cc)==sp.Rational(1,3) for aa,cc in pairs)
assert all(moment_even(2,aa,cc)==sp.Rational(19,99) for aa,cc in pairs)
assert [moment_even(3,aa,cc) for aa,cc in pairs] == [sp.Rational(95,726),sp.Rational(2185,16731)]
assert sp.Rational(95,726)-sp.Rational(2185,16731) == sp.Rational(95,368082)

# Exact rational sweep of admissible fixed-variance fold curves.
checks=0
for sv in [sp.Rational(j,13) for j in range(1,13)]:
    aa_ = sp.simplify(a_star.subs(s,sv))
    upper = (1-sv)/sv
    assert 0 < aa_ < upper
    lo = sp.N(t_min.subs(s,sv),30)
    hi = sp.Rational(sv,1+2*sv)
    assert lo < hi < sp.Rational(1,3)
    for f in [sp.Rational(1,5),sp.Rational(2,5),sp.Rational(3,5),sp.Rational(4,5)]:
        x = upper*f
        cv=sp.factor(cc_s.subs({s:sv,a:x}))
        assert cv>0
        assert sp.cancel(moment_even(1,x,cv)-sv)==0
        assert sp.cancel(moment_even(2,x,cv)/(3*sv)-t.subs({s:sv,a:x}))==0
        checks+=1
print(f'PASS: 7 beta-product moments, fold derivative/endpoints/minimum, 2 distinct exact pairs, {checks} rational fold checks')
