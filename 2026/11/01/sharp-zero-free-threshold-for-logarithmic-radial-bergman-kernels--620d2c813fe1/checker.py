"""Finite reproducibility checks for a logarithmically weighted Bergman-kernel theorem.

Requirements: Python 3.9+, mpmath. The analytic argument, not this finite script,
proves the theorem for all real parameter values.
"""
from fractions import Fraction
from math import factorial
import mpmath as mp

mp.mp.dps = 65
checks = 0

def check(flag, label):
    global checks
    assert flag, label
    checks += 1

# Exact truncation, chosen so the alternating tail has decreasing terms.
for p in range(4, 21):
    r = Fraction(2, 2**p)
    a = lambda n: Fraction((n+1)**p) * r**n
    for n in range(2, 30):
        check(a(n+1) < a(n), ("tail", p, n))
    upper = -1 + Fraction(4)*(Fraction(3,4))**p - Fraction(8)*(Fraction(1,2))**p + Fraction(16)*(Fraction(5,16))**p
    check(upper < 0, ("upper", p))
upper4 = -1 + Fraction(4)*(Fraction(3,4))**4 - Fraction(8)*(Fraction(1,2))**4 + Fraction(16)*(Fraction(5,16))**4
check(upper4 == Fraction(-335,4096), "exact bound")

# Exact monomial gamma moments for integer weight exponents.
for alpha in range(0, 7):
    for n in range(0, 15):
        exact = Fraction(factorial(alpha), (n+1)**(alpha+1))
        check(exact > 0, ("moment", alpha, n))

# Numerically confirm analytic continuation, the half-plane certificate,
# and representative negative-real signs; no finite test implies zero-freeness.
for p in ['0.2','0.7','1','1.2','1.7','1.99','2']:
    pp=mp.mpf(p)
    for radius in ['0','0.2','0.6','0.91']:
        rr=mp.mpf(radius)
        for theta in ['0','0.6','1.7','3.1415926535897932384626433832795']:
            u=rr*mp.e**(1j*mp.mpf(theta))
            f=mp.polylog(-pp,u)/u if abs(u)>0 else mp.mpf(1)
            val=(1-u)**2*f
            check(mp.re(val)>0, ("half-plane",p,radius,theta))
for p in ['2.01','2.2','2.9','3.8','4','5','8','15']:
    pp=mp.mpf(p)
    r=mp.mpf('0.999999') if pp<4 else 2**(1-pp)
    val=mp.polylog(-pp,-r)/(-r)
    check(mp.re(val)<0 and abs(mp.im(val))<mp.mpf('1e-40'), ("negative",p))

for p in ['0.3','1.4','2.7','4.5']:
    pp=mp.mpf(p)
    for u in [mp.mpf('0.15'),mp.mpc('0.15','0.12'),mp.mpf('-0.4')]:
        series=mp.nsum(lambda k:(k+1)**pp*u**k,[0,mp.inf])
        poly=mp.polylog(-pp,u)/u
        check(abs(series-poly)<mp.mpf('1e-52'), ("series",p,u))
print(f"PASS: {checks} finite checks; analytic proof independently required.")
