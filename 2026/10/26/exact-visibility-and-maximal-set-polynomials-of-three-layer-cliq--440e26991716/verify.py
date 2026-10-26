"""Independent finite checks for the mutual-visibility classification of K_n square P_3.

Uses ordinary BFS distances in the original graph and in the graph with
selected internal vertices forbidden. No precomputed geodesic-state rule
is used by the graph-theoretic oracle.
"""
from collections import Counter, deque
from math import comb


def graph(n):
    g = [set() for _ in range(3*n)]
    for layer in range(3):
        for i in range(n):
            a = layer*n + i
            for j in range(n):
                if i != j: g[a].add(layer*n+j)
            for h in (layer-1,layer+1):
                if 0 <= h < 3: g[a].add(h*n+i)
    return g


def bfs_dist(g, start, end, forbidden=0):
    q=deque([(start,0)]); seen={start}
    while q:
        a,dist=q.popleft()
        if a == end: return dist
        for b in g[a]:
            if b not in seen and (b == end or not (forbidden>>b&1)):
                seen.add(b);q.append((b,dist+1))
    return None


def visible(g, mask):
    vertices=[i for i in range(len(g)) if mask>>i&1]
    for k,u in enumerate(vertices):
        for v in vertices[k+1:]:
            if bfs_dist(g,u,v,mask) != bfs_dist(g,u,v):return False
    return True


def state_type(n,mask):
    c=[sum((1<<j) for j in range(3) if mask>>(j*n+i)&1) for i in range(n)]
    pivots=[i for i,s in enumerate(c) if s in (3,6)]
    if any(s==7 for s in c):return 'invalid'
    if not pivots and all(s in (0,1,2,4,5) for s in c):return 'I'
    if len(pivots)==1 and all(s in (0,1,2,4) for i,s in enumerate(c) if i!=pivots[0]):return 'II'
    return 'invalid'


def maximal_shape(n,mask):
    c=[sum((1<<j) for j in range(3) if mask>>(j*n+i)&1) for i in range(n)]
    pivots=[i for i,s in enumerate(c) if s in (3,6)]
    if len(pivots)==1 and all(s in (1,2,4) for i,s in enumerate(c) if i!=pivots[0]):return 'pivot'
    if not pivots and all(s in (2,5) for s in c) and 5 in c:return 'outer'
    return 'invalid'


def poly_coeff(n):
    # (1+3z+z^2)^n + 2n z^2(1+3z)^(n-1)
    acc=Counter({0:1})
    for i in range(n):
        new=Counter()
        for d,a in acc.items():
            for j,b in ((0,1),(1,3),(2,1)):
                new[d+j]+=a*b
        acc=new
    for k in range(n):acc[k+2]+=2*n*comb(n-1,k)*3**k
    return +acc


def maximal_coeff(n):
    # 2n 3^(n-1) z^(n+1) + z^n((1+z)^n-1)
    acc=Counter({n+1:2*n*3**(n-1)})
    for k in range(1,n+1):acc[n+k]+=comb(n,k)
    return +acc


def check(n):
    g=graph(n);good=bytearray(1<<(3*n));counts=Counter();maxima=Counter()
    shapes=Counter()
    for mask in range(len(good)):
        good[mask]=visible(g,mask)
        classification=(state_type(n,mask)!='invalid')
        if good[mask]!=classification:
            raise AssertionError(('visibility',n,mask,good[mask],classification))
        if good[mask]:counts[mask.bit_count()]+=1
    for mask in range(len(good)):
        maximal=bool(good[mask]) and all(not good[mask|(1<<i)] for i in range(3*n) if not (mask>>i&1))
        classification=(maximal_shape(n,mask)!='invalid')
        if maximal!=classification:
            raise AssertionError(('maximality',n,mask,maximal,classification))
        if maximal:
            maxima[mask.bit_count()]+=1
            shapes[maximal_shape(n,mask)]+=1
    assert counts==poly_coeff(n),(n,counts,poly_coeff(n))
    assert maxima==maximal_coeff(n),(n,maxima,maximal_coeff(n))
    assert shapes=={'pivot':2*n*3**(n-1),'outer':2**n-1},shapes
    print(f'n={n} tested={len(good)} all={sum(counts.values())} maximal={sum(maxima.values())} size_maxima={dict(sorted(maxima.items()))}')


if __name__=='__main__':
    for n in range(2,6):check(n)
    print('VERIFY_OK')
