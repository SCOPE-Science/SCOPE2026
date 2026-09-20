from math import gcd

def lcm(a, b):
    return a // gcd(a, b) * b

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

def lam_two_power(i):
    if i <= 1:
        return 1
    if i == 2:
        return 2
    return 1 << (i - 2)

def lam_p_power(p, j):
    if j == 0:
        return 1
    return (p - 1) * (p ** (j - 1))

def lam_divisor_weight(i, p, j):
    if i == 0:
        return lam_p_power(p, j)
    if j == 0:
        return lam_two_power(i)
    return lcm(lam_two_power(i), lam_p_power(p, j))

def direct_lambda_star(a, p, b):
    weights = sorted(
        lam_divisor_weight(i, p, j)
        for i in range(a + 1)
        for j in range(b + 1)
    )
    reachable = 0
    for w in weights:
        if w > reachable + 1:
            return False
        reachable += w
    return True

def v2(n):
    t = 0
    while n % 2 == 0:
        t += 1
        n //= 2
    return t

def theorem_criterion(a, p, b):
    q = p - 1
    t = v2(q)
    s0 = (1 << (a - 1)) + 2
    if a <= t + 2:
        C = a + 1
    else:
        C = t + 1 + (1 << (a - t - 1))
    return all(
        (p ** (j - 1)) * q
        <= s0 + C * (p ** (j - 1) - 1) + 1
        for j in range(1, b + 1)
    )

def main():
    primes = [p for p in range(3, 300, 2) if is_prime(p)]
    checked = 0
    mismatches = []
    for a in range(3, 13):
        for p in primes:
            for b in range(1, 6):
                direct = direct_lambda_star(a, p, b)
                predicted = theorem_criterion(a, p, b)
                checked += 1
                if direct != predicted:
                    mismatches.append((a, p, b, direct, predicted))

    threshold_checked = 0
    threshold_mismatches = []
    for a in range(3, 13):
        for p in primes:
            direct = direct_lambda_star(a, p, 1)
            predicted = p <= (1 << (a - 1)) + 3
            threshold_checked += 1
            if direct != predicted:
                threshold_mismatches.append((a, p, direct, predicted))

    print(f"classification_cases={checked}")
    print(f"classification_mismatches={len(mismatches)}")
    print(f"b1_threshold_cases={threshold_checked}")
    print(f"b1_threshold_mismatches={len(threshold_mismatches)}")
    if mismatches:
        print("first_classification_mismatch=", mismatches[0])
    if threshold_mismatches:
        print("first_threshold_mismatch=", threshold_mismatches[0])

if __name__ == "__main__":
    main()
