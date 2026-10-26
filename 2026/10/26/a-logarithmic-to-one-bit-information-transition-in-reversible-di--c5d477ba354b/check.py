"""Independent finite-state and asymptotic tests for reversible pair adsorption on rings."""
import itertools
import math
import numpy as np
from scipy.special import gammaln, logsumexp, i0
from scipy.linalg import null_space


def stationary_by_generator(n, p, diffusion):
    ra=p*p
    rd=(1-p)*(1-p)
    states = []
    for x in itertools.product((0,1),repeat=n):
        if n%2:
            ok=sum(x)%2==0
        elif diffusion:
            ok=sum(x)%2==0
        else:
            ok=sum(x[::2])==sum(x[1::2])
        if ok: states.append(x)
    index={x:i for i,x in enumerate(states)}
    Q=np.zeros((len(states),len(states)))
    for i,x in enumerate(states):
        for k in range(n):
            a,b=k,(k+1)%n
            y=list(x)
            if x[a]==x[b]:
                y[a]^=1;y[b]^=1
                rate=ra if x[a]==0 else rd
                j=index[tuple(y)]
                Q[j,i]+=rate;Q[i,i]-=rate
            if diffusion and x[a]!=x[b]:
                y=list(x);y[a],y[b]=y[b],y[a]
                j=index[tuple(y)]
                Q[j,i]+=0.3; Q[i,i]-=0.3
    P=np.linalg.lstsq(np.concatenate([Q,np.ones((1,len(states)))]),np.r_[np.zeros(len(states)),1],rcond=None)[0]
    analytic=np.array([(p/(1-p))**sum(x) for x in states])
    analytic/=analytic.sum()
    return states, P, analytic, np.max(abs(Q@analytic))


def MI_explicit(states,P,n):
    A=dict();B=dict();AB=dict()
    for x,pr in zip(states,P):
        a=tuple(x[::2]);b=tuple(x[1::2]);
        A[a]=A.get(a,0)+pr; B[b]=B.get(b,0)+pr
        AB[(a,b)]=AB.get((a,b),0)+pr
    return sum(pr*math.log(pr/(A[a]*B[b])) for (a,b),pr in AB.items() if pr>0)


def binary_entropy(u):
    return -u*math.log(u)-(1-u)*math.log(1-u) if 0<u<1 else 0.


def exact_MI(n,p,diffusion):
    t=1-2*p
    if (n%2) or diffusion:
        a=(n+1)//2
        b=n-a
        if n%2==0:a=b=n//2
        u=((1+t**a)*(1+t**b))/(2*(1+t**n))
        return binary_entropy(u)
    m=n//2
    j=np.arange(m+1)
    logw=2*(gammaln(m+1)-gammaln(j+1)-gammaln(m-j+1))+2*j*math.log(p/(1-p))
    w=np.exp(logw-logsumexp(logw))
    return -sum(w[w>0]*np.log(w[w>0]))

for n in [4,5,6,7,8]:
    for p in [0.18,0.5,0.76]:
        for d in [0,1]:
            st,Q,an,res=stationary_by_generator(n,p,d)
            maxerr=max(abs(Q-an))
            mi=MI_explicit(st,Q,n)
            theorem=exact_MI(n,p,d)
            assert maxerr<2e-10 and res<1e-10 and abs(mi-theorem)<2e-10,(n,p,d,maxerr,mi,theorem)
print('PASS generator + detailed balance + exhaustive full-microstate mutual information: 30 cases, n=4..8')

for p in [0.2,0.5,0.8]:
    for m in [100,1000,10000]:
        true=exact_MI(2*m,p,0)
        asym=.5*math.log(math.pi*math.e*m*p*(1-p))
        print('fixed density asymptotic',p,m,'true',round(true,8),'asympt',round(asym,8),'gap',round(true-asym,8))
        assert abs(true-asym)<.004 if m==10000 else True
    dif=exact_MI(2*10000,p,1)
    assert abs(dif-math.log(2))<1e-8
print('PASS fixed-density Gaussian entropy law and one-bit positive-diffusion limit')

for L in [0.2,1.0,2.5,5.0]:
    for m in [300,3000]:
        p=L/m
        MI=exact_MI(2*m,p,0)
        js=np.arange(0,120)
        wg=np.exp(2*js*math.log(L)-2*gammaln(js+1)-math.log(i0(2*L)))
        lim=-sum(wg[wg>0]*np.log(wg[wg>0]))
        print('Bessel scaling',L,m,'true',round(MI,8),'limit',round(lim,8),'gap',round(MI-lim,8))
        if m==3000:assert abs(MI-lim)<.005
print('PASS dilute Bessel entropy crossover')

for n in [4,6,8,10]:
    p=.5
    assert abs(exact_MI(n,p,1)-math.log(2))<1e-13
print('PASS exact one-bit global mutual information despite proper-subset uniformity at equal rates')
