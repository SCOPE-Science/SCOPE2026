from functools import lru_cache
from itertools import product
from math import comb, factorial

INF = -1

# Canonical plane rooted tree: a leaf is (), an internal node is an ordered
# tuple of at least two child trees.
@lru_cache(None)
def trees(n, N):
    if n == 1:
        return frozenset({()})
    out = set()
    maxk = n if N == INF else min(N, n)

    def comps(total, k, prefix=()):
        if k == 1:
            yield prefix + (total,)
            return
        for first in range(1, total-k+2):
            yield from comps(total-first, k-1, prefix+(first,))

    for k in range(2, maxk+1):
        for c in comps(n, k):
            child_sets = [trees(m, N) for m in c]
            for children in product(*child_sets):
                out.add(tuple(children))
    return frozenset(out)

@lru_cache(None)
def recurrence(n, N):
    if n == 1:
        return 1
    total = 0
    maxk = n if N == INF else min(N, n)

    def comps(total_n, k, prefix=()):
        if k == 1:
            yield prefix + (total_n,)
            return
        for first in range(1, total_n-k+2):
            yield from comps(total_n-first, k-1, prefix+(first,))

    for k in range(2, maxk+1):
        for c in comps(n, k):
            p = 1
            for m in c:
                p *= recurrence(m, N)
            total += p
    return total

def stir2(n, k):
    d = [[0]*(k+1) for _ in range(n+1)]
    d[0][0] = 1
    for i in range(1, n+1):
        for j in range(1, min(i,k)+1):
            d[i][j] = d[i-1][j-1] + j*d[i-1][j]
    return d[n][k]

for N in (2,3,4,INF):
    vals=[]
    for n in range(1,9):
        direct=len(trees(n,N))
        recur=recurrence(n,N)
        assert direct==recur, (N,n,direct,recur)
        vals.append(direct)
    print('N=', 'infinity' if N==INF else N, vals)

cat=[comb(2*(n-1),n-1)//n for n in range(1,9)]
assert [recurrence(n,2) for n in range(1,9)] == cat

schroeder=[1,1,3,11,45,197,903,4279]
assert [recurrence(n,INF) for n in range(1,9)] == schroeder

def injective_profile(N, upto):
    return [factorial(n)*recurrence(n,N) for n in range(1,upto+1)]

def full_profile(N, upto):
    a=[0]+injective_profile(N,upto)
    return [sum(stir2(n,k)*a[k] for k in range(1,n+1)) for n in range(1,upto+1)]

assert injective_profile(2,6)==[1,2,12,120,1680,30240]
assert injective_profile(INF,6)==[1,2,18,264,5400,141840]
assert full_profile(2,6)==[1,3,19,207,3211,64383]
assert full_profile(INF,6)==[1,3,25,387,8521,241683]

print('N=2 injective', injective_profile(2,6))
print('N=infinity injective', injective_profile(INF,6))
print('N=2 full', full_profile(2,6))
print('N=infinity full', full_profile(INF,6))
print('VERIFY_OK')
