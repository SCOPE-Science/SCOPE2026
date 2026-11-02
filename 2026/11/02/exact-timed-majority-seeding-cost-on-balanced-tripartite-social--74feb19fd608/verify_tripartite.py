"""Independent finite checks for the timed-target theorem on balanced complete tripartite graphs.
Run: python verify_tripartite.py
Uses only the Python standard library; it does not assume the theorem formulas inside the solver.
"""
from itertools import product
from math import ceil
import heapq


def labelled_timed_optimum(m):
    """Dijkstra over EVERY labelled natural-positive state and EVERY labelled intervention set."""
    n = 3*m
    universe = (1 << n) - 1
    neigh = []
    for v in range(n):
        neigh.append(sum(1 << w for w in range(n) if v//m != w//m))
    tau = m+1
    next_state = [0]*(1<<n)
    for a in range(1<<n):
        next_state[a] = sum(1<<v for v in range(n) if (a & neigh[v]).bit_count() >= tau)
    # Compute all one-round options. Interventions can include naturally positive agents;
    # they never help and may be omitted without changing the optimum.
    actions = [[] for _ in range(1<<n)]
    for q in range(1<<n):
        inactive = universe ^ q
        s = inactive
        while True:
            y=next_state[q|s]
            actions[q].append((y,s.bit_count()))
            if s==0:break
            s=(s-1)&inactive
    d = [10**9]*(1<<n); d[0]=0
    pq=[(0,0)]
    while pq:
        cost,q = heapq.heappop(pq)
        if cost!=d[q]:continue
        if q==universe:return cost
        for y,extra in actions[q]:
            z=cost+extra
            if z<d[y]:
                d[y]=z;heapq.heappush(pq,(z,y))
    raise AssertionError('unreachable')


def class_state_timed_optimum(m):
    """Independent type-count dynamic program; natural states are class-uniform."""
    edges={}
    for state in range(8):
        counts_ranges=[range(1) if state & (1<<i) else range(m+1) for i in range(3)]
        for seeds in product(*counts_ranges):
            active=[m if state & (1<<i) else seeds[i] for i in range(3)]
            nxt=sum((sum(active[j] for j in range(3) if j!=i)>=m+1)<<i for i in range(3))
            key=(state,nxt);cost=sum(seeds)
            edges[key]=min(edges.get(key,10**9),cost)
    distances=[10**9]*8;distances[0]=0
    todo=[(0,0)]
    while todo:
        d,u=heapq.heappop(todo)
        if d!=distances[u]:continue
        if u==7:return d
        for v in range(8):
            w=edges.get((u,v),10**9)
            if d+w<distances[v]:
                distances[v]=d+w;heapq.heappush(todo,(d+w,v))
    raise AssertionError('unreachable')


def static_target_optimum(m):
    """Enumerate all initial counts; then iterate natural dynamics without later seeds."""
    answer = 3*m+1
    for a,b,c in product(range(m+1),repeat=3):
        q = (a,b,c)
        seen=set()
        while q not in seen and q!=(m,m,m):
            seen.add(q)
            q=tuple(m if sum(q[j] for j in range(3) if j!=i)>=m+1 else 0 for i in range(3))
        if q == (m,m,m):answer=min(answer,a+b+c)
    return answer


def check_explicit_schedule(m):
    if m==1:
        seeds=[(1,1,1)]
    else:
        seeds=[(1,1,m),(0,0,1)]
    q=(0,0,0)
    for s in seeds:
        a=tuple(max(q[i],s[i]) for i in range(3))
        q=tuple(m if sum(a[j] for j in range(3) if j!=i)>=m+1 else 0 for i in range(3))
    assert q==(m,m,m), (m,q)
    return sum(sum(s) for s in seeds)


def main():
    labelled=0;types=0;static=0
    for m in range(1,5):
        got=labelled_timed_optimum(m);want=3 if m==1 else m+3
        assert got==want,(m,got,want)
        print('labelled exact',m,got)
        labelled+=1
    for m in range(1,61):
        got=class_state_timed_optimum(m);want=3 if m==1 else m+3
        assert got==want,(m,got,want)
        assert check_explicit_schedule(m)==want
        types+=1
    for m in range(1,31):
        got=static_target_optimum(m);want=3 if m==1 else ceil(3*(m+1)/2)
        assert got==want,(m,got,want)
        static+=1
    print('PASS',labelled,'labelled graph cases,',types,'class-count cases,',static,'static seeding cases')

if __name__=='__main__':main()
