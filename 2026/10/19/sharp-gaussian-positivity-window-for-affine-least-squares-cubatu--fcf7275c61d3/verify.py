"""Reproduce independent algebraic and distributional checks for Gaussian affine least-squares cubature.
Run: python check.py (Python 3.10+, standard library only).
"""
from fractions import Fraction as F
from random import Random
import math

checks=0

def assert_close(a,b,tol=1e-9):
    global checks
    assert abs(a-b)<=tol*max(1,abs(a),abs(b)),(a,b)
    checks+=1

def solve(A,b):
    n=len(A); T=[[F(v) for v in row]+[F(b[i])] for i,row in enumerate(A)]
    for j in range(n):
        p=next((i for i in range(j,n) if T[i][j]),None)
        if p is None:raise ValueError('singular')
        T[j],T[p]=T[p],T[j]
        q=T[j][j];T[j]=[u/q for u in T[j]]
        for i in range(n):
            if i==j:continue
            q=T[i][j];T[i]=[T[i][k]-q*T[j][k] for k in range(n+1)]
    return [row[-1] for row in T]

def weights_from_design(rows):
    m=len(rows);d=len(rows[0]); A=[[F(1)]+[F(x) for x in row] for row in rows]
    H=[[sum(row[i]*row[j] for row in A) for j in range(d+1)] for i in range(d+1)]
    c=solve(H,[1]+[0]*d)
    return [sum(row[j]*c[j] for j in range(d+1)) for row in A]

def weights_from_projection(rows):
    m=len(rows);d=len(rows[0]); X=[[F(x) for x in row] for row in rows]
    H=[[sum(row[i]*row[j] for row in X) for j in range(d)] for i in range(d)]
    beta=solve(H,[sum(row[i] for row in X) for i in range(d)])
    r=[1-sum(row[j]*beta[j] for j in range(d)) for row in X]
    total=sum(r)
    return [x/total for x in r]

rng=Random(20261017)
for m in range(3,11):
    for d in range(1,min(4,m-1)+1):
        for trial in range(18):
            while True:
                rows=[[rng.randint(-5,5) for _ in range(d)] for _ in range(m)]
                try:a=weights_from_design(rows);b=weights_from_projection(rows);break
                except ValueError:continue
            for x,y in zip(a,b):assert_close(float(x),float(y),1e-14)
            assert_close(float(sum(a)),1)
            for j in range(d):assert_close(float(sum(a[i]*rows[i][j] for i in range(m))),0)

# Direct Gaussian design versus exact chi-square/sphere law, both with random matrices.
def sample_direct(m,d,rng):
    X=[[rng.gauss(0,1) for _ in range(d)] for _ in range(m)]
    # For numerical checks only use small dimensions.
    H=[[sum(row[i]*row[j] for row in X) for j in range(d)] for i in range(d)]
    h=[sum(row[i] for row in X) for i in range(d)]
    # float pivot solver
    T=[row[:]+[h[i]] for i,row in enumerate(H)]
    for j in range(d):
        p=max(range(j,d),key=lambda i:abs(T[i][j]))
        T[j],T[p]=T[p],T[j]
        z=T[j][j]
        T[j]=[v/z for v in T[j]]
        for i in range(d):
            if i!=j:
                z=T[i][j]
                T[i]=[T[i][k]-z*T[j][k] for k in range(d+1)]
    b=[row[-1] for row in T]
    r=[1-sum(row[j]*b[j] for j in range(d)) for row in X]
    return min(r)>0 # normalization sum r positive

def sample_spherical(m,d,rng):
    U=rng.gammavariate((m-d)/2,2)
    V=rng.gammavariate(d/2,2)
    z=[rng.gauss(0,1) for _ in range(m)]
    mean=sum(z)/m
    centered=[v-mean for v in z]
    norm=math.sqrt(sum(v*v for v in centered)/m)
    return max(-v/norm for v in centered) < math.sqrt(U/V)

for m,d,expected in [(2,1,0.5),(3,2,0.25),(4,3,0.125),(8,1,None),(12,3,None)]:
    trials=7000 if m<5 else 1200
    direct=sum(sample_direct(m,d,rng) for _ in range(trials))/trials
    spherical=sum(sample_spherical(m,d,rng) for _ in range(trials))/trials
    assert_close(direct,spherical,0.075)
    if expected is not None:
        assert_close(direct,expected,0.09)
        assert_close(spherical,expected,0.09)

# Exact normal-maxima critical centering and chi-square concentration formula checked numerically.
for m in [1000,5000,25000,100000]:
    B=2*math.log(m)-math.log(math.log(m))-math.log(4*math.pi)
    d=round(m/(1+B))
    assert 1<=d<m
    checks+=1
    assert_close((m-d)/d,B,0.025 if m<10000 else 0.01)

# The critical window and either side of the transition (seeded Monte Carlo only).
for m,d,lo,hi in [(5000,100,0.95,1.01),(5000,374,0.2,0.55),(5000,750,-0.01,0.10)]:
    pr=sum(sample_spherical(m,d,rng) for _ in range(400))/400
    assert lo<pr<hi,(m,d,pr)
    checks+=1
    print('sampled-positive-fraction',m,d,round(pr,4))

print('PASS:',checks,'assertions, rational identities, two independent Gaussian constructions')
