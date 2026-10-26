"""Exact checks for the bipartite graph centered-maximal variation bounds.

Run: python3 check.py  (Python standard library only).
These finite tests supplement, and do not replace, the universal proof.
"""
from fractions import Fraction as Q
from itertools import product
from random import Random

COUNT = 0

def check(a, b, vals):
    global COUNT
    n = a+b
    values = tuple(map(Q, vals))
    x = values[:a]
    y = values[a:]
    avg_a = sum(x)/a
    avg_b = sum(y)/b
    mu = sum(values)/n
    out_a = tuple(max(t, (t+b*avg_b)/(b+1), mu) for t in x)
    out_b = tuple(max(t, (t+a*avg_a)/(a+1), mu) for t in y)
    v = sum(abs(u-w) for u in x for w in y)
    w = sum(abs(u-z) for u in out_a for z in out_b)
    m = min(a,b)
    M = max(a,b)
    U = 1 + Q(a*b, (m+1)*n)
    assert w <= U*v, (a,b,values,w,v,U)
    COUNT += 1
    if avg_a >= avg_b:
        g_a=tuple(max(t,mu) for t in x)
        assert out_a==g_a
        for z,gg in zip(out_b,(max(t,mu) for t in y)):
            assert 0 <= z-gg <= Q(a*b, (a+1)*n)*(avg_a-avg_b)
            COUNT+=1
    else:
        g_b=tuple(max(t,mu) for t in y)
        assert out_b==g_b
        for z,gg in zip(out_a,(max(t,mu) for t in x)):
            assert 0 <= z-gg <= Q(a*b, (b+1)*n)*(avg_b-avg_a)
            COUNT+=1
    return w/v if v else Q(0)

def delta(a,b):
    global COUNT
    m=min(a,b); M=max(a,b); n=m+M
    vec=[0]*n
    vec[0 if a==m else a]=1
    ratio=check(a,b,vec)
    L=2-Q(3,m+1)-Q(m-1,n)
    U=1+Q(m*M,(m+1)*n)
    assert ratio==L,(a,b,ratio,L)
    assert U-L==Q(2*n-1,(m+1)*n)
    assert L <= U < 2
    COUNT+=4

for a,b in [(2,2),(2,3),(3,3),(3,4),(4,4),(2,9),(6,11),(21,21),(11,51),(19,190),(31,961)]:
    delta(a,b)

for a,b in [(2,2),(2,3),(3,3),(3,4),(4,4),(2,5)]:
    n=a+b
    for seq in product(range(3),repeat=n):
        check(a,b,seq)

rnd=Random(83911)
for a,b in [(2,5),(5,2),(5,5),(5,13),(13,5),(11,11),(6,24),(24,6),(13,71),(71,13)]:
    for k in range(450):
        check(a,b,[Q(rnd.randrange(0,70),rnd.randrange(1,20)) for _ in range(a+b)])

# Exhibit true expansion on a balanced biclique, and convergence mechanisms.
assert delta(4,4) is None
C44=2-Q(3,5)-Q(3,8)
assert C44==Q(41,40)>1
assert 2-Q(3,1001)-Q(999,2000)>Q(149,100)
assert 2-Q(3,101)-Q(99,10100)>Q(19,10)
COUNT+=4
print(f"PASS: {COUNT} exact rational assertions and checked configurations")
