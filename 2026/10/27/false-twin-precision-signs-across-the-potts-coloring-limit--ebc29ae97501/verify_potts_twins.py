#!/usr/bin/env python3
"""Independent exact small-instance checks for a Potts false-twin precision theorem.
Uses only Python standard library. Finite checks are not infinite proofs.
"""
from fractions import Fraction as F
from itertools import product


def inverse(a):
    n=len(a)
    m=[list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for k in range(n):
        piv=next(i for i in range(k,n) if m[i][k])
        m[k],m[piv]=m[piv],m[k]
        z=m[k][k]
        m[k]=[v/z for v in m[k]]
        for i in range(n):
            if i==k:continue
            z=m[i][k]
            m[i]=[x-z*y for x,y in zip(m[i],m[k])]
    return [row[n:] for row in m]


def chromatic(edges,n):
    for k in range(1,n+1):
        for colors in product(range(k),repeat=n):
            if all(colors[i]!=colors[j] for i,j in edges):return k
    raise AssertionError('chromatic number absent')


def test_case(n, N, others, q, w):
    G=set(tuple(sorted(e)) for e in others)
    for z in N:
        G.add((0,z));G.add((1,z))
    assert (0,1) not in G
    assert q>=3
    d=len(N)
    weight=F(0)
    ss=[F(0) for _ in range(n)]
    pairs=[[F(0) for _ in range(n)] for _ in range(n)]
    # Directly enumerate all colorings, including nonproper ones if w>0.
    for color in product(range(q),repeat=n):
        mono=sum(color[i]==color[j] for i,j in G)
        z=w**mono
        if not z:continue
        weight+=z
        marks=[i for i,t in enumerate(color) if t==0]
        for i in marks:ss[i]+=z
        for i in marks:
            for j in marks:pairs[i][j]+=z
    assert weight>0
    means=[t/weight for t in ss]
    assert means==[F(1,q)]*n
    cov=[[pairs[i][j]/weight-means[i]*means[j] for j in range(n)] for i in range(n)]
    precision=inverse(cov)
    invz=inverse([row[2:] for row in cov[2:]])
    B=[cov[i][0] for i in range(2,n)]
    coef=[sum(invz[i][j]*B[j] for j in range(n-2)) for i in range(n-2)]
    R=S=F(0)
    normal=F(0)
    for H in product(range(q),repeat=n-2):
        base=w**sum(H[i-2]==H[j-2] for i,j in G if i>=2 and j>=2)
        if not base:continue
        counts=[sum(H[x-2]==c for x in N) for c in range(q)]
        weights=[w**a for a in counts]
        total=sum(weights)
        if not total:continue
        p=weights[0]/total
        prob=base*total*total/weight
        normal+=prob
        z=[F(c==0) for c in H]
        fit=means[0]+sum(coef[i]*(z[i]-means[i+2]) for i in range(n-2))
        R+=prob*(p-fit)**2
        S+=prob*p*(1-p)
    assert normal==1
    assert S>0
    assert precision[0][1]==-R/(S*(S+2*R))
    assert precision[0][1]<=0
    if w==1 or d<=1:
        assert precision[0][1]==0
    if w>0 and w!=1 and d>=2:
        assert precision[0][1]<0
    if w==0:
        clique=all(tuple(sorted((i,j))) in G for i in N for j in N if i<j)
        if clique:assert precision[0][1]==0
        if q>=n and not clique:assert precision[0][1]<0
    return 1


def main():
    cases=0
    for n in [3,4,5]:
        m=n-2
        poss=[(i,j) for i in range(2,n) for j in range(i+1,n)]
        for mask in range(1<<(m+len(poss))):
            N=[z for i,z in enumerate(range(2,n)) if mask>>i&1]
            others=[z for i,z in enumerate(poss) if mask>>(m+i)&1]
            E=others+[(0,z) for z in N]+[(1,z) for z in N]
            chi=chromatic(E,n)
            for q in [3,4]:
                for w in [F(0),F(1,2),F(2),F(1)]:
                    if w==0 and q<chi+1:continue
                    cases+=test_case(n,N,others,q,w)
    for n in [6]:
        m=n-2
        poss=[(i,j) for i in range(2,n) for j in range(i+1,n)]
        for mask in [0,3,15,255,341,682,1023]:
            N=[z for i,z in enumerate(range(2,n)) if mask>>i&1]
            others=[z for i,z in enumerate(poss) if mask>>(m+i)&1]
            E=others+[(0,z) for z in N]+[(1,z) for z in N]
            chi=chromatic(E,n)
            for q,w in [(6,F(0)),(3,F(1,2)),(3,F(2))]:
                if w==0 and q<chi+1:continue
                cases+=test_case(n,N,others,q,w)
    print('EXACT_POTTS_CHECK_OK', 'graph_palette_temperature_cases',cases)

if __name__=='__main__':main()
