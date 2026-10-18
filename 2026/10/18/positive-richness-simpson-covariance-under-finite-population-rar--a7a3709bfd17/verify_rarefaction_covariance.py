"""Exact checks for a covariance bound under uniform finite-population rarefaction.

Requires Python 3.10+ standard library. All operations use integers or Fraction.
"""
from fractions import Fraction
from itertools import combinations
from functools import lru_cache
from math import comb, factorial
import json

@lru_cache(None)
def integer_partitions(n, maximum=None):
    if maximum is None:
        maximum=n
    if n==0:
        return ((),)
    return tuple((a,)+tail for a in range(min(maximum,n),0,-1)
                 for tail in integer_partitions(n-a,a))

def fall(n,k):
    if k<0 or n<k:
        return 0
    ans=1
    for i in range(k):ans*=n-i
    return ans

def closed_form(a,m):
    N=sum(a)
    assert 2<=m<=N and all(v>0 for v in a)
    Q=sum(v*v for v in a)
    S=Q-N
    ww=[fall(N-v-2,m-2) if N-v>=m else 0 for v in a]
    theta=[S*(2*N-v-1)-N*(N-1)*(v-1) for v in a]
    value=Fraction(sum(v*w*T for v,w,T in zip(a,ww,theta)),fall(N,m)*N*(N-1))
    t=Fraction(Q,N)
    bound=Fraction(1,1)*(t-1)*(N-t)*sum(v*w for v,w in zip(a,ww))/(fall(N,m)*(N-1))
    pair=Fraction(0,1)
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            pair+=a[i]*a[j]*(a[i]-a[j])*(ww[j]-ww[i])
    correction=Fraction(S+N*(N-1),N*fall(N,m)*N*(N-1))*pair
    assert value==bound+correction
    return value,bound

def labelled_enumeration(a,m):
    labels=[i for i,v in enumerate(a) for _ in range(v)]
    N=len(labels); T=comb(N,m)
    ksum=gsum=kgsum=0
    for indices in combinations(range(N),m):
        c=[0]*len(a)
        for idx in indices:c[labels[idx]]+=1
        k=sum(x>0 for x in c)
        g=m*(m-1)-sum(x*(x-1) for x in c)
        ksum+=k; gsum+=g; kgsum+=k*g
    return Fraction(kgsum*T-ksum*gsum,T*T*m*(m-1))

def composition_enumeration(a,m):
    N=sum(a);T=comb(N,m);k_sum=g_sum=kg_sum=weight_sum=0
    def visit(i,left,k,squares,w):
        nonlocal k_sum,g_sum,kg_sum,weight_sum
        if i==len(a):
            if left:return
            g=m*(m-1)-squares
            k_sum+=w*k;g_sum+=w*g;kg_sum+=w*k*g;weight_sum+=w
            return
        for c in range(min(a[i],left)+1):
            visit(i+1,left-c,k+(c>0),squares+c*(c-1),w*comb(a[i],c))
    visit(0,m,0,0,1)
    assert weight_sum==T,(a,m,weight_sum,T)
    return Fraction(kg_sum*T-k_sum*g_sum,T*T*m*(m-1))

def run():
    profiles=triples=positive=zero=0
    for N in range(2,13):
        for a in integer_partitions(N):
            profiles+=1
            for m in range(2,N+1):
                triples+=1
                x,b=closed_form(a,m)
                y=labelled_enumeration(a,m)
                z=composition_enumeration(a,m)
                assert x==y==z,(a,m,x,y,z)
                assert x>=b>=0,(a,m,x,b)
                if 1<len(a)<N and m<=N-min(a):
                    assert x>0,(a,m,x)
                else:
                    assert x==0,(a,m,x)
                if x>0:positive+=1
                else:zero+=1
    certificate={'schema_version':1,
        'description':'Exact verification of covariance identity and positive lower bound under finite-population rarefaction',
        'maximum_population_N':12,'positive_integer_abundance_profiles':profiles,
        'profile_sample_size_pairs_checked':triples,'strict_positive_covariance_cases':positive,
        'zero_covariance_cases':zero,
        'independent_methods':['labelled subset enumeration','multivariate-hypergeometric composition enumeration','closed rational formula'],
        'status':'all exact checks passed'}
    print(json.dumps(certificate,sort_keys=True,indent=2))
    return certificate
if __name__=='__main__':run()
