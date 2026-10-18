#!/usr/bin/env python3
"""Standalone finite-grid stress tests of the stated torus rotation optimization.
The rigorous proof is analytic; grids do not certify universal inequalities.
"""
import math
import cmath
import itertools
import random



def character_profile(beta, lam, budget):
    d=len(beta)
    radius=math.floor(budget)
    candidates=[]
    for k in itertools.product(range(-radius,radius+1),repeat=d):
        if sum(t*t for t in k)<=budget*budget+1e-10:
            val=abs(cmath.exp(1j*sum(t*x for t,x in zip(k,beta)))-lam)
            candidates.append((val,k))
    return min(candidates)


def sampled_defect(u,beta):
    return max(abs(u(x+beta)-u(x)) for x in (2*math.pi*j/16384 for j in range(16384)))


def one_dim_tests():
    beta=2*math.pi*(math.sqrt(2)-1)
    for L in [0,1,2,3,5,8,13]:
        profile,k=character_profile((beta,),-1,L)
        assert abs(profile-abs(cmath.exp(1j*k[0]*beta)+1))<1e-12
        print('dimension=1', 'L=',L,'argmin_k=',k[0],'defect=',round(profile,12))
    # Perturb Fourier characters within their homotopy class; inequality should survive.
    for k in range(-4,5):
        ch=abs(cmath.exp(1j*k*beta)+1)
        for a,b in [(0.1,0.2),(-0.6,0.3),(0.43,-0.8)]:
            grid=(2*math.pi*j/16384 for j in range(16384))
            diff=max(abs(cmath.exp(1j*(k*(x+beta)+a*math.sin(x+beta)+b*math.sin(3*(x+beta))))+cmath.exp(1j*(k*x+a*math.sin(x)+b*math.sin(3*x)))) for x in grid)
            assert diff+1e-9>=ch
    print('1D perturbation tests passed')


def two_dim_tests():
    beta=(2*math.pi*(math.sqrt(2)-1),2*math.pi*(math.sqrt(3)-1))
    for L in [0,1,math.sqrt(2),2,3,4]:
        v,k=character_profile(beta,cmath.exp(0.42j),L)
        assert sum(t*t for t in k)<=L*L+1e-9
        assert abs(v-abs(cmath.exp(1j*sum(t*x for t,x in zip(k,beta)))-cmath.exp(0.42j)))<1e-12
        print('dimension=2','L=',L,'argmin_k=',k,'defect=',round(v,12))
    # Non-character perturbations: two sine modes of torus phases.
    x=[2*math.pi*j/128 for j in range(128)]
    for k in [(0,0),(1,1),(-2,1)]:
        def phi(X,Y):
            return (k[0]*X+k[1]*Y+0.5*math.sin(X-2*Y)+0.3*math.sin(2*X+Y))
        diff=max(abs(cmath.exp(1j*phi(X+beta[0],Y+beta[1]))-cmath.exp(0.42j)*cmath.exp(1j*phi(X,Y))) for X in x for Y in x)
        ch=abs(cmath.exp(1j*(k[0]*beta[0]+k[1]*beta[1]))-cmath.exp(0.42j))
        assert diff+1e-5>=ch
    print('2D perturbation tests passed')

if __name__=='__main__':
    one_dim_tests()
    two_dim_tests()
    print('Finite sample stress tests passed; the proof does not rely on sampling.')
