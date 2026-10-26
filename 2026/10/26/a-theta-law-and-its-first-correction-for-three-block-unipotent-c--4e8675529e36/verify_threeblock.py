#!/usr/bin/env python3
"""Independent finite-field checks for commuting three-block unipotent groups.

This checker uses only the standard library.  Run with Python 3.9+.
"""
import itertools
import math
from decimal import Decimal, localcontext


def mul(a, b, q):
    if q != 4:
        return (a * b) % q
    if not a or not b:
        return 0
    # F4=F2[u]/(u^2+u+1); 2 denotes u, 3 denotes u+1.
    if a == 1:
        return b
    if b == 1:
        return a
    if a == b:
        return 3 if a == 2 else 2
    return 1


def add(a, b, q):
    return (a ^ b) if q == 4 else (a + b) % q


def product_zero(x, y, q, n):
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(n):
                s = add(s, mul(x[i*n+k], y[k*n+j], q), q)
            if s:
                return False
    return True


def inverse(a, q):
    if a == 0:
        raise ZeroDivisionError
    if q == 4:
        return {1: 1, 2: 3, 3: 2}[a]
    return pow(a, -1, q)


def rank(mat, q, n):
    A = [list(mat[i*n:(i+1)*n]) for i in range(n)]
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, n) if A[i][c]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        inv = inverse(A[r][c], q)
        A[r] = [mul(inv, z, q) for z in A[r]]
        for i in range(n):
            if i != r and A[i][c]:
                a = A[i][c]
                A[i] = [add(A[i][j], (-mul(a, A[r][j], q) if q != 4 else mul(a, A[r][j], q)), q)
                        for j in range(n)]
        r += 1
    return r


def gaussian(n, k, q):
    if not 0 <= k <= n:
        return 0
    num, den = 1, 1
    for i in range(k):
        num *= q**n - q**i
        den *= q**k - q**i
    assert num % den == 0
    return num // den


def square_rank_count(n, s, q):
    return gaussian(n, s, q)*math.prod(q**n-q**j for j in range(s))


def direct(q):
    n = 2
    matrices = list(itertools.product(range(q), repeat=n*n))
    predicted = [square_rank_count(n, r, q)*q**(n*(n-r)) for r in range(n+1)]
    got = [0]*(n+1)
    for x in matrices:
        r = rank(x, q, n)
        for y in matrices:
            if product_zero(x, y, q, n):
                got[r] += 1
    assert got == predicted, (q, got, predicted)
    print(f"direct q={q} n=2 independent_pairs={q**8} zero_product={sum(got)} strata={got} OK")



def direct_conjugacy_classes(q):
    # Independent class-orbit enumeration in the (2,1,2) unipotent group.
    # Conjugating fixes A, B, and translates C by the image of
    # (A_prime,B_prime) -> A_prime B - A B_prime.
    choices = list(itertools.product(range(q), repeat=4))
    total_classes = 0
    for a0,a1,b0,b1 in choices:
        shifts = set()
        for c0,c1,d0,d1 in choices:
            left = (mul(c0,b0,q),mul(c0,b1,q),mul(c1,b0,q),mul(c1,b1,q))
            right = (mul(a0,d0,q),mul(a0,d1,q),mul(a1,d0,q),mul(a1,d1,q))
            delta = tuple(add(x, (y if q==4 else -y), q) for x,y in zip(left,right))
            shifts.add(delta)
        assert q**4 % len(shifts) == 0
        total_classes += q**4//len(shifts)
    predicted = sum(square_rank_count(2,s,q)*q**(2*(2-s)) for s in range(3))
    assert total_classes == predicted
    print(f"direct_conjugacy q={q} dimension=5 unipotent_elements={q**8} classes={total_classes} OK")

def rank_histogram(q, n):
    hist = [0]*(n+1)
    for x in itertools.product(range(q), repeat=n*n):
        hist[rank(x, q, n)] += 1
    predicted = [square_rank_count(n, s, q) for s in range(n+1)]
    assert hist == predicted
    joint = [hist[s]*q**(n*(n-s)) for s in range(n+1)]
    print(f"rank_histogram q={q} n={n} X_count={q**(n*n)} rank_counts={hist} zero_product={sum(joint)} OK")


def phi(q, n):
    return math.prod(1-q**(-j) for j in range(1, n+1))


def asymptotic():
    # High precision is important: the second-order error can be much smaller
    # than double-precision roundoff when the matrix dimension is large.
    with localcontext() as ctx:
        ctx.prec = 90
        for q in (2, 3, 4):
            Q = Decimal(q)
            def phid(j):
                z = Decimal(1)
                for i in range(1, j+1):
                    z *= 1-Q**(-i)
                return z
            pinf = phid(240)
            theta = sum((Q**(-t*t) for t in range(-24, 25)), Decimal(0))
            xi = sum((Q**(-t*t+t) for t in range(-24, 25)), Decimal(0))
            for m in (3, 5, 8, 12, 20):
                n = 2*m
                weights = [(t,Q**(-t*t)*phid(n)**2/(phid(m+t)*phid(m-t)**2))
                           for t in range(-m,m+1)]
                scaled = sum((w for _,w in weights), Decimal(0))
                leading = theta/pinf
                corrected = (theta - 3*Q**(-m)*xi/(q-1))/pinf
                residual = (scaled-corrected)*Q**(2*m)
                if m >= 5:
                    assert abs(residual) < 100
                conditional_mean = sum((t*w for t,w in weights), Decimal(0))/scaled
                first_mean = -xi/(2*(q-1)*theta)*Q**(-m)
                if m >= 5:
                    assert abs(conditional_mean-first_mean)*Q**(2*m) < 100
                print(f"asymptotic q={q} m={m} scaled={scaled:.13g} leading={leading:.13g} corrected={corrected:.13g}"
                      f" residual_times_q2m={residual:.6g} mean={conditional_mean:.12g}"
                      f" first_mean={first_mean:.12g}")


def main():
    for q in (2,3,4):
        direct(q)
        direct_conjugacy_classes(q)
    rank_histogram(2,4)
    asymptotic()
    print("THREE_BLOCK_COMMUTING_THETA_CHECKS_PASSED")


if __name__ == '__main__':
    main()
