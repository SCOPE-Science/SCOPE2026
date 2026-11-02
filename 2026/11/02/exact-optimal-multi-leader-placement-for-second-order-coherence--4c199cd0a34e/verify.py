"""Exact and numerical checks of inverse-square grounded-path leader placement.
Run: python verify.py
Uses only Python's standard library.
"""
from fractions import Fraction as Q
from itertools import combinations
from heapq import heapify, heappop, heappush
from random import Random


def F(m):
    return Q(m * (m + 1) * (m*m + m + 1), 6)


def H(m):
    return Q(m * (m + 2) * (2*m*m + 4*m + 9), 180)


def f(t):
    assert t >= 1
    return Q(t * (2*t*t + 1), 3)


def h(t):
    assert t >= 1
    return Q((2*t + 1) * (4*t*t + 4*t + 7), 180)


def gaps(n, leaders):
    a = list(leaders)
    return (a[0] - 1,) + tuple(a[i+1] - a[i] - 1 for i in range(len(a)-1)) + (n-a[-1],)


def block_cost(n, leaders):
    g = gaps(n, leaders)
    return F(g[0]) + F(g[-1]) + sum((H(v) for v in g[1:-1]), Q(0))


def greedy(n, k):
    assert 1 <= k <= n
    g = [0] * (k+1)
    heap = [(f(1) if j in (0,k) else h(1),j) for j in range(k+1)]
    heapify(heap)
    for _ in range(n-k):
        _,j = heappop(heap)
        g[j] += 1
        heappush(heap,(f(g[j]+1) if j in (0,k) else h(g[j]+1),j))
    loc = []
    x = g[0] + 1
    for j in range(k):
        loc.append(x)
        if j < k-1:
            x += g[j+1] + 1
    assert loc[-1] + g[-1] == n
    return tuple(loc), block_cost(n, loc)


def exact_inverse(A):
    d = len(A)
    if not d: return []
    B = [[Q(A[i][j]) for j in range(d)] + [Q(i == j) for j in range(d)] for i in range(d)]
    for j in range(d):
        pivot = next(i for i in range(j,d) if B[i][j] != 0)
        B[j], B[pivot] = B[pivot], B[j]
        p = B[j][j]
        B[j] = [z/p for z in B[j]]
        for i in range(d):
            if i != j:
                v=B[i][j]
                if v:
                    B[i] = [B[i][t] - v*B[j][t] for t in range(2*d)]
    return [r[d:] for r in B]


def direct_cost(n, leaders):
    follower = sorted(set(range(1,n+1)) - set(leaders))
    d = len(follower)
    A = [[0] * d for _ in range(d)]
    position={u:i for i,u in enumerate(follower)}
    for i, u in enumerate(follower):
        A[i][i] = (u > 1) + (u < n)
        for v in (u-1,u+1):
            if v in position:
                A[i][position[v]] = -1
    G=exact_inverse(A)
    return sum((G[i][j] * G[i][j] for i in range(d) for j in range(d)), Q(0))


def all_profiles(n,k):
    for leader in combinations(range(1,n+1), k):
        yield leader,block_cost(n,leader)


def main():
    matrix_checks=0
    minimizer_checks=0
    cutoff_checks=0
    for n in range(2,12):
        for k in range(1,n+1):
            candidates=list(all_profiles(n,k))
            optimum=min(v for _,v in candidates)
            best={s for s,v in candidates if v==optimum}
            g,greedy_value=greedy(n,k)
            assert greedy_value==optimum and g in best
            minimizer_checks += 1
            for leader,value in candidates:
                assert direct_cost(n,leader)==value, (n,k,leader,value)
                matrix_checks += 1
            if k >= 2:
                all_two_endpoints = all(1 in s and n in s for s in best)
                assert all_two_endpoints == (n <= 3*k-2), (n,k,best)
                cutoff_checks += 1
    rng=Random(731983)
    margin_checks=0
    exchange_checks=0
    for _ in range(500):
        n=rng.randint(12,500)
        k=rng.randint(1,n)
        s,val=greedy(n,k)
        g=list(gaps(n,s))
        for i in range(k+1):
            for j in range(k+1):
                if i==j or g[i]==0: continue
                marginal_remove = f(g[i]) if i in (0,k) else h(g[i])
                marginal_add = f(g[j]+1) if j in (0,k) else h(g[j]+1)
                assert marginal_remove <= marginal_add, (n,k,g,i,j)
                exchange_checks += 1
        for j,t in enumerate(g):
            p=f if j in (0,k) else h
            assert (F(t) if j in (0,k) else H(t)) == sum((p(a) for a in range(1,t+1)),Q(0))
            margin_checks += 1
    # Continuum constant and location ratios for fixed k, with a tolerance based on O(1/n).
    limit_checks=0
    q=15**(1/3)
    for k in (1,2,3,5,8):
        n=20000
        s,val=greedy(n,k)
        g=gaps(n,s)
        tail=1/(2+(k-1)*q)
        center=q*tail
        assert abs(g[0]/n-tail) < .001
        assert abs(g[-1]/n-tail) < .001
        assert all(abs(t/n-center) < .001 for t in g[1:-1])
        assert abs(float(val)/n**4 - 1/(6*(2+(k-1)*q)**3)) < 1e-5
        limit_checks+=1
    print('PASS exact grounded inverses:',matrix_checks)
    print('PASS exhaustive global optimizers:',minimizer_checks)
    print('PASS exact endpoint-leader cutoff:',cutoff_checks)
    print('PASS sampled optimality exchanges:',exchange_checks)
    print('PASS marginal telescoping identities:',margin_checks)
    print('PASS fixed-k asymptotic profiles:',limit_checks)
    print('PASS all tests')

if __name__ == '__main__':
    main()
