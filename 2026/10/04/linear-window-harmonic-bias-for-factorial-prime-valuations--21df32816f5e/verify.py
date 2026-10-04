import math


def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            sieve[p * p:n + 1:p] = b"\x00" * (((n - p * p) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def vp_fact(n, p):
    total = 0
    q = n
    while q:
        q //= p
        total += q
    return total


NMAX = 2_000_000
primes = primes_upto(NMAX)

exact_cases = 0
for n in [1000, 10000, 123457, 1000000, 2000000]:
    for K in [1, 2, 3, 5, 8]:
        if n <= (K + 1) ** 2:
            continue
        for h in [2, 3, 5]:
            for c in range(h):
                direct = 0.0
                regrouped = 0.0
                for p in primes:
                    if p > n:
                        break
                    if p > n / (K + 1):
                        v = vp_fact(n, p)
                        if v % h == c:
                            direct += v * math.log(p)
                for j in range(1, K + 1):
                    if j % h != c:
                        continue
                    for p in primes:
                        if p > n / j:
                            break
                        if p > n / (j + 1):
                            regrouped += j * math.log(p)
                assert abs(direct - regrouped) < 1e-7 * max(1.0, abs(direct))
                exact_cases += 1

rows = []
for n in [100000, 500000, 1000000, 2000000]:
    odd = 0.0
    even = 0.0
    for p in primes:
        if p > n:
            break
        if p > n / 3:
            v = vp_fact(n, p)
            if v % 2:
                odd += v * math.log(p)
            else:
                even += v * math.log(p)
    rows.append((n, odd / n, even / n, odd / (odd + even)))

print(f"VERIFY_OK exact_cell_cases={exact_cases} asymptotic_rows={len(rows)}")
for row in rows:
    print("n=%d odd_over_n=%.9f even_over_n=%.9f odd_share=%.9f" % row)
print("predicted odd_over_n=0.500000000 even_over_n=0.333333333 odd_share=0.600000000")
