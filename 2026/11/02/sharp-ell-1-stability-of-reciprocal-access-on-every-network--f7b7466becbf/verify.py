"""Exact checks for reciprocal weighted-min access and its inverse."""
from fractions import Fraction as F
from itertools import combinations
from random import Random

rng=Random(2610114)

def access(x, edges):
    y=list(x)
    for i,j,w in edges:
        z=w*min(x[i],x[j])
        y[i]+=z
        y[j]+=z
    return y

def inverse(a, edges):
    n=len(a)
    rem=set(range(n))
    residual=list(a)
    out=[None]*n
    while rem:
        candidates=[]
        for i in sorted(rem):
            d=F(1)+sum(w for p,q,w in edges if (p==i and q in rem) or (q==i and p in rem))
            candidates.append((residual[i]/d,i))
        level,i=min(candidates)
        assert level>=0
        out[i]=level
        rem.remove(i)
        for p,q,w in edges:
            if p==i and q in rem: residual[q]-=w*level
            elif q==i and p in rem: residual[p]-=w*level
    return out

checks=0
for n in range(1,7):
    for rep in range(500 if n<5 else 120):
        edges=[(i,j,F(rng.randrange(1,7),rng.randrange(1,6))) for i,j in combinations(range(n),2) if rng.randrange(3)]
        x=[F(rng.randrange(0,16),rng.randrange(1,8)) for _ in range(n)]
        z=[F(rng.randrange(0,16),rng.randrange(1,8)) for _ in range(n)]
        ax,az=access(x,edges),access(z,edges)
        assert sum(abs(u-v) for u,v in zip(ax,az))>=sum(abs(u-v) for u,v in zip(x,z))
        assert inverse(ax,edges)==x
        assert inverse(az,edges)==z
        # Test onto positive orthant, not merely inversion on observed images.
        a=[F(rng.randrange(1,23),rng.randrange(1,7)) for _ in range(n)]
        assert access(inverse(a,edges),edges)==a
        checks+=1

# Exact sharpness with a strictly positive two-vertex instance.
e=[(0,1,F(7,3))]
x=[F(4),F(1)]
y=[F(5),F(1)]
assert sum(abs(t-s) for t,s in zip(access(x,e),access(y,e)))==sum(abs(t-s) for t,s in zip(x,y))==1

# Reciprocity matters: a one-way edge destroys uniform inverse nonexpansivity.
w=F(3); eps=F(1,10)
x=[F(5),F(1)]
y=[x[0]-w*eps,x[1]+eps]
A=lambda z:[z[0]+w*min(z),z[1]]
assert A(y)[0]==A(x)[0]
assert sum(abs(t-s) for t,s in zip(y,x))==4*eps
assert sum(abs(t-s) for t,s in zip(A(y),A(x)))==eps
# Connected stars show that no degree-free infinity-norm analogue holds.
for d in range(3,13):
    edges=[(0,j,F(1)) for j in range(1,d+1)]
    x=[F(d+3)]+[F(1)]*d
    y=[F(d+3)-F(d,2)]+[F(3,2)]*d
    ax,ay=access(x,edges),access(y,edges)
    assert ax[0]==ay[0] and all(ay[j]-ax[j]==1 for j in range(1,d+1))
    assert max(abs(u-v) for u,v in zip(x,y))==F(d,2)
    assert max(abs(u-v) for u,v in zip(ax,ay))==1
    assert sum(abs(u-v) for u,v in zip(x,y))==sum(abs(u-v) for u,v in zip(ax,ay))==d
print('PASS',checks,'exact rational graph/target tests; sharp l1, star l_inf, and directed limits')
