"""Independent enumeration by recursive ordered prime products; subset sums by Python integers.

Run: python3 verify_alternate.py
This program requires only the standard library; it does not call the C++ checker.
"""

BOUND = 19_120_000
SUM_BOUND = 40_000_000
COIN_COUNT = 3100
EXPECTED = 19_027_139

# A seven-prime product at most BOUND has smallest six prime factors
# whose product is at least 2*3*5*7*11*13=30030.
prime_cap = BOUND // 30030
primes = []
for n in range(2, prime_cap + 1):
    if all(n % p for p in primes if p*p <= n):
        primes.append(n)

coins = []
def collect(remaining, start, value):
    if remaining == 0:
        coins.append(value)
        return
    for i in range(start, len(primes) - remaining + 1):
        # Monotone lower bound using the next 'remaining' available primes.
        candidate_min = value
        for j in range(i, i+remaining):
            candidate_min *= primes[j]
        if candidate_min > BOUND:
            break
        collect(remaining - 1, i + 1, value * primes[i])

collect(7, 0, 1)
coins.sort()
assert len(coins) >= COIN_COUNT + 1
assert coins[0] == 510510 and coins[3099] == 19111638 and coins[3100] == 19114095

mask = (1 << (SUM_BOUND+1)) - 1
reachable = 1  # bit zero
for c in coins[:COIN_COUNT]:
    reachable |= (reachable << c) & mask
largest_missing = ((~reachable) & mask).bit_length()-1
assert largest_missing == EXPECTED
assert not (reachable >> EXPECTED) & 1
assert ((reachable >> (EXPECTED+1)) & 1) == 1
assert SUM_BOUND-largest_missing >= coins[COIN_COUNT]
print(f"terms={COIN_COUNT} first={coins[0]} last_used={coins[3099]} next={coins[3100]}")
print(f"largest_missing={largest_missing} represented_interval=[{largest_missing+1},{SUM_BOUND}]")
print("VERIFY_OK")
