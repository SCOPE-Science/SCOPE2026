#!/usr/bin/env python3
import itertools, math
import numpy as np
from scipy.optimize import linprog


def words(d,n):
    return list(itertools.product(range(d), repeat=n))


def counts(w,d):
    return np.array([w.count(i) for i in range(d)], dtype=int)


def type_words(target):
    d=len(target); n=sum(target)
    return [w for w in words(d,n) if np.array_equal(counts(w,d), np.array(target))]


def formula(target):
    target=np.array(target,dtype=int); n=int(target.sum()); d=len(target)
    p=target/n
    ans=0.0
    for y in words(d,n):
        prob=1.0
        for a in y: prob*=p[a]
        ans += prob*0.5*np.abs(counts(y,d)-target).sum()
    return ans


def transport_lp(target):
    target=np.array(target,dtype=int); n=int(target.sum()); d=len(target)
    X=type_words(target.tolist()); Y=words(d,n); p=target/n
    mu=np.full(len(X),1.0/len(X))
    nu=np.array([math.prod(p[a] for a in y) for y in Y])
    cost=np.array([[sum(a!=b for a,b in zip(x,y)) for y in Y] for x in X],dtype=float)
    m=len(X)*len(Y); A=[]; b=[]
    for i in range(len(X)):
        row=np.zeros(m); row[i*len(Y):(i+1)*len(Y)]=1; A.append(row); b.append(mu[i])
    for j in range(len(Y)):
        row=np.zeros(m); row[j::len(Y)]=1; A.append(row); b.append(nu[j])
    res=linprog(cost.ravel(), A_eq=np.array(A), b_eq=np.array(b), bounds=(0,None), method='highs')
    if not res.success: raise RuntimeError(res.message)
    return float(res.fun)


def check(target):
    f=formula(target); lp=transport_lp(target)
    assert abs(f-lp)<1e-10, (target,f,lp)
    n=sum(target); p=np.array(target)/n
    b1=0.5*math.sqrt(n)*sum(math.sqrt(float(q*(1-q))) for q in p)
    b2=0.5*math.sqrt(n*(len(target)-1))
    assert f <= b1+1e-12
    assert b1 <= b2+1e-12

for target in ([2,2],[2,1],[1,1,1],[2,1,1]):
    check(target)

for n in (2,4,6,8,10):
    target=[n//2,n//2]
    f=formula(target)
    closed=n*math.comb(n,n//2)/(2**(n+1))
    assert abs(f-closed)<1e-12, (n,f,closed)

print('VERIFY_OK')
