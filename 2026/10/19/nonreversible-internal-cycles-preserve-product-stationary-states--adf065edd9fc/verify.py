#!/usr/bin/env python3
"""Exact finite-state checks for a colored exclusion process on periodic rings.

Requires only Python 3's standard library. Each master-equation term is evaluated
using rational arithmetic, with no floating-point tolerance.
"""
from fractions import Fraction as F
from itertools import product
from math import comb


def color_weights(r):
    """Three-type directed Markov-tree formula, no matrix solver required."""
    return (
        r[1][0] * r[2][0] + r[1][2] * r[2][0] + r[2][1] * r[1][0],
        r[0][1] * r[2][1] + r[0][2] * r[2][1] + r[2][0] * r[0][1],
        r[0][2] * r[1][2] + r[0][1] * r[1][2] + r[1][0] * r[0][2],
    )


def ring_rates(forward, backward):
    return tuple(tuple(F(0) if i == j else F(forward if (j - i) % 3 == 1 else backward)
                       for j in range(3)) for i in range(3))


def partition(M, V, a, w):
    # Finite coefficient extraction of [x^V](sum_i w_i/(1-x/a_i))^M.
    atom = [sum((F(w[i], a[i]**j) for i in range(len(a))), F()) for j in range(V+1)]
    coeff = [F(1)] + [F(0)]*V
    for _ in range(M):
        coeff = [sum((coeff[k]*atom[j-k] for k in range(j+1)), F()) for j in range(V+1)]
    return coeff[V]


def configurations(L, M):
    return [s for s in product(range(4), repeat=L) if sum(t != 0 for t in s) == M]


def weight(s, a, w):
    L = len(s)
    val = F(1)
    for i, t in enumerate(s):
        if t:
            gap = 0
            while s[(i+1+gap) % L] == 0:
                gap += 1
            val *= F(w[t-1], a[t-1]**gap)
    return val


def check(L, M, a, r):
    w = color_weights(r)
    assert all(x > 0 for x in w)
    for i in range(3):
        assert sum((w[j]*r[j][i] for j in range(3)), F()) == w[i]*sum(r[i])
    states = configurations(L, M)
    weights = {s:weight(s,a,w) for s in states}
    balance = dict.fromkeys(states, F(0))
    # Compute incoming and outgoing jump fluxes independently from the claimed law.
    for s in states:
        for i,t in enumerate(s):
            if t == 0:
                continue
            j=(i+1)%L
            if s[j] == 0:
                dst=list(s); dst[i]=0; dst[j]=t; dst=tuple(dst)
                amount = F(a[t-1])*weights[s]
                balance[s]-=amount
                balance[dst]+=amount
            else:
                for other in (1,2,3):
                    if other == t:continue
                    dst=list(s); dst[i]=other; dst=tuple(dst)
                    amount = r[t-1][other-1]*weights[s]
                    balance[s]-=amount
                    balance[dst]+=amount
    assert all(x==0 for x in balance.values()), next((s,x) for s,x in balance.items() if x)
    V=L-M
    total=sum(weights.values(), F(0))
    assert total == F(L,M)*partition(M,V,a,w), (total,L,M)
    # All directed color-edge currents: direct enumeration versus coefficient formula.
    for origin in range(3):
        for target in range(origin+1,3):
            direct = F()
            for s in states:
                for i,t in enumerate(s):
                    if t == origin+1 and s[(i+1)%L]!=0:
                        direct += weights[s]*r[origin][target]
                    elif t == target+1 and s[(i+1)%L]!=0:
                        direct -= weights[s]*r[target][origin]
            direct /= total
            predicted = (F(M)*partition(M-1,V,a,w)/partition(M,V,a,w)
                         *(w[origin]*r[origin][target] - w[target]*r[target][origin]))
            assert direct == predicted, (L,M,origin,target,direct,predicted)
    return len(states)


def main():
    a = (1,2,3)
    rates = [ring_rates(2,1),ring_rates(1,2),ring_rates(4,1),
             ((F(0),F(2),F(1)),(F(3),F(0),F(5)),(F(4),F(2),F(0)))]
    nstates = 0
    ntests = 0
    for r in rates:
        for L in range(3,7):
            for M in range(2, min(L,3)+1):
                nstates += check(L,M,a,r)
                ntests += 1
    # Irreversible three-cycle with uniform invariant weights: its stationary law
    # ignores the forward/backward split although its flip current does not.
    assert color_weights(ring_rates(2,1)) == color_weights(ring_rates(1,2))
    p21 = partition(2,1,a,(1,1,1))
    p11 = partition(1,1,a,(1,1,1))
    assert (p21,p11) == (F(11),F(11,6))
    assert 2*p11/p21 == F(1,3)
    assert F(2)**3 != F(1)**3  # detailed-balance cycle criterion fails
    print('PASS: %d rational generator cases, %d exact weighted state balances,'
          ' canonical normalization and every color-pair current' % (ntests,nstates))
    print('PASS: stationary-law invariance and exact L=3, M=2 circulation factor 1/3')

if __name__ == '__main__':
    main()
