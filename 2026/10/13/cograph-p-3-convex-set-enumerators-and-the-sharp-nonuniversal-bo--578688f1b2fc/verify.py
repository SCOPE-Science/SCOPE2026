"""Independent finite checks for P3-convex-set polynomial formulas on cographs.
Python 3.9+, standard library only. Finite tests are not a proof of the universal result.
"""
from itertools import combinations
import random


def components(adj, complement=False):
    n = len(adj)
    unseen = (1 << n) - 1
    result = []
    while unseen:
        v = (unseen & -unseen).bit_length() - 1
        stack = [v]
        unseen ^= 1 << v
        found = 0
        while stack:
            u = stack.pop()
            found |= 1 << u
            neigh = (((1 << n) - 1) ^ (adj[u] | (1 << u))) if complement else adj[u]
            visit = neigh & unseen
            unseen ^= visit
            while visit:
                bit = visit & -visit
                stack.append(bit.bit_length() - 1)
                visit ^= bit
        result.append(found)
    return result


def induced(adj, subset):
    ids = [v for v in range(len(adj)) if subset >> v & 1]
    return tuple(sum((1 << j) for j, w in enumerate(ids) if adj[v] >> w & 1) for v in ids)


def multiply(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return result


def cotree_prediction(adj):
    """Return coefficient vector or None if a non-cograph is detected."""
    n = len(adj)
    if n == 1:
        return [1, 1]
    conn = components(adj)
    if len(conn) > 1:
        A = induced(adj, conn[0])
        B = induced(adj, ((1 << n) - 1) ^ conn[0])
        a, b = cotree_prediction(A), cotree_prediction(B)
        return None if a is None or b is None else multiply(a,b)
    co = components(adj, True)
    if len(co) == 1:
        return None
    A = induced(adj, co[0])
    B = induced(adj, ((1 << n) - 1) ^ co[0])
    if cotree_prediction(A) is None or cotree_prediction(B) is None:
        return None
    na, nb = len(A), len(B)
    if na > 1 and nb > 1:
        ia = sum(not neighbors for neighbors in A)
        ib = sum(not neighbors for neighbors in B)
        p = [0] * (n+1)
        p[0], p[1], p[2], p[n] = 1, n, ia*ib, 1
        return p
    H = B if na == 1 else A
    p = [0] * (n+1)
    p[0], p[1] = 1, len(H)
    part_poly = [1]
    for C in components(H):
        m = C.bit_count()
        factor = [0] * (m+1)
        factor[0] = factor[-1] = 1
        part_poly = multiply(part_poly, factor)
    for k, value in enumerate(part_poly):
        p[k+1] += value
    return p


def brute_convex_poly(adj):
    n = len(adj)
    out = [0] * (n+1)
    for mask in range(1 << n):
        if all((adj[v] & mask).bit_count() <= 1 for v in range(n) if not(mask >> v & 1)):
            out[mask.bit_count()] += 1
    return out


def is_balanced_complete_bipartite(adj):
    n = len(adj)
    cc = components(adj, True)
    if len(cc) != 2 or abs(cc[0].bit_count() - cc[1].bit_count()) > 1:
        return False
    for mask in cc:
        verts = [i for i in range(n) if mask >> i & 1]
        if any(adj[i] & mask for i in verts):
            return False
    return True


def check_graph(adj):
    q = cotree_prediction(adj)
    if q is None:return False
    n = len(adj)
    b = brute_convex_poly(adj)
    assert q == b, (adj,q,b)
    if n >= 4 and len(components(adj)) == 1 and max(row.bit_count() for row in adj) < n-1:
        bound=n+2+(n*n//4)
        assert sum(q)<=bound,(adj,q,bound)
        assert (sum(q)==bound)==is_balanced_complete_bipartite(adj),(adj,q)
    return True


def graph_from_edges(n,code):
    adj=[0]*n
    for k,(a,b) in enumerate(combinations(range(n),2)):
        if code>>k&1:
            adj[a]|=1<<b
            adj[b]|=1<<a
    return tuple(adj)


def join_or_union(A,B,join):
    n,m=len(A),len(B)
    out=list(A)+[b<<n for b in B]
    if join:
        for i in range(n):out[i]|=((1<<m)-1)<<n
        for j in range(m):out[n+j]|=(1<<n)-1
    return tuple(out)


def main():
    total=0
    per_order=[]
    for n in range(1,7):
        found=0
        for code in range(1 << (n*(n-1)//2)):
            if check_graph(graph_from_edges(n,code)):
                found+=1
        per_order.append((n,found))
        total+=found
    print('Exhaustive labeled cographs for n=1..6:',per_order)
    print('Total exhaustive labeled cographs:',total)
    for a,b in [(2,2),(2,3),(3,4),(4,4)]:
        G = join_or_union((0,)*a,(0,)*b,True)
        p=cotree_prediction(G)
        want=[0]*(a+b+1)
        want[0],want[1],want[2],want[-1]=1,a+b,a*b,1
        assert p==want and brute_convex_poly(G)==want
    print('Complete bipartite coefficient anchors: 4 verified')
    random.seed(260304706)
    for k in range(1000):
        n=random.randrange(1,13)
        pool=[(0,)]*n
        while len(pool)>1:
            i=random.randrange(len(pool));a=pool.pop(i)
            j=random.randrange(len(pool));b=pool.pop(j)
            pool.append(join_or_union(a,b,bool(random.getrandbits(1))))
        assert check_graph(pool[0])
    print('Random binary cotrees with 1..12 vertices: 1000 verified')
    print('ALL FINITE CHECKS PASSED')

if __name__ == '__main__':main()
