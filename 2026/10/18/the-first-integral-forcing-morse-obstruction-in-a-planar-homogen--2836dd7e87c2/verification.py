#!/usr/bin/env python3
"""Exact arithmetic checks for a planar homogeneous cubic flow."""
from fractions import Fraction
from itertools import permutations


def add(a, b):
    c = dict(a)
    for k, v in b.items():
        c[k] = c.get(k, 0) + v
    return {k:v for k,v in c.items() if v}


def scale(a, s):
    return {k:s*v for k,v in a.items()}


def multiply(a, b):
    c = {}
    for (i,j), av in a.items():
        for (k,l), bv in b.items():
            key=(i+k,j+l)
            c[key]=c.get(key,0)+av*bv
    return {k:v for k,v in c.items() if v}


def differentiate(a, axis):
    c = {}
    for (i,j), v in a.items():
        k=(i-1,j) if axis==0 else (i,j-1)
        t=i if axis==0 else j
        if t: c[k]=c.get(k,0)+t*v
    return c


def gram(Q, n):
    a = {}
    for i,row in enumerate(Q):
        for j,v in enumerate(row):
            key=(2*n-i-j,i+j)
            a[key]=a.get(key,0)+v
    return {k:v for k,v in a.items() if v}


def determinant(A):
    n=len(A)
    total=0
    for p in permutations(range(n)):
        inversions=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        product=1
        for i in range(n): product*=A[i][p[i]]
        total+=(-1 if inversions%2 else 1)*product
    return total


def minors(Q):
    return [determinant([row[:i] for row in Q[:i]]) for i in range(1,len(Q)+1)]


def check():
    fx={(3,0):1,(1,2):-3,(2,1):-1,(0,3):-1}
    fy={(3,0):1,(1,2):1,(2,1):1,(0,3):-3}
    V={(4,0):33,(3,1):-150,(2,2):326,(1,3):-318,(0,4):125}
    minus_D={(6,0):18,(5,1):80,(4,2):-254,(3,3):-896,(2,4):3598,(1,5):-3664,(0,6):1182}
    Q4=[[33,-75,50],[-75,226,-159],[50,-159,125]]
    Q6=[[18,40,-220,140],[40,186,-588,330],[-220,-588,2938,-1832],[140,330,-1832,1182]]
    checks=0
    assert gram(Q4,2)==V;checks+=1
    assert gram(Q6,3)==minus_D;checks+=1
    Lie=add(multiply(differentiate(V,0),fx),multiply(differentiate(V,1),fy))
    assert scale(Lie,-1)==minus_D;checks+=1
    for Q,expect in [(Q4,[33,1833,22352]),(Q6,[18,1748,258632,5083552])]:
        assert Q==[list(r) for r in zip(*Q)]
        assert minors(Q)==expect
        assert all(v>0 for v in expect)
        checks+=3
    r2={(2,0):1,(0,2):1}
    qd={(2,0):1,(0,2):-1}
    qe={(1,1):2}
    LD0=add(multiply(differentiate(r2,0),fx),multiply(differentiate(r2,1),fy))
    LDd=add(multiply(differentiate(qd,0),fx),multiply(differentiate(qd,1),fy))
    LDe=add(multiply(differentiate(qe,0),fx),multiply(differentiate(qe,1),fy))
    def evaluation(P,x,y):return sum(v*x**i*y**j for (i,j),v in P.items())
    for pt,expect in [((1,0),(2,2,2)),((1,1),(-8,-8,-8)),((2,1),(10,-34,38))]:
        got=tuple(evaluation(p,*pt) for p in (LD0,LDd,LDe))
        assert got==expect, (pt,got)
        checks+=1
    # The angular derivative at (1,0) is -4d+4e.
    got=tuple(evaluation(differentiate(p,1),1,0) for p in (LD0,LDd,LDe))
    assert got==(0,-4,4);checks+=1
    # For d=e=-1/2 the derivative at (2,1) is strictly positive.
    result=LD0
    result=add(result,scale(LDd,Fraction(-1,2)))
    result=add(result,scale(LDe,Fraction(-1,2)))
    assert evaluation(result,2,1)==8;checks+=1
    print('PASS: %d exact identities / principal-minor certificates' % checks)

if __name__=='__main__':check()
