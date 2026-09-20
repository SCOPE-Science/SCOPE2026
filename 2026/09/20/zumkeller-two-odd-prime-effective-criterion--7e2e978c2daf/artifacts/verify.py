from math import isqrt


def is_prime(n: int) -> bool:
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


def sigma_n(a: int, p: int, q: int) -> int:
    M = (1 << (a + 1)) - 1
    return M * (p + 1) * (q + 1)


def structural(a: int, p: int, q: int):
    M = (1 << (a + 1)) - 1
    if p <= M:
        return True, None
    u, v = p - M, q - M
    B = M * (M + 1)
    if u * v > B:
        return False, None
    D = (B - u * v) // 2
    for z in range(M + 1):
        r = D - q * z
        if r < 0:
            break
        ylo = max(0, (r - M + p - 1) // p)
        yhi = min(M, r // p)
        if ylo <= yhi:
            y = ylo
            x = r - p * y
            return True, (x, y, z, D)
    return False, (None, None, None, D)


def direct_zumkeller(a: int, p: int, q: int) -> bool:
    n = (1 << a) * p * q
    sig = sigma_n(a, p, q)
    if sig % 2:
        return False
    target = sig // 2
    divs = []
    for i in range(a + 1):
        t = 1 << i
        for ep in (0, 1):
            for eq in (0, 1):
                d = t * (p if ep else 1) * (q if eq else 1)
                divs.append(d)
    # Exact subset-sum bitset over all divisors.
    bits = 1
    for d in divs:
        bits |= bits << d
    return ((bits >> target) & 1) == 1


def candidates(a: int):
    M = (1 << (a + 1)) - 1
    B = M * (M + 1)
    out = []
    # For p>M and p<q, u=p-M satisfies u^2 < B.
    umax = isqrt(B - 1)
    for u in range(1, umax + 1):
        p = M + u
        if not is_prime(p):
            continue
        qmax = M + B // u
        start = p + 2
        if start % 2 == 0:
            start += 1
        for q in range(start, qmax + 1, 2):
            if not is_prime(q):
                continue
            v = q - M
            if u * v <= B:
                out.append((p, q))
    return out

EXPECTED_FAILURES = {
    1: [],
    2: [(11, 17)],
    3: [(19, 67), (23, 41)],
    4: [(37, 173), (43, 101), (43, 107), (47, 83), (47, 89), (53, 67), (53, 73)],
}

for a in range(1, 5):
    M = (1 << (a + 1)) - 1
    cs = candidates(a)
    failures = []
    mismatches = []
    certs = 0
    for p, q in cs:
        s, cert = structural(a, p, q)
        d = direct_zumkeller(a, p, q)
        if s != d:
            mismatches.append((p, q, s, d))
        if s:
            certs += 1
        else:
            D = (M * (M + 1) - (p - M) * (q - M)) // 2
            failures.append((p, q, D))
    got_pairs = [(p, q) for p, q, _ in failures]
    assert got_pairs == EXPECTED_FAILURES[a], (a, got_pairs)
    assert not mismatches, (a, mismatches)
    print(f"a={a} M={M} p>M abundant_candidates={len(cs)} criterion_pass={certs} criterion_fail={len(failures)} direct_mismatches=0")
    if failures:
        print("  exceptions=" + ", ".join(f"({p},{q};D={D})" for p, q, D in failures))

# Supplementary direct checks in the automatic p<=M region.
for a in range(1, 5):
    M = (1 << (a + 1)) - 1
    checked = 0
    bad = []
    ps = [p for p in range(3, M + 1, 2) if is_prime(p)]
    qs = [q for q in range(3, 500, 2) if is_prime(q)]
    for p in ps:
        for q in qs:
            if q <= p:
                continue
            checked += 1
            if not direct_zumkeller(a, p, q):
                bad.append((p, q))
    assert not bad, (a, bad[:5])
    print(f"automatic_region_sample a={a} p<=M q<500 checked={checked} direct_failures=0")
