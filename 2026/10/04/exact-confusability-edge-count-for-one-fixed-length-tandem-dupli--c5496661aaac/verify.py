#!/usr/bin/env python3
from itertools import product

def tandem_duplicate(x, ell, pos):
    return x[:pos] + x[pos:pos+ell] + x[pos:pos+ell] + x[pos+ell:]

def derivative(x, ell, q):
    a = x[:ell]
    b = tuple((x[ell+j] - x[j]) % q for j in range(len(x)-ell))
    return a, b

def predicted_edges(q, ell, n):
    if n <= 2*ell:
        return 0
    N = n - 2*ell
    num = N*(q-1)*(q**(n-ell-2))*((q-1)*(N-1)+2*q)
    assert num % 2 == 0
    return num//2

def direct_check(q, ell, n):
    words = list(product(range(q), repeat=n))
    balls = {}
    for x in words:
        outs = set()
        a,b = derivative(x, ell, q)
        for p in range(n-ell+1):
            y = tandem_duplicate(x, ell, p)
            outs.add(y)
            ay,by = derivative(y, ell, q)
            assert ay == a
            assert by == b[:p] + (0,)*ell + b[p:]
        balls[x] = outs
    edges = 0
    max_intersection = 0
    for i,x in enumerate(words):
        for y in words[i+1:]:
            common = balls[x].intersection(balls[y])
            if common:
                edges += 1
                max_intersection = max(max_intersection, len(common))
                assert len(common) == 1
    assert edges == predicted_edges(q, ell, n), (q,ell,n,edges,predicted_edges(q,ell,n))
    return edges, max_intersection

def main():
    cases=[]
    for ell in (1,2,3):
        for n in range(ell, min(2*ell+5,9)+1):
            cases.append((2,ell,n))
    for ell in (1,2):
        for n in range(ell,7):
            cases.append((3,ell,n))
    for n in range(1,6):
        cases.append((4,1,n))
    seen=set()
    rows=[]
    for q,ell,n in cases:
        if (q,ell,n) in seen:
            continue
        seen.add((q,ell,n))
        e,m=direct_check(q,ell,n)
        rows.append((q,ell,n,e,m))
    special=[]
    for n in range(2,11):
        e=predicted_edges(2,2,n)
        rhs=0 if n<=4 else (2**(n-5))*(n-4)*(n-1)
        assert e==rhs
        special.append((n,e))
    print('checked_cases=',len(rows))
    print('binary_ell2_edges=',','.join(f'{n}:{e}' for n,e in special))
    print('max_common_descendant_count=',max((m for *_,m in rows), default=0))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
