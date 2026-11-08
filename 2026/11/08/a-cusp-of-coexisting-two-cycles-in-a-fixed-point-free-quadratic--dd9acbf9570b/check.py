"""Reproduce exact polynomial identities and representative rational checks.

Requires SymPy; the general theorem is proved analytically, not by finite sampling.
"""
import sympy as S

x, q, k, u = S.symbols('x q k u', real=True)
G = k*(1-q*(1-x)**2)**2
# Independently compose the original two piecewise polynomial branches.
a, b, c = S.symbols('a b c', real=True)
left_of_t = 1-(1-a)*(1-x)**2
right_of_left = c*((left_of_t-b)/(1-b))**2
assert S.factor(right_of_left/b - G.subs({q:(1-a)/(1-b),k:c/b})) == 0
assert S.factor(S.diff(G,x)-4*k*q*(1-x)*(1-q*(1-x)**2)) == 0
qf = 1/(u*(4-3*u))
kf = (4-3*u)**2/(16*(1-u))
assert S.factor((G-x).subs({q:qf,k:kf,x:1-u})) == 0
assert S.factor((S.diff(G,x)-1).subs({q:qf,k:kf,x:1-u})) == 0
cusp = S.factor((G-x).subs({q:S.Rational(3,4),k:S.Rational(3,4)}))
assert cusp == (x-3)*(3*x-1)**3/64
sample = S.factor((G-x).subs({q:S.Rational(4,5),k:S.Rational(4,5)}))
assert sample == (4*x**2-13*x+4)*(16*x**2-12*x+1)/125
left = (3-S.sqrt(5))/8
middle = (13-S.sqrt(105))/8
right = (3+S.sqrt(5))/8
assert 0<left<middle<right<1
for r in (left,right):
    assert S.simplify(S.diff(G,x).subs({q:S.Rational(4,5),k:S.Rational(4,5),x:r})) == S.Rational(4,5)
assert S.simplify(S.diff(G,x).subs({q:S.Rational(4,5),k:S.Rational(4,5),x:middle})) == (26-2*S.sqrt(105))/5
# The fourth zero is outside [0,1].
assert (13+S.sqrt(105))/8 > 1
# Exact sign tests over the sample basin threshold.
gsample = G.subs({q:S.Rational(4,5),k:S.Rational(4,5)})
assert S.sign((gsample-x).subs({x:S.Rational(1,100)})) == 1
assert S.sign((gsample-x).subs({x:S.Rational(1,4)})) == -1
assert S.sign((gsample-x).subs({x:S.Rational(1,2)})) == 1
assert S.sign((gsample-x).subs({x:S.Rational(9,10)})) == -1
# More exact rational instances, testing predicted numbers of roots in (0,1).
cases = [
    (S.Rational(1,2),S.Rational(4,5),1),
    (S.Rational(3,4),S.Rational(3,4),1),
    (S.Rational(4,5),S.Rational(3,4),1),
    (S.Rational(4,5),S.Rational(4,5),3),
    (S.Rational(4,5),S.Rational(9,10),1),
    (S.Rational(9,10),S.Rational(9,10),3),
    (S.Rational(99,100),S.Rational(9,10),3),
]
for qq,kk,expected in cases:
    poly = S.Poly(S.together((G-x).subs({q:qq,k:kk})),x)
    assert poly.count_roots(0,1) == expected, (qq,kk,poly.count_roots(0,1))
print('EXACT_CUSP_AND_BASIN_IDENTITIES_OK',len(cases))
