"""Exact-rational checks for sharp endemic-attractor capacity in homogeneous higher-order SIS."""
from fractions import Fraction
from math import factorial
from itertools import combinations


def mul(p, q):
    r = [Fraction(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i+j] += a*b
    return r


def product_roots(roots):
    p = [Fraction(1)]
    for z in roots:
        p = mul(p, [-z, Fraction(1)])
    return p


def ev(p, z):
    return sum(a * z**i for i, a in enumerate(p))


def divided_difference_at_one(p):
    degree = len(p) - 1
    q = [Fraction(0)] * degree
    q[degree-1] = p[-1]
    for j in range(degree-2, -1, -1):
        q[j] = p[j+1] + q[j+1]
    assert ev(p, Fraction(1)) - p[0] == q[0]
    return q


def trial(roots):
    M = len(roots)
    assert roots == sorted(roots) and len(set(roots)) == M
    assert all(Fraction(0)<r<Fraction(1) for r in roots) and sum(roots)<1
    E = product_roots(roots)
    gamma = ev(E, Fraction(1))
    q = divided_difference_at_one(E)
    assert gamma > 0 and all(b>0 for b in q)
    assert min(q) > 0
    assert mul([Fraction(1), Fraction(-1)], q) == [gamma-E[0]] + [-a for a in E[1:]]
    vector = [-a for a in mul([Fraction(0), Fraction(1)], E)]
    infectious = mul([Fraction(0), Fraction(1)], q)
    formula = mul([Fraction(1), Fraction(-1)], infectious)
    formula[1] -= gamma
    assert formula == vector
    recovered = [q[i]*factorial(i+1) for i in range(M)]
    assert all(z>0 for z in recovered)
    signs = []
    for j, r in enumerate(roots):
        assert ev(vector, r) == 0
        deriv = sum(i*vector[i]*r**(i-1) for i in range(1, len(vector)))
        expected = -r * product((r-other) for other in roots if other!=r)
        assert deriv == expected and deriv != 0
        signs.append(deriv<0)
    assert sum(signs) == (M+1)//2
    assert signs == [(M-j-1)%2==0 for j in range(M)]
    return (gamma, q, recovered, signs)


def product(vals):
    out = Fraction(1)
    for v in vals:out*=v
    return out


def main():
    count = 0
    for M in range(1, 21):
        roots = [Fraction(j,M*(M+1)) for j in range(1,M+1)]
        gamma, q, s, signs = trial(roots)
        count += 1
        if M in (3, 4, 5, 6):
            print('M=',M,'roots=',roots,'gamma=',gamma,'b=',q,'s=',s,'attracting_indices=',[j+1 for j,v in enumerate(signs) if v])
    # Additional exact rational nonuniform root patterns.
    for M in range(1,10):
        for shift in range(1,9):
            den = 4 * (M+shift) * (M+shift+1)
            roots = [Fraction((j+shift)*(j+shift+1), den) for j in range(1,M+1)]
            # Certain late patterns may exceed the sum constraint and are skipped.
            if sum(roots) >= 1 or max(roots) >= 1:
                continue
            trial(roots)
            count += 1
    print('PASSED:',count,'complete exact-rational polynomial, positivity, root and Jacobian cases')

if __name__=='__main__': main()
