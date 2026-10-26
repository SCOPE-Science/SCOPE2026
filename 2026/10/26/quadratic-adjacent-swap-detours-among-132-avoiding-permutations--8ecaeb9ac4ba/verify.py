"""Reproduce the adjacency-swap counts and canonical geodesics for Av_n(132).

Usage: python3 verify.py
Requires only Python's standard library.
"""
from collections import deque
from functools import lru_cache
from itertools import permutations
from math import comb

@lru_cache(None)
def avoiding_words(n):
    if n == 0:
        return ((),)
    out = []
    for a in range(n):
        b = n - 1 - a
        for L in avoiding_words(a):
            for R in avoiding_words(b):
                out.append(tuple(t + b for t in L) + (n,) + R)
    assert len(out) == len(set(out))
    return tuple(out)

def avoids_132(p):
    n = len(p)
    return not any(p[i] < p[k] < p[j]
                   for i in range(n)
                   for j in range(i+1,n)
                   for k in range(j+1,n))

def neighbors(p, words):
    out = []
    for j in range(len(p)-1):
        q = p[:j] + (p[j+1],p[j]) + p[j+2:]
        if q in words:
            out.append(q)
    return out

def check(n):
    words = set(avoiding_words(n))
    if n <= 7:
        brute = {p for p in permutations(range(1,n+1)) if avoids_132(p)}
        assert words == brute
    c_n = comb(2*n,n)//(n+1)
    assert len(words) == c_n
    edge_twice = sum(len(neighbors(p,words)) for p in words)
    assert edge_twice%2 == 0
    edges = edge_twice//2
    assert edges == comb(2*n-2,n-2)
    start=tuple(range(1,n+1))
    goal=(n,)+tuple(range(1,n))
    distance={start:0}
    todo=deque([start])
    while todo:
        p=todo.popleft()
        for q in neighbors(p,words):
            if q not in distance:
                distance[q]=distance[p]+1
                todo.append(q)
    assert len(distance)==len(words)
    assert distance[goal]==(n-1)**2
    if n<=7:
        for p in words:
            for j in range(n-1):
                x,y=p[j:j+2]
                q=p[:j]+(y,x)+p[j+2:]
                if x<y:
                    legal=all(p[i]>x for i in range(j))
                else:
                    legal=all(not(y<z<x) for z in p[j+2:])
                assert (q in words) == legal
    return c_n,edges,distance[goal]

if __name__=='__main__':
    for n in range(2,11):
        count,edges,dist=check(n)
        print(f'n={n:2d} C_n={count:5d} edges={edges:6d} distance={dist:3d} OK')
    print('VERIFY_OK')
