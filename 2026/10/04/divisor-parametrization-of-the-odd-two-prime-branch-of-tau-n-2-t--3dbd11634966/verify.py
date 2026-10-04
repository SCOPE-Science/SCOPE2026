#!/usr/bin/env python3
from math import isqrt

TMAX = 20

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def divisors(n):
    out = []
    r = isqrt(n)
    for d in range(1, r + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)

def tau(n):
    return len(divisors(n))

def parametrized(t, branch=False):
    N = 3 * (2 * t - 1)
    out = []
    for d in divisors(N):
        if d <= 1:
            continue
        a = 3 * t - 2 - N // d
        b = d - 2
        if a < 0 or b < 0:
            continue
        if branch and not (a >= 2 and b >= 2):
            continue
        out.append((a, b, d))
    return out

def brute(t):
    # For t <= 20, every solution has
    # 0 <= a <= 3t-3 and 1 <= b <= 3(2t-1)-2.
    A = max(0, 3 * t - 3)
    B = max(0, 3 * (2 * t - 1) - 2)
    out = []
    for a in range(A + 1):
        for b in range(B + 1):
            if a * b + 2 * a + 2 * b + 1 == 3 * b * t:
                out.append((a, b))
    return sorted(out)

def main():
    prime_t = []
    branch_rows = []
    for t in range(TMAX + 1):
        P = 2 * (3 ** t) + 1
        pflag = is_prime(P)
        if pflag:
            prime_t.append(t)

        if t == 0:
            assert brute(t) == []
            continue

        got = sorted((a, b) for a, b, _ in parametrized(t))
        want = brute(t)
        assert got == want, (t, got, want)
        assert len(got) == tau(3 * (2 * t - 1)) - 1

        branch = parametrized(t, branch=True)
        assert len(branch) == tau(3 * (2 * t - 1)) - 2
        for a, b, d in branch:
            assert d > 3
            assert a >= 2 and b >= 2
            assert a * b + 2 * a + 2 * b + 1 == 3 * b * t
            if pflag:
                # Direct exponent-count verification:
                # tau(n^2)=(2a+1)(2b+1);
                # phi(n)=2^2*3^(a+t-1)*P^(b-1).
                lhs = (2 * a + 1) * (2 * b + 1)
                rhs = 3 * (a + t) * b
                assert lhs == rhs
                branch_rows.append((t, P, a, b, d))

    assert prime_t == [0, 1, 2, 4, 5, 6, 9, 16, 17]

    # Source example and its second forced companion at t=5.
    t5 = sorted((a, b, d) for a, b, d in parametrized(5, branch=True))
    assert t5 == [(10, 7, 9), (12, 25, 27)]

    print("VERIFY_OK")
    print("checked_t_max=" + str(TMAX))
    print("prime_exponents_through_20=" + ",".join(map(str, prime_t)))
    print("t5_branch=(10,7,d=9);(12,25,d=27)")
    print("prime_branch_rows_checked=" + str(len(branch_rows)))

if __name__ == "__main__":
    main()
