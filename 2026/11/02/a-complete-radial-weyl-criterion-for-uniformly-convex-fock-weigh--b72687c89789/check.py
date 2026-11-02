"""Finite diagnostic checks for radial Fock Toeplitz asymptotics (not a proof)."""
import math
from scipy.integrate import quad
from scipy.optimize import brentq

def phi(r,mode,a):
    if mode=='gaussian': return r*r/2
    if mode=='convex_osc': return r*r/2 + a*(1-math.cos(r))
    if mode=='log_osc':
        L=math.log1p(r*r)
        return r*r/2 + a*((1+r*r)*(math.sin(L)-math.cos(L))+1)/4
    raise ValueError(mode)

def h(r,mode,a):
    if mode=='gaussian':return 1.
    if mode=='convex_osc':return 1+a*math.sin(r)/r if r else 1+a
    if mode=='log_osc':return 1+a*math.sin(math.log1p(r*r))

def q(r,mode,a):return r*r*h(r,mode,a)

def eig(k,d,beta,mode,a):
    r0=brentq(lambda r:q(r,mode,a)-(k+d-.5),.01,3*math.sqrt(k+d)+5)
    def log_dens(r):return (2*k+2*d-1)*math.log(r)-2*phi(r,mode,a)
    L0=log_dens(r0)
    lo=max(1e-10,r0-20);hi=r0+20
    den=quad(lambda r:math.exp(log_dens(r)-L0),lo,hi,epsabs=1e-12)[0]
    num=quad(lambda r:(1+r*r)**(-beta/2)*math.exp(log_dens(r)-L0),lo,hi,epsabs=1e-12)[0]
    return r0,num/den

if __name__=='__main__':
    checked=0
    for mode,a in [('gaussian',0),('convex_osc',.15),('log_osc',.15)]:
        for d in (1,2,3):
            for beta in (.7,1.4,3.):
                for k in (20,80,320):
                    r,lam=eig(k,d,beta,mode,a)
                    predicted=r**(-beta)
                    err=abs(lam/predicted-1)
                    assert err < .27, (mode,d,beta,k,err)
                    checked+=1
                    total=math.comb(k+d,d)
                    scale=(total**(beta/(2*d)))*lam
                    target=(h(r,mode,a)/(math.factorial(d)**(1/d)))**(beta/2)
                    assert abs(scale/target-1)<.35,(mode,d,beta,k,scale,target)
                    checked+=1
    print('Passed',checked,'finite asymptotic diagnostics, including dimensions 1,2,3 and two nonquadratic weights.')
    for mode in ('gaussian','convex_osc','log_osc'):
        print('example',mode,'d=2,beta=2')
        for k in (40,160,640):
            r,lam=eig(k,2,2,mode,.15)
            j=math.comb(k+2,2)
            print(k,'r',round(r,4),'j^.5 lambda',round(j**.5*lam,6),'prediction',round(h(r,mode,.15)/math.sqrt(2),6))
