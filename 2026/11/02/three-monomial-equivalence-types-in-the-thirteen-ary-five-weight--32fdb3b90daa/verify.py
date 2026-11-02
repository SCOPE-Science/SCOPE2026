#!/usr/bin/env python3
"""Exact projective-line census for three 13-ary cyclic-code specializations.

The code constructs columns in GF(13)^4, using GF(169)=GF(13)[z]/(z^2-2).
The 4 coordinates are equivalent to a trace generator by an invertible row change.
"""
from collections import Counter
from itertools import combinations, product
from math import comb, isqrt

Q = 13
DELTA = 2
N = Q * Q - 1
REPRESENTATIVES = (1, 3, 5)
EXPECTED = {
  1:{0:10264,1:14448,2:3024,3:3360,12:14},
  3:{0:10744,1:12768,2:5040,3:2520,7:24,12:14},
  5:{0:10936,1:11928,2:6384,3:1680,5:168,12:14},
}
EXPECTED_WEIGHTS = {0:1,144:2100,155:14112,156:168,157:12096,168:84}


def multiply(a,b):
    u,v=a; x,y=b
    return ((u*x+DELTA*v*y)%Q,(u*y+v*x)%Q)

def power(a,k):
    out=(1,0)
    while k:
        if k&1:out=multiply(out,a)
        a=multiply(a,a)
        k//=2
    return out

def columns(r):
    return [power((a,b),(Q-1)*r)+(a,b)
            for a in range(Q) for b in range(Q) if (a,b)!=(0,0)]

def normalize(vector):
    v=tuple(x%Q for x in vector)
    pivot=next((x for x in v if x),None)
    if pivot is None:raise ValueError('zero vector')
    t=pow(pivot,-1,Q)
    return tuple(x*t%Q for x in v)

def rank2_key(v,w):
    a=list(v);b=list(w)
    for j in range(4):
        if a[j]:
            t=pow(a[j],-1,Q);a=[x*t%Q for x in a]
            c=b[j];b=[(x-c*y)%Q for x,y in zip(b,a)]
            break
        if b[j]:
            t=pow(b[j],-1,Q);b=[x*t%Q for x in b]
            c=a[j];a=[(x-c*y)%Q for x,y in zip(a,b)]
            a,b=b,a
            break
    else:raise ValueError('zero rows')
    for j in range(4):
        if b[j]:
            t=pow(b[j],-1,Q);b=[x*t%Q for x in b]
            c=a[j];a=[(x-c*y)%Q for x,y in zip(a,b)]
            return tuple(a+b)
    raise ValueError('proportional rows')

def enumerate_pair_secants(vectors):
    tally=Counter(rank2_key(a,b) for a,b in combinations(vectors,2))
    histogram=Counter()
    for c in tally.values():
        j=(1+isqrt(1+8*c))//2
        assert j*(j-1)//2==c, (c,j)
        histogram[j]+=1
    assert sum(comb(k,2)*v for k,v in histogram.items())==comb(N,2)
    return dict(histogram)

def all_rref_lines():
    for i,j in combinations(range(4),2):
        positions=[]
        for row,pivot in ((0,i),(1,j)):
            for col in range(pivot+1,4):
                if col not in (i,j):positions.append((row,col))
        for params in product(range(Q),repeat=len(positions)):
            rows=[[0]*4,[0]*4]
            rows[0][i]=1;rows[1][j]=1
            for (row,col),value in zip(positions,params):rows[row][col]=value
            yield rows[0],rows[1]

def enumerate_all_lines(vectors):
    known={normalize(v) for v in vectors}
    assert len(known)==N
    histogram=Counter();nlines=0
    for a,b in all_rref_lines():
        cnt=int(normalize(b) in known)
        for t in range(Q):
            vec=[(x+t*y)%Q for x,y in zip(a,b)]
            cnt+=int(normalize(vec) in known)
        histogram[cnt]+=1
        nlines+=1
    assert nlines==(Q*Q+1)*(Q*Q+Q+1)==31110
    assert sum(k*v for k,v in histogram.items())==N*(Q*Q+Q+1)
    return dict(histogram)

def full_weight_spectrum(vectors):
    # Pure integer enumeration of the 13^4 generator-row combinations.
    hist=Counter()
    for a,b,c,d in product(range(Q),repeat=4):
        w=sum(bool((a*u+b*v+c*x+d*y)%Q) for u,v,x,y in vectors)
        hist[w]+=1
    return dict(hist)

def main():
    assert pow(DELTA,(Q-1)//2,Q)==Q-1
    assert {r for r in range(1,14) if __import__('math').gcd(r,14)==1}=={1,3,5,9,11,13}
    for r in REPRESENTATIVES:
        pts=columns(r)
        pair=enumerate_pair_secants(pts)
        full=enumerate_all_lines(pts)
        spectrum=full_weight_spectrum(pts)
        print('r=',r,'pair=',dict(sorted(pair.items())),'full=',dict(sorted(full.items())),'weights=',dict(sorted(spectrum.items())))
        assert pair=={k:v for k,v in full.items() if k>=2}
        assert full==EXPECTED[r]
        assert spectrum==EXPECTED_WEIGHTS
    # Frobenius on the last GF(169) coordinate maps the r-model to -r.
    for r in REPRESENTATIVES:
        transported={normalize((u,v,x,(-y)%Q)) for u,v,x,y in columns(r)}
        assert transported=={normalize(v) for v in columns((-r)%14)}
    print('VERIFY_OK')
if __name__=='__main__':main()
