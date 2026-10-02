"""Exact symbolic checks; the accompanying proof covers every unit phase."""
import json
import sympy as S

t, s = S.symbols('t s', real=True)
C = S.diag(1, -1)
I = S.eye(2)


def mul(z):
    return S.Matrix([[S.re(z), -S.im(z)], [S.im(z), S.re(z)]])


def zero(matrix):
    assert all(S.cancel(S.expand_complex(v)) == 0 for v in matrix)


def check(lam, mu):
    q = mul(1 / (lam - mu)) * (C - mul(mu))
    r = I - q
    zero(q * q - q)
    zero(r * r - r)
    zero(q * r)
    zero(r * q)
    zero(mul(lam) * q + mul(mu) * r - C)
    zero(C * q - mul(lam) * q)
    zero(C * r - mul(mu) * r)
    alpha, kappa = 1 / lam, mu / lam
    old = mul(1 / (1 - kappa)) * (mul(alpha) * C - mul(kappa))
    zero(old - q)


phase_t = (1 + S.I * t) / (1 - S.I * t)
phase_s = (1 + S.I * s) / (1 - S.I * s)
check(phase_t, phase_s)
check(-1, phase_s)
check(phase_t, -1)
q = S.Matrix([[1, 1], [0, 0]])
r = I - q
zero(mul(1) * q + mul(S.I) * r - C)
rho = (1 + S.I) / S.sqrt(2)
unit_mu = (1 - S.I) / S.sqrt(2)
z = 1 - unit_mu
v = S.Matrix([S.re(z), S.im(z)])
zero((q + mul(rho) * r) * v)
assert S.simplify(v.dot(v)) > 0
assert S.simplify((q + mul(rho) * r).det()) == 0
print(json.dumps({
    'status': 'VERIFY_OK',
    'exact_checks': ['generic distinct Cayley phases', 'lambda=-1 patch',
                     'mu=-1 patch', 'all complementary projection identities',
                     'exact 2019 scalar phase substitution',
                     'lambda=1,mu=i conjugation', 'nonbicircular cancellation'],
    'limitations': 'Rational identities hold away from lambda=mu. They supplement, not replace, the all-phase function-space proof and primary-source comparison.'
}, indent=2))
