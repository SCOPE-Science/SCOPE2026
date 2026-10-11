from fractions import Fraction
from itertools import combinations

def spider_edges(lengths):
    edges=[]
    for i,L in enumerate(lengths):
        for j in range(1,L+1):
            edges.append((i,j))
    return edges

def beta_ratio(lengths, A):
    d=len(lengths)
    C={(i,1) for i in range(d)}
    A=set(A)
    leaves=sum((i,L) in A for i,L in enumerate(lengths))
    beta=leaves + ((2-d) if C <= A else 0)
    return beta, Fraction(beta,len(A))

def check_spider(lengths):
    d=len(lengths)
    r=sum(L>=2 for L in lengths)
    assert r>=3
    E=spider_edges(lengths)
    C={(i,1) for i in range(d)}
    target=Fraction(2-r,d)
    best=None
    mins=[]
    for mask in range(1,1<<len(E)):
        A=[E[j] for j in range(len(E)) if (mask>>j)&1]
        _,q=beta_ratio(lengths,A)
        if best is None or q<best:
            best=q; mins=[set(A)]
        elif q==best:
            mins.append(set(A))
    assert best==target
    assert mins==[C], (lengths,best,mins,C)

samples=[
    (2,2,2),
    (2,3,2,1),
    (5,2,3,1,1),
    (2,2,2,2),
    (3,1,2,1,4),
]
for s in samples:
    check_spider(s)

for d in range(3,10):
    for r in range(3,d+1):
        c=Fraction(2-r,d)
        pL=Fraction(d+r-2,2*d*(r-1))
        pU=Fraction(r-2,2*d*(r-1))
        assert r*pL+(d-r)*pU == 1
        D = r/pL + (d-r)/pU if d>r else r/pL
        qL=1/(pL*D)
        assert (2-d)*qL == c
        if d>r:
            qU=1/(pU*D)
            assert 1+(2-d)*qU == c
            assert pL/pU == Fraction(d+r-2,r-2)
        else:
            assert pL == Fraction(1,d)

print("VERIFY_OK samples=5 formulas=d3..9")
