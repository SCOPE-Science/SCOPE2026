"""Verify prime simultaneous ubiquity ledger for lane-1054.

Checks:
 1. Sieve primes in [1000, N], Mertens-divergent ledger S1 = sum 4/(p+1) >= 3.
 2. Disjointness 2*psi(p) < 1 for all p >= 1000.
 3. 1D Fourier coefficient bound spot-check.
 4. Overlap error constant C0 from (pq)^-3/2 tails.
 5. Chung-Erdos ratio S1^2/(S1^2+S1+C0) and half-loss condition.
"""
import math

N = 3500000
P_MIN = 1000

def sieve(n):
    bs = bytearray(b'\x01') * (n + 1)
    bs[0:2] = b'\x00\x00'
    for i in range(2, int(n ** 0.5) + 1):
        if bs[i]:
            bs[i*i:n+1:i] = b'\x00' * ((n - i*i) // i + 1)
    return [i for i in range(n + 1) if bs[i]]

primes = sieve(N)
primes_big = [p for p in primes if p >= P_MIN]
print(f"primes up to {N}: {len(primes)}, with p>=1000: {len(primes_big)}")

def psi(p):
    return 1.0 / math.sqrt(p + 1)

# 1. ledger
S1 = sum(4.0 / (p + 1) for p in primes_big)
print(f"S1 = sum 4/(p+1) over p in [1000,{N}] = {S1:.6f}")
assert S1 >= 3.0, "ledger must reach >=3 for half-loss threshold"

# small-block ledger (audit plan window)
S1_small = sum(4.0 / (p + 1) for p in primes_big if p <= 8000)
print(f"S1 over [1000,8000] = {S1_small:.6f}")

# 2. disjointness
worst = max(2 * psi(p) for p in primes_big)
print(f"max 2*psi = {worst:.6f} (<1 required)")
assert worst < 1.0

# 3. Fourier 1D bound spot check: d_p(k) = 2 sin(2 pi k psi)/(2 pi k)
def d(p, k):
    if k == 0:
        return 2 * psi(p)
    return 2 * math.sin(2 * math.pi * k * psi(p)) / (2 * math.pi * k)

for (p, k) in [(1009, 0), (1009, 1), (1009, 7), (7919, 3), (104729, 11), (1009, 1013)]:
    exact = abs(d(p, k))
    if k == 0:
        bound = 2 * psi(p)
    else:
        bound = min(2 * psi(p), 1.0 / (math.pi * abs(k)))
    assert exact <= bound + 1e-15, (p, k, exact, bound)
print("1D Fourier bound spot-checks OK")

# 4. tail constant: sum_{p>=1000} p^-3/2 <= sum_{n>=1000} n^-3/2
#    <= 1000^-3/2 + integral_{1000}^inf x^-3/2 dx = 1000^-3/2 + 2/sqrt(1000)
tail = 1000 ** -1.5 + 2.0 / math.sqrt(1000)
C0_main = (8.0 / 3.0) * tail ** 2
# second-order term sum_{p,q} 1/(9 p^2 q^2) <= (1/9)(sum n^-2)^2 <= (1/9)(1/1000+1/1000^2... ) use integral
tail2 = 1.0 / 1000.0 + 1.0 / 1000.0  # generous upper bound of sum_{n>=1000} n^-2 <= 1/999 - ... < 0.002
C0 = C0_main + (1.0 / 9.0) * tail2 ** 2
print(f"tail sum p^-3/2 <= {tail:.6f}, C0 <= {C0:.6f}")
assert C0 < 0.02

# 5. Chung-Erdos ratio on the explicit block + half-loss
S2ub = S1 ** 2 + S1 + C0
ratio = S1 ** 2 / S2ub
print(f"S2 upper bound = {S2ub:.6f}, Chung-Erdos ratio >= {ratio:.6f}")
assert S1 + C0 <= 0.5 * S1 ** 2, "overlap loss at most half S1^2"
print("half-loss condition (S1+C0 <= S1^2/2) OK")

# pairwise error spot check for (1009,1013)
p, q = 1009, 1013
e0 = 4 * psi(p) * psi(q)
R = (1.0 / (3 * p * q)) * (2 * e0 + 1.0 / (3 * p * q))
main = 16.0 / ((p + 1) * (q + 1))
print(f"spot (1009,1013): main={main:.8f}, err bound R={R:.9f}, ratio={R/main:.6f}")
assert R < 0.05 * main

print("VERIFY_OK")
