"""Exact arithmetic checks for the directional range split of a once-reinforced walk.

This checker establishes only finite identities; the full theorem requires the
inductive proof and the infinite-limit arguments in RESULT.md.
"""
from fractions import Fraction as F
from math import comb

checks = 0

def test(lhs, rhs, context):
    global checks
    checks += 1
    if lhs != rhs:
        raise AssertionError((context, lhs, rhs))


def rise(c, n):
    out = F(1)
    for i in range(n):
        out *= c + i
    return out


def bb(c, k, j):
    if j < 0 or j > k:
        return F(0)
    return F(comb(k, j)) * rise(c, j) * rise(c, k-j) / rise(2*c, k)


def solve_linear(a, b):
    n = len(b)
    a = [list(row) + [b[i]] for i, row in enumerate(a)]
    for i in range(n):
        pivot = next(j for j in range(i, n) if a[j][i])
        a[i], a[pivot] = a[pivot], a[i]
        z = a[i][i]
        a[i] = [v/z for v in a[i]]
        for j in range(n):
            if j != i:
                z = a[j][i]
                a[j] = [a[j][h]-z*a[i][h] for h in range(n+1)]
    return [row[-1] for row in a]


def direct_exit(c, k):
    """Solve all first-exit probabilities from native walk transitions."""
    a = [[F(0)]*(k+1) for _ in range(k+1)]
    b = [F(0)]*(k+1)
    for j in range(k+1):
        a[j][j] = F(1)
        if j == 0:
            a[j][1] = -c/(1+c)
        elif j == k:
            a[j][k-1] = -c/(1+c)
            b[j] = 1/(1+c)
        else:
            a[j][j-1] = F(-1,2)
            a[j][j+1] = F(-1,2)
    return solve_linear(a,b)


for c in [F(1,5), F(1,2), F(1), F(4,3), F(2), F(5)]:
    for k in range(1,13):
        h = direct_exit(c,k)
        for j in range(k+1):
            test(h[j], (c+j)/(k+2*c), ('exit',str(c),k,j))

    # Joint distribution of (number of right expansions, last expansion sign).
    law = {(1,+1):F(1,2), (0,-1):F(1,2)}
    for k in range(1,31):
        for j in range(k+1):
            plus = law.get((j,+1), F(0))
            minus = law.get((j,-1), F(0))
            ref = bb(c,k,j)
            test(plus+minus,ref,('bb',str(c),k,j))
            test(plus, F(j,k)*ref,('plus',str(c),k,j))
            test(minus, F(k-j,k)*ref,('minus',str(c),k,j))
        test(sum(law.values()), F(1), ('normalization',str(c),k))
        test(sum(F(j)*v for (j,s),v in law.items()),F(k,2),('mean',str(c),k))
        e2 = sum(F(j*j)*v for (j,s),v in law.items())
        variance = e2-F(k*k,4)
        test(variance,F(k)*(k+2*c)/(4*(2*c+1)),('variance',str(c),k))
        if k==30:
            break
        same=(k+c)/(k+2*c)
        flip=c/(k+2*c)
        nxt={}
        for (j,sign),prob in law.items():
            for nextsign,weight in [(sign,same),(-sign,flip)]:
                idx=(j+int(nextsign==+1),nextsign)
                nxt[idx]=nxt.get(idx,F(0))+prob*weight
        law=nxt

    rrl = F(1,2)*(1+c)/(1+2*c)*c/(2+2*c)
    rlr = F(1,2)*c/(1+2*c)*c/(2+2*c)
    test(rrl/rlr,(1+c)/c,('nonexchangeability',str(c)))
    test(rrl!=rlr,True,('distinct sequences',str(c)))

print(f'PASS {checks} exact-rational assertions, six reinforcement parameters, 30 record levels')
