#!/usr/bin/env python3
"""Standalone exact and numerical checks for a binary observation of a directed four-cycle.

Requires Python 3 standard library only. The analytical proof is in RESULT.md;
finite checks here are diagnostic, not an exhaustive replacement for the proof.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial, exp, log


def setup(rr):
    rates = tuple(F(x) for x in rr)
    j = 1 / sum((1 / x for x in rates), F(0))
    pi = [j / x for x in rates]
    q = [[F(0) for _ in range(4)] for _ in range(4)]
    for i, x in enumerate(rates):
        q[i][i] -= x
        q[i][(i + 1) % 4] += x
    return rates, j, pi, q


def matmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(4)), F(0))
             for j in range(4)] for i in range(4)]


def mpowers(q, nmax=3):
    powers = [[[F(i == j) for j in range(4)] for i in range(4)]]
    for _ in range(nmax):
        powers.append(matmul(powers[-1], q))
    return powers


def word_coefficients(word, pi, powers):
    out = [F(0)] * 4
    allowed = [[i for i in range(4) if i % 2 == int(ch)] for ch in word]
    for i, j, k, ell in product(*allowed):
        for n1 in range(4):
            for n2 in range(4 - n1):
                for n3 in range(4 - n1 - n2):
                    n = n1 + n2 + n3
                    out[n] += (pi[i] * powers[n1][i][j] * powers[n2][j][k] *
                               powers[n3][k][ell] /
                               (factorial(n1) * factorial(n2) * factorial(n3)))
    return out


def transition(rr, h):
    rr = list(map(float, rr))
    q = [[0.0] * 4 for _ in range(4)]
    lam = max(rr)
    for i, r in enumerate(rr):
        q[i][i] -= r
        q[i][(i + 1) % 4] += r
    rmat = [[float(i == j) + q[i][j] / lam for j in range(4)] for i in range(4)]
    cur = [[float(i == j) for j in range(4)] for i in range(4)]
    P = [[0.0] * 4 for _ in range(4)]
    weight = exp(-lam * h)
    for n in range(100):
        for i in range(4):
            for j in range(4):
                P[i][j] += weight * cur[i][j]
        weight *= lam * h / (n + 1)
        if weight < 1e-18 and n > lam * h + 10:
            break
        cur = [[sum(cur[i][k] * rmat[k][j] for k in range(4))
                for j in range(4)] for i in range(4)]
    return P


def word_numeric(word, pi, P):
    prob = 0.0
    for i, j, k, ell in product(*(range(int(ch), 4, 2) for ch in word)):
        prob += pi[i] * P[i][j] * P[j][k] * P[k][ell]
    return prob


def main():
    checks = 0
    for k in range(60):
        rr = (1 + k % 7, 2 + (k * 3) % 11, 1 + (k * 5) % 13, 3 + (k * 7) % 17)
        rates, J, pi, q = setup(rr)
        powers = mpowers(q)
        ps = {''.join(w): word_coefficients(''.join(w), pi, powers)
              for w in product('01', repeat=4)}
        a, b, c, d = rates
        X = b * c + a * d
        Y = c * d + a * b
        assert ps['0101'][3] == J * X
        assert ps['1010'][3] == J * Y
        checks += 2
        assert J * (X - Y) == -J * (a-c)*(b-d)
        checks += 1
        # No block of at most three binary frames is directionally asymmetric.
        for w, wR in [('0001','1000'), ('0010','0100'), ('0011','1100'),
                      ('0101','1010'), ('0111','1110'), ('1011','1101')]:
            assert all(ps[w][n] == ps[wR][n] for n in range(3)), (rr,w)
            checks += 1
        Delta = J * (X-Y)
        for w, expected in [('0001',0), ('0010',Delta), ('0011',-Delta),
                            ('0101',Delta), ('0111',0), ('1011',Delta)]:
            assert ps[w][3] - ps[w[::-1]][3] == expected, (rr, w)
            checks += 1
        if a == c or b == d:
            assert Delta == 0
            checks += 1
    # Verify normalized word probabilities and KL asymptotics directly from a
    # uniformized transition semigroup (algorithm distinct from polynomial method).
    for rr in [(1,2,3,4),(2,7,3,5),(1,1,1,1),(1,2,1,3),(2,2,3,2)]:
        rates, J, piq, q = setup(rr)
        pi = [float(x) for x in piq]
        a, b, c, d = rates
        X, Y = b*c+a*d, c*d+a*b
        target = float(J*(X-Y))*log(float(X/Y))
        vals = []
        for h in [0.01,0.005,0.0025]:
            P = transition(rr,h)
            probs = {''.join(w): word_numeric(''.join(w), pi, P)
                     for w in product('01',repeat=4)}
            assert abs(sum(probs.values())-1) < 1e-10
            checks += 1
            for w in ['0001','0010','0011','0101','0111','1011']:
                wR=w[::-1]
                assert abs((probs[w]-probs[wR]) -
                           ({'0001':0,'0010':1,'0011':-1,
                             '0101':1,'0111':0,'1011':1}[w] *
                            (probs['0101']-probs['1010']))) < 1e-12
                checks += 1
            kl = sum(probs[w]*log(probs[w]/probs[w[::-1]]) for w in probs)
            assert kl > -1e-12
            checks += 1
            vals.append(kl/h**3)
        if abs(target)>1e-13:
            assert abs(vals[-1]-target)<abs(vals[0]-target)+1e-5
            assert abs(vals[-1]-target) < 0.04 * target
            checks += 2
        else:
            assert abs(vals[-1]) < 1e-5
            checks += 1
    print(f'PASS: {checks} deterministic exact-rational and numerical assertions')

if __name__=='__main__':
    main()
