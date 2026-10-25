#!/usr/bin/env python3
"""Standalone checks of a two-level chain polytope directional-width limit."""
import itertools, math
import numpy as np
from scipy.integrate import quad
from scipy.stats import norm

MU=1/math.sqrt(2*math.pi)
SIG2=0.5-1/(2*math.pi)
SIG=math.sqrt(SIG2)
RHO=-1/(math.pi-1)
CUBE_VAR=1-3/math.pi

def support_formula(g,p):
    a=np.asarray(g[:p]); b=np.asarray(g[p:])
    return max(float(np.maximum(a,0).sum()), float(np.maximum(b,0).sum()))

def support_enum(g,p):
    n=len(g)
    candidates=[0.0]
    for ids in (range(p),range(p,n)):
        ids=list(ids)
        for mask in range(1,1<<len(ids)):
            candidates.append(sum(g[ids[k]] for k in range(len(ids)) if (mask>>k)&1))
    return max(candidates)

def p_same(t):
    x=MU*t/SIG
    def bvn_cdf(a):
        r=math.sqrt(1-RHO*RHO)
        return quad(lambda z: norm.pdf(z)*norm.cdf((a-RHO*z)/r),-10,a,epsabs=3e-10)[0]
    return bvn_cdf(x)+bvn_cdf(-x)

rng=np.random.default_rng(20261020)
count=0
for n in range(2,10):
    for p in range(1,n):
        for _ in range(24):
            g=rng.normal(size=n)
            brute=support_enum(g,p)
            quick=support_formula(g,p)
            assert abs(brute-quick)<1e-11,(n,p,brute,quick)
            wd=(quick+support_formula(-g,p))/np.linalg.norm(g)
            aa=g[:p];bb=g[p:]
            dplus=np.maximum(aa,0).sum()-np.maximum(bb,0).sum()
            dminus=np.maximum(-aa,0).sum()-np.maximum(-bb,0).sum()
            wd2=(np.abs(g).sum()+abs(dplus)+abs(dminus))/(2*np.linalg.norm(g))
            assert abs(wd-wd2)<1e-11
            count+=1
print('FINITE_SUPPORT_PASS',count)
assert SIG2>0 and -1<RHO<0
assert abs(p_same(0)-(0.5+math.asin(RHO)/math.pi))<1e-8
print('rho',RHO,'p_same_zero',p_same(0),'p_same_t1',p_same(1),'p_same_t2',p_same(2))

for t in (0.0,1.0,2.5):
    n=1400; rep=25000; p=round((n+t*math.sqrt(n))/2);q=n-p
    t_real=(p-q)/math.sqrt(n)
    ww=[]; ss=[]
    for batch in range(25):
        g=rng.normal(size=(1000,n))
        aa=g[:,:p];bb=g[:,p:]
        plus=np.maximum(aa,0).sum(axis=1)-np.maximum(bb,0).sum(axis=1)
        minus=np.maximum(-aa,0).sum(axis=1)-np.maximum(-bb,0).sum(axis=1)
        width=(np.abs(g).sum(axis=1)+np.abs(plus)+np.abs(minus))/(2*np.linalg.norm(g,axis=1))
        ww.append(width-MU*math.sqrt(n))
        ss.append(np.sign(plus)==np.sign(minus))
    ww=np.concatenate(ww);ss=np.concatenate(ss)
    predicted_same=p_same(t_real)
    assert abs(ss.mean()-predicted_same)<0.04,(ss.mean(),predicted_same)
    pred_mean=SIG*math.sqrt(2/math.pi)*math.exp(-0.5*(MU*t_real/SIG)**2)+MU*t_real*(2*norm.cdf(MU*t_real/SIG)-1)
    assert abs(ww.mean()-pred_mean)<0.05,(ww.mean(),pred_mean)
    z=rng.normal(size=2*rep).reshape(rep,2)
    z[:,1]=RHO*z[:,0]+math.sqrt(1-RHO**2)*z[:,1]
    limit=0.5*rng.normal(scale=math.sqrt(CUBE_VAR),size=rep)+0.5*(np.abs(MU*t_real+SIG*z[:,0])+np.abs(MU*t_real+SIG*z[:,1]))
    assert abs(ww.std()-limit.std())<0.05,(ww.std(),limit.std())
    print('LIMIT_DIAGNOSTIC', 'n',n,'p',p,'q',q,'t',round(t_real,5), 'same_emp',round(float(ss.mean()),5),'same_lim',round(float(predicted_same),5),'centered_width_mean_emp',round(float(ww.mean()),5),'lim_mean',round(float(pred_mean),5),'centered_width_sd_emp',round(float(ww.std()),5),'lim_sd',round(float(limit.std()),5))
print('CHECK_PASS')
