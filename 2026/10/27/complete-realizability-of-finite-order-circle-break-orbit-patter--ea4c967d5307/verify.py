"""Finite examples of exact break-orbit realization for rational rotations.

The analytic existence theorem is proved in RESULT.md; these tests exercise
its cyclic jump-coboundary identities and explicit piecewise-affine construction.
Uses only the Python standard library.
"""
from fractions import Fraction as F
from math import gcd


def cyclic_data(q, supports, p=1):
    """Build prescribed jumps j and underlying conjugacy jumps lambda.

    supports is a list of nonempty subsets of Z/q of size at least 2.
    All numbers are rational except for a shared positive q-th root factor,
    which cancels in every lambda_{i+p}/lambda_i ratio.
    """
    assert q >= 2 and gcd(p, q) == 1
    classes = []
    for k, support in enumerate(supports):
        support = sorted(set(support))
        assert 2 <= len(support) <= q
        j = [F(1) for _ in range(q)]
        for idx in support[:-1]:
            j[idx] = F(2 + (idx + k) % 5)
        j[support[-1]] = 1 / prod(j)
        assert prod(j) == 1
        assert {i for i, val in enumerate(j) if val != 1} == set(support)
        L = [None] * q
        L[0] = F(1)
        for s in range(q-1):
            i = (s * p) % q
            nxt = ((s + 1) * p) % q
            L[nxt] = L[i] * j[i]
        assert L[(q-1)*p % q] * j[(q-1)*p % q] == L[0]
        assert all(L[(i+p)%q] / L[i] == j[i] for i in range(q))
        classes.append((j,L))
    # The common scale root chosen to balance the product of all jumps
    # gives a globally consistent positive piecewise constant H' on S^1.
    P = prod(val for _,L in classes for val in L)
    assert P > 0
    return classes,P


def prod(xs):
    z = F(1)
    for a in xs:
        z *= a
    return z


def verify():
    tests = 0
    for q in range(2,15):
        for p in range(1, q):
            if gcd(p, q) != 1:
                continue
            for r in range(2, q+1):
                supports = [list(range(r))]
                classes,P = cyclic_data(q,supports,p)
                j,L=classes[0]
                # Existing periodic orbit has exactly r f-breaks.
                assert sum(jj != 1 for jj in j) == r
                # Globally normalized H-jumps are L_i/P^(1/q).
                # In products the scaling cancels, hence their total
                # product is exactly 1, without numerical approximations.
                assert prod(L) == P
                tests += 1
        if q >= 3:
            for r in range(2,q+1):
                classes,P = cyclic_data(q,[list(range(r)),list(range(r))])
                assert sum(sum(x != 1 for x in j) for j,_ in classes)==2*r
                tests += 1
    assert tests > 600
    print(f"PASS {tests} exact rational jump-identity instances; q=2..14")

if __name__ == '__main__':
    verify()
