"""Exact symbolic checks for the sixth-cumulant witness in a trapped reversing particle.

Run: python verify_sixth.py. Requires sympy (tested with 1.13+).
The proof in RESULT.md does not rely on this finite symbolic verification.
"""
import sympy as S

D, G = S.symbols('d g', positive=True)


def moment_table(d, g, order=6):
    """Stationary Fourier moment triangle, using the generator recurrence."""
    tab = {(0, 0): S.Integer(1)}
    for n in range(1, order + 1):
        for k in range(-n, n + 1):
            if (n+k) % 2:
                continue
            numerator = S.Rational(n, 2) * (
                tab.get((n-1, k-1), 0) + tab.get((n-1, k+1), 0))
            denominator = n + d*k*k + (2*g if k % 2 else 0)
            tab[n,k] = S.factor(numerator/denominator)
    return tab


def equal(a, b):
    assert S.factor(a-b) == 0, (a, b)


table = moment_table(D, G, 4)
m2_general = 1/(2*(D+2*G+1))
m4_general = 3*(4*D+3)/(8*(2*D+1)*(D+2*G+1)*(D+2*G+3))
equal(table[2,0],m2_general)
equal(table[4,0],m4_general)
k4 = S.factor(table[4,0]-3*table[2,0]**2)
equal(k4,-3*(7*D-2*G+3)/(8*(2*D+1)*(D+2*G+1)**2*(D+2*G+3)))
assert S.solve(S.together(k4).as_numer_denom()[0],G)==[(7*D+3)/2]

critical_g=(7*D+3)/2
full=moment_table(D,critical_g,6)
m2,m4,m6 = [full[n,0] for n in (2,4,6)]
equal(m2, 1/(8*(2*D+1)))
equal(m4, 3/(64*(2*D+1)**2))
equal(m6,15*(8*D**2+15*D+5)/(1024*(D+1)**2*(2*D+1)**2*(8*D+3)))
equal(full[3,1],3/(64*(2*D+1)**2))
equal(full[3,3],3/(64*(2*D+1)**2*(8*D+3)))
equal(full[4,2],3/(32*(D+1)*(2*D+1)*(8*D+3)))
equal(full[5,1],m6)
k6 = S.factor(m6-15*m4*m2+30*m2**3)
equal(k6,-15*(3*D+1)/(1024*(D+1)**2*(2*D+1)**3*(8*D+3)))
standardized = S.factor(k6/m2**3)
equal(standardized,-S.Rational(15,2)*(3*D+1)/((D+1)**2*(8*D+3)))
equal(S.diff((3*D+1)/((D+1)**2*(8*D+3)), D),
      -(48*D**2+33*D+5)/((D+1)**3*(8*D+3)**2))
equal(standardized.subs(D,1),-S.Rational(15,22))
equal(S.limit(standardized,D,0,dir='+'),-S.Rational(5,2))
equal(S.limit(standardized,D,S.oo),0)

# Independently obtain the critical-line sixth moment as rational stationary
# generator identities evaluated at several exact parameter pairs.
for d in [S.Rational(1,5), S.Integer(1), S.Rational(5,2), S.Integer(7)]:
    g=(7*d+3)/2
    tri=moment_table(d,g,6)
    assert all(S.together(v).is_Rational for v in tri.values())
    for (n,k),val in tri.items():
        if n == 0:
            continue
        rate=n+d*k*k+(2*g if k%2 else 0)
        lower=S.Rational(n,2)*(tri.get((n-1,k-1),0)+tri.get((n-1,k+1),0))
        equal(rate*val,lower)
    equal(tri[6,0]-15*tri[4,0]*tri[2,0]+30*tri[2,0]**3,
          k6.subs(D,d))

print('PASS: generic second and fourth moments match published formulas')
print('PASS: exact zero-kurtosis parameter line')
print('PASS: sixth moment, sixth cumulant and normalized witness')
print('PASS: strict monotonicity polynomial and endpoint limits')
print('PASS: four independent rational-parameter generator tables')
print('All symbolic assertions passed.')
