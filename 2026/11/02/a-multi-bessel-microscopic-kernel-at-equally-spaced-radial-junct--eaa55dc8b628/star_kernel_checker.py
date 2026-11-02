"""Standalone exact-arithmetic checks of a q-ray polynomial kernel formula.

Run with Python 3: python3 star_kernel_checker.py
These checks test finitely many instances; the locally uniform limit is proved analytically.
"""
from fractions import Fraction as Q
from math import gamma


def rising(a, n):
    ans = Q(1)
    for k in range(n):
        ans *= a + k
    return ans


def factorial(n):
    ans = 1
    for k in range(2, n + 1):
        ans *= k
    return ans


def shifted_jacobi(j, a, t):
    # P_j^(0,a-1)(2t-1)=(-1)^j(a)_j/j! * 2F1(-j,j+a;a;t).
    term = Q(1)
    val = term
    for k in range(1, j + 1):
        term *= Q(-j + k - 1) * (j + a + k - 1) * t
        term /= (a + k - 1) * k
        val += term
    return (-1)**j * rising(a, j) * val / factorial(j)


def inverse(mat):
    n = len(mat)
    a = [r[:] + [Q(int(j == k)) for k in range(n)] for j, r in enumerate(mat)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if a[i][k])
        a[k], a[pivot] = a[pivot], a[k]
        x = a[k][k]
        a[k] = [z / x for z in a[k]]
        for i in range(n):
            if i != k:
                x = a[i][k]
                a[i] = [u - x * v for u, v in zip(a[i], a[k])]
    return [r[n:] for r in a]


def kernel_from_jacobi(q, n, z, w):
    result = Q(0)
    for h in range(min(q, n+1)):
        a = Q(2*h+1, q)
        for j in range((n-h)//q + 1):
            result += q * z**h * w**h * (2*j+a) * shifted_jacobi(j, a, z**q) * shifted_jacobi(j, a, w**q)
    return result


def center_formula(q, n):
    m = n // q
    return (rising(Q(1) + Q(1,q), m) / factorial(m))**2


def run():
    tests = 0
    for q in (2, 3, 4, 5, 7):
        for n in range(0, 13):
            gram = [[Q(1, j+k+1) if ((j-k) % q == 0) else Q(0)
                     for k in range(n+1)] for j in range(n+1)]
            gi = inverse(gram)
            assert gi[0][0] == center_formula(q,n)
            tests += 1
            if n <= 9:
                for z, w in ((Q(1,3), Q(-1,4)), (Q(0), Q(1,5))):
                    k_direct = sum(z**j * gi[j][k] * w**k for j in range(n+1) for k in range(n+1))
                    k_jacobi = kernel_from_jacobi(q,n,z,w)
                    assert k_direct == k_jacobi, (q,n,z,w)
                    tests += 1
    # Limit at the junction, from a closed gamma quotient, with no floating cancellation.
    for q in (3,4,6):
        a=1.0/q
        target=1.0 / gamma(1+a)**2
        for m in (200, 2000, 20000):
            value = (gamma(1+a)**-2) * __import__('math').exp(2 * (__import__('math').lgamma(m+1+a)-__import__('math').lgamma(m+1)-a*__import__('math').log(m)))
            assert abs(value/target-1) < 0.012, (q,m,value,target)
            tests += 1
    print(f"PASS: {tests} exact and asymptotic finite checks")


if __name__ == '__main__':
    run()
