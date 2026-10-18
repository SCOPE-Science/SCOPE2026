"""Exact integer checks for Roman-weight polynomial recurrences on P4-sparse graphs.

This checker generates graphs independently, enumerates all vertex labels,
and compares the resulting weight polynomials with the closed recurrences.
The mathematical theorem uses the recurrences' proofs, not extrapolation from these tests.
"""
from itertools import product
from collections import Counter
import random


def add(a,b):
    p=[0]*max(len(a),len(b))
    for i,v in enumerate(a): p[i]+=v
    for i,v in enumerate(b): p[i]+=v
    return trim(p)
def scale(a,k): return trim([x*k for x in a])
def sub(a,b): return add(a,scale(b,-1))
def mul(a,b):
    p=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): p[i+j]+=x*y
    return trim(p)
def power(a,n):
    p=[1]
    for _ in range(n): p=mul(p,a)
    return p
def zp(k): return [0]*k+[1]
def trim(p):
    while len(p)>1 and not p[-1]: p.pop()
    return p

Q=[1,1,1]; B=[1,1]

def roman_bruteforce(g):
    n,edges,_=g
    neighbors=[set() for _ in range(n)]
    for i,j in edges:
        neighbors[i].add(j); neighbors[j].add(i)
    counts=[0]*(2*n+1)
    for f in product(range(3),repeat=n):
        if all(f[v] or any(f[w]==2 for w in neighbors[v]) for v in range(n)):
            counts[sum(f)]+=1
    return trim(counts)

def atom(): return 1,set(),[0,1,1]  # one isolated vertex: assignments 1 or 2

def empty(): return 0,set(),[1]

def union(g,h):
    a,e,p=g; b,d,q=h
    return a+b,e|{(u+a,v+a) for u,v in d},mul(p,q)

def join(g,h):
    a,e,p=g; b,d,q=h
    edges=e|{(u+a,v+a) for u,v in d}|{(u,v+a) for u in range(a) for v in range(b)}
    polynomial=add(zp(a+b),mul(sub(p,zp(a)),power(B,b)))
    polynomial=add(polynomial,mul(sub(q,zp(b)),power(B,a)))
    polynomial=add(polynomial,mul(sub(power(Q,a),power(B,a)),sub(power(Q,b),power(B,b))))
    return a+b,edges,polynomial

def spider(g,n,thick):
    r,head,head_poly=g
    # Vertex order: core c_i [0,n), feet s_i [n,2n), head [2n,2n+r)
    edges={(i,j) for i in range(n) for j in range(i+1,n)}
    for i in range(n):
        for j in range(n):
            if (i!=j)==bool(thick): edges.add((i,n+j))
    for i in range(n):
        for j in range(r): edges.add((i,2*n+j))
    edges|={(2*n+u,2*n+v) for u,v in head}
    Z=mul(B,[0,1,1]) # (1+z)(z+z^2)
    U=power(Q,r)
    if not thick:
        X=mul(zp(2),Q)
        plus=sub(power(add(X,Z),n),power(Z,n))
        nocore_nohead=power([0,0,2,1],n) # (2z^2+z^3)^n
    else:
        E=mul(B,Q) # (1+z)(1+z+z^2)
        plus=sub(sub(power(power(Q,2),n),power(E,n)),scale(mul(zp(2),power(E,n-1)),n))
        feet_ge2=sub(sub(power([0,1,1],n),zp(n)),scale(zp(n+1),n))
        nocore_nohead=add(mul(power(B,n),feet_ge2),scale(mul(zp(n+2),power(B,n-1)),n))
        nocore_nohead=add(nocore_nohead,zp(2*n))
    # Head with at least one 2: it must itself be Roman dominating.
    polynomial=add(mul(U,plus),mul(sub(head_poly,zp(r)),power(Z,n)))
    polynomial=add(polynomial,mul(zp(r),nocore_nohead))
    return 2*n+r,edges,polynomial

def assert_graph(g):
    brute=roman_bruteforce(g)
    if g[2]!=brute: raise AssertionError(f'mismatch vertices={g[0]}, model={g[2]}, brute={brute}')
    assert all(c>=0 for c in brute)
    assert sum(brute)<=3**g[0]
    return 3**g[0]


def run():
    checks=0; assignments=0
    heads=[empty(),atom(),union(atom(),atom()),join(atom(),atom()),
           union(union(atom(),atom()),atom()),
           join(join(atom(),atom()),atom()),
           union(join(atom(),atom()),atom())]
    for n in (2,3,4):
        for head in heads:
            for thick in (False,True):
                g=spider(head,n,thick)
                if g[0]>11: continue
                assignments+=assert_graph(g); checks+=1
    rng=random.Random(174213)
    # Random composition with headless and headed spiders; no formula used by brute checker.
    for _ in range(85):
        g=atom()
        for __ in range(rng.randint(2,5)):
            kind=rng.choice(['union','join','spider'])
            if kind=='spider':
                n=rng.randint(2,3)
                if g[0]+2*n>11: break
                g=spider(g,n,rng.choice([True,False]))
            else:
                h=rng.choice(heads[1:])
                if g[0]+h[0]>11: break
                g=union(g,h) if kind=='union' else join(g,h)
            assignments+=assert_graph(g);checks+=1
    # Critical aggregate results for headless spiders and independent auxiliary head.
    for n in range(2,10):
        for thick in (False,True):
            g=spider(empty(),n,thick)
            p=g[2]
            minimum=next(i for i,x in enumerate(p) if x)
            expected=3 if thick else n+1
            if (minimum,p[minimum])!=(expected,n):
                raise AssertionError(('minimum',n,thick,minimum,p[minimum],expected,n))
    print('PASS: independent exhaustive checks on',checks,'graph instances;')
    print('PASS: ',format(assignments,','),'label assignments examined.')
    print('PASS: 16 extremal tests of headless spiders through size n=9.')
    print('PASS: union, join, and both spider transforms matched every enumerated coefficient.')

if __name__=='__main__':run()
