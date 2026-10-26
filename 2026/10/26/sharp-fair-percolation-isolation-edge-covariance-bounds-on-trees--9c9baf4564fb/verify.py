"""Exact fair-bond-percolation covariance and sharp tree-extremum verifier."""
from fractions import Fraction as F
from functools import lru_cache
from heapq import heapify, heappop, heappush


def partitions(total, max_part=None):
    if total == 0:
        yield ()
        return
    if max_part is None:
        max_part = total
    for p in range(min(total, max_part), 0, -1):
        for tail in partitions(total - p, p):
            yield (p,) + tail


def degrees(n):
    for part in partitions(n-2):
        yield tuple(1+x for x in part) + (1,)*(n-len(part))


def prufer_tree(degrees):
    n = len(degrees)
    code = [v for v,d in enumerate(degrees) for _ in range(d-1)]
    count = [1]*n
    for v in code: count[v] += 1
    heap = [v for v in range(n) if count[v] == 1]
    heapify(heap)
    edges = []
    for v in code:
        u = heappop(heap)
        edges.append((u,v))
        count[u] -= 1
        count[v] -= 1
        if count[v] == 1: heappush(heap,v)
    edges.append((heappop(heap),heappop(heap)))
    assert sorted(sum(v in e for e in edges) for v in range(n)) == sorted(degrees)
    return edges


def closed_cov(ds):
    return -sum((F(d,2**d) for d in ds),F(0))/2


def brute_cov(ds):
    edges = prufer_tree(ds)
    n = len(ds)
    t = 1<<len(edges)
    sx = sy = sxy = 0
    for mask in range(t):
        exposed = [False]*n
        for i,(u,v) in enumerate(edges):
            if mask & (1<<i):
                exposed[u] = exposed[v] = True
        x = exposed.count(False)
        y = mask.bit_count()
        sx += x; sy += y; sxy += x*y
    return F(sxy,t) - F(sx*sy,t*t)


def upper(n):
    if n <= 3: return -F(n,4)
    if n == 4: return -F(15,16)
    B = n-2
    delta = (0,3,2,1)[B%4]
    return -F(n,4)+F(11*B-delta,256)


def optimum_profiles(n):
    B=n-2
    if n < 5:
        return None
    r=B%4
    if r==0:
        return [(0,B//4,0)]
    if r==1:
        p=[(0,(B-5)//4,1)]
        if B >= 9: p.append((3,(B-9)//4,0))
        return p
    if r==2:
        return [(2,(B-6)//4,0)]
    return [(1,(B-3)//4,0)]


def profiles_from_degree(ds):
    return (ds.count(4),ds.count(5),ds.count(6))


def exhaustive(n):
    D = list(degrees(n))
    vals=[closed_cov(d) for d in D]
    assert min(vals) == -F(n,4)
    assert max(vals) == upper(n)
    if n >=5:
        found=set()
        for d,v in zip(D,vals):
            if v==upper(n):
                assert all(x in (1,4,5,6) for x in d)
                assert profiles_from_degree(d) in optimum_profiles(n)
                found.add(profiles_from_degree(d))
        assert found == set(optimum_profiles(n)),(n,found,optimum_profiles(n))
    if n <= 10:
        for d in D:
            assert brute_cov(d) == closed_cov(d), (n,d,brute_cov(d),closed_cov(d))
    print(f'DEGREE_CLASS_PASS n={n} profiles={len(D)} full_pairings={n<=10}')


def dp_check(limit=120):
    @lru_cache(None)
    def f(B):
        if B==0: return F(0)
        return max([F(0)]+[F(1,2)-F(d,2**d)+f(B-(d-1)) for d in range(3,B+2)])
    for n in range(5,limit+1):
        B=n-2
        assert -F(n,4)+f(B)/2 == upper(n), n
    print('DYNAMIC_PROGRAM_PASS n<=',limit)

if __name__=='__main__':
    for n in range(2,17): exhaustive(n)
    dp_check(120)
    print('VERIFY_OK')
