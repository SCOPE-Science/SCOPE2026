"""Independent finite checks for the cyclic Rule-184 sharp-transient formula."""
from collections import Counter
from math import comb
from random import Random


def step(x, n):
    mask = (1 << n) - 1
    left = ((x << 1) & mask) | (x >> (n - 1))
    right = (x >> 1) | ((x & 1) << (n - 1))
    return (left & (mask ^ x)) | (x & right)


def settled(x, n, k):
    if k <= n // 2:
        return (x & (((x << 1) & ((1 << n) - 1)) | (x >> (n - 1)))) == 0
    mask = (1 << n) - 1
    z = mask ^ x
    return (z & (((z << 1) & mask) | (z >> (n - 1)))) == 0


def transient(x, n, k):
    t = 0
    while not settled(x, n, k):
        x = step(x, n)
        t += 1
        assert t <= n
    return t


def cat(m):
    return comb(2 * m, m) // (m + 1)


def gap_event_count(x, n):
    ps = [i for i in range(n) if x >> i & 1]
    k = len(ps)
    if k < 2 or 2 * k > n:
        return 0
    holes = []
    for j in range(k):
        nextp = ps[(j + 1) % k] + (n if j + 1 == k else 0)
        holes.append(nextp - ps[j] - 1)
    hits = 0
    for ell in range(k):
        s = 0
        success = True
        for q in range(1, k):
            s += holes[(ell - q) % k]
            if s >= q:
                success = False
                break
        hits += success
    return hits


checks = 0
case_count = 0
for n in range(3, 17):
    counts = Counter()
    for x in range(1 << n):
        k = x.bit_count()
        if k in (0, n):
            continue
        m = min(k, n-k)
        t = transient(x, n, k)
        assert t <= m - 1, (n, k, x, t)
        counts[(k, t)] += 1
        if 2 <= k <= n//2:
            hits = gap_event_count(x, n)
            assert hits in (0,1), (n,k,x,hits)
            assert (hits == 1) == (t == k-1), (n,k,x,t,hits)
            checks += 2
        checks += 1
    for k in range(1, n):
        m = min(k,n-k)
        assert counts[(k,m-1)] == n * cat(m-1), (n,k,counts[(k,m-1)], n*cat(m-1))
        checks += 1
    case_count += 1

rng = Random(1842026)
for n in (17, 19, 23, 37, 64, 81, 99):
    for _ in range(1500):
        k = rng.randrange(1, n)
        pos = rng.sample(range(n),k)
        x = sum(1<<i for i in pos)
        t = transient(x,n,k)
        assert t <= min(k,n-k)-1
        if 2 <= k <= n//2:
            assert (gap_event_count(x,n)==1) == (t==k-1)
        checks += 1
print('VERIFY_OK exhaustive_n=3..16 random_cases=10500 checks='+str(checks)+' ring_sizes='+str(case_count))
