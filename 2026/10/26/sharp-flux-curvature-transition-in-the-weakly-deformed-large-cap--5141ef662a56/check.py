"""Standalone finite-volume algebraic and large-capacity checks of a K-ASEP flux law."""
import math
from fractions import Fraction
from itertools import product

def qint(k,t): return sum((t**j for j in range(k)),Fraction(0))

def weights(K,t):
    qbin=[]
    for a in range(K+1):
        numerator=math.prod(qint(j,t) for j in range(1,K+1))
        denominator=math.prod(qint(j,t) for j in range(1,a+1))*math.prod(qint(j,t) for j in range(1,K-a+1))
        qbin.append(t**((a-1)*(a-2)//2)*numerator/denominator)
    return qbin

def exact_current(L,K,n,t,q):
    ws=weights(K,t)
    Z=Fraction(0); J=Fraction(0)
    stationary={}
    for cfg in product(range(K+1), repeat=L):
        if sum(cfg)!=n:continue
        p=math.prod(ws[a] for a in cfg)
        stationary[cfg]=p
        Z+=p
        J+=p*(qint(cfg[0],t)*(qint(K,t)-qint(cfg[1],t))-q*qint(cfg[1],t)*(qint(K,t)-qint(cfg[0],t)))
    # Forward/backward master equation, exact fractions; check all configurations.
    for cfg,pi in stationary.items():
        out=Fraction(0); incoming=Fraction(0)
        for i in range(L):
            j=(i+1)%L; a=cfg[i];b=cfg[j]
            if a>0 and b<K:
                out+=pi*qint(a,t)*(qint(K,t)-qint(b,t))
                cfg2=list(cfg);cfg2[i]-=1;cfg2[j]+=1
                incoming+=stationary[tuple(cfg2)]*q*qint(b+1,t)*(qint(K,t)-qint(a-1,t))
            if b>0 and a<K:
                out+=pi*q*qint(b,t)*(qint(K,t)-qint(a,t))
                cfg2=list(cfg);cfg2[i]+=1;cfg2[j]-=1
                incoming+=stationary[tuple(cfg2)]*qint(a+1,t)*(qint(K,t)-qint(b-1,t))
        assert incoming==out,(cfg,incoming,out)
    return J/Z

def analytic(K,t,q,y):
    W=weights(K,t)
    F=sum((W[a]*y**a for a in range(K+1)),Fraction(0))
    fac=t
    for j in range(-1,K-1):fac*=1+t**j*y
    assert F==fac,(F,fac)
    mu=sum((qint(a,t)*W[a]*y**a for a in range(K+1)),Fraction(0))/F
    mu_expected=qint(K,t)*y/(t+y)
    assert mu==mu_expected,(mu,mu_expected)
    return (1-q)*mu*(qint(K,t)-mu)

for K in (1,2,3,4,5):
    for t in (Fraction(1,2),Fraction(1),Fraction(2),Fraction(5,3)):
        for y in (Fraction(1,4),Fraction(1),Fraction(5,2),t):
            analytic(K,t,Fraction(1,3),y)
        rho_star=sum((t**j/(1+t**j) for j in range(K)),Fraction(0))
        Jstar=analytic(K,t,Fraction(1,3),t)
        assert Jstar==(1-Fraction(1,3))*qint(K,t)**2/4
        print('K,t,rho*,J*=',K,str(t),str(rho_star),str(Jstar))

for L,K,n in ((3,2,3),(4,2,4),(3,3,4),(5,2,5)):
    j=exact_current(L,K,n,Fraction(3,2),Fraction(1,3))
    print('EXACT stationarity / current',L,K,n,str(j))

for lam in (-3.,-1.,0.,1.,3.):
    target=0.5 if lam==0 else math.log((1+math.exp(lam))/2)/lam
    for K in (100,1000):
        t=math.exp(lam/K)
        rho=sum(1/(1+math.exp(-lam*j/K)) for j in range(K))/K
        print('K,lam,density fraction,limit,error',K,lam,round(rho,10),round(target,10),round(rho-target,10))

# Independent numerical checks of the capacity-normalized flux and its curvature.
for lam in (-3.,-math.log(3),-.7,0.,.7,math.log(3),3.):
    H=math.exp(lam)
    ustar=.5 if lam==0 else math.log((1+H)/2)/lam
    for u in (.15,.35,.6,.85):
        if lam==0:
            target=(1-Fraction(1,3))*u*(1-u)
            y=u/(1-u)
        else:
            E=math.exp(lam*u)
            target=(1-Fraction(1,3))*(E-1)*(H-E)/lam**2
            y=(E-1)/(H-E)
        K=2500
        t=math.exp(lam/K)
        # Grand canonical inversion is approximated at fixed fugacity; density convergence is separately tested.
        kbr=sum(t**j for j in range(K))
        actual=(1-Fraction(1,3))*kbr**2*t*y/(t+y)**2/K**2
        rho=sum(y*math.exp(lam*j/K)/(1+y*math.exp(lam*j/K)) for j in range(-1,K-1))/K
        assert abs(rho-u)<.002,(lam,u,rho)
        assert abs(float(actual)-float(target))<.01,(lam,u,target,actual)
    # Check inflection threshold and second derivative numerically against exact expression.
    for u in (.02,.25,.7,.98):
        expected=(1-Fraction(1,3))*math.exp(lam*u)*(1+H-4*math.exp(lam*u))
        def flux(v):
            return (1-Fraction(1,3))*v*(1-v) if lam==0 else (1-Fraction(1,3))*(math.exp(lam*v)-1)*(H-math.exp(lam*v))/lam**2
        h=1e-4
        fd=(flux(u+h)-2*flux(u)+flux(u-h))/h**2
        assert abs(float(fd)-float(expected))<.002,(lam,u,fd,expected)
    print('limiting-flux-and-curvature checks',lam,ustar,'passed')
print('ALL CHECKS PASSED')
