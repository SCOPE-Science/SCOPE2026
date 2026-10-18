"""Exact-arithmetic reproduction for volume-sampled hard constraints.

Requires Python 3 and SymPy. Run: python CHECK.py
"""
from itertools import combinations
from math import comb
import random
import sympy as sp


def check(A, b, k):
    m, n = A.shape
    assert m > n >= 2 and b.shape == (m, 1) and 1 <= k < n
    G = A.T * A
    assert G.det() != 0
    x_star = G.inv() * A.T * b
    r = b - A*x_star
    z = (r.T*r)[0]
    assert z > 0 and A.T*r == sp.zeros(n, 1)
    H = A*G.inv()*A.T
    Q = H + (r*r.T)/z
    assert H*H == H and Q*Q == Q
    weight_total, weighted_excess, singular_augmented = 0, 0, 0
    raw_augmented_total = 0
    checks = 0
    for S in combinations(range(m), k):
        J = list(S)
        B = H.extract(J, J)
        R = Q.extract(J, J)
        d, dplus = B.det(), R.det()
        raw_augmented_total += dplus
        assert d >= 0 and dplus >= 0
        checks += 2
        if d:
            weight_total += d
            As = A.extract(J, list(range(n)))
            rs = r.extract(J, [0])
            delta = G.inv()*As.T*B.inv()*rs
            xs = x_star + delta
            assert As*xs == b.extract(J, [0])
            excess = ((A*xs-b).T*(A*xs-b))[0] - z
            assert sp.simplify(excess - (rs.T*B.inv()*rs)[0]) == 0
            assert sp.simplify(dplus-d*(1+excess/z)) == 0
            weighted_excess += d*excess
            checks += 3
        else:
            singular_augmented += dplus
    normalization = sp.binomial(n,k)
    assert weight_total == normalization
    assert raw_augmented_total == sp.binomial(n+1,k)
    excess_avg = weighted_excess/normalization
    predicted = z*(sp.Rational(k, n-k+1)-singular_augmented/normalization)
    assert sp.simplify(excess_avg-predicted) == 0
    assert excess_avg >= 0 and excess_avg <= z*sp.Rational(k,n-k+1)
    return checks+5, excess_avg, z, singular_augmented


def full_spark_example(n, k):
    # Distinct points make every k-subset of the Vandermonde rows independent.
    m = n+1
    A = sp.Matrix([[sp.Integer(t)**j for j in range(n)] for t in range(m)])
    b = sp.eye(m)[:, 0]
    cnt, excess, z, bad = check(A, b, k)
    assert bad == 0 and excess == z*sp.Rational(k, n-k+1)
    return cnt+1


def lower_example(n, k):
    A = sp.eye(n).col_join(sp.zeros(1,n))
    b = sp.eye(n+1)[:,n]
    cnt, excess, z, bad = check(A, b, k)
    assert z == 1 and excess == 0
    return cnt+1


def duplicate_example():
    A = sp.Matrix([[1,0,0],[1,0,0],[0,1,0],[0,0,1],[1,1,1]])
    b = sp.Matrix([1,0,4,2,0])
    cnt, excess, z, bad = check(A, b, 2)
    assert (excess, z, bad) == (sp.Rational(87,7), sp.Rational(88,7), sp.Rational(3,88))
    return cnt+1


def main():
    total = duplicate_example()
    for n in range(2,5):
        for k in range(1,n):
            total += full_spark_example(n,k)
            total += lower_example(n,k)
    rng = random.Random(3719)
    used = 0
    for n,m in [(2,3),(2,5),(3,4),(3,6),(4,5),(4,6)]:
        for attempt in range(10):
            A = sp.Matrix([[rng.randrange(-3,4) for _ in range(n)] for _ in range(m)])
            if (A.T*A).det() == 0:
                continue
            b = sp.Matrix([rng.randrange(-4,5) for _ in range(m)])
            rr = b-A*(A.T*A).inv()*A.T*b
            if (rr.T*rr)[0] == 0:
                continue
            for k in range(1,n):
                cnt, _, _, _ = check(A,b,k)
                total += cnt
            used += 1
    print(f"PASS: {total} exact determinant, constraint, objective and bound checks across {used} random admissible designs, explicit full-support, zero-row, and dependent-row cases")

if __name__ == '__main__':
    main()
