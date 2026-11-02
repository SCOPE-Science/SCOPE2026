"""Independent exact combinatorial check of the EFX/MMS sparsity statement.

A focal agent's positive two-value utility is represented by counts of
low/high goods in each bundle.  All integer arithmetic; no dependencies.
"""
from functools import lru_cache
from itertools import product
from math import comb


def compositions(total, parts):
    if parts == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, parts - 1):
                yield (first,) + rest


@lru_cache(maxsize=None)
def can_exceed(p, q, n, low, high, own):
    """Does some n-partition give everyone >=own+1?"""
    threshold = own + 1
    infinity = q + 1
    costs = [max(0, (threshold - high * x + low - 1) // low)
             for x in range(p + 1)]
    dp = [infinity] * (p + 1)
    dp[0] = 0
    for _ in range(n):
        nxt = [infinity] * (p + 1)
        for used in range(p + 1):
            if dp[used] > q:
                continue
            for number in range(p - used + 1):
                val = dp[used] + costs[number]
                if val < nxt[used + number]:
                    nxt[used + number] = val
        dp = nxt
    return dp[p] <= q


def efx_for_focal(lows, highs, low, high):
    own = lows[0] * low + highs[0] * high
    for k in range(1, len(lows)):
        other = lows[k] * low + highs[k] * high
        if lows[k] > 0 and other - low > own:
            return False
        if highs[k] > 0 and other - high > own:
            return False
    return True


def check():
    num_profiles = num_efx = num_raised = 0
    for n in range(2, 6):
        for m in range(0, 2 * n):
            for low in (1, 2, 3):
                for high in (low + 1, low + 2, low + 3):
                    for p in range(m + 1):
                        q = m - p
                        hs = tuple(compositions(p, n))
                        ls = tuple(compositions(q, n))
                        for hcounts in hs:
                            for lcounts in ls:
                                num_profiles += 1
                                if not efx_for_focal(lcounts, hcounts, low, high):
                                    continue
                                num_efx += 1
                                own = lcounts[0] * low + hcounts[0] * high
                                is_more = can_exceed(p, q, n, low, high, own)
                                if is_more:
                                    raise AssertionError(('EFX-not-MMS',n,m,low,high,hcounts,lcounts))
                                num_raised += 1
        # Sharp witness at m=2n for all n.
        p, q, low, high = 2 * n - 2, 2, 2, 3
        lows = (2,) + (0,) * (n - 1)
        highs = (0,) + (2,) * (n - 1)
        assert efx_for_focal(lows, highs, low, high)
        assert can_exceed(p, q, n, low, high, 4)
        # All agents' EFX, using identical valuations.
        bundles = tuple(zip(lows, highs))
        for a in range(n):
            aa = bundles[a][0] * low + bundles[a][1] * high
            for b in range(n):
                if a == b:
                    continue
                l, h = bundles[b]
                if l:
                    assert aa >= l * low + h * high - low
                if h:
                    assert aa >= l * low + h * high - high
        assert p + q == 2 * n
        print('witness n=', n, 'm=', p + q, 'EFX=True', 'own=4', 'MMS>=5')
    print('VERIFY_OK count_profiles=',num_profiles,'count_EFX=',num_efx,
          'count_sufficient=',num_raised,'cache=',can_exceed.cache_info())

if __name__ == '__main__':
    check()
