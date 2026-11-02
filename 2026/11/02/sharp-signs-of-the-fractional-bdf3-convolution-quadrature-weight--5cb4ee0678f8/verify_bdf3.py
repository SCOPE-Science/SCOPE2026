#!/usr/bin/env python3
"""Exact certificate for the fractional BDF3 coefficient-sign theorem.

Requires only the Python standard library.  Run: python verify_bdf3.py
"""
from fractions import Fraction as F
from math import comb


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    out = [F(0)] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    return trim(out)


def scale(a, c):
    return trim([c * v for v in a])


def multiply(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def normalized_coefficients(limit):
    # beta = 1-alpha. The formal series is
    # F(z) = [1-18z/11+9z^2/11-2z^3/11]^(1-beta).
    # Differentiating F(z)*delta(z) gives this *exact* recurrence.
    out = [[F(1)]]
    for n in range(1, limit + 1):
        v = [F(0)]
        if n >= 1:
            v = add(v, multiply(out[n - 1], [F(3*(n-2)), F(3)]))
        if n >= 2:
            v = add(v, multiply(out[n - 2], [F(-3*(n-4), 2), F(-3)]))
        if n >= 3:
            v = add(v, multiply(out[n - 3], [F(n-6, 3), F(1)]))
        out.append(scale(v, F(6, 11*n)))
    return out


def divide_beta_one_minus_beta(p):
    # p(z) = z(1-z)q(z), exact polynomial division by comparing coefficients.
    p = trim(p)
    assert len(p) >= 3 and p[0] == 0
    q = []
    for j in range(1, len(p) - 1):
        q.append(p[j] + (q[-1] if q else F(0)))
    assert p[-1] == -q[-1]
    assert trim(multiply([F(0), F(1), F(-1)], q)) == p
    return trim(q)


def bernstein_coefficients(p):
    # If p(x)=sum_j a_j*x^j, b_k=sum_{j<=k} a_j*C(k,j)/C(d,j)
    # and p(x)=sum_k b_k*C(d,k)*x^k*(1-x)^(d-k).
    p = trim(p)
    d = len(p) - 1
    return [sum((p[j] * F(comb(k,j), comb(d,j)) for j in range(k+1)), F(0))
            for k in range(d+1)]


def prove_positive(p, name):
    coeff = bernstein_coefficients(p)
    assert all(v > 0 for v in coeff), (name, [i for i,v in enumerate(coeff) if v<=0])
    return len(coeff), min(coeff)


def direct_binomial_coefficients(alpha, N):
    # Independent reconstruction via the binomial theorem, not the recurrence.
    v = [F(0), F(-18,11), F(9,11), F(-2,11)]
    powers = [[F(1)]]
    for k in range(1, N+1):
        powers.append(multiply(powers[-1], v)[:N+1])
    out = [F(0)]*(N+1)
    choose = F(1)
    for k in range(N+1):
        if k:
            choose *= (alpha-k+1)/k
        for j,x in enumerate(powers[k]):
            out[j] += choose*x
    return out


def eval_poly(p,x):
    y = F(0)
    for c in reversed(p):
        y=y*x+c
    return y


def main():
    rows = normalized_coefficients(21)
    beta = F(1)
    assert rows[1] == [F(-18,11),F(18,11)]
    assert rows[2] == [F(99,121),F(-261,121),F(162,121)]  # 9(beta-1)(18beta-11)/121
    # -w_3/(1-beta)=2(486*beta^2-405*beta+121)/1331.
    assert rows[3] == [F(-242,1331), F(1052,1331), F(-1782,1331),F(972,1331)]
    assert 405**2 - 4*486*121 == -71199 < 0
    successes = 0
    minimal = None
    reduced = {}
    for n in range(4,22):
        q = divide_beta_one_minus_beta(scale(rows[n],F(-1)))
        reduced[n] = q
        num,lo = prove_positive(q,f'positive normalized -coefficient n={n}')
        successes += num
        if minimal is None or lo<minimal: minimal=lo
    c, C = F(4,5), F(11,10)
    for n in (20,21):
        for name,p in [('ratio-lower',add(reduced[n],scale(reduced[n-1],-c))),
                       ('ratio-upper',add(scale(reduced[n-1],C),scale(reduced[n],F(-1))))]:
            num,lo = prove_positive(p,f'{name} n={n}')
            successes += num
            if lo<minimal: minimal=lo
    n_direct = 0
    for alpha in (F(1,5),F(7,18),F(1,2),F(9,10)):
        other = direct_binomial_coefficients(alpha,12)
        for n in range(13):
            assert eval_poly(rows[n],1-alpha)==other[n]
            n_direct += 1
    # The inductive interval calculation, checked independently in integers:
    # q_n increases with q_{n-1} and decreases with q_{n-2} for n>=22.
    # phi(c,C)-c=(49*n-510*t)/(2420*n)>0 for n>=22,1<t<2.
    # C-phi(C,c)=(n+930*t)/(1210*n)>0.
    # Derivative sign: B-D/c = (13*n)/12-(7*t)/4 >0.
    for n in (22,23,50):
        for t in (F(1),F(2)):
            A=3*(n-t); B=F(3,2)*(n-2*t); D=F(n-3*t,3); den=F(11*n,6)
            phi=lambda x,y:(A-B/x+D/(x*y))/den
            assert phi(c,C)-c == F(49*n-510*t,2420*n)
            assert C-phi(C,c) == F(n+930*t,1210*n)
            assert B-D/c == F(13*n,12)-F(7*t,4)
            assert phi(c,C)>c and phi(C,c)<C
    print('PASS: exact symbolic polynomial recurrence through n=21')
    print('PASS: 18 strict Bernstein positivity certificates, n=4,...,21')
    print('PASS: four strict Bernstein ratio certificates for n=20,21')
    print('PASS: %d positive rational Bernstein coefficients'%successes)
    print('PASS: %d direct generalized-binomial coefficient equalities'%n_direct)
    print('PASS: closed-form invariant ratio bounds for all n>=22')
    print('PASS: exact discriminant and first coefficient formulas')
    print('Smallest finite-certificate Bernstein coefficient: %.12g'%float(minimal))

if __name__ == '__main__':
    main()
