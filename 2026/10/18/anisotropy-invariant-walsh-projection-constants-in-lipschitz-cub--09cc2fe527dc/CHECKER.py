"""Exact-arithmetic checks for weighted-Lipschitz Walsh projection constants.

Run: python CHECKER.py
Uses only the Python standard library; finite checks support, but do not replace, proof.
"""
from fractions import Fraction
from itertools import product
from math import comb


def sign(v):
    return -1 if v < 0 else 1


def spectral_constant(n, A, i):
    """Exact c_i from the Boolean derivative convolution kernel."""
    out = 0
    for z in product((-1, 1), repeat=n-1):
        K = 0
        for S in A:
            if i not in S:
                continue
            value = 1
            for j in S:
                if j != i:
                    value *= z[j if j < i else j-1]
            K += value
        out += abs(K)
    return Fraction(out, 2**(n-1))


def exact_test(n, A, weights):
    assert A and all(S for S in A)
    assert len(weights) == n and all(w > 0 for w in weights)
    cs = [spectral_constant(n, A, i) for i in range(n)]
    # These examples all have matching coordinate-shadow constants.
    assert len(set(cs)) == 1, (n, A, cs)
    i = weights.index(min(weights))
    vertices = tuple(product((-1, 1), repeat=n))
    v_index = {v: k for k, v in enumerate(vertices)}
    m = len(vertices)
    # Gradient-sign extremizer f(x)=w_i*x_i*sgn(K_i(x_{-i}))/2.
    def kval(x):
        out = 0
        for S in A:
            if i in S:
                prod = 1
                for j in S:
                    if j != i:
                        prod *= x[j]
                out += prod
        return out
    g = [v[i] * sign(kval(v)) for v in vertices]
    coeff_num = {}
    for S in A:
        coeff_num[S] = sum(g[t] * __import__('math').prod(vertices[t][j] for j in S) for t in range(m))
    pg_num = [sum(coeff_num[S] * __import__('math').prod(v[j] for j in S) for S in A) for v in vertices]
    # The unscaled g has Lipschitz seminorm 2/w_i.
    lip_g = Fraction(0)
    lip_pg = Fraction(0)
    for t, v in enumerate(vertices):
        for j in range(n):
            if v[j] == -1:
                other = list(v); other[j] = 1
                z = v_index[tuple(other)]
                lip_g = max(lip_g, Fraction(abs(g[t]-g[z]), weights[j]))
                lip_pg = max(lip_pg, Fraction(abs(pg_num[t]-pg_num[z]), m*weights[j]))
    assert lip_g == Fraction(2, weights[i]), (n, A, weights, lip_g)
    assert lip_pg / lip_g == cs[i], (n, A, weights, cs, lip_pg/lip_g)
    return cs[i]


def test():
    count = 0
    for n in range(2, 7):
        for degrees in [(d,) for d in range(1, n+1)] + [tuple(range(1, n+1)), tuple(d for d in range(1,n+1) if d % 2)]:
            A = tuple(frozenset(S) for size in degrees for S in __import__('itertools').combinations(range(n), size))
            for weights in [tuple(range(1,n+1)), tuple(range(n,0,-1)), tuple([1]+[7]*(n-1)), tuple([7]*(n-1)+[1])]:
                exact_test(n, A, weights)
                count += 1
    # 3-regular vertex-transitive Möbius ladder, not a union of full homogeneous levels.
    n = 6
    edges = {frozenset((i,(i+1)%6)) for i in range(n)} | {frozenset((i,(i+3)%6)) for i in range(3)}
    for weights in [(1,2,3,4,5,6), (10,7,8,3,6,4), (2,2,2,2,2,2)]:
        assert exact_test(n,tuple(edges),weights) == Fraction(3,2)
        count += 1
    # Check the Krawtchouk/binomial expression against direct kernels.
    for n in range(2,12):
        for d in range(1,n+1):
            from itertools import combinations
            A = tuple(frozenset(S) for S in combinations(range(n), d))
            if n <= 7:
                direct=spectral_constant(n,A,0)
            else:
                direct=None
            total=0
            for k in range(n):
                val=sum((-1)**j * comb(k,j)*comb(n-1-k,d-1-j) for j in range(d) if j<=k and d-1-j<=n-1-k)
                total += comb(n-1,k)*abs(val)
            K=Fraction(total,2**(n-1))
            if direct is not None:
                assert direct==K
            if d==2:
                assert K==Fraction((n-1)*comb(n-2,(n-2)//2), 2**(n-2))
    print('PASS: %d exact witness/edge checks; binomial formulas n<=11' % count)

if __name__ == '__main__':
    test()
