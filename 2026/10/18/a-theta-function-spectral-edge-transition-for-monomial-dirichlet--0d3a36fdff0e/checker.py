#!/usr/bin/env python3
"""Finite diagnostics for the stated high-Schatten lattice concentration theorem.

All infinite-dimensional limits in the accompanying result are proved analytically;
these computations test the exact singular weights and phase predictions only.
No third-party modules are required.
"""
import math

def derivative_without_h(x, k, m, beta):
    return (sum(1.0/(x - i) for i in range(k))
            + beta*(1.0/(x-k+m+1.0) - 1.0/(x+1.0)))

def log_weight_continuous(x, h, k, m, beta):
    return (sum(math.log(x-i) for i in range(k))
            - h*(x-k)
            + beta*math.log((x-k+m+1.0)/(x+1.0)))

def normalized_mass(N, theta, tau, k, m, alpha, window=42):
    beta = (1.0-alpha)/2.0
    x = N+theta
    h = derivative_without_h(x, k, m, beta)
    p = tau/h**2
    mx = log_weight_continuous(x, h, k, m, beta)
    L = max(k, N-window)
    R = N+window
    observed = sum(math.exp(p*(log_weight_continuous(j,h,k,m,beta)-mx))
                   for j in range(L, R+1))
    predicted = sum(math.exp(-tau*(j-theta)**2/(2.0*k))
                    for j in range(-window,window+1))
    return h, observed, predicted

def diffuse_mass(N, k, m, alpha, p):
    beta=(1-alpha)/2
    x=N+0.2
    h=derivative_without_h(x,k,m,beta)
    mx=log_weight_continuous(x,h,k,m,beta)
    # Beyond this window the weights contribute negligibly in the selected tests.
    R=max(10*N,1000)
    obs=sum(math.exp(p*(log_weight_continuous(j,h,k,m,beta)-mx))
            for j in range(k,R))
    pred=math.sqrt(2*math.pi*k/(p*h*h))
    return obs,pred

def run():
    checks=0
    for k,m,alpha in [(2,0,0.5),(2,4,0.5),(3,1,0.3),(4,7,0.8)]:
        for theta in (0.0,0.5):
            errors=[]
            for N in (30,100,300):
                h,obs,pred=normalized_mass(N,theta,8.0,k,m,alpha)
                assert 0<h<1
                assert abs(obs-pred)<0.004, (k,m,alpha,theta,N,obs,pred)
                errors.append(abs(obs-pred))
                checks+=1
            assert errors[2] < errors[0], errors
            checks+=1
    for k,m,alpha,p in [(2,0,0.5,20),(3,2,0.3,40),(4,7,0.8,60)]:
        obs,pred=diffuse_mass(150,k,m,alpha,p)
        assert abs(obs/pred-1) <0.07,(k,m,alpha,p,obs,pred)
        checks+=1
    for k in (2,3,4):
        tau=8.0
        z0=sum(math.exp(-tau*j*j/(2*k)) for j in range(-30,31))
        zhalf=sum(math.exp(-tau*(j-.5)**2/(2*k)) for j in range(-30,31))
        assert z0>zhalf
        checks+=1
    print('PASS',checks,'finite numerical diagnostics; theorem proved separately')

if __name__=='__main__':run()
