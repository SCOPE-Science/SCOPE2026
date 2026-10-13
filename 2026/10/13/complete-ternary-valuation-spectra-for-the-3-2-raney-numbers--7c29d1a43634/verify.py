"""Reproducibility checks for the ternary Raney valuation-frequency theorem.

Uses only the Python standard library. Finite checks are corroboration,
not a proof of the all-index generating-function identity.
"""
from collections import Counter
from math import comb


def nu3_factorial(n):
    ans = 0
    while n:
        n //= 3
        ans += n
    return ans


def nu3_integer(n):
    ans = 0
    while n % 3 == 0:
        n //= 3
        ans += 1
    return ans


def nu3_via_factorials(n):
    return (nu3_factorial(3*n + 1)
            - nu3_factorial(2*n + 1)
            - nu3_factorial(n + 1))


def digit_sum_3(n):
    ans = 0
    while n:
        ans += n % 3
        n //= 3
    return ans


def nu3_via_digits(n):
    u = n + 1
    while u % 3 == 0:
        u //= 3
    s = digit_sum_3(2*u - 1)
    assert s % 2 == 1
    return (s - 1)//2


def add(*ps):
    r = [0] * max(len(p) for p in ps)
    for p in ps:
        for i, a in enumerate(p):
            r[i] += a
    while len(r) > 1 and r[-1] == 0:
        r.pop()
    return r


def mul(p, q):
    r = [0] * (len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i+j] += a*b
    while len(r) > 1 and r[-1] == 0:
        r.pop()
    return r


def scale(p, c):
    return [c*x for x in p]


def recurrence_polynomials(max_m):
    A = {1: [2], 2: [3,3]}
    for L in range(3, max_m+1):
        A[L] = add(scale(mul([1,1], A[L-1]), 2),
                   scale(mul([1,1,1], A[L-2]), -1))
    P = {0: [1]}
    for m in range(1, max_m+1):
        P[m] = add(P[m-1], A[m])
    return A, P


def check_all():
    max_m = 8
    N = 3**max_m
    A, P = recurrence_polynomials(12)
    checksum = 0
    for n in range(N):
        a = nu3_via_factorials(n)
        b = nu3_via_digits(n)
        assert a == b, (n, a, b)
        checksum += b
    for n in range(220):
        t = comb(3*n + 1, n)//(n + 1)
        assert nu3_integer(t) == nu3_via_digits(n)
    print(f"CHECK exact Raney integers n<220: PASS; factorial and digit valuations n<{N}: PASS; valuation_sum={checksum}")

    for m in range(9):
        hist = Counter(nu3_via_factorials(n) for n in range(3**m))
        coeffs = [hist.get(i, 0) for i in range(max(hist)+1)]
        assert coeffs == P[m], (m, coeffs, P[m])
        assert sum(P[m]) == 3**m
        assert P[m][0] == comb(m+2, 2)
        if m >= 2:
            assert len(P[m])-1 == m-1 and P[m][-1] == m+1
        print(f"CHECK m={m}: counts={coeffs}; recurrence=PASS; total=PASS")

    # The degree-three recurrence in m is equivalent to the claimed rational OGF.
    # (1-z)(1-2(1+q)z+(1+q+q^2)z^2)F=(1-qz)^2.
    E = [[1],[-3,-2],[3,3,1],[-1,-1,-1]]
    R = {0:[1], 1:[0,-2], 2:[0,0,1]}
    for m in range(13):
        lhs = add(*(mul(E[j],P[m-j]) for j in range(min(3,m)+1)))
        assert lhs == R.get(m,[0]), (m,lhs)
    print("CHECK rational generating identity to z^12 coefficientwise: PASS")

    # Exact r=2 count and fixed valuation-leading-degree validation.
    for m in range(13):
        want_j1 = 3*comb(m+2,4)-2*comb(m+1,4) if m>=2 else 0
        assert (P[m][1] if len(P[m])>1 else 0) == want_j1
    print("CHECK modulo-nine exact prefix formula for m=0..12: PASS")
    print("VERIFY_OK")

if __name__ == '__main__':
    check_all()
