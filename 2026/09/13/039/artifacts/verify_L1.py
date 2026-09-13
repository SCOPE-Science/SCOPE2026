"""Verification support for lane-1600 TARGET disproof.

Checks for L1 = x - (1+x)*Phi_2 + Phi_2^2 = (Phi_2 - x)(Phi_2 - 1):
  1. Coefficient identities from triangular factorization with u=1, v=x:
       (Phi - v)(Phi - u) = Phi^2 - (u(x^2)+v(x)) Phi + v(x) u(x).
  2. Truncated-series verification that F_N(x) = -sum_{k: 2^k < N} x^{2^k}
     satisfies F(x^2) = F(x) + x and L1(F) = 0 up to order N.

These are finite-order consistency checks supporting the analytic proof in
output/DRAFT.md (which proves the identities exactly as formal power series).
No external dependencies; pure Python.
"""

N = 200


def is_power_of_two(n):
    return n >= 1 and (n & (n - 1)) == 0


def main():
    # ---- 1. Factorization coefficient identities (as integer polys in x) ----
    # u(x) = 1, v(x) = x. Check u(x^2)+v(x) == 1+x and v(x)*u(x) == x.
    # Represent polynomials as dicts {exponent: coeff}.
    u = {0: 1}
    v = {1: 1}

    def compose_square(p):
        return {2 * e: c for e, c in p.items()}

    def add(p, q):
        r = dict(p)
        for e, c in q.items():
            r[e] = r.get(e, 0) + c
        return {e: c for e, c in r.items() if c != 0}

    def mul(p, q):
        r = {}
        for e1, c1 in p.items():
            for e2, c2 in q.items():
                r[e1 + e2] = r.get(e1 + e2, 0) + c1 * c2
        return {e: c for e, c in r.items() if c != 0}

    u_x2 = compose_square(u)          # u(x^2) = 1
    assert u_x2 == {0: 1}, u_x2
    s = add(u_x2, v)                  # should be 1 + x
    assert s == {0: 1, 1: 1}, s
    p = mul(v, u)                     # should be x
    assert p == {1: 1}, p
    # Hence (Phi-v)(Phi-u) = Phi^2 - (1+x) Phi + x, i.e. l0=x, l1=-(1+x), l2=1.
    print("factorization coefficients OK: l0=x, l1=-(1+x), l2=1")

    # ---- 2. Truncated series checks ----
    # F[n] = -1 if n = 2^k (k>=0), else 0, for 0 <= n < N.
    F = [0] * N
    for n in range(N):
        if is_power_of_two(n):
            F[n] = -1

    def F2(n):
        # coefficient of x^n in F(x^2): F[n/2] if n even else 0.
        if n % 2 == 1:
            return 0
        m = n // 2
        return F[m] if m < N else 0

    def F4(n):
        # coefficient of x^n in F(x^4): F[n/4] if 4|n else 0.
        if n % 4 != 0:
            return 0
        m = n // 4
        return F[m] if m < N else 0

    # Check F(x^2) - F(x) - x == 0 for n < N-1 (avoid truncation edge at top).
    for n in range(N - 1):
        rhs = 1 if n == 1 else 0
        assert F2(n) - F[n] - rhs == 0, ("inhomogeneous check failed at", n)
    print("inhomogeneous identity F(x^2)-F(x)=x OK to order", N - 1)

    # Check L1(F) = x*F - (1+x)*F(x^2) + F(x^4) == 0.
    # Coeff n: F[n-1] - F2[n] - F2[n-1] + F4[n] (with F[-1]:=0, F2[-1]:=0).
    for n in range(N - 1):
        t1 = F[n - 1] if n - 1 >= 0 else 0
        t2 = F2(n)
        t3 = F2(n - 1) if n - 1 >= 0 else 0
        t4 = F4(n)
        assert t1 - t2 - t3 + t4 == 0, ("L1 check failed at", n)
    print("operator identity L1(F)=0 OK to order", N - 1)
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
