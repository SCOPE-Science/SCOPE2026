from math import gcd

LIMIT = 2_000_000
B = 10**24

spf = list(range(LIMIT + 1))
for i in range(2, int(LIMIT**0.5) + 1):
    if spf[i] == i:
        for m in range(i * i, LIMIT + 1, i):
            if spf[m] == m:
                spf[m] = i

def factor(n):
    out = []
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out.append((p, e))
    return out

def lcm(a, b):
    return a // gcd(a, b) * b

def carmichael_primes(n):
    fs = factor(n)
    if len(fs) < 3 or any(e != 1 for _, e in fs):
        return None
    ps = [p for p, _ in fs]
    if any((n - 1) % (p - 1) for p in ps):
        return None
    return ps

def divisors_squarefree(ps):
    ds = [1]
    for p in ps:
        ds += [d * p for d in ds]
    return ds

def lambda_of_divisor(d, ps):
    val = 1
    for p in ps:
        if d % p == 0:
            val = lcm(val, p - 1)
    return val

cn_count = 0
hierarchy_checks = 0
samples = []
for n in range(3, LIMIT + 1, 2):
    ps = carmichael_primes(n)
    if ps is None:
        continue
    cn_count += 1
    stopping = []
    for d in divisors_squarefree(ps):
        if d > 1 and d * lambda_of_divisor(d, ps) > n:
            stopping.append(d)
    assert stopping
    dm = min(stopping)
    dps = sorted([p for p in ps if dm % p == 0], reverse=True)
    for j in range(2, len(dps) + 1):
        p = dps[j - 1]
        assert p ** (j + 1) < n, (n, dm, dps, j, p)
        hierarchy_checks += 1
    if len(samples) < 8:
        samples.append((n, dm, dps))

assert cn_count == 55, cn_count
assert hierarchy_checks == 64, hierarchy_checks

cutoffs = {2: 10**8, 3: 10**6, 4: 63096, 5: 10**4, 6: 2683, 7: 10**3}
for j, ceiling in cutoffs.items():
    assert (ceiling - 1) ** (j + 1) < B <= ceiling ** (j + 1), (j, ceiling)

cutoff_text = ','.join(f'{j}:{cutoffs[j]}' for j in sorted(cutoffs))
print(f'VERIFY_OK carmichael_count={cn_count} hierarchy_checks={hierarchy_checks} depth_cutoffs={cutoff_text}')
print('samples=' + repr(samples))
