"""Model verification for C: y^2 = f(x), f = x^5-5x^3+4x+1.
Self-contained GF(p) polynomial arithmetic (no sympy dependency for the
finite-field claims). Run: python3 verify_model.py
Checks:
  M1: disc(f) = 38569 exactly (integer resultant via Sylvester determinant,
      Fraction-free Bareiss), 38569 prime (trial division), hence smooth/QQ
      and good reduction away from 38569 (in particular good at 7).
  M2: f has no rational root (f(1)=f(-1)=1, monic so any integer root | 1);
      f mod 2 irreducible  -> f irreducible over QQ.
  M3: mod-p factorization degree patterns (Dedekind cycle types):
      2 -> [5], 7 -> [1,4], 11 -> [1,1,3], 19 -> [2,3]; each p not | disc.
"""
import math

F = [1, 0, -5, 0, 4, 1]  # coeffs degree 5 -> 0

def poly_mod_mul(a, b, p):
    r = [0]*(len(a)+len(b)-1)
    for i, ca in enumerate(a):
        for j, cb in enumerate(b):
            r[i+j] = (r[i+j] + ca*cb) % p
    return r

def poly_mod(a, b, p):
    # returns a mod b over GF(p); polys as low->high coeff lists
    a = [c % p for c in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    b = [c % p for c in b]
    db = len(b)-1
    inv = pow(b[-1], -1, p)
    while len(a)-1 >= db and not (len(a) == 1 and a[0] == 0):
        c = a[-1]*inv % p
        d = len(a)-1-db
        for i in range(db+1):
            a[d+i] = (a[d+i] - c*b[i]) % p
        while len(a) > 1 and a[-1] == 0:
            a.pop()
    return a

def poly_gcd(a, b, p):
    while not (len(b) == 1 and b[0] == 0):
        a, b = b, poly_mod(a, b, p)
    return a

def deg(a):
    d = len(a)-1
    while d > 0 and a[d] % 1 == 0 and a[d] == 0:
        d -= 1
    return d

def distinct_degree_factorization(f_lowhigh, p):
    """Squarefree assumed. Returns sorted list of factor degrees via
    distinct-degree factorization: g_i = gcd(x^{p^i}-x, h)."""
    x = [0, 1]
    h = [c % p for c in f_lowhigh]
    # x^{p^i} mod h by repeated Frobenius powering
    xp = list(x)  # x^{p^0} = x
    degs = []
    rem = [c % p for c in h]
    i = 0
    while True:
        i += 1
        # compute x^{p^i} mod h from x^{p^{i-1}}: raise to p-th power mod h
        if i == 1:
            base = list(x)
        else:
            base = list(xp)
        # base^p mod h
        res = [1]
        bb = list(base)
        e = p
        while e:
            if e & 1:
                res = poly_mod_mul(res, bb, p)
                res = poly_mod(res, h, p)
            bb = poly_mod_mul(bb, bb, p)
            bb = poly_mod(bb, h, p)
            e >>= 1
        xp = res
        diff = [(xp[k] if k < len(xp) else 0) - (x[k] if k < 2 else 0)
                for k in range(max(len(xp), 2))]
        diff = [c % p for c in diff]
        g = poly_gcd(diff, rem, p)
        d = len(g)-1 if not (len(g) == 1 and g[0] == 0) else 0
        if d > 0:
            assert d % i == 0, (p, i, d)
            degs += [i]*(d//i)
            # divide rem by g
            q, r = poly_divmod(rem, g, p)
            assert all(c == 0 for c in r), (p, i)
            rem = q
        if len(rem) == 1 and rem[0] != 0:
            break
        if len(rem) == 1 and rem[0] == 0:
            break
        assert i <= 6
    return sorted(degs)

def poly_divmod(a, b, p):
    a = [c % p for c in a]
    b = [c % p for c in b]
    db = len(b)-1
    inv = pow(b[-1], -1, p)
    q = [0]*max(1, len(a)-db)
    while len(a)-1 >= db and not (len(a) == 1 and a[0] == 0):
        c = a[-1]*inv % p
        d = len(a)-1-db
        q[d] = c
        for i in range(db+1):
            a[d+i] = (a[d+i] - c*b[i]) % p
        while len(a) > 1 and a[-1] == 0:
            a.pop()
    return q, a

def bareiss_det(M):
    n = len(M)
    A = [row[:] for row in M]
    prev = 1
    for k in range(n-1):
        if A[k][k] == 0:
            for i in range(k+1, n):
                if A[i][k] != 0:
                    A[k], A[i] = A[i], A[k]
                    break
        for i in range(k+1, n):
            for j in range(k+1, n):
                A[i][j] = (A[i][j]*A[k][k] - A[i][k]*A[k][j])//prev
            A[i][k] = 0
        prev = A[k][k]
    return A[n-1][n-1]

def resultant(f_hi_lo, g_hi_lo):
    # Sylvester matrix, polys high->low
    n, m = len(f_hi_lo)-1, len(g_hi_lo)-1
    N = n+m
    M = [[0]*N for _ in range(N)]
    for i in range(m):
        for j in range(n+1):
            M[i][i+j] = f_hi_lo[j]
    for i in range(n):
        for j in range(m+1):
            M[m+i][i+j] = g_hi_lo[j]
    return bareiss_det(M)

def is_prime(n):
    import math
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = math.isqrt(n)
    k = 3
    while k <= r:
        if n % k == 0:
            return False
        k += 2
    return True

def main():
    f_hi = [1, 0, -5, 0, 4, 1]
    fp_hi = [5, 0, -15, 0, 4]
    res = resultant(f_hi, fp_hi)
    print("resultant(f,f') =", res)
    assert res == 38569
    print("38569 prime:", is_prime(38569))
    assert is_prime(38569)
    # rational roots: monic => integer root divides 1
    fv = lambda v: v**5 - 5*v**3 + 4*v + 1
    print("f(1) =", fv(1), "f(-1) =", fv(-1))
    assert fv(1) == 1 and fv(-1) == 1
    f_low = [1, 4, 0, -5, 0, 1]  # low->high
    for p in [2, 7, 11, 19]:
        assert 38569 % p != 0, p
        fac = distinct_degree_factorization(f_low, p)
        print(f"mod {p}: factor degrees {fac}")
    assert distinct_degree_factorization(f_low, 2) == [5]
    assert distinct_degree_factorization(f_low, 7) == [1, 4]
    assert distinct_degree_factorization(f_low, 11) == [1, 1, 3]
    assert distinct_degree_factorization(f_low, 19) == [2, 3]
    print("VERIFY_MODEL_OK")

if __name__ == "__main__":
    main()
