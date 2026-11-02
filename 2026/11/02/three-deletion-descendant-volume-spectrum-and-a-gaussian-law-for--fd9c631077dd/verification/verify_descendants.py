#!/usr/bin/env python3
"""Independent exact checks for multiset three-deletion descendant volume."""
from math import comb
from collections import Counter

def comp(n,q):
    if q==1:
        yield (n,)
    else:
        for v in range(n+1):
            for tail in comp(n-v,q-1):
                yield (v,)+tail

def descendants3(x):
    return {tuple(x[i]-d[i] for i in range(len(x))) for d in comp(3,len(x)) if all(d[i]<=x[i] for i in range(len(x)))}

def volume3(x):
    k=sum(a>=1 for a in x); h=sum(a>=2 for a in x); j=sum(a>=3 for a in x)
    return (comb(k,3) if k>=3 else 0)+(k-1)*h+j

def hist_formula(n,q):
    z=Counter()
    for k in range(1,min(q,n)+1):
        for h in range(k+1):
            for j in range(h+1):
                baseline=k+h+j
                if j==0:
                    c=int(n==baseline)
                else:
                    c=comb(n-baseline+j-1,j-1) if n>=baseline else 0
                if c:
                    v=(comb(k,3) if k>=3 else 0)+(k-1)*h+j
                    z[v]+=comb(q,k)*comb(k,h)*comb(h,j)*c
    return z

def ck(n,r):
    return comb(n,r) if n>=r>=0 else 0

count=0
for q in range(2,7):
    for n in range(3,14):
        h=Counter()
        for x in comp(n,q):
            v=len(descendants3(x))
            assert v==volume3(x),(q,n,x,v,volume3(x))
            h[v]+=1
            count+=1
        assert h==hist_formula(n,q),(q,n,h,hist_formula(n,q))
        assert sum(h.values())==comb(n+q-1,q-1)
print('Exact distribution, direct three-deletion descendant enumeration:',count,'centers checked')
for q,n in [(4,10),(6,12),(8,16),(12,24),(20,40),(30,60),(50,100)]:
    H=hist_formula(n,q)
    S=sum(H.values())
    mu=sum(k*v for k,v in H.items())/S
    var=sum((k-mu)**2*v for k,v in H.items())/S
    p=n/(n+q-1)
    predict=p**6*(1-p)/4
    print('q,n',q,n,'min,max volumes',min(H),max(H),'mean',round(mu,4), 'var/q^5',round(var/q**5,9),'limit coefficient',round(predict,9))
