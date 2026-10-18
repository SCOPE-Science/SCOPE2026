"""Standalone finite checks for three-core Gaussian tensor-train variance ordering.
Only scientific definitions and reproducible arithmetic are used.
"""
from fractions import Fraction as F
import random
import numpy as np

def var(p,q,r,chi):
    return 2*(p+r)/chi + 4*p*r/(chi*chi) + (2*q/(chi*chi))*(1+(chi+1)*p)*(1+(chi+1)*r)

def check_exact():
    rng=random.Random(240731)
    N=0
    for chi in range(1,16):
        for _ in range(500):
            a,b,c=[F(rng.randint(1,200),200) for z in range(3)]
            ps=sorted((a,b,c),reverse=True)
            a,b,c=ps
            low=var(b,a,c,chi)
            mid=var(a,b,c,chi)
            high=var(a,c,b,chi)
            assert low<=mid<=high, (chi,ps,low,mid,high)
            assert high <=chi*low
            d=var(b,a,c,chi)-var(a,b,c,chi)
            assert d== F(2*(a-b)*(c-1)*(chi-1),chi*chi)
            N+=4
    return N

def simulate():
    rng=np.random.default_rng(240731)
    chi=3; d=4
    weights=[np.array([0.7,0.2,0.1,0.0]), np.array([0.25,0.25,0.25,0.25]), np.array([0.97,0.02,0.01,0.0])]
    ps=[float(sum(w*w)/(sum(w)**2)) for w in weights]
    B=140000
    reported=[]
    for ids in ((0,1,2),(1,0,2),(1,2,0)):
        scores=[]
        for base in range(0,B,2000):
            b=min(2000,B-base)
            g=rng.normal(size=(b,d,chi))
            M=rng.normal(size=(b,d,chi,chi))
            h=rng.normal(size=(b,d,chi))
            val=np.einsum('bip,bjpq,bkq->bijk',g,M,h,optimize=True)/chi
            score=np.einsum('i,j,k,bijk->b',weights[ids[0]],weights[ids[1]],weights[ids[2]],val*val,optimize=True)
            scores.append(score)
        emp=np.concatenate(scores).var()
        theo=float(var(ps[ids[0]],ps[ids[1]],ps[ids[2]],chi))
        rel=abs(emp/theo-1)
        reported.append((ids,emp,theo,rel))
        assert rel<0.08,(ids,emp,theo,rel)
    return reported

if __name__=='__main__':
    print('EXACT_CHECKS',check_exact())
    for x in simulate():print('VARIANCE',x)
    for chi in (2,3,5,12):
        for d in (8,100,10000,1000000):
            a=F(1);b=c=F(1,d)
            ratio=float(var(a,c,b,chi)/var(b,a,c,chi))
            print('AMPLIFICATION',chi,d,ratio)
