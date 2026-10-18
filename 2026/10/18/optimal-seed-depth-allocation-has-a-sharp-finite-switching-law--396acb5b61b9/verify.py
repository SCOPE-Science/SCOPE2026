"""Exact rational consistency checks for a seed-depth growth-allocation theorem.

The analytical determinant-lemma proof in RESULT.md, not finite sampling,
establishes the universal assertion.
"""
from fractions import Fraction as F


def framework(s, g, beta, q):
    assert len(s) == len(g) and all(0 < z < 1 for z in s)
    assert all(0 < z <= 1 for z in g) and beta > 0 and 0 < q <= 1
    d = [s[k] * (1 - q * g[k]) for k in range(len(s))]
    L = [d[k] + beta * q * g[k] for k in range(len(s))]
    highest = max(L)
    assert highest > max(d)
    return d, L, highest


def three_depths():
    s = [F(9, 10), F(4, 5), F(1, 2)]
    g = [F(1, 11), F(5, 12), F(3, 5)]
    beta = F(2)
    assert [beta * x - s[i] * x for i, x in enumerate(g)] == [F(1, 10), F(1, 2), F(9, 10)]
    for q, opt in [(F(1,10), {0}), (F(1,4), {0, 1}),
                   (F(1,2), {1}), (F(3,4), {1, 2}), (F(9,10), {2})]:
        d, L, highest = framework(s, g, beta, q)
        assert {i for i, v in enumerate(L) if v == highest} == opt
        # The matrix determinant lemma, evaluated at its candidate optimum:
        # beta*q*sum_i w_i*g_i/(highest-d_i) <= 1,
        # with equality exactly for policies supported on optimal depths.
        policies = [[F(1) if i == j else F(0) for i in range(3)] for j in range(3)]
        policies += [[F(1,3)] * 3, [F(1,2), F(1,2), F(0)],
                     [F(0), F(1,2), F(1,2)], [F(1,2), F(0), F(1,2)]]
        for w in policies:
            criterion = beta*q*sum(w[i]*g[i]/(highest-d[i]) for i in range(3))
            assert criterion <= 1
            assert (criterion == 1) == all(w[i] == 0 for i in set(range(3))-opt)
            # Verify eigenvalue identity using exact rational determinant lemma
            import sympy as S
            mat = S.diag(*map(S.Rational,d)) + S.Matrix([list(map(S.Rational,w))]).T * S.Matrix([[S.Rational(beta*q*x) for x in g]])
            det = (S.Rational(highest)*S.eye(3) - mat).det()
            assert (det == 0) == (criterion == 1)
    assert framework(s,g,beta,F(1,4))[2] == F(37,40)
    assert framework(s,g,beta,F(3,4))[2] == F(47,40)


def sharp_families():
    for n in range(2, 17):
        delta = F(1, 8*n*n)
        a = [F(3,4)-delta*i*(i+1) for i in range(n)]
        b = [F(1,4)+2*delta*n*i for i in range(n)]
        g = [b[i]/(2-a[i]) for i in range(n)]
        assert all(0 < a[i] < 1 and 0 < g[i] < 1 for i in range(n))
        assert all(a[i] > a[i+1] and g[i] < g[i+1] for i in range(n-1))
        for i in range(n):
            q = F(2*i+1, 2*n)
            d, L, top = framework(a,g,F(2),q)
            assert L[i] == top and L.count(top) == 1
        for k in range(1,n):
            q = F(k,n)
            _, L, top = framework(a,g,F(2),q)
            assert {i for i,v in enumerate(L) if v == top} == {k-1,k}
        for i in range(n):
            for j in range(n):
                for q in [F(0),F(1,7),F(1,2),F(6,7),F(1)]:
                    li = a[i]+b[i]*q
                    lj = a[j]+b[j]*q
                    assert li-lj == delta*(i-j)*(2*n*q-(i+j+1))


if __name__ == '__main__':
    three_depths()
    sharp_families()
    print('PASS: three-depth exact determinant tests and sharp families n=2..16')
