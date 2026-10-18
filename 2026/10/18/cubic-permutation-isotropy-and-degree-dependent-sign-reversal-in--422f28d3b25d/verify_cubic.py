"""Exact finite checks of a cubic expectation identity for uniform coordinate shuffles.
All checks use integer or rational arithmetic; no random seeds or simulations.
"""
from fractions import Fraction as F
from itertools import permutations, product
from math import factorial


def mul(v, P):
    return tuple(sum(v[i] * P[i][j] for i in range(len(v))) for j in range(len(v)))


def p3(v):
    return sum(v_i ** 3 for v_i in v)


def p4(v):
    return sum(v_i ** 4 for v_i in v)


def centered_matrix(P):
    d = len(P)
    return [[v - F(1, d) for v in row] for row in P]


def cubic_scalar(P):
    d = len(P)
    C = centered_matrix(P)
    return F(d, (d-1)*(d-2))*sum(v**3 for row in C for v in row)


def mean_cubic_one(v, P):
    d = len(v)
    return sum(p3(mul(perm, P)) for perm in permutations(v)) / factorial(d)


def verify_one_step(v, P):
    d = len(v)
    assert d >= 3 and sum(v) == 0
    assert all(sum(P[i][j] for j in range(d)) == 1 for i in range(d))
    assert all(sum(P[i][j] for i in range(d)) == 1 for j in range(d))
    lhs = mean_cubic_one(v, P)
    rhs = cubic_scalar(P) * p3(v)
    assert lhs == rhs, (d,v,lhs,rhs)


def mat_perm(d, shift):
    return [[F(int(j == ((i + shift) % d))) for j in range(d)] for i in range(d)]


def mat_mix(d):
    A, B, C = mat_perm(d, 0), mat_perm(d, 1), mat_perm(d, 2)
    return [[(A[i][j] + 2 * B[i][j] + 3 * C[i][j])/6 for j in range(d)] for i in range(d)]


def mat_regular(d, r):
    return [[F(1, r) if (j-i)%d < r else F(0) for j in range(d)] for i in range(d)]


def many_step_mean(v, matrices):
    d = len(v)
    perms = list(permutations(range(d)))
    total = F(0)
    for seq in product(perms, repeat=len(matrices)):
        x = v
        for perm, P in zip(seq, matrices):
            x = mul(tuple(x[perm[i]] for i in range(d)), P)
        total += p3(x)
    return total / (factorial(d)**len(matrices))


def fourth_obstruction():
    P = [[F(1,2),F(1,2),F(0),F(0)],
         [F(1,2),F(1,2),F(0),F(0)],
         [F(0),F(0),F(1),F(0)],
         [F(0),F(0),F(0),F(1)]]
    va, vb = (F(3),F(-1),F(-1),F(-1)), (F(1),F(1),F(-1),F(-1))
    def ratio(v):
        return sum(p4(mul(perm,P)) for perm in permutations(v)) / (factorial(4) * p4(v))
    assert ratio(va) == F(11,21)
    assert ratio(vb) == F(2,3)
    return 2


def check():
    assertions=0
    for d in range(3,7):
        Ps=[mat_perm(d, 0), mat_mix(d),
            [[F(1,d) for j in range(d)] for i in range(d)]]
        Ps += [mat_regular(d,r) for r in range(1,d)]
        vs=[tuple([F(d-1)] + [F(-1)]*(d-1)),
            tuple([F(3),F(-2),F(-1)]+[F(0)]*(d-3)),
            tuple([F(2),F(-1),F(-1)]+[F(0)]*(d-3))]
        for P in Ps:
            for v in vs:
                verify_one_step(v,P); assertions+=1
        for r in range(1,d):
            P=mat_regular(d,r)
            assert cubic_scalar(P)==F((d-r)*(d-2*r), r*r*(d-1)*(d-2))
            assertions+=1
    for d, L in ((3,3),(4,2)):
        v=tuple([F(d-1)]+[F(-1)]*(d-1))
        Ps=[mat_mix(d)]*L
        assert many_step_mean(v,Ps) == p3(v) * cubic_scalar(Ps[0])**L
        assertions+=1
    assertions+=fourth_obstruction()
    print(f'PASS {assertions} exact rational assertions; d=3..6 one-step, d=3/4 multi-step, and quartic obstruction')

if __name__=='__main__':
    check()
