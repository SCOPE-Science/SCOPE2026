"""Verify the Kl2 x quadratic-Kummer off-diagonal correlation bound.

For odd prime p, a in F_p^x, K(n) = Kl2(a*n;p) * chi(n) with K(0)=0,
C(h) = sum_{x in F_p} K(x) * conj(K(x+h))  (values are real).

Checks for each prime p in scope: for every nonzero shift h,
|C(h)| <= 6*sqrt(p)  (bad locus empty), and reports max |C(h)|/sqrt(p).

Classical (non-sheaf) definitions only; stdlib only.
"""
import cmath
import math


def primes_upto(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i:n + 1:i] = [False] * len(range(i * i, n + 1, i))
    return [i for i, v in enumerate(sieve) if v]


def check_prime(p, a=1):
    assert p % 2 == 1
    w = cmath.exp(2j * cmath.pi / p)
    # powers of w cached
    wp = [1.0 + 0.0j] * p
    for i in range(1, p):
        wp[i] = wp[i - 1] * w
    inv = [0] * p
    for u in range(1, p):
        inv[u] = pow(u, p - 2, p)
    sq = math.sqrt(p)

    def chi(x):
        x %= p
        if x == 0:
            return 0
        return 1 if pow(x, (p - 1) // 2, p) == 1 else -1

    # Normalized classical Kloosterman values Kl2(a*n), n != 0; K(0)=0.
    K = [0.0] * p
    for n in range(1, p):
        an = (a * n) % p
        s = 0j
        for u in range(1, p):
            v = (an * inv[u]) % p
            s += wp[(u + v) % p]
        K[n] = (s / sq).real * chi(n)
    K[0] = 0.0
    sqp = math.sqrt(p)
    worst = 0.0
    worst_h = 0
    bad = []
    for h in range(1, p):
        c = 0.0
        for x in range(p):
            c += K[x] * K[(x + h) % p]
        r = abs(c) / sqp
        if r > worst:
            worst = r
            worst_h = h
        if abs(c) > 6.0 * sqp + 1e-9:
            bad.append(h)
    return worst, worst_h, bad


def main():
    primes = [p for p in primes_upto(61) if p % 2 == 1]
    global_worst = 0.0
    global_loc = None
    all_ok = True
    for p in primes:
        worst, h, bad = check_prime(p)
        print("p=%d worst|C|/sqrt(p)=%.6f at h=%d bad=%s" % (p, worst, h, bad))
        if bad:
            all_ok = False
        if worst > global_worst:
            global_worst = worst
            global_loc = (p, h)
    print("global worst ratio: %.6f at %s" % (global_worst, global_loc))
    print("VERIFY_OK" if all_ok else "VERIFY_FAIL")


if __name__ == "__main__":
    main()
