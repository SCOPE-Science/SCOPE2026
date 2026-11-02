"""Exact nilpotency-index census for finite Brandt power semigroups.

Run: python verify.py. Uses only Python's standard library.
The graph and direct multiplication routines are independent implementations.
"""
from collections import defaultdict
from itertools import combinations
from math import factorial


def compositions(n, k):
    if k == 1:
        yield (n,)
        return
    for v in range(1, n-k+2):
        for tail in compositions(n-v, k-1):
            yield (v,) + tail


def layer_formula(n, group_order):
    q = (1 << group_order) - 1
    ans = [0] * (n + 1)
    ans[1] = 1
    for r in range(2, n + 1):
        total = 0
        for a in compositions(n, r):
            # Compute multinomial exactly with sequential binomial factors.
            ways = 1
            left = n
            from math import comb
            for b in a:
                ways *= comb(left, b)
                left -= b
            for j in range(1, r):
                ways *= ((1 + q) ** a[j - 1] - 1) ** a[j]
            for i in range(r):
                for j in range(i + 2, r):
                    ways *= (1 + q) ** (a[i] * a[j])
            total += ways
        ans[r] = 2 * total
    return ans


def weighted_digraph_census(n, group_order):
    q = (1 << group_order) - 1
    arcs = [(i, j) for i in range(n) for j in range(n) if i != j]
    arr = [0] * (n + 1)
    for mask in range(1 << len(arcs)):
        out = [[] for _ in range(n)]
        indeg = [0] * n
        m = 0
        for bit, (i, j) in enumerate(arcs):
            if mask >> bit & 1:
                out[i].append(j)
                indeg[j] += 1
                m += 1
        ready = [i for i in range(n) if not indeg[i]]
        dp = [0] * n
        count = 0
        while ready:
            i = ready.pop()
            count += 1
            for j in out[i]:
                dp[j] = max(dp[j], dp[i] + 1)
                indeg[j] -= 1
                if not indeg[j]:
                    ready.append(j)
        if count == n:
            arr[max(dp)+1] += q**m
    return [0,1] + [2*v for v in arr[2:]] if n >= 2 else [0,1]


def direct_power_census(n, group_order):
    """Exhaust all nonempty subsets and their successive setwise powers."""
    elems = [None] + [(i,h,j) for i in range(n)
                      for j in range(n) for h in range(group_order)]
    N = len(elems)
    P = [[0] * N for _ in range(N)]
    ids = {v:i for i,v in enumerate(elems)}
    for a in range(1,N):
        i,h,j = elems[a]
        for b in range(1,N):
            k,t,l = elems[b]
            if j == k:
                P[a][b] = ids[(i,(h+t)%group_order,l)]

    def product(a,b):
        res = 0
        while a:
            x = a & -a
            ia = x.bit_length() - 1
            a ^= x
            bb = b
            while bb:
                y = bb & -bb
                ib = y.bit_length() - 1
                bb ^= y
                res |= (1 << P[ia][ib])
        return res

    counts = [0] * (n + 1)
    for mask in range(1,1<<N):
        power=mask
        for r in range(1,n+1):
            if power == 1:
                counts[r] += 1
                break
            power = product(power,mask)
    return counts


def main():
    for g in (1,2,4):
        for n in range(1,5):
            lhs = layer_formula(n,g)
            rhs = weighted_digraph_census(n,g)
            assert lhs == rhs, (n,g,lhs,rhs)
            q = (1<<g)-1
            expected_max = 1 if n==1 else 2*factorial(n)*q**(n-1)*(1+q)**((n-1)*(n-2)//2)
            assert lhs[n] == expected_max
            print('GRAPH',n,g,'index_counts',lhs[1:],'total',sum(lhs))
    for n,g in ((1,1),(1,2),(2,1),(2,2),(2,4),(3,1),(3,2)):
        exact = direct_power_census(n,g)
        expected = layer_formula(n,g)
        assert exact == expected,(n,g,exact,expected)
        print('DIRECT',n,g,'index_counts',exact[1:])
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
