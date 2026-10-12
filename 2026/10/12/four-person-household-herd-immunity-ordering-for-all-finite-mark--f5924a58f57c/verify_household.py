#!/usr/bin/env python3
"""Exact symbolic certificate for the 4-person household comparison.

Requires Python 3 and SymPy. Run in directory containing positivity_coefficients.tsv.
No floats are used to establish inequalities.
"""
from pathlib import Path
from math import comb
import sympy as sp

ell, pi = sp.symbols('ell pi')
N = 4
q = lambda i: sp.Integer(1) / (1 + i * ell)
beta = {}
for k in range(1, N + 1):
    beta[k] = sp.factor(k - sum(comb(k, i) * beta[i] * q(i)**(k-i)
                                for i in range(1, k)))
mu = {0: sp.Integer(0)}
for k in range(1, N + 1):
    mu[k] = sp.factor(k - sum(comb(k-1, j) * beta[j] * q(j)**(k-j)
                              for j in range(1, k)))
P = {}
for v in range(N):
    P[v] = sp.factor((comb(N,v)*pi**(N-v)
                     -sum(comb(N-i, v-i)*P[i]/q(N-v)**i for i in range(v)))
                     *q(N-v)**v)
s = sp.factor(sum(sp.Rational(N-v,N)*P[v] for v in range(N)))
assert sp.factor(s.subs(pi,1)-1)==0
D = sum(sp.Rational(N-v,N) *
        (P[v] - comb(N,v)*(1-s)**v*s**(N-v))*mu[N-v]
        for v in range(N))
F = sp.cancel(D / (ell**2*pi**2*(1-pi)))
num, den = sp.fraction(F)
expected_den = (ell+1)**15*(2*ell+1)**10*(3*ell+1)**5
assert sp.cancel(den/expected_den-1)==0, 'unexpected normalizer'
H = sp.Poly(num, pi, ell)
assert H.degree(pi)==13 and H.degree(ell)==28
# Equality follows from the exact sp.cancel defining F and normalized num/den.

univ = sp.Poly(H.as_expr(), pi)
n = univ.degree()
coef_power = [sp.Poly(univ.nth(j), ell) for j in range(n+1)]
rows = []
for k in range(n+1):
    bk = sp.Poly(sum(coef_power[j].as_expr()*sp.Rational(comb(k,j),comb(n,j))
                     for j in range(k+1)),ell)
    assert bk.degree()<=28
    row=[bk.nth(j) for j in range(29)]
    assert all(a>=0 and a.is_Rational for a in row), f'negative coefficient in row {k}'
    assert any(a>0 for a in row)
    rows.append(row)

# Reconstruct all power-basis coefficients by the exact Bernstein inversion.
# This uses coefficient arrays, not a floating-point or sample-point check.
power_coeffs = [sp.Poly(sp.Poly(H.as_expr(), pi).nth(j), ell) for j in range(14)]
for j in range(14):
    powerrow = [sum(sp.Rational(comb(13,k)*comb(13-k,j-k)*(-1)**(j-k))
                    * rows[k][m] for k in range(j+1)) for m in range(29)]
    assert all(powerrow[m] == power_coeffs[j].nth(m)
               for m in range(29))

path = Path(__file__).resolve().parent/'positivity_coefficients.tsv'
claimed = path.read_text(encoding='utf-8')
lines=['k\\j\t'+'\t'.join(map(str,range(29)))]
lines.extend(str(k)+'\t'+'\t'.join(map(str, row)) for k,row in enumerate(rows))
assert claimed == '\n'.join(lines)+'\n', 'certificate table does not match reconstruction'

# Independent finite-state Markov chain, using distinct algorithm (see independent_dp.py).
from independent_dp import survivors
from fractions import Fraction
rate = Fraction(1)
escape = Fraction(1,2)
directP = [Fraction(0) for _ in range(5)]
for k in range(5):
    wt = Fraction(comb(4,k))*escape**(4-k)*(1-escape)**k
    for u, mass in survivors(4-k,k,rate).items():
        directP[4-u] += wt*mass
for v in range(4):
    assert P[v].subs({ell:1,pi:sp.Rational(1,2)}) == sp.Rational(directP[v].numerator,directP[v].denominator)
for k in range(1,5):
    directmu=sum((k-u)*mass for u,mass in survivors(k-1,1,rate).items())
    assert mu[k].subs(ell,1)==sp.Rational(directmu.numerator,directmu.denominator)
assert sum(directP)==1
print(f'VERIFY_OK: Bernstein degree {n}; positive rows {len(rows)}, ell degree {H.degree(ell)}; nonnegative coefficients {sum(int(bool(a>=0)) for row in rows for a in row)} of {len(rows)*29}; exact independent CTMC checks PASS')
