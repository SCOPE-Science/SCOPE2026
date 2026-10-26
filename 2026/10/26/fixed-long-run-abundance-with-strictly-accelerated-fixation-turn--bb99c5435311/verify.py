"""Independent exact-arithmetic checks for the fixation-turnover theorem.

Run: python verify.py  (Python >=3.9, standard library only).
The analytic argument in RESULT.md is required for arbitrary population size.
"""
from fractions import Fraction as Q
from math import comb, exp, floor, sqrt, pi, log

CHECKS=0

def ck(a, b):
    global CHECKS
    CHECKS += 1
    assert a == b, (a, b)

def choose(a, b):
    return comb(a,b) if 0 <= b <= a and a >= 0 else 0

def hprob(a,b,k,l):
    if any(x<0 for x in (a,b,k,l)) or k>a or l>b:
        return Q(0)
    return Q(choose(a,k)*choose(b,l), choose(a+b,k+l))

def delta_direct(N,g,c,R,i):
    pC=-c
    pD=Q(0)
    for j in range(1,g+1):
        pC+=c*Q(j,g)*R[j-1]*hprob(i-1,N-i,j-1,g-j)
        pD+=c*Q(j,g)*R[j-1]*hprob(i,N-i-1,j,g-j-1)
    return pC-pD

def cumulative_closed(N,g,c,R,k):
    s=-c*k
    den=choose(N-1,g-1)
    for j in range(1,g+1):
        s+=Q(c*j*R[j-1]*choose(k,j)*choose(N-k-1,g-j),g*den)
    return s

def coeff_closed(N,g,c,k,j):
    return Q(c*j*choose(k,j)*choose(N-k-1,g-j),g*choose(N-1,g-1))

def exact_cases():
    global CHECKS
    for N in range(3,15):
        for g in range(2,N):
            profiles=[]
            for shift in range(3):
                profiles.append([Q((j*7+N+shift)%13+1,(N+g+shift)%5+1) for j in range(1,g+1)])
            for R in profiles:
                c=Q(N+1,g+2)
                diffs=[delta_direct(N,g,c,R,i) for i in range(1,N)]
                cum=Q(0)
                for k,d in enumerate(diffs,1):
                    cum+=d
                    ck(cum,cumulative_closed(N,g,c,R,k))
                    for j in range(1,g+1):
                        pert=R.copy(); pert[j-1]+=1
                        ck(cumulative_closed(N,g,c,pert,k)-cum, coeff_closed(N,g,c,k,j))
                        if j<g:
                            ck(coeff_closed(N,g,c,k,j)>0, j <= k <= N-g+j-1)
                ck(cum, c*(Q((N-g)*R[-1],g)-(N-1)))
    print('exact-combinatorial checks:',CHECKS)

def fixation(N,g,c,R,delta):
    Bs=[0.0]+[float(cumulative_closed(N,g,c,R,k)) for k in range(1,N)]
    denom=sum(exp(-delta*x) for x in Bs)
    rhoC=1/denom
    rhoD=rhoC*exp(-delta*Bs[-1])
    return rhoC,rhoD

def floating_cases():
    global CHECKS
    for N in (3,4,5,8,12):
        for g in range(2,N):
            for sel in (0.03,0.2,1.0):
                c=Q(2,3)
                R=[Q(j+1,3) for j in range(1,g+1)]
                rC,rD=fixation(N,g,c,R,sel)
                S=float(cumulative_closed(N,g,c,R,N-1))
                f=1/(1+exp(-sel*S))
                ck(abs(rC/(rC+rD)-f)<1e-12,True)
                ck(0<rC+rD<1,True)
                # Independent reverse-trajectory formula for a defecting mutant:
                diffs=[float(delta_direct(N,g,c,R,i)) for i in range(1,N)]
                den_reverse=1.0
                cum_reverse=0.0
                for j in range(1,N):
                    cum_reverse -= diffs[N-1-j]
                    den_reverse += exp(-sel*cum_reverse)
                ck(abs(1/den_reverse-rD)<1e-11,True)
                for j in range(g-1):
                    RR=R.copy();RR[j]+=Q(1,2)
                    rc,rd=fixation(N,g,c,RR,sel)
                    ck(rc>rC and rd>rD,True)
                    ck(abs(rc/(rc+rd)-f)<1e-12,True)
                huge=[Q(10**7)]*(g-1)+R[-1:]
                rhi,dhi=fixation(N,g,c,huge,sel)
                ck(abs(rhi-f)<1e-8,True)
                ck(abs(dhi-(1-f))<1e-8,True)
    for N in (4,10,30,100,300,1000):
        g=2;c=Q(1)
        final=Q(2*(N-1),N-2)
        z=[Q(0),final]
        rhoC,rhoD=fixation(N,g,c,z,0.4)
        ck(abs(rhoC-rhoD)<1e-12,True)
        # compare stable log Gaussian sum rather than underflow-sensitive raw series
        h=(N-1)/2
        zstar=.4*(N-1)**2/(4*(N-2))
        terms=sum(exp(-.4*(k-h)**2/(N-2)) for k in range(N))
        denom=exp(zstar)*terms
        ck(abs(rhoC-1/denom)/rhoC<1e-9,True)
    for N in (40,80,160,320,640,1000):
        c=1.;s=.4
        final=Q(2*(N-1),N-2)
        r,_=fixation(N,2,Q(1),[Q(0),final],s)
        approximate=sqrt(s/(pi*N))*exp(-s*N/4)
        ck(abs(r/approximate-1)<0.12,True)
    for g in (3,4,5,6):
        for N in (g+1, g+5, 30, 80, 150, 400):
            if N <= g: continue
            eps=Q(1);c=Q(1)
            q=Q(N-g,g*(N-1))
            R=[eps]*(g-1)+[Q(1,q)]
            v=1-eps*q
            def fall(x,m):
                p=1
                for z in range(m): p*=x-z
                return p
            for k in range(N):
                target= -c*v*(k-Q(fall(k,g),fall(N-2,g-1)))
                ck(cumulative_closed(N,g,c,R,k), target)
            if N>=30:
                weights=[float(-cumulative_closed(N,g,c,R,k))*.4 for k in range(N)]
                mx=max(weights)
                loggap=log(2)-mx-log(sum(exp(z-mx) for z in weights))
                kappa=(1-1/g)*g**(-1/(g-1))
                asymp= -.4*(1-1/g)*kappa
                ck(abs(loggap/N-asymp)<0.07, True)
    print('all checks passed:',CHECKS)

if __name__=='__main__':
    exact_cases()
    floating_cases()
