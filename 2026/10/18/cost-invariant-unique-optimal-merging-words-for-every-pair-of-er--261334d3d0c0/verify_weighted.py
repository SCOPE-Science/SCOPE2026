"""Exact weighted pair resetting on the standard Cerny transition system.

Independent reverse Dijkstra for every pair and seven integer letter-weight choices.
No external libraries or network required. Execute: python3 verify_weighted.py
"""
import heapq


def formula(n, i, j, wa, wb):
    d = j - i
    if 2*d < n:
        return ((n-1)*d-i)*wa + d*wb
    return ((n-1)*(n-d)-j)*wa + (n-d)*wb


def exact(n, wa, wb):
    pairs = [(i, j) for i in range(n) for j in range(i+1, n)]
    index = {p:k for k,p in enumerate(pairs)}
    terminal = len(pairs)
    incoming = [[] for _ in range(terminal+1)]
    def a(x): return (x+1) % n
    def b(x): return 0 if x == n-1 else x
    for p, k in index.items():
        for fn, weight in ((a,wa),(b,wb)):
            out = tuple(sorted((fn(p[0]),fn(p[1]))))
            dest = terminal if out[0] == out[1] else index[out]
            incoming[dest].append((k,weight))
    inf = 10**100
    dist = [inf]*(terminal+1)
    dist[terminal] = 0
    heap = [(0,terminal)]
    while heap:
        d,v = heapq.heappop(heap)
        if d != dist[v]: continue
        for u,w in incoming[v]:
            if dist[u] > d+w:
                dist[u]=d+w
                heapq.heappush(heap,(dist[u],u))
    assert all(dist[k] == formula(n,*p,wa,wb) for p,k in index.items()), (n,wa,wb)
    for p,k in index.items():
        choices=[]
        for fn,w,label in ((a,wa,'a'),(b,wb,'b')):
            out=tuple(sorted((fn(p[0]),fn(p[1]))))
            dest=terminal if out[0]==out[1] else index[out]
            if dist[k] == w+dist[dest]: choices.append(label)
        assert len(choices)==1,(n,wa,wb,p,choices)
    if wa==wb==1:
        assert sorted(dist[:-1]) == list(range(1,terminal+1))
        assert pairs[dist[:-1].index(terminal)] == (0, n//2)
    return terminal

if __name__ == '__main__':
    for n in range(3,41):
        for wa,wb in [(1,1),(1,7),(7,1),(3,2),(2,3),(1,100),(100,1)]:
            exact(n,wa,wb)
    print('WEIGHTED_VERIFY_OK n=3..40, 7 positive weight pairs; all pair states; unique optimum; exact spectrum')
