#!/usr/bin/env python3
"""Independent numerical spot checks of exact phase-orbit identities.
Requires Python 3, numpy, scipy. Finite experiments are not infinite proofs.
"""
import math
import numpy as np
from scipy.special import ive
from scipy.stats import poisson, chi2

nchecks=0

def check(ok,msg):
    global nchecks
    assert ok,msg
    nchecks+=1

def top_mass(a,n):
    return float(np.sort(np.ravel(a))[::-1][:n].sum())

def quant_dim(a,epsilon):
    z=np.sort(np.ravel(a))[::-1]
    c=np.cumsum(z)
    ix=np.searchsorted(c,1-epsilon**2)
    return int(ix+1)

# Exact finite-dimensional phase-orbit Fourier diagonals.
for d in [1,2]:
    grids=np.indices((5,)*d).reshape(d,-1).T
    means=np.array([0.7+0.4*j for j in range(d)])
    p=np.array([np.prod(poisson.pmf(k,means)) for k in grids])
    p/=p.sum()
    c=np.sqrt(p)
    # HS Fourier mode weight for each number-difference vector.
    diagonals={}
    for i,a in enumerate(grids):
        for j,b in enumerate(grids):
            key=tuple(a-b)
            diagonals[key]=diagonals.get(key,0.)+p[i]*p[j]
    q=np.array(list(diagonals.values()))
    check(abs(q.sum()-1)<5e-14,'HS Fourier masses')
    for n in range(1,min(16,len(grids))):
        check(top_mass(q,n)<=top_mass(p,n)+1e-12,'convolution majorization')
    for t in [0.11,0.77,1.29,2.52]:
        theta=np.array([t*(k+1) for k in range(d)])
        phases=np.exp(1j*(grids@theta))
        v=c*phases
        A=np.outer(v,np.conjugate(v))
        check(abs(np.vdot(v,v)-1)<1e-13,'norm-one ket')
        check(abs(np.sum(np.abs(A)**2)-1)<1e-13,'norm-one projector')
        # Each difference diagonal has constant projected HS norm.
        for key,mass in diagonals.items():
            diag=sum(abs(A[i,j])**2 for i,a in enumerate(grids)
                     for j,b in enumerate(grids) if tuple(a-b)==key)
            check(abs(diag-mass)<1e-12,'Fourier block constant norm')

# Poisson and modified-Bessel/Skellam identities.
for mu in [0.1,0.8,1.0,3.7,15.,100.]:
    kmax=int(max(70,10*math.sqrt(mu)+20))
    q=np.array([ive(k,2*mu) for k in range(kmax)])
    check(abs(q[0]+2*q[1:].sum()-1)<1e-10,'Skellam normalization')
    for k in range(0,min(30,kmax-1)):
        check(q[k]>q[k+1],'strict Bessel mode ordering')
    p=np.array([poisson.pmf(k,mu) for k in range(int(mu+12*math.sqrt(mu)+40))])
    check(abs(p.sum()-1)<1e-11,'Poisson normalization')
    for n in [1,2,3,5,9,17]:
        selected=q[0]+2*q[1:(n+1)//2].sum()
        if n%2==0: selected+=q[n//2]
        direct=sum(sorted([q[0]]+[q[k] for k in range(1,kmax) for _ in (0,1)],reverse=True)[:n])
        check(abs(selected-direct)<5e-13,'optimal projector Fourier selection')
        check(direct<=top_mass(p,n)+2e-12,'strict phase cost (numerical)')

# Multimode high-intensity resource counts and Gaussian volume coefficient.
for d,tlist in [(1,[10.,25.,60.]),(2,[5.,10.,20.]),(3,[4.,7.,10.])]:
    amps=np.array([1.+0.22*j for j in range(d)])
    for t in tlist:
        p1=[];q1=[]
        for a in amps:
            mu=(t*a)**2
            sd=math.sqrt(mu)
            k0=max(0,int(mu-5.5*sd-10));k1=int(mu+5.5*sd+10)
            p1.append(poisson.pmf(np.arange(k0,k1+1),mu))
            m=int(5.5*math.sqrt(2*mu)+10)
            q1.append(ive(np.arange(-m,m+1),2*mu))
        pp=p1[0]
        qq=q1[0]
        for j in range(1,d):
            pp=np.multiply.outer(pp,p1[j])
            qq=np.multiply.outer(qq,q1[j])
        check(pp.sum()>0.99999 and qq.sum()>0.99999,'tails in finite calculation')
        for eps in [0.4,0.65]:
            nv=quant_dim(pp,eps)
            npj=quant_dim(qq,eps)
            check(npj>=nv,'multimode phase loss')
            R2=chi2.ppf(1-eps*eps,d)
            vd=math.pi**(d/2)/math.gamma(d/2+1)
            cv=vd*(R2**(d/2))*np.prod(amps)
            pred_v=cv*t**d
            pred_p=cv*(math.sqrt(2)*t)**d
            # Finite-grid counts converge to asymptotic volume: moderate t ranges.
            check(abs(nv/pred_v-1)<0.48,'vector Gaussian-volume prediction')
            check(abs(npj/pred_p-1)<0.48,'projector Gaussian-volume prediction')
            print('d',d,'t',t,'eps',eps,'nvector',nv,'nprojector',npj,
                  'ratio',round(npj/nv,6),'limit',round(2**(d/2),6))
print('PASS',nchecks,'finite checks')
