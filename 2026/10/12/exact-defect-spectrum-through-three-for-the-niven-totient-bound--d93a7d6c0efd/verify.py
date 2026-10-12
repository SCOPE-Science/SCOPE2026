LIMIT = 1_000_000


def build_spf(n):
    spf = list(range(n + 1))
    if n >= 1:
        spf[1] = 1
    for i in range(2, int(n ** 0.5) + 1):
        if spf[i] == i:
            start = i * i
            for j in range(start, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def phi_and_H(n, spf):
    x = n
    phi = n
    H = 0
    least = spf[n]
    while x > 1:
        p = spf[x]
        e = 0
        phi -= phi // p
        while x % p == 0:
            x //= p
            e += 1
        if e > H:
            H = e
    return phi, H, least


def main():
    spf = build_spf(LIMIT)
    low = {0: [], 1: [], 2: [], 3: []}
    prime_zero_count = 0
    composite_zero = []
    bound_violations = 0
    for n in range(2, LIMIT + 1):
        phi, H, p = phi_and_H(n, spf)
        d = n - phi - H
        if d < 0:
            raise AssertionError(("negative defect", n, phi, H, d))
        if n - phi < n // p:
            bound_violations += 1
        if d <= 3:
            if d not in low:
                raise AssertionError(("unexpected low defect", n, d))
            if spf[n] == n:
                if d != 0:
                    raise AssertionError(("prime nonzero defect", n, d))
                prime_zero_count += 1
            else:
                low[d].append(n)
    expected = {0: [4], 1: [8, 9], 2: [], 3: [6, 25]}
    if low != expected:
        raise AssertionError(("fiber mismatch", low, expected))
    if bound_violations:
        raise AssertionError(("least-prime bound violations", bound_violations))
    print("VERIFY_OK")
    print(f"n_max={LIMIT}")
    print(f"prime_zero_count={prime_zero_count}")
    print(f"composite_low_fibers={low}")
    print(f"least_prime_bound_violations={bound_violations}")


if __name__ == "__main__":
    main()
