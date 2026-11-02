"""Reproducible combinatorial and probabilistic checks for Haar 4-cube sections.
Python standard library only. The analytic Gaussian/Cauchy and reflection
arguments are proved in the accompanying mathematical statement.
"""
from fractions import Fraction
from itertools import combinations, product
from collections import Counter
from math import atan, sqrt, pi
from random import Random

def signature(values):
    """Compute section vertices by crossed 4-cube edges, then all facet sizes."""
    v = [Fraction(x) for x in values]
    vertices=[]
    for i in range(4):
        js=[j for j in range(4) if j != i]
        for eps in product((-1,1),repeat=3):
            s=sum(v[j]*eps[k] for k,j in enumerate(js))
            if -v[i]<s<v[i]:
                z=list(map(Fraction,(0,0,0,0)))
                for k,j in enumerate(js): z[j]=Fraction(eps[k])
                z[i]=-s/v[i]
                vertices.append(tuple(z))
    assert len(vertices)==len(set(vertices))
    facet_sizes=[]
    for i in range(4):
        for s in (-1,1):
            z=sum(x[i]==s for x in vertices)
            if z >=3: facet_sizes.append(z)
            else: assert z==0, (values,i,s,z)
    return (len(vertices),tuple(sorted(facet_sizes)))

EXPECTED={
    "cube": (8,(4,)*6),
    "triangular_pentagonal": (12,(3,)*2+(5,)*6),
    "hexagonal_quadrilateral": (12,(4,)*6+(6,)*2),
}

def chamber(v):
    a,b,c,d=v
    assert 0<a<b<c<d
    x=d-a-b-c
    y=d+a-b-c
    assert x!=0 and y!=0
    if x>0: return "cube"
    return "triangular_pentagonal" if y>0 else "hexagonal_quadrilateral"

def reflection(v):
    a,b,c,d=v
    y=d+a-b-c
    return tuple(z for z in (a-y/2,b+y/2,c+y/2,d-y/2))

def run():
    assert abs((1-2*atan(sqrt(3))/pi)-1/3)<1e-15
    assert signature((1,2,3,7)) == EXPECTED["cube"]
    assert signature((1,2,3,5)) == EXPECTED["triangular_pentagonal"]
    assert signature((6,8,10,11)) == EXPECTED["hexagonal_quadrilateral"]
    checked=Counter()
    for v in combinations(range(1,17),4):
        a,b,c,d=map(Fraction,v)
        if d==a+b+c or d+a==b+c: continue
        v=(a,b,c,d)
        k=chamber(v)
        assert signature(v)==EXPECTED[k],(v,k,signature(v))
        checked[k]+=1
        if k!='cube':
            w=reflection(v)
            assert 0<w[0]<w[1]<w[2]<w[3]
            assert sum(z*z for z in v)==sum(z*z for z in w)
            assert reflection(w)==v
            assert chamber(w)!=k
            assert signature(w)==EXPECTED[chamber(w)]
    assert all(checked.values())
    rng=Random(20261031)
    N=75000
    freq=Counter()
    for _ in range(N):
        v=sorted(abs(rng.gauss(0,1)) for _ in range(4))
        freq[chamber(v)]+=1
    assert all(abs(freq[k]/N-1/3)<0.012 for k in EXPECTED),freq
    print("GRID_CHAMBERS",dict(checked))
    print("GAUSSIAN_CHAMBERS",dict(freq))
    print("ALL_FOURCUBE_THREE_TYPE_CHECKS_PASSED")

if __name__=='__main__':run()
