import math
import random

def normalize(v):
    n=math.sqrt(sum(x*x for x in v))
    return [x/n for x in v],n

random.seed(350076)

for _ in range(5000):
    T=random.randint(2,8)
    d=random.randint(1,7)
    G=[]
    G0=[]
    scales=[]
    for _k in range(T):
        v=[random.uniform(-4,4) for _ in range(d)]
        v0=[random.uniform(-4,4) for _ in range(d)]
        if sum(x*x for x in v)<1e-8: v[0]=1.0
        if sum(x*x for x in v0)<1e-8: v0[0]=1.0
        G.append(v); G0.append(v0)
        scales.append(10**random.uniform(-2,2))
    U=[]; norms=[]; norms0=[]
    for v,v0 in zip(G,G0):
        u,n=normalize(v); _,n0=normalize(v0)
        U.append(u); norms.append(n); norms0.append(n0)
    raw=[n/n0 for n,n0 in zip(norms,norms0)]
    sr=sum(raw)
    alpha=[x/sr for x in raw]
    C=sum(a*n for a,n in zip(alpha,norms))
    p=[a*n/C for a,n in zip(alpha,norms)]
    assert abs(sum(p)-1)<2e-12

    Gs=[[s*x for x in v] for s,v in zip(scales,G)]
    G0s=[[s*x for x in v] for s,v in zip(scales,G0)]
    Us=[]; ns=[]; n0s=[]
    for v,v0 in zip(Gs,G0s):
        u,n=normalize(v); _,n0=normalize(v0)
        Us.append(u); ns.append(n); n0s.append(n0)
    raws=[n/n0 for n,n0 in zip(ns,n0s)]
    ss=sum(raws)
    alphas=[x/ss for x in raws]
    assert max(abs(a-b) for a,b in zip(alpha,alphas))<3e-12
    assert max(abs(x-y) for u,v in zip(U,Us) for x,y in zip(u,v))<3e-12

    Cs=sum(a*n for a,n in zip(alphas,ns))
    A=sum(pi*si for pi,si in zip(p,scales))
    assert abs(Cs-A*C)<5e-11*max(1.0,Cs,A*C)
    assert min(scales)-1e-12 <= A <= max(scales)+1e-12

    sumU=[sum(U[k][j] for k in range(T)) for j in range(d)]
    base=[C*x for x in sumU]
    scaled=[Cs*x for x in sumU]
    assert max(abs(x-A*y) for x,y in zip(scaled,base))<5e-11*max(1.0,max(map(abs,scaled),default=0))

# Task-specific first-order gradients inherit their own scale.
for _ in range(2000):
    s1=10**random.uniform(-2,2)
    s2=10**random.uniform(-2,2)
    h1=random.uniform(0.1,5.0)
    h2=random.uniform(0.1,5.0)
    r1=random.uniform(0.1,5.0)
    r2=random.uniform(0.1,5.0)
    assert abs((s1*h1)/(s2*h2) - (s1/s2)*(h1/h2))<1e-12*max(1.0,(s1*h1)/(s2*h2))
    assert abs((s1*r1)/(s2*r2) - (s1/s2)*(r1/r2))<1e-12*max(1.0,(s1*r1)/(s2*r2))

# Common scaling is exactly removed by reciprocal learning rates in all source channels.
for _ in range(2000):
    s=10**random.uniform(-3,3)
    eta=10**random.uniform(-4,-1)
    er=10**random.uniform(-5,-2)
    gb=random.uniform(-10,10)
    gh=random.uniform(-10,10)
    gr=random.uniform(-10,10)
    assert abs((eta/s)*(s*gb)-eta*gb)<1e-12*max(1.0,abs(eta*gb))
    assert abs((eta/s)*(s*gh)-eta*gh)<1e-12*max(1.0,abs(eta*gh))
    assert abs((er/s)*(s*gr)-er*gr)<1e-12*max(1.0,abs(er*gr))

# Unequal nonzero head scales cannot share one exact common learning-rate compensation.
for _ in range(1000):
    s1=10**random.uniform(-2,2)
    s2=s1*10**random.uniform(0.2,1.5)
    assert abs(1/s1-1/s2)>1e-12

print("verification passed")
