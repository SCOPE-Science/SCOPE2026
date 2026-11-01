#!/usr/bin/env python3
"""Standalone numerical and algebraic corroboration of the uniform-profile theorem.

This finite checker does not replace the analytical argument for arbitrary time or network size.
"""
import math

def norms(v):
    return math.sqrt(sum(z*z for z in v))

def centered(v):
    mu=sum(v)/len(v)
    return [z-mu for z in v]

a,b,c=.89,.18,.28
Y=c/(1-a)
Lx=2*(math.sqrt(2)-1)*math.exp(Y+math.sqrt(2)-2)
Ly=4*math.exp(Y-2)
L=Lx+b*Ly/(1-a)
assert abs(L-17.17280149107571)<1e-10
assert abs(1/L-0.05823161704394)<2e-12
# Inspect the explicit absorbing box at fixed source parameters.
delta=.1
kmin,kmax=.026,.03
X=kmax+4*math.exp(Y+delta-2)
H=(c-b*X)/(1-a)-delta
assert a*(Y+delta)-b*kmin+c <= Y+delta
assert a*H-b*X+c >= H
assert kmin>0 and X>kmax
# These sampled checks corroborate, but do not replace, the scalar box proof.
import random
rng=random.Random(1729)
for _ in range(50):
    xx=[rng.uniform(kmin,X) for i in range(17)]
    yy=[rng.uniform(H,Y+delta) for i in range(17)]
    ff=[u*u*math.exp(v-u)+(kmin+(kmax-kmin)*i/16) for i,(u,v) in enumerate(zip(xx,yy))]
    q_sample=rng.random()
    ffmean=sum(ff)/17
    nextx=[q_sample*z+(1-q_sample)*ffmean for z in ff]
    nexty=[a*v-b*u+c for u,v in zip(xx,yy)]
    assert min(nextx)>=kmin-1e-12 and max(nextx)<=X+1e-12
    assert min(nexty)>=H-1e-12 and max(nexty)<=Y+delta+1e-12
N=17
k=[.026+(.004*i/(N-1)) for i in range(N)]
kappa=centered(k)
k_norm=norms(kappa)
assert k_norm>0
for q in (.03,.01,.003,.001):
    assert q*L<1
    x=[.9+.2*i/(N-1) for i in range(N)]
    y=[.2+.5*i/(N-1) for i in range(N)]
    bound_x=q*q*L/(1-q*L)*k_norm
    bound_y=b/(1-a)*bound_x
    worstx=0.0
    worsty=0.0
    for t in range(12000):
        f=[u*u*math.exp(v-u)+ki for u,v,ki in zip(x,y,k)]
        fm=sum(f)/N
        nx=[q*f_i+(1-q)*fm for f_i in f]
        ny=[a*v-b*u+c for u,v in zip(x,y)]
        x,y=nx,ny
        if t>=4000:
            assert min(x)>0
            assert max(y)<Y+1e-12
            errx=norms([u-q*kk for u,kk in zip(centered(x),kappa)])
            erry=norms([v+b*q/(1-a)*kk for v,kk in zip(centered(y),kappa)])
            worstx=max(worstx,errx)
            worsty=max(worsty,erry)
    assert worstx<=bound_x*(1+1e-8), (q,worstx,bound_x)
    assert worsty<=bound_y*(1+1e-8), (q,worsty,bound_y)
    print(f"q={q:.3f}, observed centered voltage residual={worstx:.12g}, bound={bound_x:.12g}; recovery residual={worsty:.12g}, bound={bound_y:.12g}")
# Algebraic centered identity for generic 5-vector, any average common term.
w=[2.,3.,4.,5.,7.]
P=centered(w)
for q in (0.,.2,.75,1.):
    mean=sum(w)/len(w)
    sample=[q*v+(1-q)*mean for v in w]
    assert max(abs(z-q*p) for z,p in zip(centered(sample),P))<1e-12
print('PASS: 4 coupling strengths, 17-neuron trajectories, exact projection identities.')
