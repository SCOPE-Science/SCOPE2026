"""Reproduce the Fourier zero-circle fold classification for a Gaussian-circle mixture.
Requires scipy and numpy. All displayed radii are angular Fourier frequencies.
"""
import math
import numpy as np
from scipy.special import j0, j1, jn_zeros
from scipy.optimize import brentq

def fold(a,k):
    zz=jn_zeros(0,2*k)
    left,right=zz[-2:]
    def crit(x): return 2*a*x*j0(x)-j1(x)
    # Endpoint derivative may change sign for huge a; split and select sign transition.
    xs=np.linspace(left+1e-7,right-1e-7,1001)
    roots=[]
    for x,y in zip(xs[:-1],xs[1:]):
        if crit(x)*crit(y)<0: roots.append(brentq(crit,x,y,xtol=3e-14))
    assert len(roots)==1,(a,k,roots)
    rho=roots[0]
    logLam=a*rho*rho+math.log(-j0(rho))
    Lam=math.exp(logLam) if logLam<690 else float("inf")
    assert Lam>0
    h=j0(rho)
    hprime=-j1(rho)
    assert abs(hprime+2*a*rho*h)<1e-8
    u2=4*a-1-4*a*a*rho*rho
    assert u2<0
    g2=h*u2  # sign-normalized curvature; exp(a*rho²)>0
    assert g2>0
    return (rho,Lam,left,right,g2,logLam)

print('Gaussian-circle normalized mixture: F_t=(1-t)exp(-a*r²)+tJ0(r)')
for a in (0.001,0.02,0.2):
    print('a=',a)
    for k in (1,2,3,8,15):
        rho,Lam,lft,rt,g2,logLam=fold(a,k)
        t=1/(1+Lam)
        # fold sign checks
        mid=(lft+rho)/2
        assert j0(mid)<0
        if k<=3 and math.isfinite(Lam):
            for eps in (0.01,0.1):
                Lbelow=(1-eps)*Lam
                Labove=(1+eps)*Lam
                g=lambda x:math.exp(a*x*x)*j0(x)
                assert g(rho)+Lbelow<0 and g(rho)+Labove>0
        logAsym=a*rt*rt-1-math.log(a*math.sqrt(2*math.pi))-1.5*math.log(rt)
        print('k %2d  rho=%.10f j_right=%.10f t=%.5g  Lam=%.7g asym ratio=%.6f' % (k,rho,rt,t,Lam,math.exp(logLam-logAsym)))
print('PASS: every tested interval has one nondegenerate fold, with expected signs')

# Numerical crosschecks for pairwise threshold crossings, as opposed to proofs.
def log_threshold(a,k):
    return fold(a,k)[-1]
for k,l in ((1,2),(1,3),(2,3)):
    acrit=brentq(lambda a: log_threshold(a,l)-log_threshold(a,k),1e-7,0.04,xtol=1e-14)
    assert log_threshold(acrit*0.9,l)<log_threshold(acrit*0.9,k)
    assert log_threshold(acrit*1.1,l)>log_threshold(acrit*1.1,k)
    print('pairwise crossover (%d,%d): a*=%.15f' % (k,l,acrit))

# For representative lobe values, the two roots must be separated by the fold.
for a in (0.001,0.02):
    for k in (1,2,5):
        rho,Lam,left,right,_,_=fold(a,k)
        q=lambda x: math.exp(a*x*x)*j0(x)+0.8*Lam
        rminus=brentq(q,left,rho)
        rplus=brentq(q,rho,right)
        assert left<rminus<rho<rplus<right
        assert abs(q(rminus))<1e-6 and abs(q(rplus))<1e-6
        assert q(rho)<0
print('PASS: sample two-circle regimes and pairwise crossover sign changes')
