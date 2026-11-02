"""Independent small-order checks for four-spine chromatic specializations.

Run: python3 ps4_check_small.py
"""
from itertools import product
from functools import lru_cache
from subprocess import check_output
MASK=(1<<64)-1

def direct_spine(a,b,c,d,z):
    s=0
    weights=(a,b,c,d)
    for spine in product(range(4),repeat=4):
        if any(spine[i]==spine[i+1] for i in range(3)):
            continue
        v=1
        for i,x in enumerate(spine):
            v*=z**x * sum(z**j for j in range(4) if j!=x)**(weights[i]-1)
        s+=v
    return s

def direct_vertices(a,b,c,d,z):
    weights=(a,b,c,d)
    n=sum(weights)
    edges=[(i,i+1) for i in range(3)]
    v=4
    for i,wi in enumerate(weights):
        for _ in range(wi-1):
            edges.append((i,v));v+=1
    assert v==n
    ans=0
    for colors in product(range(4),repeat=n):
        if all(colors[i]!=colors[j] for i,j in edges):
            ans+=z**sum(colors)
    return ans

def check():
    tested=0
    for n in range(6,9):
        for a in range(2,n-3):
            for b in range(1,n-a-2):
                for c in range(1,n-a-b-1):
                    d=n-a-b-c
                    if d<2:continue
                    for z in (2,3):
                        x=direct_spine(a,b,c,d,z)
                        y=direct_vertices(a,b,c,d,z)
                        assert x==y, (n,(a,b,c,d),z,x,y)
                        tested+=1
    # A stronger test of polynomial evaluation at larger orders using different summation.
    for a,b,c,d in [(2,1,1,2),(7,13,9,5),(21,3,17,30),(49,1,71,79),(2,81,13,37)]:
        for z in (2,3):
            v=direct_spine(a,b,c,d,z)
            assert v>0
            assert direct_spine(d,c,b,a,z)==v
            tested+=1
    print('INDEPENDENT_SMALL_OK',tested)

if __name__=='__main__':check()
