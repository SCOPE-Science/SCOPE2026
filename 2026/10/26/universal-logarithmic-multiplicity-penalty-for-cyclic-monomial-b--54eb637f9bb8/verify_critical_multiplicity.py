"""Numerical and exact-algebra checks for the critical boundary-zero multiplicity formula.

All tests are supplementary to the proof in RESULT.md. Standard Python library only.
"""
from fractions import Fraction
from math import factorial, gamma, pi, sqrt, prod, log, lgamma, exp, isfinite


def solve(A, b):
    n = len(b)
    M = [list(row) + [b[i]] for i, row in enumerate(A)]
    for j in range(n):
        pivot = max(range(j, n), key=lambda i: abs(M[i][j]))
        assert M[pivot][j] != 0
        M[j], M[pivot] = M[pivot], M[j]
        p = M[j][j]
        for k in range(j, n + 1):
            M[j][k] /= p
        for i in range(n):
            if i != j:
                p = M[i][j]
                for k in range(j, n + 1):
                    M[i][k] -= p * M[j][k]
    return [M[i][n] for i in range(n)]


def harmonic(n):
    return sum(Fraction(1, j) for j in range(1, n + 1))


# Exact rational Cauchy/Hilbert Schur complement identity.
for r in range(2, 10):
    b = [Fraction(1, i) for i in range(1, r)]
    H = [[Fraction(1, i + j) for j in range(1, r)]
         for i in range(1, r)]
    q = solve(H, b)
    assert sum(b[i] * q[i] for i in range(r - 1)) == 2 * harmonic(r - 1)


def constants(n, a):
    m, d = len(a), sum(a)
    alpha = n - Fraction(m-1, 2)
    C = factorial(n-1) * (2*pi)**((m-1)/2) * sqrt(prod(a)) * d**(1-m/2)
    return float(alpha), C


def weight_inverse_sequence(n, a, maxK):
    alpha, _ = constants(n, a)
    d = sum(a)
    # First term of w_k=(n+dk)^alpha (n-1)! c^(2k) prod (a_j k)! / (n-1+dk)!.
    w = float(n)**alpha
    inv = [1/w]
    logc2 = d*log(d) - sum(j*log(j) for j in a)
    for k in range(maxK):
        logratio = alpha*log((n+d*(k+1))/(n+d*k)) + logc2
        for j in a:
            for h in range(1, j+1):
                logratio += log(j*k+h)
        for h in range(1, d+1):
            logratio -= log(n-1+d*k+h)
        w *= exp(logratio)
        inv.append(1/w)
    return inv


def inverse_error(inv, K, r):
    L = K+r
    p = r-1
    A = sum(inv[:L+1])
    if not p:
        return A  # the reciprocal of the minimum squared error
    v = [sum(inv[k]*(k/L)**i for k in range(L+1)) for i in range(1,r)]
    B = [[sum(inv[k]*(k/L)**(i+j) for k in range(L+1))
          for j in range(1,r)] for i in range(1,r)]
    x = solve(B,v)
    return A-sum(v[i]*x[i] for i in range(p))


# Verify several unrelated dimensions and monomial exponent patterns.
for n,a in [(2,(1,1)),(3,(1,2)),(4,(2,3,1))]:
    alpha, C=constants(n,a)
    inv=weight_inverse_sequence(n,a,20004)
    # Uniform coefficient limit in the Stirling expansion.
    assert abs(C*20000*inv[20000]-1)<0.002
    for r in (2,3,4):
        k=20000
        actual = C*(inverse_error(inv,k,r)-inverse_error(inv,k,1))
        target = -2*float(harmonic(r-1))
        assert abs(actual-target)<0.06,(n,a,r,actual,target)
        assert isfinite(actual)
print('CHECK_OK: exact Cauchy identities r=2..9 and 9 independent 20000-degree asymptotic tests')
