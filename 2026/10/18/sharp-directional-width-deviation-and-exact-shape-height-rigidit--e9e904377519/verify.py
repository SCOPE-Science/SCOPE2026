#!/usr/bin/env python3
"""Numerical regression for sharp right-prism directional-width deviation.

Only standard-library dependencies. Symbolic proof is in RESULT.md.
"""
import math
import random

P = math.pi

def opt_lambda(q):
    return (4*q-P)/(P-2)

def ratio(q, lam):
    return (16/3)*(lam*lam+2*lam+2*q)/(P+2*lam)**2

def ratio_best(q):
    return 16*(2*q-1)/(3*(P*P-4*P+8*q))

def identity(q, lam):
    lhs=ratio(q,lam)-ratio_best(1)
    height=16*((P-2)*lam+P-4*q)**2/(3*(P+2*lam)**2*(P*P-4*P+8*q))
    shape=32*(P-2)**2*(q-1)/(3*(P*P-4*P+8)*(P*P-4*P+8*q))
    return lhs, height+shape

def polygon(n, r=1.0):
    return [(r*math.cos(2*P*j/n),r*math.sin(2*P*j/n)) for j in range(n)]

def planar_width(vertices, theta):
    c,s=math.cos(theta),math.sin(theta)
    p=[x*c+y*s for x,y in vertices]
    return max(p)-min(p)

def tests():
    random.seed(3907)
    checks=0
    for i in range(4000):
        q=1+2*random.random()
        lam=0.00001+5*random.random()
        left,right=identity(q,lam)
        assert abs(left-right)<1e-12, (i,left,right)
        assert ratio(q,lam)>=ratio_best(1)-1e-12
        lo=opt_lambda(q)
        assert ratio(q,lo)<=ratio(q,max(0.00001,lo-0.2))+1e-11
        assert ratio(q,lo)<=ratio(q,lo+0.2)+1e-11
        checks+=4
    assert abs(math.sqrt(ratio_best(1)-1)-0.0753372200107352)<1e-13
    assert abs(opt_lambda(1)-0.7519383938841087)<1e-13
    checks+=2
    # Independent integration over actual planar support widths and spherical directions,
    # not evaluation of the closed second-moment formula used above.
    n_theta=720; n_t=500
    for n in (3,4,5,7):
        verts=polygon(n)
        ws=[planar_width(verts,2*P*(j+0.5)/n_theta) for j in range(n_theta)]
        mu=sum(ws)/n_theta
        q=sum(x*x for x in ws)/n_theta/mu**2
        if n!=4:
            q_reinhardt=P/(4*n*math.tan(P/(2*n))) + P*P/(8*n*n*math.sin(P/(2*n))**2)
            if n%2==1: # regular odd-gons are Reinhardt minimizers
                assert abs(q-q_reinhardt)<2e-5, (n,q,q_reinhardt)
                checks+=1
        for lam in (0.2,opt_lambda(q),1.6):
            height=mu*lam
            moment1=moment2=0.0
            for wi in ws:
                for k in range(n_t):
                    alpha=(k+0.5)*P/(2*n_t)
                    t=math.sin(alpha)
                    weight=math.cos(alpha)*P/2
                    val=math.cos(alpha)*wi+height*t
                    moment1+=val*weight
                    moment2+=val*val*weight
            moment1/=n_theta*n_t; moment2/=n_theta*n_t
            observed=moment2/moment1**2
            expected=ratio(q,lam)
            assert abs(observed-expected)<4e-6, (n,lam,observed,expected)
            checks+=1
    # A genuinely constant-width planar body has planar q=1; simulate
    # directly using constant planar widths and spherical polar samples.
    for height in (0.35,opt_lambda(1),1.25):
        m1=m2=0
        for k in range(500000):
            t=(k+0.5)/500000
            w=math.sqrt(1-t*t)+height*t
            m1+=w
            m2+=w*w
        observed=(m2/500000)/(m1/500000)**2
        assert abs(observed-ratio(1,height))<2e-6
        checks+=1
    print('VERIFY_OK',checks,'optimal_const_width_cv',math.sqrt(ratio_best(1)-1), 'opt_height_by_width',opt_lambda(1))

if __name__=='__main__':
    tests()
