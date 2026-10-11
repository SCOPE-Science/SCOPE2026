"""Small finite checks for the exact unit-indexed Fourier eigenphase formulas.

Uses only the Python standard library.  Numerical matrices test a finite
set of parameters; the accompanying mathematical proof handles all odd moduli.
"""
import cmath
import math


def factor_prime_powers(n):
    ans = []
    rem = n
    p = 3
    while p * p <= rem:
        if rem % p == 0:
            q = 1
            k = 0
            while rem % p == 0:
                q *= p
                k += 1
                rem //= p
            ans.append((p, k, q))
        p += 2
    if rem != 1:
        ans.append((rem, 1, rem))
    return ans


def units(n):
    return [x for x in range(n) if math.gcd(x, n) == 1]


def matmul(a, b):
    n = len(a)
    return [[sum(a[i][t] * b[t][j] for t in range(n)) for j in range(n)]
            for i in range(n)]


def maxdiff(a, b):
    return max(abs(a[i][j] - b[i][j]) for i in range(len(a)) for j in range(len(a)))


def local_multiplicities(p, k, twist):
    """Dictionary eigenvalue -> multiplicity, with algebraic predictions."""
    if k > 1:
        h = (p - 1) * p ** (k - 2)
        r = (p - 1) * h
        assert r % 4 == 0
        return {0j: h, 1+0j: r//4, -1+0j: r//4,
                1j: r//4, -1j: r//4}
    symbol = pow(twist, (p - 1)//2, p)
    symbol = 1 if symbol == 1 else -1
    output = {-1/math.sqrt(p): 1}
    if p % 4 == 1:
        output.update({1+0j: (p-3+2*symbol)//4,
                       -1+0j: (p-3-2*symbol)//4,
                       1j: (p-1)//4, -1j: (p-1)//4})
    else:
        output.update({1+0j: (p-3)//4, -1+0j: (p-3)//4,
                       1j: (p-1+2*symbol)//4,
                       -1j: (p-1-2*symbol)//4})
    return output


def local_check(p, k, twist):
    q = p ** k
    uu = units(q)
    n = len(uu)
    A = [[cmath.exp(2j * math.pi * ((twist*x*y) % q) / q) / math.sqrt(q)
          for y in uu] for x in uu]
    A2 = matmul(A, A)
    # The normalized Ramanujan Gram matrix is exactly K.
    K = [[(float(x == y) - (1/p if k > 1 and x % (q//p) == y % (q//p) else 0))
          if k > 1 else (float(x == y) - 1/p) for y in uu] for x in uu]
    R = [[float((x+y) % q == 0) for y in uu] for x in uu]
    KR = matmul(K, R)
    assert maxdiff(A2, KR) < 1e-10, (p, k, twist, maxdiff(A2, KR))
    expected = local_multiplicities(p, k, twist)
    assert sum(expected.values()) == n
    for power in (1, 2, 3, 4):
        # The first four power sums distinguish the potential phase counts.
        tr = sum(A[i][i] for i in range(n))
        prediction = sum(mult * eigen**power for eigen, mult in expected.items())
        assert abs(tr-prediction) < 1e-9, (p, k, twist, power, tr, prediction)
        A = matmul(A, [[cmath.exp(2j * math.pi * ((twist*x*y) % q) / q) / math.sqrt(q)
                       for y in uu] for x in uu])
    return n


def crt_check(n):
    pieces = factor_prime_powers(n)
    pairs = units(n)
    for x in pairs:
        for y in pairs:
            identity = sum(pow(n//q, -1, q)*(n//q)*(x%q)*(y%q)
                           for p,k,q in pieces)
            assert (identity-x*y) % n == 0
    return len(pairs)**2


def main():
    local_cases = [(p,k,t) for p,k in ((3,1),(5,1),(7,1),(11,1),(13,1),
                                      (3,2),(3,3),(5,2),(7,2))
                   for t in (1,2) if math.gcd(t,p)==1]
    dimensions = sum(local_check(p,k,t) for p,k,t in local_cases)
    composites = [15,21,35,45,63,75,105]
    pair_count = sum(crt_check(n) for n in composites)
    print(f'VERIFY_OK local_cases={len(local_cases)} dimensions_sum={dimensions} '
          f'crt_pairs={pair_count} spectral_power_traces=PASS block_identity=PASS')


if __name__ == '__main__':
    main()
