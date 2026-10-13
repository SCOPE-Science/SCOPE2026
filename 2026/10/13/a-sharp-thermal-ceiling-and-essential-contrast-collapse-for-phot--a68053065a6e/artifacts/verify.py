#!/usr/bin/env python3
"""Numerical cross-checks for finite multiplexed click statistics of photon-added thermal light.
This is a finite numerical corroboration, not an infinity proof.
"""
from math import comb, log, exp, sqrt

def pgf(m, b, z):
    return z**m / (1+b*(1-z))**(m+1)

def q_analytic(m, b, N, eta):
    h=eta/N
    a=pgf(m,b,1-h)
    bb=pgf(m,b,1-2*h)
    return (N-1)*(bb-a*a)/(a*(1-a))

def q_direct(m,b,N,eta):
    # Mix photon-added thermal probabilities into a direct photon-by-photon occupancy Markov chain.
    q=b/(1+b)
    pn=(1-q)**(m+1)
    cap=max(m+100, int(m+(m+2)*b+110*(1+b)))
    pm=[1.0]+[0.0]*N
    dist=[0.0]*(N+1)
    tail=0.0
    for k in range(cap+1):
        if k>=m:
            for j in range(N+1):
                dist[j]+=pn*pm[j]
            tail+=pn
            pn*=q*(k+1)/(k-m+1)
        if k<cap:
            nxt=[0.0]*(N+1)
            for j in range(N+1):
                nxt[j]+=pm[j]*(1-eta+eta*j/N)
                if j<N: nxt[j+1]+=pm[j]*eta*(N-j)/N
            pm=nxt
    assert abs(tail-1)<1e-11, (m,b,tail)
    mean=sum(j*dist[j] for j in range(N+1))
    var=sum((j-mean)**2*dist[j] for j in range(N+1))
    return N*var/(mean*(N-mean))-1

def cutoff(m,h):
    if h==0.5: return float('inf')
    A=log((1-h)**2/(1-2*h))
    r=m/(m+1)
    t=sqrt(-__import__('math').expm1(-r*A))
    return t/(h*(1-t))

def B(h,b):
    return log((1+b*h)**2/(1+2*b*h))
def A(h):
    return log((1-h)**2/(1-2*h))

def run():
    tests=0; err=0.0
    for N in (2,3,4,7):
        for m in (1,2,3,5):
            for b in (0,0.2,0.7,1.5,3.0):
                for eta in (0.25,0.7,1.0):
                    val=q_direct(m,b,N,eta)
                    exact=q_analytic(m,b,N,eta)
                    e=abs(val-exact)
                    err=max(err,e)
                    assert e<1e-9,(m,b,N,eta,val,exact,e)
                    tests+=1
    threshold_tests=0
    for N in (2,3,4,5,12):
      for eta in (0.14,0.5,0.9,1.0):
        h=eta/N
        for m in (1,2,3,5,10,30):
          bc=cutoff(m,h)
          assert bc > sqrt(m/(m+1)) or h==0.5
          if h<0.5:
            assert abs(B(h,bc)/A(h)-m/(m+1))<1e-8,(m,N,eta,bc)
            assert q_analytic(m,bc*0.5,N,eta)<0
            assert q_analytic(m,bc*1.5,N,eta)>0
            assert bc<1/(1-2*h)
          threshold_tests+=1
    for m in (1,2,5,20):
      vals=[cutoff(m,h) for h in (.01,.1,.2,.3,.4,.48,.499)]
      assert all(y>x for x,y in zip(vals,vals[1:])),(m,vals)
    for h in (0.01,0.1,0.3,0.49):
      vals=[cutoff(m,h) for m in (1,2,3,5,10,30,1000)]
      assert all(y>x for x,y in zip(vals,vals[1:])),(h,vals)
      assert abs(vals[-1]/(1/(1-2*h))-1)<0.001 if h<0.49 else vals[-1] <1/(1-2*h)
    # High-addition regime is evaluated in logarithms to avoid floating-point underflow.
    h=0.25; N=4; bc=1/(1-2*h)
    Ah=A(h); deriv=2*h*h*(1-2*h)/(1-h)
    kappa=Ah/deriv*log(1/(1-2*h))
    asymptotic=[]
    for eps in (0.05,0.02,0.01,0.005,0.002,0.001):
        b=bc-eps; delta=Ah-B(h,b); t=B(h,b)/delta
        lam=(1-h)/(1+b*h); u=1/(1+b*h)
        candidates=[]
        for m in range(max(1,int(t)+1),int(t)+32):
            y=delta*(m-t)
            log_D=log(N-1)+log(u)+m*log(lam)+log(-__import__('math').expm1(-y))-__import__('math').log1p(-u*lam**m)
            candidates.append((log_D,m))
        best,m=max(candidates)
        asymptotic.append(-eps*best)
    assert all(x>y for x,y in zip(asymptotic,asymptotic[1:])),asymptotic
    assert abs(asymptotic[-1]-kappa)<0.009,(asymptotic[-1],kappa)
    print(f'VERIFY_OK direct_click_distributions={tests} cutoffs={threshold_tests} monotonicity_grids=8 asymptotic_grids={len(asymptotic)} kappa={kappa:.12f} scaled_001={asymptotic[-1]:.12f} max_abs_error={err:.3g}')
if __name__=='__main__': run()
