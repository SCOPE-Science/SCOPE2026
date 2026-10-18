"""Finite, reproducible checks of the lattice fractional-power endpoint-norm formulas.
Requires mpmath. These tests are not substitutes for the general proof.
"""
from math import comb
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 75
checks = 0

def test(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1

def coefficients(alpha, K):
    a = [mp.gamma(2*alpha+1) / mp.gamma(alpha+1)**2]
    for k in range(K):
        a.append(a[-1]*(k-alpha)/(k+alpha+1))
    return a

def proposed_norm(alpha):
    m = int(mp.floor(alpha))
    if alpha == m:
        return mp.mpf(4)**m
    a = coefficients(alpha, m+1)
    if m % 2 == 0:
        return 2*a[0] + 4*sum(a[k] for k in range(2,m+1,2))
    return -4*sum(a[k] for k in range(1,m+1,2))

# Exact binomial coefficient and central coefficient checks.
for m in range(1,13):
    integer_coeffs = [Fraction((-1)**k * comb(2*m,m-k), 1) for k in range(m+1)]
    test(integer_coeffs[0] + 2*sum(integer_coeffs[1:]) == 0,
         f'integer zero sum {m}')
    test(abs(integer_coeffs[0]) + 2*sum(abs(t) for t in integer_coeffs[1:]) == 4**m,
         f'integer norm {m}')

# Independent absolute-coefficient sum with an exactly summed constant-sign tail.
# The tail recurrence yields sum_{k>K} |a_k| = |a_{K+1}| (K+alpha+1)/(2 alpha)
# when K is beyond the first sign-change boundary.
for raw in ['0.23','0.50','0.86','1.14','1.65','1.92','2.17','2.78',
            '3.28','3.93','4.16','4.71','5.33','6.48','8.73','12.21']:
    alpha = mp.mpf(raw)
    a = coefficients(alpha, 120)
    direct = abs(a[0]) + 2*sum(abs(z) for z in a[1:120])
    direct += abs(a[120])*(119+alpha+1)/alpha
    test(abs(direct - proposed_norm(alpha)) < mp.mpf('1e-60'),
         f'norm versus independently summed coefficient tail {raw}')
    test(proposed_norm(alpha) > mp.power(4,alpha), f'normaloid gap {raw}')
    m = int(mp.floor(alpha))
    for k in range(1,40):
        predicted = (-1)**k if k<=m+1 else (-1)**(m+3)
        test(mp.sign(a[k]) == predicted, f'sign alpha {raw} k{k}')

# Original defining Fourier integral against exact coefficient formula.
for raw in ['0.6','1.4','2.6','4.3']:
    alpha = mp.mpf(raw)
    a=coefficients(alpha,8)
    for k in range(9):
        integral = mp.quad(lambda t: (2-2*mp.cos(t))**alpha*mp.cos(k*t), [0,mp.pi])/mp.pi
        test(abs(integral-a[k])<mp.mpf('1e-55'), f'Fourier integral alpha {raw} k{k}')

# Exact beta-series identity giving the cusp jump and precise finite differences.
for m in range(1,9):
    beta_sum = mp.mpf('1')/(2*m)
    finite = sum(mp.beta(j+1,2*m+1) for j in range(90))
    tail = mp.beta(91,2*m)/(1) # sum_{j>=90} B(j+1,2m+1) = B(91,2m)
    # Note finite sum above j=0..89; B(91,2m) is tail by telescoping.
    test(abs(finite+tail-beta_sum)<mp.mpf('1e-65'), f'beta sum {m}')
    h=mp.mpf('1e-14')
    left=(proposed_norm(mp.mpf(m))-proposed_norm(mp.mpf(m)-h))/h
    right=(proposed_norm(mp.mpf(m)+h)-proposed_norm(mp.mpf(m)))/h
    test(abs((right-left)-mp.mpf(2)/m) < mp.mpf('2e-7'),f'cusp jump m={m}')

# Zero-order discontinuity and finite-support pointwise convergence.
for raw in ['0.01','0.001','0.0001']:
    alpha=mp.mpf(raw)
    a=coefficients(alpha,20)
    test(abs(proposed_norm(alpha)-2)<mp.mpf('0.001'),f'zero order norm {raw}') if alpha<mp.mpf('0.001') else None
    test(abs(a[0]-1)<mp.mpf('0.0003'),f'central coefficient {raw}')
    test(abs(a[1])<mp.mpf('0.011'),f'nearest coefficient {raw}')
print('VERIFY_OK checks=',checks)
