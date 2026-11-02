"""Finite exhaustive proof cross-check: independent subset enumerator + exact DP.
No external packages are needed. Run: python3 verify_direct.py
"""

def run(n):
    N = 2*n
    edges = sorted({tuple(sorted((i, (i+1)%N))) for i in range(N)} |
                   {tuple(sorted((i,i+n))) for i in range(n)})
    total = 1 << N
    cuts = [0]*total
    size = [0]*total
    profile = [4*N]* (N+1)
    profile[0] = 0
    optset_counts = [0]*(N+1)
    # independent edge-by-edge evaluation avoids the incremental recurrence.
    for s in range(total):
        k = s.bit_count()
        b = sum(bool((s>>u)&1) != bool((s>>v)&1) for u,v in edges)
        cuts[s] = b
        size[s] = k
        if b < profile[k]:
            profile[k] = b
            optset_counts[k] = 1
        elif b == profile[k]:
            optset_counts[k] += 1
    assert profile == [0]+[3 if min(k,N-k)==1 else 4 if k%2==0 else 5 for k in range(1,N)]+[0], (n,profile)
    # DP counts optimal-prefix chains exactly. No candidate ordering sampling.
    ways = [0]*total
    ways[0] = 1
    for s in range(1,total):
        if cuts[s] != profile[size[s]]:
            continue
        temp = s
        while temp:
            bit = temp & -temp
            ways[s] += ways[s^bit]
            temp ^= bit
    assert sum(profile) == 9*n-8
    assert ways[-1] == n*4**n, (n,ways[-1],n*4**n)
    print(f'n={n}: subsets={total}, minimum arrangement={sum(profile)}, optimal layouts={ways[-1]}')

if __name__ == '__main__':
    for n in range(4,10):
        run(n)
    print('INDEPENDENT_DIRECT_ENUMERATION_PASS')
