"""Independent checks of weighted-join Cesaro resonance formulas."""
import math
import numpy as np
from numpy.linalg import eigh

def complete(n):
    return np.ones((n,n))-np.eye(n)

def cycle(n):
    a=np.zeros((n,n))
    for k in range(n): a[k,(k+1)%n]=a[(k+1)%n,k]=1
    return a

def join(x,y,g):
    n,m=x.shape[0],y.shape[0]
    return np.block([[x,np.full((n,m),g)],[np.full((m,n),g),y]])

def time_average(a,T=None):
    v,u=eigh(a)
    # Return probability from initial vertex 0 to all targets, integral exactly in eigenfrequencies.
    amps=u[0,:][None,:]*u
    delta=v[:,None]-v[None,:]
    weight=np.sinc(delta*T/np.pi) if T is not None else (abs(delta)<1e-8).astype(float)
    return np.einsum('ij,ik,jk->i',amps,amps,weight)

def exact_pred(x,y,g):
    n,m=x.shape[0],y.shape[0]
    r=x.sum(axis=1)[0];s=y.sum(axis=1)[0]
    D=math.sqrt((r-s)**2+4*g*g*n*m)
    minus=(r+s-D)/2
    beta=(1-(r-s)/D)/2
    alpha=1-beta
    vv,ee=eigh(x)
    resonant=np.abs(vv-minus)<1e-8
    if np.any(resonant): proj=ee[:,resonant]@ee[:,resonant].T
    else: proj=np.zeros_like(x)
    baseline=time_average(x)
    return baseline-2*alpha*beta/n**2+(2*beta/n)*proj[:,0],minus,alpha,beta

def check(x,y,g):
    actual=time_average(join(x,y,g))[:x.shape[0]]
    pred,lam,_,_=exact_pred(x,y,g)
    err=np.max(abs(actual-pred))
    assert err<2e-9,(err,actual,pred)
    return err,lam

checks=0
errs=[]
for n in range(3,10):
    for m in range(2,7):
        for X in [complete(n),cycle(n)]:
            for Y in [complete(m),cycle(m) if m>2 else complete(m)]:
                for g in [0.27,0.66,1.0,1.7,3.0]:
                    e,_=check(X,Y,g); errs.append(e);checks+=1
                vx=np.linalg.eigvalsh(X)
                r=X.sum(axis=1)[0];s=Y.sum(axis=1)[0]
                for mu in np.unique(np.round(vx,10)):
                    if mu>=min(r,s)-1e-8:continue
                    g=math.sqrt((r-mu)*(s-mu)/(n*m))
                    e,_=check(X,Y,g); errs.append(e);checks+=1

X=complete(3);Y=complete(2)
base=113/225
assert abs(time_average(join(X,Y,1))[0]-17/25)<1e-12
for c in [-5.,-3.,-1.,0,0.8,2.,6.]:
    for T in [100.,250.,600.,1200.]:
        g=1+c/T
        actual=time_average(join(X,Y,g),T)[0]
        z=12*c/5
        pred=base+(8/45)*np.sinc(z/np.pi)
        diff=abs(actual-pred)
        assert diff<0.32/T,(c,T,actual,pred,diff)
        checks+=1
print('CHECKS_PASSED',checks,'max stationarity discrepancy',max(errs))
print('K3_K2_resonant_return',time_average(join(X,Y,1))[0])
print('K3_K2_generic_one_sided_limit',base)
print('K3_K2_jump',8/45)

def sinc(z):
    return 1.0 if abs(z)<1e-12 else math.sin(z)/z

def equal_clique_formula(n,g,T):
    baseline=1-2/n+3/(2*n*n)
    return baseline+(n-1)/(n*n)*(sinc(n*(1-g)*T)+sinc(n*(1+g)*T)) + sinc(2*n*g*T)/(2*n*n)

for n in range(2,12):
    for g in [0.02,0.3,0.72,1.0,1.21,1.8,3.]:
        for T in [0.05,0.8,3.1,10.,60.]:
            observed=time_average(join(complete(n),complete(n),g),T)[0]
            predicted=equal_clique_formula(n,g,T)
            assert abs(observed-predicted)<5e-12,(n,g,T,observed,predicted)
            checks+=1
print('ALL_TESTS_PASSED',checks)
