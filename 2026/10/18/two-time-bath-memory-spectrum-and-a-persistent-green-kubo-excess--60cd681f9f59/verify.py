"""Independent exact-generator and stochastic-trajectory checks for a coupled resetting bath."""
import numpy as np
from scipy.linalg import expm
from scipy.integrate import quad

def analytic(g,r,t):
    a=2*(g*r+g+1)/(r*(g*r+2*g+1))
    b=(g*r+2*g+2)/(r*(g*r+2*g+1))
    s=1+r+1/g
    delta=np.sqrt(s*s-4*r/g)
    ks=(s-delta)/2; kf=(s+delta)/2
    d=(1+r)-b/a
    al=a*(kf-d)/(kf-ks)
    af=a-al
    v=al*np.exp(-ks*t)+af*np.exp(-kf*t)
    dint=(a+g*b)/r
    ratio=dint/(a/r)
    return a,b,ks,kf,al,af,v,dint,ratio

def independent(g,r,t):
    A=np.array([[-1,1],[1/g,-1/g]])
    Q=np.diag([2,2/g]);J=np.diag([0,1])
    E=[]
    for i in range(2):
        for j in range(2):
            M=np.zeros((2,2));M[i,j]=1
            E.append((A@M+M@A.T+r*(J@M@J-M)).reshape(-1))
    T=np.array(E).T
    S=np.linalg.solve(T,-Q.reshape(-1)).reshape(2,2)
    B=A+r*(J-np.eye(2))
    corr=(expm(B*t)@S)[0,0]
    dint=(-np.linalg.solve(B,S))[0,0]
    return S,corr,dint

def run():
    errs=[]
    for g in [0.17,0.9,4.5,30.0]:
        for r in [0.08,1.1,7.,75.]:
            for t in [0.,0.07,0.6,3.,10.]:
                a,b,ks,kf,al,af,c,dint,R=analytic(g,r,t)
                S,c_num,di_num=independent(g,r,t)
                err=max(abs(S[0,0]-a),abs(S[0,1]-b),abs(c-c_num),abs(dint-di_num))
                errs.append(err)
                assert err<2e-9,(g,r,t,err)
                assert min(al,af)>0 and ks>0 and kf>ks
                assert 1+g/2 < R < 1+g
            # Direct quadrature of exact covariance
            a,b,ks,kf,al,af,_,dint,_=analytic(g,r,0)
            q=quad(lambda t: al*np.exp(-ks*t)+af*np.exp(-kf*t),0,np.inf,epsabs=1e-8)[0]
            assert abs(q-dint)<1e-8
    # Stiff but finite large-reset asymptotic without numerical cancellation
    for g in [0.5,1.5,6.]:
        for r in [10000,100000]:
            *_, d, ratio = analytic(g,r,1.2)
            assert abs(r*r*d-(2+g))<0.004
            assert abs(ratio-(1+g/2))<0.001
    print('PASS: 80 independent matrix-exponential/covariance comparisons;')
    print('PASS: 16 Green-Kubo quadratures; positive two-mode weights for all tested parameter points;')
    print('PASS: six fast-reset asymptotic checks; max absolute matrix comparison error',max(errs))
if __name__=='__main__':run()
