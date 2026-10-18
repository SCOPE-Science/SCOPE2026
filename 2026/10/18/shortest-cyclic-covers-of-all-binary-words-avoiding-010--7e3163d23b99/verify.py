#!/usr/bin/env python3
"""Independent finite checks for shortest cyclic covers avoiding 010.

Python standard library only. Exact infinite assertion is proved in RESULT.md;
this file verifies enumerative consequences and finite optimality certificates.
"""
from collections import Counter, deque
from itertools import product


def ok(s):
    return '010' not in s


def words(n):
    return [''.join(x) for x in product('01', repeat=n) if ok(''.join(x))]


def feasible_cycle(s, n):
    length = len(s)
    if not ok(s+s[:2]):
        return False
    seen = {''.join(s[(i+j) % length] for j in range(n)) for i in range(length)}
    return seen == set(words(n))


def near_positive_distance(v, positives):
    n = len(v)
    Q = deque([(v, 0)])
    visited = {v}
    while Q:
        u, d = Q.popleft()
        if u in positives:
            return d
        for letter in '01':
            if ok(u+letter):
                nxt = u[1:] + letter
                if nxt not in visited:
                    visited.add(nxt)
                    Q.append((nxt, d + 1))
    raise AssertionError('positive state unreachable')


def build(n):
    L = n-1
    required = words(n)
    vertices = words(L)
    out = Counter(x[:-1] for x in required)
    indeg = Counter(x[1:] for x in required)
    neg = sorted(v for v in vertices if indeg[v] - out[v] == 1)
    pos = sorted(v for v in vertices if out[v] - indeg[v] == 1)
    assert len(neg) == len(pos)
    assert all(abs(out[v]-indeg[v])<=1 for v in vertices)
    adj = {v:[] for v in vertices}
    for s in required:
        adj[s[:-1]].append((s[1:],s[-1]))
    inject = {}
    extra = 0
    for v in neg:
        if '10' not in v:
            assert v == '0'*(L-1)+'1'
            q = '1'+'0'*(L-1)
        else:
            j=v.index('10')
            p,t=v[:j],v[j:]
            a=len(p)-len(p.lstrip('0'))
            b=j-a
            assert b>=1 and p=='0'*a+'1'*b and t.startswith('10') and t.endswith('01')
            q = '1'*b + '0'*a
        u = v
        for letter in q:
            assert ok(u+letter)
            to=u[1:]+letter
            adj[u].append((to,letter))
            u=to
        assert u in pos
        assert u not in inject
        assert len(q)==near_positive_distance(v,set(pos)), (n,v,len(q))
        inject[u]=v
        extra+=len(q)
    assert set(inject)==set(pos)
    # Explicit degree check after augmentation.
    all_out=Counter({v:len(adj[v]) for v in vertices})
    all_in=Counter()
    for v,lst in adj.items():
        for u,bit in lst:
            all_in[u]+=1
    assert all(all_out[v]==all_in[v] for v in vertices)
    # Hierholzer; encode a closed tour by edge labels.
    start=vertices[0]
    stack=[(start,None)]
    tour=[]
    while stack:
        v=stack[-1][0]
        if adj[v]:
            nxt,letter=adj[v].pop()
            stack.append((nxt,letter))
        else:
            _,letter=stack.pop()
            if letter is not None:
                tour.append(letter)
    s=''.join(reversed(tour))
    assert len(s)==len(required)+extra
    assert feasible_cycle(s,n)
    return len(required),extra,len(s),len(neg)


def recurrences(upper):
    E=[0]*(upper+1)
    E[0]=1
    for n in range(1,upper+1):
        E[n]=2*E[n-1]-E[n-2]+E[n-3] if n>=3 else 2**n
    B=[0]*(upper+1)
    for k in range(3,upper+1):
        B[k]=sum(1 for s in words(k) if s.startswith('10') and s.endswith('01'))
    return E,B


def brute_small(n,length):
    req=set(words(n))
    for bits in product('01',repeat=length):
        s=''.join(bits)
        if ok(s+s[:2]):
            seen={''.join(s[(i+j)%length] for j in range(n)) for i in range(length)}
            if req<=seen:
                return s
    return None


def main():
    E,B=recurrences(14)
    output=[]
    for n in range(3,13):
        e,c,m,degree=build(n)
        formula=(n-1)+sum(j*j*B[n-1-j] for j in range(1,n-3))
        assert e==E[n] and c==formula
        output.append((n,e,c,m,degree))
    assert [x[2] for x in output[:8]]==[2,3,5,10,20,38,70,127]
    for n in (3,4):
        optimum=next(a[3] for a in output if a[0]==n)
        for length in range(n,optimum):
            assert brute_small(n,length) is None,(n,length)
        assert brute_small(n,optimum) is not None
    print('n  admissible  repeated  minimum  negative_vertices')
    for v in output:
        print('%2d %10d %9d %8d %18d'%v)
    print('CHECK_OK: 10 Euler tours, closest-positive shortest paths, and exhaustive n=3,4 optimality')

if __name__=='__main__':
    main()
