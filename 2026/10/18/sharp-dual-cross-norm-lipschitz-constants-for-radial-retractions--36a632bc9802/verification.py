"""Deterministic computational corroboration of sharp cross-norm radial retraction laws.

This finite program tests exact algebraic norm formulas and derivative witnesses.
It does not replace the analytic proof for all parameters.
"""
import math
import random


def scalar_max(q, k):
    assert q > 1 and k > 0
    lo, hi = 0.0, 1.0
    def eq(t):
        return q * t ** (q-1) + (q-1) * k * t ** q
    while eq(hi) < k:
        hi *= 2.0
    for _ in range(100):
        mid = (lo+hi)/2
        if eq(mid)<k:
            lo=mid
        else:
            hi=mid
    t=(lo+hi)/2
    return (1+k*t)/(1+t**q),t


def predictions(p, w):
    i = min(range(len(w)), key=w.__getitem__)
    m=w[i]
    q=p/(p-1)
    kp=(sum((v/m)**p for j,v in enumerate(w) if j!=i))**(1/p)
    kq=(sum((v/m)**q for j,v in enumerate(w) if j!=i))**(1/q)
    sup, ts=scalar_max(p,kp)
    one, tv=scalar_max(q,kq)
    return i,(sup, ts),(one,tv)


def witnesses(p,w):
    i,(sup,ts),(one,tv)=predictions(p,w)
    n=len(w)
    q=p/(p-1)
    B=(sum(w[j]**p for j in range(n) if j!=i))**(1/p)
    a=(1+ts**p)**(-1/p)
    u=[a*w[j]/B if j!=i else a*ts for j in range(n)]
    Bq=(sum(w[j]**q for j in range(n) if j!=i))**(1/q)
    t=tv**(1/(p-1))
    a=(1+t**p)**(-1/p)
    v=[a*(w[j]/Bq)**(1/(p-1)) if j!=i else a*t for j in range(n)]
    return i,(sup,u),(one,v)


def derivative(p, u):
    phi=[math.copysign(abs(a)**(p-1),a) for a in u]
    return [[(1.0 if j==i else 0)-u[i]*phi[j] for j in range(len(u))] for i in range(len(u))]


def induced_norms(A,w):
    ns=len(w)
    return (max(sum(abs(A[i][j])*w[j]/w[i] for j in range(ns)) for i in range(ns)),
            max(sum(abs(A[i][j])*w[i]/w[j] for i in range(ns)) for j in range(ns)))


def radial(p,x):
    r=sum(abs(a)**p for a in x)**(1/p)
    return [a/max(1.,r) for a in x]


def close(a,b,tol=3e-10):
    assert abs(a-b)<=tol*max(1,abs(a),abs(b)), (a,b)


rnd=random.Random(1729)
checks=0
for p in [1.12,1.3,1.5,1.8,2.,2.4,3.5,5.,11.]:
    for n in [2,3,5,8]:
        for trial in range(20):
            w=[rnd.uniform(.2,3.) for _ in range(n)]
            i,(M,u),(N,v)=witnesses(p,w)
            close(sum(a**p for a in u),1.)
            close(sum(a**p for a in v),1.)
            supi, sumi=induced_norms(derivative(p,u),w)
            supj, sumj=induced_norms(derivative(p,v),w)
            close(supi,M)
            close(sumj,N)
            assert sumi <= N+3e-10 and supj <= M+3e-10
            w2=[rnd.uniform(.15,2.5) for _ in range(n)]
            z=[rnd.uniform(-1,1) for _ in range(n)]
            z=[a/(sum(abs(b)**p for b in z)**(1/p)) for a in z]
            sr,cr=induced_norms(derivative(p,z),w)
            pred_sup,pred_one=predictions(p,w)[1][0],predictions(p,w)[2][0]
            assert sr<=pred_sup+3e-10 and cr<=pred_one+3e-10
            checks+=6

for p in [1.25,1.75,2.,2.5,4.]:
    for n in [2,3,6]:
        w=[rnd.uniform(.2,2.5) for _ in range(n)]
        i,(M,u),(N,v)=witnesses(p,w)
        eps=1e-6; radius=1+3e-4
        x=[radius*a for a in u]
        A=derivative(p,u)
        h=[w[j]*(1 if j==i else -1) for j in range(n)]
        y=[x[j]+eps*h[j] for j in range(n)]
        Ru,Ry=radial(p,x),radial(p,y)
        ratio=max(abs(Ry[j]-Ru[j])/w[j] for j in range(n))/eps
        assert abs(ratio-M/radius)<2e-4,(p,n,ratio,M/radius)
        checks+=1

for n in [2,4,17]:
    for w in [[1.0]*n,[1.0]+[3.0]*(n-1)]:
        M=predictions(2,w)[1][0]
        old=(1+math.sqrt(sum(a*a for a in w))/min(w))/2
        close(M,old)
        checks+=1

for p in [1.2,1.6,2,3.,5.]:
    for n in [100,1000,10000]:
        q=p/(p-1)
        s=predictions(p,[1.]*n)[1][0]
        o=predictions(p,[1.]*n)[2][0]
        cs=(p-1)**((p-1)/p)/p
        co=(q-1)**((q-1)/q)/q
        assert cs*(n-1)**(1/p)<=s<=cs*(n-1)**(1/p)+1+1e-8
        assert co*(n-1)**(1/q)<=o<=co*(n-1)**(1/q)+1+1e-8
        checks+=2

print('VERIFY_OK',checks,'assertion groups, multiple assertions per group')
