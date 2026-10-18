#!/usr/bin/env python3
"""Exact arithmetic checks for the directed-cycle fourth-order Gauss transfer theorem.

Requires SymPy. This finite test corroborates but does not replace the proof
for arbitrary cycle lengths, positive rates and step sizes.
"""
from itertools import product
from sympy import Matrix, Rational, eye, zeros, symbols, factor, simplify, Poly, nroots

count = 0

def confirm(statement, message):
    global count
    assert bool(statement), message
    count += 1

def cycle_q(rates):
    n = len(rates)
    Q = zeros(n)
    for i, r in enumerate(rates):
        Q[i, i] -= r
        Q[i, (i + 1) % n] += r
    return Q

def transfer(Q, h):
    n = Q.rows
    A = 12 * eye(n) - 6 * h * Q + h * h * Q * Q
    return A.inv() * (12 * eye(n) + 6 * h * Q + h * h * Q * Q)

def check_group_inverse(rates):
    n = len(rates)
    s = [1 / r for r in rates]
    S = sum(s)
    pi = [r / S for r in s]
    Q = cycle_q(rates)
    Pi = Matrix(n, n, lambda i, j: pi[j])
    m = Matrix(n, n, lambda i, j: 0 if i == j else sum(s[k % n] for k in range(i, i + ((j - i) % n))))
    G = Matrix(n, n, lambda i, j: pi[j] * (m[i, j] - sum(pi[k] * m[k, j] for k in range(n))))
    confirm(Q * G == eye(n) - Pi, 'QG identity')
    confirm(G * Q == eye(n) - Pi, 'GQ identity')
    confirm(G * Matrix([1] * n) == zeros(n, 1), 'G1 identity')
    confirm(Matrix(1, n, pi) * G == zeros(1, n), 'pi G identity')
    # The limiting aggregate concerns the immediate predecessor of each target.
    cyc = sum(G[(j - 1) % n, j] for j in range(n))
    if n >= 3:
        if n == 3:
            confirm(cyc == 0, 'three-cycle zero sum')
            for j in range(n):
                expr = s[j] * (s[j] * s[(j - 1) % n] - s[(j + 1) % n] ** 2) / S ** 2
                confirm(G[(j - 1) % n, j] == expr, 'triangle individual term')
        else:
            chord = sum(s[i] * s[j] for i in range(n) for j in range(i + 1, n)
                        if (j - i) not in (1, n - 1))
            confirm(cyc == -chord / S, 'non-edge identity')
            confirm(cyc < 0, 'strict aggregate negativity')
            confirm(any(G[(j - 1) % n, j] < 0 for j in range(n)), 'some negative entry')
    if n == 3 and len(set(rates)) > 1:
        confirm(any(G[(j - 1) % n, j] < 0 for j in range(n)), 'heterogeneous triangle')
    for h in (Rational(1, 10), Rational(3, 2), Rational(25), Rational(400)):
        T = transfer(Q, h)
        confirm(T * Matrix([1] * n) == Matrix([1] * n), 'mass preservation')
        confirm(T == T.applyfunc(lambda z: z), 'exact rational transfer')
        # Check matrix resolvent identity: R(hQ) = I+12hQ/(12I-6hQ+h²Q²).
        A = 12 * eye(n) - 6 * h * Q + h * h * Q * Q
        confirm(T == eye(n) + 12 * h * Q * A.inv(), 'Padé resolvent formula')
    return G

for n in range(2, 9):
    samples = [tuple(Rational(1) for _ in range(n)),
               tuple(Rational(1 + (i % 3)) for i in range(n)),
               tuple(Rational(i + 1, i + 2) for i in range(n))]
    for rates in samples:
        check_group_inverse(rates)

x = symbols('x', nonnegative=True)
for n in (3, 4):
    Q = cycle_q((Rational(1),) * n)
    T = transfer(Q, x)
    confirm(all(simplify(T[i,j] - T[0,(j-i)%n])==0 for i in range(n) for j in range(n)), 'circulant')
    if n == 3:
        expected = [(x*x-2*x+4)/(x*x+2*x+4),
                    8*x/((x+2)*(x*x+2*x+4)),
                    4*x*x/((x+2)*(x*x+2*x+4))]
        for j, e in enumerate(expected):
            confirm(simplify(T[0,j]-e) == 0, 'triangle transfer')
    if n == 4:
        den = 2*(x*x+3*x+3)*(x**4+6*x**3+18*x*x+36*x+36)
        expected = [
            (2*x**6+9*x**5+6*x**4+72*x*x+216*x+216)/den,
            -3*x*(x**4-24*x*x-72*x-72)/den,
            3*x*x*(x**3+12*x*x+36*x+36)/den,
            9*x**3*(x+2)**2/den]
        for j, e in enumerate(expected):
            confirm(simplify(T[0,j]-e) == 0, 'square transfer')
        f=Poly(x**4 -24*x*x-72*x-72,x)
        confirm(f.count_roots(0,100) == 1, 'single positive threshold')
        confirm(f.eval(6)<0 and f.eval(7)>0, 'positive root bracket')
print(f'VERIFY_OK {count} exact matrix, group-inverse and polynomial checks')
