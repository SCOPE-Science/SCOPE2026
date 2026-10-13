#!/usr/bin/env python3
"""Construct and verify shortest cyclic covers of binary words avoiding adjacent 1s."""
from itertools import product
from collections import defaultdict, deque, Counter


def fib(i):
    a, b = 0, 1
    for _ in range(i):
        a, b = b, a + b
    return a


def words(length):
    return [''.join(bits) for bits in product('01', repeat=length)
            if '11' not in ''.join(bits)]


def construct(n):
    assert n >= 2
    m = n - 1
    V = words(m)
    E = words(n)
    arcs = defaultdict(list)
    indeg = Counter()
    outdeg = Counter()
    def add(u, v, label):
        assert u[1:] + label == v and '11' not in u + label
        arcs[u].append((v,label))
        outdeg[u] += 1
        indeg[v] += 1
    for x in E:
        add(x[:-1], x[1:], x[-1])
    extra = 0
    deficits = []
    sinks = []
    for u in V:
        if u[0] == '0' and u[-1] == '1':
            r = len(u) - len(u.lstrip('0'))
            assert 1 <= r <= m-1
            v = u
            for _ in range(r):
                t = v[1:] + '0'
                add(v,t,'0')
                v = t
                extra += 1
            assert v == u[r:]+'0'*r and v[0] == '1' and v[-1]=='0'
            deficits.append(u)
            sinks.append(v)
    assert len(set(sinks)) == len(sinks)
    assert set(sinks) == {u for u in V if u[0]=='1' and u[-1]=='0'}
    assert all(indeg[u]==outdeg[u] for u in V)
    assert extra == fib(n)-1
    total = len(E)+extra
    # Euler cycle by a separate traversal of the explicitly constructed multigraph.
    stack = [V[0]]
    order = []
    while stack:
        v = stack[-1]
        if arcs[v]:
            target,_ = arcs[v].pop()
            stack.append(target)
        else:
            order.append(stack.pop())
    order.reverse()
    assert len(order) == total+1 and order[0]==order[-1]
    cycle = ''.join(v[0] for v in order[:-1])
    factors = Counter(''.join(cycle[(i+j)%total] for j in range(n))
                      for i in range(total))
    assert '11' not in cycle+cycle[:1]
    assert set(factors) == set(E)
    assert total == fib(n+2)+fib(n)-1
    return cycle, extra, factors


def exact_closed_bfs(n):
    # Independent exhaustive search over all states (overlap state, edge coverage mask).
    E = words(n)
    V = words(n-1)
    ix = {s:i for i,s in enumerate(E)}
    succ = {u: [(x[1:],1<<ix[x]) for x in E if x[:-1]==u] for u in V}
    full = (1 << len(E)) - 1
    best = 10**9
    for start in V:
        seen = {(start,0)}
        q = deque([(start,0,0)])
        while q:
            v,mask,d = q.popleft()
            if d>=best: continue
            for w,bit in succ[v]:
                new_mask=mask|bit
                if w==start and new_mask==full:
                    best=min(best,d+1)
                elif (w,new_mask) not in seen:
                    seen.add((w,new_mask))
                    q.append((w,new_mask,d+1))
    return best


def main():
    rows=[]
    for n in range(2,13):
        cycle,extra,factors = construct(n)
        rows.append((n,len(cycle),extra,len(factors),max(factors.values())))
        if n<=5:
            minimum=exact_closed_bfs(n)
            assert minimum==len(cycle),(n, minimum,len(cycle))
        if n<=6:
            print('n',n,'cycle',cycle)
    print('verified n,length,duplicated,covered,max-multiplicity')
    for row in rows:print(*row)
    print('EXHAUSTIVE_CLOSED_WALK_BFS_2_TO_5_OK')
    print('CONSTRUCTION_AND_FORMULA_2_TO_12_OK')

if __name__=='__main__':main()
