from fractions import Fraction
from bisect import bisect_right


def rho(x):
    return Fraction(x, x + 1)


def upper_bound(t, m):
    """Largest integer x>=1 with (x/(x+1))^m <= t, for 0<t<1."""
    if not (0 < t < 1):
        return None
    lo, hi = 1, 2
    while rho(hi) ** m <= t:
        lo, hi = hi, 2 * hi
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if rho(mid) ** m <= t:
            lo = mid
        else:
            hi = mid
    return lo


def primes_up_to(n):
    sieve = bytearray(b'\x01') * (n + 1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    p = 2
    while p * p <= n:
        if sieve[p]:
            sieve[p*p:n+1:p] = b'\x00' * (((n - p*p) // p) + 1)
        p += 1
    return [i for i in range(2, n + 1) if sieve[i]]


def i_components_up_to(limit):
    out = set()
    for p in primes_up_to(limit):
        e = 1
        while True:
            x = p ** e
            if x > limit:
                break
            out.add(x)
            e *= 2
    return sorted(out)


def is_prime_64(n):
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        s += 1
        d //= 2
    # Deterministic Miller-Rabin bases for n < 2^64.
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def iroot(n, e):
    lo, hi = 1, 1 << ((n.bit_length() + e - 1) // e)
    if hi ** e <= n:
        while hi ** e <= n:
            lo, hi = hi, 2 * hi
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid ** e <= n:
            lo = mid
        else:
            hi = mid
    return lo


def is_i_component(n):
    if n < 2 or n >= 2**64:
        return False
    e = 1
    while (2 ** e) <= n:
        q = iroot(n, e)
        if q ** e == n and is_prime_64(q):
            return True
        e *= 2
    return False


H = tuple(range(6, 16))
targets = {h: Fraction(h, 16) for h in H}

# Establish finite search bounds successively from the monotonicity inequality.
u1 = max(upper_bound(targets[h], 4) for h in H)
C1 = i_components_up_to(u1)

u2 = 0
for h in H:
    for x1 in C1:
        if rho(x1) ** 4 > targets[h]:
            continue
        t1 = targets[h] / rho(x1)
        if t1 < 1:
            u = upper_bound(t1, 3)
            if u is not None:
                u2 = max(u2, u)
C2 = i_components_up_to(u2)

u3 = 0
for h in H:
    for x1 in C1:
        if rho(x1) ** 4 > targets[h]:
            continue
        t1 = targets[h] / rho(x1)
        if not (0 < t1 < 1):
            continue
        stop2 = bisect_right(C2, upper_bound(t1, 3))
        for x2 in C2[:stop2]:
            if x2 <= x1:
                continue
            t2 = t1 / rho(x2)
            if 0 < t2 < 1:
                u = upper_bound(t2, 2)
                if u is not None:
                    u3 = max(u3, u)
C3 = i_components_up_to(u3)

solutions = []
integer_last_candidates = []
branch_counts = {h: 0 for h in H}
for h in H:
    T = targets[h]
    stop1 = bisect_right(C1, upper_bound(T, 4))
    for x1 in C1[:stop1]:
        t1 = T / rho(x1)
        if not (0 < t1 < 1):
            continue
        stop2 = bisect_right(C2, upper_bound(t1, 3))
        for x2 in C2[:stop2]:
            if x2 <= x1:
                continue
            t2 = t1 / rho(x2)
            if not (0 < t2 < 1):
                continue
            stop3 = bisect_right(C3, upper_bound(t2, 2))
            for x3 in C3[:stop3]:
                if x3 <= x2:
                    continue
                branch_counts[h] += 1
                t3 = t2 / rho(x3)
                if not (0 < t3 < 1):
                    continue
                z = t3 / (1 - t3)  # unique possible fourth component
                if z.denominator != 1:
                    continue
                x4 = z.numerator
                integer_last_candidates.append(x4)
                if x4 <= x3 or not is_i_component(x4):
                    continue
                xs = (x1, x2, x3, x4)
                n = x1 * x2 * x3 * x4
                # Independent direct exact check of the defining mean.
                mean = Fraction(16, 1)
                for x in xs:
                    mean *= rho(x)
                assert mean == h
                solutions.append((n, h, xs))

solutions.sort()
assert all(x < 2**64 for x in integer_last_candidates)
print('J=4 infinitary harmonic classification')
print('harmonic means tested:', H)
print('successive universal bounds for x1,x2,x3:', u1, u2, u3)
print('branches after choosing three I-components:', sum(branch_counts.values()))
print('integer fourth-component candidates:', len(integer_last_candidates))
print('largest integer fourth-component candidate:', max(integer_last_candidates))
print('solutions (N, H_infty(N), ordered I-components):')
for row in solutions:
    print(row)
print('count:', len(solutions))
