#!/usr/bin/env python3
"""Numerical consistency checks for the neutral-to-damped exchange mode.
No finite numerical check is intended to replace the analytic proof.
"""
from math import exp
P=dict(phi=50.,muH=1.,gamma=2.,l=2.,muY=3.,muV=4.,delta=1.,theta=2.,omega=(.2,.4,.1),alpha=(.3,.2,.5))

def parameters(p):
    omega=p['omega'];alpha=p['alpha']; s=exp(-sum(x*y for x,y in zip(omega,alpha)))
    k=p['l']*p['muY']*p['muV']/(s*p['delta']*p['theta'])
    assert p['phi']*p['gamma']>p['muH']*k
    v0=(p['phi']*p['gamma']-p['muH']*k)/(2*p['gamma']*k)
    tau=sum(omega)
    D=p['l']*p['muY']+p['l']*p['muV']+p['muY']*p['muV']+p['l']*p['muY']*p['muV']*tau
    c=p['l']*p['muY']*p['muV']*v0/D
    return s,k,v0,tau,c

def equilibria(p,psi):
    s,k,v0,tau,c=parameters(p)
    v=(p['phi']*p['gamma']-p['muH']*k)/(k*(2*p['gamma']+p['muH']*psi))
    H=k*(1+psi*v)/p['gamma']
    L=exp(-p['alpha'][0]*p['omega'][0])*k*v/p['l']
    Y=exp(-p['alpha'][1]*p['omega'][1])*p['delta']*L/p['muY']
    C=exp(-p['alpha'][2]*p['omega'][2])*p['theta']*Y/p['muV']
    assert abs(v-C)<2e-13
    F=p['gamma']*H*C/(1+psi*C)
    residual=[p['phi']-p['muH']*H-2*F,
      exp(-p['alpha'][0]*p['omega'][0])*F-p['l']*L,
      exp(-p['alpha'][1]*p['omega'][1])*p['delta']*L-p['muY']*Y,
      exp(-p['alpha'][2]*p['omega'][2])*p['theta']*Y-p['muV']*C]
    assert max(map(abs,residual))<1e-11, residual
    return H,v

def main():
    p=P;s,k,v0,tau,c=parameters(p)
    print('s=',s,'k=',k,'v0=',v0,'tau=',tau,'leading c=',c)
    rows=[]
    for psi in (0.,1e-4,1e-3,1e-2,0.1,1.,10.):
      H,v=equilibria(p,psi)
      G=p['l']*p['muY']*p['muV']/(1+psi*v)
      def F(x):return (x+p['l'])*(x+p['muY'])*(x+p['muV'])-G*exp(-tau*x)
      lo=-min(p['l'],p['muY'],p['muV']);hi=0.
      for _ in range(120):
        mid=(lo+hi)/2
        if F(mid)<0:lo=mid
        else: hi=mid
      root=(lo+hi)/2
      assert abs(F(root))<2e-11
      rows.append(root)
      if psi:print('psi=',psi,'v=',v,'antisymmetric_root=',root,'root/psi=',root/psi)
    assert abs(rows[0])<1e-12
    assert all(a>b for a,b in zip(rows,rows[1:])),rows
    assert abs(rows[1]/1e-4+c)<1e-3,(rows[1]/1e-4,c)
    # unsaturated branch with unequal compositions, testing both strain equations
    T=(p['phi']*p['gamma']-p['muH']*k)/(p['gamma']*k)
    for frac in (0.,.13,.41,1.):
      H=k/p['gamma']; v1=frac*T;v2=(1-frac)*T
      assert abs(p['phi']-p['muH']*H-k*(v1+v2))<1e-12
      for v in (v1,v2):
        L=exp(-p['alpha'][0]*p['omega'][0])*k*v/p['l']
        Y=exp(-p['alpha'][1]*p['omega'][1])*p['delta']*L/p['muY']
        V=exp(-p['alpha'][2]*p['omega'][2])*p['theta']*Y/p['muV']
        assert abs(V-v)<1e-12
    print('CHECK_OK')
if __name__=='__main__': main()
