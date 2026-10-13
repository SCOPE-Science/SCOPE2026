import math

def is_spike_index(k):
    # phi(k) is spiked when k = 2^m + 1, m>=1.
    n = k - 1
    return n >= 2 and (n & (n - 1)) == 0

def phi(k):
    p = 5 if is_spike_index(k) else 4
    return float((k + 1) ** p)

# Generic decay checks on increasing windows.
for K in [100, 1000, 10000, 100000]:
    a = K / phi(K)
    b = K * phi(K + 1) / (phi(K) ** 2)
    assert a < 1.0 / math.sqrt(K)
    assert b < 0.1

# Pre-spike ratios diverge while the proof-exact burst term decays.
prev_ratio = 0.0
for m in range(4, 16):
    k = 2 ** m
    ratio = phi(k + 1) / phi(k)
    burst_term = k * phi(k + 1) / (phi(k) ** 2)
    assert ratio > prev_ratio
    assert burst_term < 10.0 / (k ** 2)
    prev_ratio = ratio

# Immediately after a spike the quadratic denominator dominates strongly.
for m in range(4, 16):
    k = 2 ** m + 1
    burst_term = k * phi(k + 1) / (phi(k) ** 2)
    assert burst_term < 1.0 / (k ** 4)

print("VERIFY_OK")
