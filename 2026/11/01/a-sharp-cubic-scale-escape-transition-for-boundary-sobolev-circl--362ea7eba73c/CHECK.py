"""Supplementary finite checks for boundary-derivative Sobolev polynomials.
The analytical assertions are proved in RESULT.md; finite tests do not prove them.
Run: python CHECK.py  (requires NumPy and SymPy).
"""
import math
from fractions import Fraction
import numpy as np
import sympy as sp

checks = 0
z, A, m = sp.symbols('z A m', real=True)
B = (1-z)**2 + A*(m+1) - A*m*z
x = sp.symbols('x', real=True)
lhs = sp.expand(B * B.subs(z, 1/z) - A**2)
rhs = 2*(1-(z+1/z)/2)*(A*(A*m*(m+1)-2) + 2*(1-(z+1/z)/2)*(A*(m+1)+1))
assert sp.simplify(lhs-rhs) == 0
checks += 1
for n in range(2, 70):
    S = Fraction(n*(n-1)*(2*n-1), 6)
    critical = Fraction(6, n*(n*n-1))
    for lam in [critical/3, critical, 2*critical, Fraction(1, 7), Fraction(71, 3)]:
        amp = n*lam/(1+lam*S)
        c = {j: -amp*j for j in range(1, n)}
        c[n] = Fraction(1)
        deriv = sum(k*v for k,v in c.items())
        assert deriv == n/(1+lam*S)
        checks += 1
        for j in range(n):
            assert c.get(j, Fraction(0)) + lam*j*deriv == 0
            checks += 1
        q1 = 1 - amp*n*(n-1)/2
        assert (q1 > 0) == (lam < critical)
        assert (q1 == 0) == (lam == critical)
        assert (q1 < 0) == (lam > critical)
        checks += 3

for n in range(2, 24):
    critical = 6/(n*(n*n-1))
    S = n*(n-1)*(2*n-1)/6
    for lam in [critical/2, critical, critical*2, 1.0]:
        amp = lam*n/(1+lam*S)
        # Q_{n-1}(z) = z^{n-1} - A sum_{k=1}^{n-1} k z^{k-1}
        coef = [1.0] + [-amp*k for k in range(n-1, 0, -1)]
        roots = np.roots(coef)
        outside = sum(abs(r) > 1+1e-6 for r in roots)
        on = sum(abs(abs(r)-1) <= 1e-6 for r in roots)
        assert outside == int(lam > critical*(1+1e-10)), (n,lam,outside)
        if abs(lam-critical)<critical*1e-10:
            assert on == 1, (n,lam,on)
        else:
            assert on == 0, (n,lam,on)
        pos_real = [r.real for r in roots if r.real>0 and abs(r.imag)<1e-6]
        assert len(pos_real)==1
        checks += 3

def root_u(n, lam):
    sn = n*(n-1)*(2*n-1)/6
    aa = n*lam/(1+lam*sn)
    def ratio(u):
        return 1/sum(k*math.exp(u*(k-n)/n) for k in range(1,n))
    low, high = -80.0, 80.0
    for _ in range(100):
        mid=(low+high)/2
        if ratio(mid)<aa:low=mid
        else:high=mid
    return (low+high)/2

def H(u):
    return 1/sum([]) if False else (u*u/(u-1+math.exp(-u)) if abs(u)>1e-4 else 2+2*u/3)

for tau in (1,6,10,100):
    n=4000
    u=root_u(n, tau/n**3)
    assert abs(H(u)-3*tau/(tau+3))<0.01
    checks+=1
for n in (1000,4000):
    u=root_u(n, n**(-2))
    assert abs(H(u)-3)<0.03
    checks+=1
for n in (1000,4000):
    for s in (4,5):
        u=root_u(n, n**(-s))
        asym=(s-3)*math.log(n)+2*math.log(math.log(n))+2*math.log(s-3)
        assert abs(-u-asym)<2.0, (n,s,-u,asym)
        checks+=1
print(f'PASS: {checks} supplementary assertions; finite checks are not proofs.')
