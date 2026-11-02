#!/usr/bin/env python3
"""Exact integer-polynomial certificate for the minimal open exclusion rectifier.

Run with Python 3: python verify.py. All mathematical checks use integer arithmetic;
no floating-point calculation or third-party library is required.
"""
import json
from pathlib import Path

DATA = json.loads((Path(__file__).parent / 'certificate.json').read_text(encoding='utf-8'))
STATES = [tuple(s) for s in DATA['states']]
INDEX = {s: i for i, s in enumerate(STATES)}
assert len(STATES) == 16 and set(STATES) == {tuple((i >> k) & 1 for k in (3, 2, 1, 0)) for i in range(16)}


def trim(a):
    z = list(a)
    while len(z) > 1 and z[-1] == 0:
        z.pop()
    return z


def add(a, b):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])


def neg(a):
    return [-x for x in a]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return trim(c)


def scale(a, z):
    return trim([z * x for x in a])


def powpoly(a, n):
    out = [1]
    for _ in range(n):
        out = mul(out, a)
    return out


def matvec(M, v):
    return [sum_polys([mul(M[i][j], v[j]) for j in range(len(v))]) for i in range(len(v))]


def sum_polys(terms):
    ans = [0]
    for z in terms:
        ans = add(ans, z)
    return ans


def zero(a):
    return trim(a) == [0]


def generator_doubled():
    """Construct 2Q0 and 2Q1 for reservoirs (1+delta)/2,(1-delta)/2."""
    n = len(STATES)
    q0 = [[[0] for _ in range(n)] for _ in range(n)]
    q1 = [[[0] for _ in range(n)] for _ in range(n)]
    def edge(j, target, base, gradient):
        i = INDEX[target]
        q0[i][j] = add(q0[i][j], base)
        q0[j][j] = sub(q0[j][j], base)
        q1[i][j] = add(q1[i][j], gradient)
        q1[j][j] = sub(q1[j][j], gradient)
    for j, conf in enumerate(STATES):
        for site, sign in ((0, 1), (3, -1)):
            t = list(conf)
            t[site] ^= 1
            edge(j, tuple(t), [1], [sign if conf[site] == 0 else -sign])
        rates = [[1], [0, 1], [1], [1]]
        for site in range(3):
            if conf[site] != conf[site+1]:
                t = list(conf)
                t[site], t[site+1] = t[site+1], t[site]
                departure = site if conf[site] else site+1
                edge(j, tuple(t), scale(rates[departure], 2), [0])
    return q0, q1


def main():
    D = DATA['D_ascending']
    P = DATA['P_ascending']
    R = DATA['R_ascending']
    assert len(D) == 6 and len(P) == 9 and len(R) == 5
    assert all(z > 0 for z in D+P+R), 'Strict positivity requires every coefficient to be positive'
    S = [1,1]
    V = [DATA[name]['polys_ascending'] for name in ('p0','p1','p2')]
    assert all(DATA[name]['scale'] == 8 and DATA[name]['denom_power_D'] == k for k,name in enumerate(('p0','p1','p2')))
    assert all(len(row) == 16 for row in V)
    q0,q1 = generator_doubled()
    assert all(zero(a) for a in matvec(q0,V[0]))
    SD = mul(S,D)
    for k in (1,2):
        balance = [add(a,mul(SD,b)) for a,b in zip(matvec(q0,V[k]),matvec(q1,V[k-1]))]
        assert all(zero(v) for v in balance), f'Order {k} balance failed'
    assert sub(sum_polys(V[0]),scale(S,8)) == [0]
    assert zero(sum_polys(V[1])) and zero(sum_polys(V[2]))
    occupied = [i for i,x in enumerate(STATES) if x[0] == 1]
    A1 = sum_polys([V[1][i] for i in occupied])
    A2 = sum_polys([V[2][i] for i in occupied])
    # J(delta) = (1+delta)/2 - <eta_1>(delta).
    # Coefficient of delta: 1/2 - sum eta_1 p1 = 2t R(t)/D(t).
    lhs1 = sub(scale(mul(powpoly(S,2),D),4),A1)
    rhs1 = scale(mul([0,1],mul(R,powpoly(S,2))),16)
    assert zero(sub(lhs1,rhs1)), 'Linear response identity failed'
    # Quadratic coefficient: -sum eta_1 p2 = 2t(t-1)P/((t+1)D^2).
    rhs2 = scale(mul([0,-1,1],mul(P,powpoly(S,2))),16)
    assert zero(sub(neg(A2),rhs2)), 'Quadratic response identity failed'
    # All analytic claims follow from balance, normalization, uniqueness, and
    # strictly positive coefficients of D and P for t>0.
    print('PASS: exact polynomial balances at orders 0, 1, 2; normalization;')
    print('      exact current coefficients; positive-coefficient sign certificate.')
    print('D(t) ascending:',D)
    print('P(t) ascending:',P)


if __name__ == '__main__':
    main()
