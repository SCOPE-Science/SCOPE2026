"""Independent finite checks for weighted cross-polytope projection formulas.
Run with Python 3.10+; no external packages required.
These tests are finite corroboration, not a proof of global identities.
"""
import itertools
import math
import random


def norm_p(v, p):
    return sum(abs(x)**p for x in v)**(1.0/p)


def project(x, w, p, radius=1.0):
    q=p/(p-1.0)
    if sum(wi*abs(xi) for xi,wi in zip(x,w)) <= radius:
        return list(x), 0.0
    powers=[wi**(q-1.0) for wi in w]
    hi=max(abs(xi)/ai for xi,ai in zip(x,powers))
    lo=0.0
    for _ in range(95):
        mid=(lo+hi)/2.0
        mass=sum(wi*max(abs(xi)-mid*ai,0.0) for xi,wi,ai in zip(x,w,powers))
        if mass>radius:lo=mid
        else:hi=mid
    tau=(lo+hi)/2.0
    return [math.copysign(max(abs(xi)-tau*ai,0.0),xi) for xi,ai in zip(x,powers)],tau


def J(u,w,p):
    q=p/(p-1.0)
    a=[wi**(q-1.0) for wi in w]
    t=sum(wi*ui for wi,ui in zip(w,u))/sum(wi**q for wi in w)
    return [ui-t*ai for ui,ai in zip(u,a)]


def planar_formula(w,p):
    q=p/(p-1.0)
    return (sum(wi**p for wi in w)**(1.0/p)*sum(wi**(q*(q-1.0)) for wi in w)**(1.0/q)/sum(wi**q for wi in w))


def main():
    rng=random.Random(240441)
    checks=0
    for n in (1,2,3,4,5):
        for p in (1.3,1.5,2.0,3.0,4.0,7.0):
            w=[rng.uniform(0.5,3.0) for _ in range(n)]
            for _ in range(40):
                x=[rng.uniform(-3,3) for _ in range(n)]
                z,t=project(x,w,p)
                assert sum(wi*abs(zi) for wi,zi in zip(w,z))<=1.0+1.0e-11
                for xi,zi,wi in zip(x,z,w):
                    gap=abs(xi)-abs(zi)
                    if abs(zi)>1.0e-8:
                        assert xi*zi>0.0
                        assert abs(gap-t*wi**(1.0/(p-1.0)))<1.0e-8
                    else:
                        assert abs(xi)<=t*wi**(1.0/(p-1.0))+1.0e-8
                checks+=1
    for p in (1.3,1.5,2.0,3.0,4.0,7.0):
        for w in ((1.0,1.0),(1.0,2.0),(0.5,3.0)):
            q=p/(p-1.0)
            c=(w[1]**(q-1.0),-w[0]**(q-1.0))
            test=[math.copysign(abs(ci)**(q-1.0),ci) for ci in c]
            predicted=planar_formula(w,p)
            observed=norm_p(J(test,w,p),p)/norm_p(test,p)
            assert abs(observed-predicted)<1.0e-11,(p,w,observed,predicted)
            assert predicted>=1.0-1.0e-12
            if p==2.0 or w[0]==w[1]: assert abs(predicted-1.0)<1.0e-11
            else: assert predicted>1.0+1.0e-4
            # Realize the local derivative as a finite difference of the actual map.
            a=[wi**(q-1.0) for wi in w]
            x=[0.5/wi+0.75*ai for wi,ai in zip(w,a)]
            epsilon=1.0e-6
            y=[xi+epsilon*ui for xi,ui in zip(x,test)]
            px,_=project(x,w,p)
            py,_=project(y,w,p)
            ratio=norm_p([ui-vi for ui,vi in zip(px,py)],p)/(epsilon*norm_p(test,p))
            assert abs(ratio-predicted)<2.0e-7,(p,w,ratio,predicted)
            checks+=2
    for p in (1.5,3.0,4.0,7.0):
        w=[1.0,1.0,1.0]
        v=[1.0,1.0,-2.0]
        q=p/(p-1.0)
        a=[wi**(q-1.0) for wi in w]
        ratios=[]
        for t in (-0.2,-0.1,0.1,0.2):
            u=[vi+t*ai for vi,ai in zip(v,a)]
            ratios.append(norm_p(J(u,w,p),p)/norm_p(u,p))
        assert max(ratios)>1.0+1.0e-6,(p,ratios)
        checks+=1
    print('VERIFY_OK checks=%d random_seeds=240441 all_scenarios_passed' % checks)

if __name__=='__main__': main()
