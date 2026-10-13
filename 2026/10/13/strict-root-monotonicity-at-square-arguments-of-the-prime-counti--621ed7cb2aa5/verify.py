#!/usr/bin/env python3
import math

LIMIT_N = 1000
LIMIT_X = LIMIT_N * LIMIT_N

def prime_pi_table(limit):
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0:2] = b"\x00\x00"
    for p in range(2, int(limit ** 0.5) + 1):
        if is_prime[p]:
            is_prime[p*p:limit+1:p] = b"\x00" * (((limit - p*p) // p) + 1)
    pi = [0] * (limit + 1)
    count = 0
    for x in range(limit + 1):
        if is_prime[x]:
            count += 1
        pi[x] = count
    return pi

pi = prime_pi_table(LIMIT_X)

checked = 0
smallest_gap_n = None
smallest_log_gap = None

for n in range(3, 1000):
    A = pi[n*n]
    B = pi[(n+1)*(n+1)]
    lhs = pow(B, n)
    rhs = pow(A, n+1)
    assert lhs < rhs, (n, A, B)
    log_gap = (n + 1) * math.log(A) - n * math.log(B)
    if smallest_log_gap is None or log_gap < smallest_log_gap:
        smallest_log_gap = log_gap
        smallest_gap_n = n
    checked += 1

assert checked == 997
assert pi[1_000_000] == 78_498

# Elementary anchors used in the analytic tail.
assert math.log(1000) < 10
assert math.e < 3
assert 3**9 == 19_683
assert 3**9 < 50_000

print(
    "VERIFY_OK",
    f"finite_cases={checked}",
    f"pi_1000000={pi[1_000_000]}",
    f"smallest_log_gap_n={smallest_gap_n}",
    f"smallest_log_gap={smallest_log_gap:.12g}",
    "tail_start=1000",
)
