#!/usr/bin/env python3
"""Exact finite-size verification of crossing-cut profile covariance."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import factorial

def matchings(vertices):
    if not vertices:
        yield ()
    else:
        first = vertices[0]
        for i in range(1,len(vertices)):
            other=vertices[i]
            rem=vertices[1:i]+vertices[i+1:]
            for rest in matchings(rem):
                yield ((first,other),)+rest

def obs(pairing,m):
    return tuple(sum((a<k<=b) for a,b in pairing) for k in range(m+1))

def mean(m,k):
    return F(k*(m-k),m-1)

def kernel(m,k,l):
    s,t=min(k,l),max(k,l)
    return F(2*s*(s-1)*(m-t)*(m-t-1),(m-3)*(m-1)**2)

def mat_inv(a):
    n=len(a); z=[[F(v) for v in row]+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for i in range(n):
        assert z[i][i]!=0
        v=z[i][i]; z[i]=[u/v for u in z[i]]
        for j in range(n):
            if i!=j:
                w=z[j][i]
                if w: z[j]=[u-w*v for u,v in zip(z[j],z[i])]
    return [row[n:] for row in z]

def det(m):
    return F(2*4**(m-3)*factorial(m-3)*factorial(m-4),(m-3)**(m-4)*(m-1)**(m-2))

def var_init(m):
    return F(4*(m-2),(m-1)**2)

def ar(m,k):
    return F(m-k-2,m-k)

def innovation(m,k):
    return F(4*k*(m-k-1)*(m-k-2),(m-k)*(m-3)*(m-1))

def precision(m):
    inds=range(2,m-1)
    n=m-3
    Q=[[F(0) for _ in inds] for _ in inds]
    Q[0][0]+=1/var_init(m)
    for k in range(2,m-2):
        a=ar(m,k); iq=1/innovation(m,k)
        i=k-2
        Q[i][i]+=a*a*iq
        Q[i][i+1]-=a*iq
        Q[i+1][i]-=a*iq
        Q[i+1][i+1]+=iq
    return Q

def main():
    assertions=0
    for m in (4,6,8,10,12):
        allh=[obs(p,m) for p in matchings(list(range(m)))]
        N=len(allh)
        assert N==factorial(m)//(2**(m//2)*factorial(m//2))
        means=[F(sum(h[k] for h in allh),N) for k in range(m+1)]
        for k in range(m+1):
            assert means[k]==mean(m,k), (m,k,means[k],mean(m,k))
            assertions+=1
        Ks=[]
        for k in range(2,m-1):
            row=[]
            for l in range(2,m-1):
                exp2=F(sum(h[k]*h[l] for h in allh),N)
                cov=exp2-means[k]*means[l]
                assert cov==kernel(m,k,l),(m,k,l,cov,kernel(m,k,l))
                row.append(cov)
                assertions+=1
            Ks.append(row)
        P=precision(m)
        actual=mat_inv(Ks)
        assert P==actual,(m,P,actual)
        assertions+= (m-3)**2
        from functools import reduce
        v=var_init(m)
        for k in range(2,m-2):
            v*=innovation(m,k)
        assert v==det(m)
        assertions+=1
        # Check actual conditional Markov down probabilities, plus mean-zero innovation variance.
        for k in range(1,m):
            freq=Counter(h[k] for h in allh)
            down=Counter(h[k] for h in allh if h[k+1]==h[k]-1)
            for level,times in freq.items():
                assert F(down[level],times)==F(level,m-k),(m,k,level)
                assertions+=1
        print(f'M={m}, perfect_matchings={N}, interior={m-3}, covariance/precision/transition verified')
    print('PASS',assertions,'exact checks')

if __name__=='__main__':main()
