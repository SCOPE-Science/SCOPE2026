"""Numerical cross-checks for a random-telegraph plus depolarizing qubit channel.
Run: python verify.py; requires numpy and scipy. Finite tests do not prove asymptotic claims.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize_scalar
from scipy.special import lambertw


def coherence(t, rate, frequency):
    if rate == 0:
        return math.cos(frequency*t)
    if frequency > rate:
        w=math.sqrt(frequency**2-rate**2)
        return math.exp(-rate*t)*(math.cos(w*t)+(rate/w)*math.sin(w*t))
    if abs(frequency-rate)<1e-13:
        return math.exp(-rate*t)*(1+rate*t)
    mu=math.sqrt(rate**2-frequency**2)
    return (0.5*(1+rate/mu)*math.exp((-rate+mu)*t)
           +0.5*(1-rate/mu)*math.exp((-rate-mu)*t))


def telegraph_expm(t, rate, frequency):
    q=np.array([[-rate-1j*frequency,rate],[rate,-rate+1j*frequency]],dtype=complex)
    return (np.ones(2)@expm(q*t)@np.ones(2)/2).real

I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],dtype=complex)
Y=np.array([[0,-1j],[1j,0]],dtype=complex)
Z=np.diag([1.,-1.]).astype(complex)
PAULIS=[I,X,Y,Z]


def min_choi_ppt(t,rate,frequency,kappa):
    f=coherence(t,rate,frequency)
    s=math.exp(-kappa*t)
    weights=[1,s*f,s*f,s]
    def channel(op):
        return sum(weight*np.trace(p@op)*p/2 for weight,p in zip(weights,PAULIS))
    choi=np.zeros((4,4),dtype=complex)
    for i in range(2):
        for j in range(2):
            e=np.zeros((2,2),dtype=complex)
            e[i,j]=1
            choi+=np.kron(e,channel(e))/2
    ppt=choi.reshape(2,2,2,2).swapaxes(1,3).reshape(4,4)
    return np.linalg.eigvalsh(ppt)[0]


def parameters(rate,frequency):
    w=math.sqrt(frequency**2-rate**2)
    theta=math.atan2(rate,w)
    return w,theta,math.pi/w


def threshold(index,rate,frequency):
    w,theta,P=parameters(rate,frequency)
    zl=(theta+math.pi/2+index*math.pi)/w
    zr=zl+P
    def fun(t):
        return math.log1p(2*abs(coherence(t,rate,frequency)))/t
    res=minimize_scalar(lambda t:-fun(t),bounds=(zl,zr),method='bounded',options={'xatol':1e-11})
    return -res.fun


def check():
    worst=0.
    checks=0
    for rate,frequency in [(0.,1.7),(.12,1.9),(.8,1.),(1.,1.),(1.5,1.)]:
        for t in [0.,.1,.4,.9,1.7,3.1,6.2,10.]:
            delta=abs(telegraph_expm(t,rate,frequency)-coherence(t,rate,frequency))
            assert delta<3e-13,(rate,frequency,t,delta)
            worst=max(worst,delta);checks+=1
    ppt_checks=0
    for rate,frequency in [(0.,1.5),(.2,1.6),(.9,1.),(1.1,1.)]:
        for t in [.03,.35,.7,1.2,1.9,3.8,5.6]:
            for kap in [.005,.06,.7]:
                s=math.exp(-kap*t)
                expected=(1-s*(1+2*abs(coherence(t,rate,frequency))))/4
                actual=min_choi_ppt(t,rate,frequency,kap)
                assert abs(actual-expected)<2e-13,(rate,frequency,t,kap,actual,expected)
                ppt_checks+=1
    for rate,frequency in [(0.,1.5),(.18,1.51),(.4,1.5),(.9,1.1)]:
        w,theta,P=parameters(rate,frequency)
        prev=math.inf
        for k in range(36):
            kval=threshold(k,rate,frequency)
            tk=(k+1)*P;zk=(theta+math.pi/2+k*math.pi)/w
            peak=math.exp(-rate*tk)
            lower=math.log1p(2*peak)/tk
            upper=math.log1p(2*peak)/zk
            assert lower*(1-2e-12)<=kval<=upper*(1+2e-12),(k,rate,kval,lower,upper)
            assert kval<prev,(k,rate,kval,prev)
            prev=kval
        if rate>0:
            for k in [25,35]:
                kval=threshold(k,rate,frequency)
                tk=(k+1)*P
                approx=2*math.exp(-rate*tk)/tk
                # for at least moderately large k, ratio approaches 1
                assert abs(kval/approx-1)<.09,(rate,k,kval/approx)
    for kap in [1e-3,1e-5,1e-7,1e-9]:
        rate=.18;freq=1.51
        w,_,P=parameters(rate,freq)
        N=sum(kap<threshold(k,rate,freq) for k in range(200))
        asym=(w/(math.pi*rate))*lambertw(2*rate/kap).real
        assert abs(N-asym)<3.5,(kap,N,asym)
    for kap in [1e-2,1e-3,1e-4]:
        rate=0.;freq=1.5
        w,_,_=parameters(rate,freq)
        approx=freq*math.log(3)/(math.pi*kap)
        # direct count can use threshold upper/lower instead of thousands optimizations
        n=int(approx)
        count=0
        # threshold k is decreasing; search by bisection
        lo,hi=0,int(approx*1.2+10)
        while lo<hi:
            mid=(lo+hi)//2
            if kap<threshold(mid,rate,freq):lo=mid+1
            else:hi=mid
        count=lo
        assert abs(count-approx)<3,(kap,count,approx)
    # A second independent count uses signs of the PPT eigenvalue sampled inside lobes.
    lobe_checks=0
    rate=.18;freq=1.51
    w,theta,P=parameters(rate,freq)
    for kap in [.008,.04,.15,.4]:
        for k in range(14):
            zl=(theta+math.pi/2+k*math.pi)/w
            zs=np.linspace(zl+1e-6,zl+P-1e-6,400)
            negative=sum(min_choi_ppt(float(t),rate,freq,kap)<-1e-12 for t in zs)
            prediction=kap<threshold(k,rate,freq)
            if prediction:
                # near threshold the interval can be smaller than the finite grid
                if abs(threshold(k,rate,freq)-kap)>0.0005:
                    assert negative>0,(kap,k)
            else:
                assert negative==0,(kap,k,negative)
            lobe_checks+=1
    print(f'VERIFY_OK telegraph_expm={checks} choi_ppt={ppt_checks} threshold_bounds=144'
          f' weak_noise_counts=4 static_counts=3 lobe_grids={lobe_checks} max_telegraph_error={worst:.2e}')


if __name__=='__main__':check()
