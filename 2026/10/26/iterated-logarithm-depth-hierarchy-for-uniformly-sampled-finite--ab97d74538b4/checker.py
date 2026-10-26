"""Reproducible finite checks for bounded-height unary functional forests.

Checks complete exact layer-vector enumeration against the coefficient formula.
No finite check is offered as an infinite proof.
"""
import itertools
from collections import Counter


def depth_profile(f, h):
    n = len(f)
    result = [0] * (h + 1)
    for start in range(n):
        cur = start
        for d in range(h + 1):
            if f[cur] == cur:
                result[d] += 1
                break
            cur = f[cur]
        else:
            return None
    return tuple(result)


def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for i in range(n + 1):
            for tail in compositions(n - i, k - 1):
                yield (i,) + tail


def predicted_count(vec):
    n = sum(vec)
    # Compute the multinomial coefficient by exact binomial factors.
    from math import comb
    ans = 1
    rem = n
    for v in vec:
        ans *= comb(rem, v)
        rem -= v
    for i in range(1, len(vec)):
        if vec[i] and vec[i-1] == 0:
            return 0
        ans *= vec[i-1] ** vec[i]
    return ans


def check():
    total_tested = 0
    profile_checks = 0
    for h in (3, 4):
        for n in range(1, 7):
            obs = Counter()
            for f in itertools.product(range(n), repeat=n):
                v = depth_profile(f, h)
                if v is not None:
                    obs[v] += 1
            expect = {v: predicted_count(v) for v in compositions(n, h + 1)}
            expect = {v: count for v, count in expect.items() if count > 0}
            assert obs == expect, (h, n, obs, expect)
            assert sum(obs.values()) > 0
            total_tested += n ** n
            profile_checks += len(expect)
            print(f'h={h}, n={n}, models={sum(obs.values())}, profiles={len(expect)}: PASS')
    print(f'ALL PASS; enumerated {total_tested} raw functions, {profile_checks} nonzero level-profile coefficients')

if __name__ == '__main__':
    check()
