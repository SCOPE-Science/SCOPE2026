"""Exact independent checks for same-side UST distance law and likelihood-ratio order.

Run: python verify.py  (Python 3.9+, standard library only)
"""
from fractions import Fraction
from itertools import combinations
from math import prod

checks = 0

def assert_equal(x, y):
    global checks
    assert x == y, (x, y)
    checks += 1

def falling(x, r):
    assert r >= 0
    return prod(range(x-r+1, x+1))

def mass(a, b, j):
    if j < 1 or j > min(a-1, b):
        return Fraction(0)
    n=a+b
    return Fraction(falling(a-2, j-1)*falling(b,j)*(j*n+b-j*(j+1)), b**(j+1)*a**j)

def survival(a, b, j):
    if j <= 1:
        return Fraction(1)
    if j > min(a-1,b):
        return Fraction(0)
    return Fraction(prod((a-i-1)*(b-i) for i in range(1,j)), (a*b)**(j-1))

# Exact analytic law, tail recursion, normalization and ordered likelihood ratios.
for a in range(2,31):
    for b in range(1,31):
        m=min(a-1,b)
        assert_equal(sum((mass(a,b,j) for j in range(1,m+1)),Fraction(0)),Fraction(1))
        for j in range(1,m+2):
            assert_equal(sum((mass(a,b,k) for k in range(j,m+1)),Fraction(0)),survival(a,b,j))
            if j <=m:
                assert_equal(mass(a,b,j), survival(a,b,j)-survival(a,b,j+1))
        if a>b>=2:
            for j in range(1,b):
                assert_equal(mass(a,b,j+1)*mass(b,a,j)>mass(a,b,j)*mass(b,a,j+1),True)
            assert_equal(mass(a,b,b)>0,True)
            assert_equal(mass(b,a,b),Fraction(0))

# Independent exact spanning-tree enumeration, not reusing the path-count formula.
def exact_tree_distances(a,b):
    v=a+b
    edges=[(i,a+j) for i in range(a) for j in range(b)]
    counts_A={};counts_B={};tree_count=0
    for chosen in combinations(edges, v-1):
        parent=list(range(v))
        def find(x):
            while parent[x]!=x:
                x=parent[x]
            return x
        valid=True
        for u,w in chosen:
            ru,rw=find(u),find(w)
            if ru==rw:
                valid=False;break
            parent[ru]=rw
        if not valid:
            continue
        tree_count+=1
        adj=[[] for _ in range(v)]
        for x,y in chosen:
            adj[x].append(y);adj[y].append(x)
        for start,end,counts in [(0,1,counts_A),(a,a+1,counts_B)]:
            if end>=v or (start<a and end>=a):
                continue
            frontier=[(start,-1,0)]
            while frontier:
                x,prev,d=frontier.pop()
                if x==end:
                    assert d%2==0
                    counts[d//2]=counts.get(d//2,0)+1
                    break
                frontier.extend((y,x,d+1) for y in adj[x] if y!=prev)
    return counts_A,counts_B,tree_count

for a in range(2,5):
    for b in range(2,5):
        ca,cb,total=exact_tree_distances(a,b)
        assert_equal(total, a**(b-1)*b**(a-1))
        for j in range(1,min(a-1,b)+1):
            assert_equal(Fraction(ca.get(j,0),total),mass(a,b,j))
        for j in range(1,min(b-1,a)+1):
            assert_equal(Fraction(cb.get(j,0),total),mass(b,a,j))

print('PASS',checks,'exact checks; independent tree enumeration up to K_4,4')
