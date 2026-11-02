#!/usr/bin/env python3
"""Deterministic checks for the entropy-optimal thermodynamic triangle."""
import math
import random


def optimum(beta, weights):
    b1,b2,b3=beta
    assert abs(b1+b2+b3)<1e-9*max(1.,abs(b1),abs(b2),abs(b3))
    r=(-b1,b3,0.)
    def grad(c):
        out=0.
        for ri,w in zip(r,weights):
            j=ri+c
            out+=math.asinh(j/(2*w))+j/math.hypot(j,2*w)
        return out
    bound=4.*(max(map(abs,r))+sum(weights)+1.)
    lo,hi=-bound,bound
    assert grad(lo)<0<grad(hi)
    for _ in range(110):
        m=(lo+hi)/2
        if grad(m)>0:hi=m
        else:lo=m
    c=(lo+hi)/2
    j=tuple(ri+c for ri in r)
    aff=sum(2*math.asinh(ji/(2*w)) for ji,w in zip(j,weights))
    return c,j,aff


def linear(beta,weights):
    r=(-beta[0],beta[2],0.)
    c=-sum(ri/w for ri,w in zip(r,weights))/sum(1./w for w in weights)
    return tuple(ri+c for ri in r)


def strong_limit(beta,weights):
    r=(-beta[0],beta[2],0.)
    k=sorted(range(3),key=lambda i:r[i]); lo,mid,hi=k
    assert r[lo]<r[mid]<r[hi]
    R=((r[hi]-r[mid])/weights[hi])/((r[mid]-r[lo])/weights[lo])
    target=-math.log(R)
    left,right=-1-abs(target),1+abs(target)
    for _ in range(100):
        u=(left+right)/2
        if u+math.tanh(u)>target:right=u
        else:left=u
    u=(left+right)/2
    return -2*math.tanh(u)


def main():
    count=0
    rng=random.Random(72551640)
    for _ in range(700):
        w=tuple(math.exp(rng.uniform(-1.6,1.6)) for _ in range(3))
        b1,b2=(rng.uniform(-2,2),rng.uniform(-2,2))
        beta=(b1,b2,-b1-b2)
        c,j,aff=optimum(beta,w)
        L=linear(beta,w)
        assert abs(sum(li/wi for li,wi in zip(L,w)))<1e-12
        count+=1
        assert abs((j[2]-j[0])-beta[0])<1e-11 and abs((j[0]-j[1])-beta[1])<1e-11
        count+=1
        prod=L[0]*L[1]*L[2]
        if abs(prod)>1e-7:
            assert aff*prod>0, (beta,w,aff,prod)
            count+=1
        epsilon=0.002
        _,_,small=optimum(tuple(epsilon*x for x in beta),w)
        theory=(epsilon**3/8)*math.prod(Li/wi for Li,wi in zip(L,w))
        if abs(theory)>1e-14:
            assert abs(small/theory-1)<0.004,(small,theory,beta,w)
            count+=1
        # Conservative families: choose linear zero-current fluxes via L=(0,t,-t*w2/w3)
        # Flux divergence follows the chosen triple, so its linear projection is identical.
        for zero in range(3):
            z=[0.,0.,0.]
            ids=[i for i in range(3) if i!=zero]
            z[ids[0]]=1.3
            z[ids[1]]=-z[ids[0]]*w[ids[1]]/w[ids[0]]
            beta_z=(z[2]-z[0],z[0]-z[1],z[1]-z[2])
            _,jj,aa=optimum(beta_z,w)
            assert abs(aa)<3e-12 and abs(jj[zero])<3e-12
            count+=1
    for _ in range(130):
        w=tuple(math.exp(rng.uniform(-.7,.7)) for _ in range(3))
        b1,b2=rng.uniform(-2,2),rng.uniform(-2,2)
        beta=(b1,b2,-b1-b2)
        if min(abs(x) for x in beta)<.12:continue
        lim=strong_limit(beta,w)
        _,_,a=optimum(tuple(x*3.e5 for x in beta),w)
        assert abs(a-lim)<0.00012,(a,lim,w,beta)
        count+=1
    b=(-3.,1.,2.);w=(1.,1.,1.)
    lin=linear(b,w)
    assert all(abs(x-y)<1e-12 for x,y in zip(lin,(4/3,1/3,-5/3)))
    count+=1
    assert abs(strong_limit(b,w)+0.6791125644)<3e-7
    count+=1
    print(f'PASS: {count} deterministic numerical assertions')

if __name__=='__main__':main()
