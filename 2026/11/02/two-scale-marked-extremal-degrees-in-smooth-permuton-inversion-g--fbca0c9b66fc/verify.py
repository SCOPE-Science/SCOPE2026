"""Self-contained finite checks for the two-scale extremal-degree theorem.
Use Python 3.10+; no external packages. Checks are not an infinite-proof certificate.
"""
from __future__ import annotations
import itertools, math, random
from fractions import Fraction as Q

checks = 0

def eq(a,b):
    global checks
    assert a==b, (a,b)
    checks += 1

# Graph inversion-degree identity, exhaustively for every permutation of n<=8.
for n in range(2,9):
    for p in itertools.permutations(range(n)):
        for i in range(n):
            d = sum((i-j)*(p[i]-p[j]) < 0 for j in range(n))
            m = sum(j<i and p[j]<p[i] for j in range(n))
            eq(d, i+p[i]-2*m)

# f(x,y)=1+(3/5)(2x-1)(6y(1-y)-1) has uniform marginals.
# Integral of 2x-1 on [0,1], and integral of 6y-6y^2-1 are exactly zero.
eq(Q(1)-Q(1),Q(0))
eq(Q(3)-Q(2)-Q(1),Q(0))
# Since |2x-1|<=1 and |6y(1-y)-1|<=1, f>=2/5 and f<=8/5.
eq(Q(1)+Q(3,5),Q(8,5))
eq(Q(1)-Q(3,5),Q(2,5))
A=lambda z:z*z-z
B=lambda z:3*z*z-2*z*z*z-z
# Exact covariance: Cov(N_{X<=a/sqrt(n)},N_{Y<=b/sqrt(n)})
# = n*(3/5)*A(a/sqrt(n))*B(b/sqrt(n)).
for m in (100,200,400,800):
    n=m*m; a=2; b=3
    cov=n*Q(3,5)*A(Q(a,m))*B(Q(b,m))
    eq(n*(Q(a,m)-Q(a*a,n)),a*m-a*a)
    assert abs(float(cov/m))<0.06
    checks+=1

# Reproducible optional finite-sample diagnostics at a non-symmetric density.
def sample(rng,n):
    xx=[];yy=[]
    while len(xx)<n:
        x=rng.random();y=rng.random()
        f=1+0.6*(2*x-1)*(6*y*(1-y)-1)
        if 1.6*rng.random()<f:
            xx.append(x);yy.append(y)
    return xx,yy

def degrees(xx,yy):
    n=len(xx)
    ox=sorted(range(n),key=xx.__getitem__)
    oy=sorted(range(n),key=yy.__getitem__)
    rank=[0]*n
    for j,i in enumerate(oy,1):rank[i]=j
    bit=[0]*(n+1);d=[0]*n
    for pos,i in enumerate(ox):
        r=rank[i];s=0;k=r-1
        while k:
            s+=bit[k];k-=k&-k
        d[i]=pos+r-1-2*s
        while r<=n:
            bit[r]+=1;r+=r&-r
    return d

rng=random.Random(261031)
N=1800;reps=350
BL=[];V=[];R=[];H=[];V2=[]
for _ in range(reps):
    xx,yy=sample(rng,N)
    ds=degrees(xx,yy)
    order=sorted(range(N),key=lambda i:(ds[i],i))
    i=order[0];j=order[1]
    bl=xx[i]+yy[i]<=1
    u=math.sqrt(N)*(xx[i] if bl else 1-xx[i])
    v=math.sqrt(N)*(yy[i] if bl else 1-yy[i])
    s=u+v
    BL.append(int(bl));V.append(ds[i]/math.sqrt(N))
    V2.append(ds[j]/math.sqrt(N));R.append(u/s)
    H.append((ds[i]-math.sqrt(N)*s)/(N**.25*math.sqrt(s)))
mean=lambda a:sum(a)/len(a)
blhat=mean(BL);angle=mean(R);first=mean(V);second=mean(V2)
mark_mean=mean(H);mark_var=mean([(h-mark_mean)**2 for h in H])
# Tolerances only screen catastrophic normalization errors, not validate convergence.
for a,b,tol in [(blhat,.8,.14),(angle,.5,.10),
                (first,math.sqrt(math.pi)/2,.20),
                (second,3*math.sqrt(math.pi)/4,.25)]:
    assert abs(a-b)<tol,(a,b)
    checks+=1
print(f'PASS: {checks} exact-identity, rational and diagnostic assertions')
print(f'n={N}; repetitions={reps}; first-rank BL frequency={blhat:.6f}; angle mean={angle:.6f}')
print(f'first scaled degree mean={first:.6f}; predicted={math.sqrt(math.pi)/2:.6f}')
print(f'second scaled degree mean={second:.6f}; predicted={3*math.sqrt(math.pi)/4:.6f}')
print(f'first Gaussian mark standardized mean={mark_mean:.6f}; variance={mark_var:.6f}')
