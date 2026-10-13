#!/usr/bin/env python3
"""Recompute projective-plane incidence and check explicit sequence b-colorings.

Requires only the Python standard library. Run: python3 verify.py
"""
import itertools
import json
from pathlib import Path

DATA = json.loads(Path(__file__).with_name('certificates.json').read_text(encoding='utf-8'))

def add(q,a,b):
    return (a+b)%3 if q==3 else a^b

def mul(q,a,b):
    if q==3:
        return a*b%3
    result=0
    for j in range(2):
        if b&(1<<j):
            result ^= a<<j
    for j in (3,2):
        if result&(1<<j):
            result ^= 7<<(j-2)
    return result

def inv(q,a):
    return next(b for b in range(1,q) if mul(q,a,b)==1)

def norm(q,v):
    first=next(a for a in v if a!=0)
    scalar=inv(q,first)
    return tuple(mul(q,scalar,a) for a in v)

def check_case(q):
    case=DATA['cases'][str(q)]
    points=[tuple(v) for v in case['points']]
    expected={norm(q,v) for v in itertools.product(range(q),repeat=3) if any(v)}
    assert len(expected)==q*q+q+1
    assert set(points)==expected and len(points)==len(expected)
    N=len(points)
    colors=case['colors']
    assert len(colors)==2*N and set(colors)==set(range(q+2))
    for a,b,c in itertools.product(range(q),repeat=3):
        assert add(q,add(q,a,b),c)==add(q,a,add(q,b,c))
    for a,b,c in itertools.product(range(q),repeat=3):
        assert mul(q,mul(q,a,b),c)==mul(q,a,mul(q,b,c))
        assert mul(q,a,add(q,b,c))==add(q,mul(q,a,b),mul(q,a,c))
    for a in range(1,q):
        assert mul(q,a,inv(q,a))==1
    nbr=[[] for _ in range(2*N)]
    for i,p in enumerate(points):
        for j,l in enumerate(points):
            dot=0
            for a,b in zip(p,l):
                dot=add(q,dot,mul(q,a,b))
            if dot==0:
                nbr[i].append(N+j)
                nbr[N+j].append(i)
    assert all(len(x)==q+1 for x in nbr)
    # Every pair of distinct projective points is on precisely one line.
    for i in range(N):
        for j in range(i+1,N):
            assert len(set(nbr[i])&set(nbr[j]))==1
    # Connectedness, and a six-cycle exists; bipartiteness and no C4 give girth six.
    reached={0}; stack=[0]
    while stack:
        for v in nbr[stack.pop()]:
            if v not in reached:
                reached.add(v);stack.append(v)
    assert len(reached)==2*N
    # Three noncollinear points provide a six-cycle in their incidence graph.
    triples=next((i,j,k) for i in range(N) for j in range(i+1,N)
                 for k in range(j+1,N)
                 if len(set(nbr[i])&set(nbr[j])&set(nbr[k]))==0)
    i,j,k=triples
    edges=[(set(nbr[i])&set(nbr[j])).pop(),
           (set(nbr[j])&set(nbr[k])).pop(),
           (set(nbr[k])&set(nbr[i])).pop()]
    assert len(set(edges))==3
    for u in range(2*N):
        for v in nbr[u]:
            assert colors[u]!=colors[v]
    bverts={c:[] for c in range(q+2)}
    for v in range(2*N):
        if set(colors[w] for w in nbr[v])==set(range(q+2))-{colors[v]}:
            bverts[colors[v]].append(v)
    assert min(map(len,bverts.values()))>=2
    print(f'q={q}: |V|={2*N}, |E|={N*(q+1)}, regular_degree={q+1}, girth=6, colors={q+2}')
    print('b-vertex counts by color:',*[len(bverts[c]) for c in range(q+2)])
    print('two explicit b-vertices per color (points 0..N-1, lines N..2N-1):',
          *(f'{c}:{bverts[c][:2]}' for c in range(q+2)))
    print('status: PASS')

if __name__=='__main__':
    for q in (3,4):
        check_case(q)
