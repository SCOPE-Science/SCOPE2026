"""Exact symbolic verification for two-site memory on a ten-state jump ring.
Run with: python verify.py (requires SymPy).
"""
import sympy as sp

rho = sp.symbols('rho', positive=True)
n = 10
L = sp.zeros(n)
for i in range(n):
    for step, weight in [(1, sp.Integer(1)), (3, rho)]:
        j = (i + step) % n
        L[i, i] += weight
        L[j, j] += weight
        L[i, j] -= weight
        L[j, i] -= weight

J = sp.ones(n) / n
Q = (L + J).inv() - J
assert (L * Q - sp.eye(n) + J).applyfunc(sp.cancel) == sp.zeros(n)
assert (Q * L - sp.eye(n) + J).applyfunc(sp.cancel) == sp.zeros(n)
assert (Q * sp.ones(n, 1)).applyfunc(sp.cancel) == sp.zeros(n, 1)
assert (Q-Q.T).applyfunc(sp.cancel) == sp.zeros(n)
P = (rho**2 + 3*rho + 1) * (rho**2 + 7*rho + 1)
T = {
    1: (rho+2)*(3*rho**2+11*rho+3)/(25*P),
    2: (9*rho**4+74*rho**3+143*rho**2+90*rho+17)/(100*(rho+1)*P),
    3: (2*rho+1)*(3*rho**2+11*rho+3)/(25*P),
    4: (17*rho**4+90*rho**3+143*rho**2+74*rho+9)/(100*(rho+1)*P),
    5: 2*(rho+1)/(25*(rho**2+3*rho+1)),
}
for d, t in T.items():
    a = sp.zeros(n, 1)
    a[0] = a[d] = 1
    a = a - sp.ones(n, 1) * sp.Rational(1, 5)
    actual = (a.T*Q*a)[0]/n
    assert sp.cancel(actual - t) == 0, (d, sp.factor(actual-t))

expected_diffs = {
    (1,2): (3*rho**4+6*rho**3+25*rho**2+34*rho+7)/(100*(rho+1)*P),
    (1,3): -(rho-1)*(3*rho**2+11*rho+3)/(25*P),
    (1,4): -(rho**2-rho-3)/(20*(rho+1)*(rho**2+7*rho+1)),
    (1,5): (rho**3+rho**2+9*rho+4)/(25*P),
    (2,3): -(3*rho**2+rho-1)/(20*(rho+1)*(rho**2+7*rho+1)),
    (2,4): -2*(rho-1)*(rho+1)**2/(25*P),
    (2,5): (rho**4+2*rho**3+15*rho**2+18*rho+9)/(100*(rho+1)*P),
    (3,4): (7*rho**4+34*rho**3+25*rho**2+6*rho+3)/(100*(rho+1)*P),
    (3,5): (4*rho**3+9*rho**2+rho+1)/(25*P),
    (4,5): (9*rho**4+18*rho**3+15*rho**2+2*rho+1)/(100*(rho+1)*P),
}
for (i,j), val in expected_diffs.items():
    assert sp.cancel(T[i] - T[j] - val)==0, (i,j)

alpha = (sp.sqrt(13)-1)/6
beta = (sp.sqrt(13)+1)/2
assert sp.simplify(3*alpha**2+alpha-1) == 0
assert sp.simplify(beta**2-beta-3)==0
assert bool(0 < alpha < 1 < beta)
for r, order in [
    (sp.Rational(1,5), [1,2,3,4,5]),
    (sp.Rational(1,2), [1,3,2,4,5]),
    (sp.Rational(3,2), [3,1,4,2,5]),
    (sp.Integer(4), [3,4,1,2,5]),
]:
    vals = [T[d].subs(rho,r) for d in order]
    assert all(vals[i] > vals[i+1] for i in range(4))
assert T[1].subs(rho,1)==T[3].subs(rho,1)
assert T[2].subs(rho,1)==T[4].subs(rho,1)
assert sp.simplify((T[2]-T[3]).subs(rho,alpha))==0
assert sp.simplify((T[1]-T[4]).subs(rho,beta))==0

# Independent Fourier-spectrum cross-check at five rational coupling ratios.
for r in [sp.Rational(1,4),sp.Rational(1,2),sp.Integer(1),sp.Integer(2),sp.Integer(4)]:
    for d in range(1,6):
        terms = []
        for k in range(1,n):
            theta=2*sp.pi*k/n
            lam=2*(1-sp.cos(theta))+2*r*(1-sp.cos(3*theta))
            terms.append((2+2*sp.cos(theta*d))/(100*lam))
        spect = sum(terms)
        assert abs(float(sp.N(spect-T[d].subs(rho,r),16)))<1e-12

print('PASS: exact Green identities, 5 closed forms, 10 comparison factorizations,')
print('3 exact crossover identities, 4 phase orders, 25 independent spectral comparisons.')
