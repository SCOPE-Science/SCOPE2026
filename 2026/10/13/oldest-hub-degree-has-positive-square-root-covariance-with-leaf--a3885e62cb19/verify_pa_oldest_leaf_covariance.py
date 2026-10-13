#!/usr/bin/env python3
from fractions import Fraction
from collections import defaultdict
import math

def q_exact(n):
    q=Fraction(1)
    for r in range(1,n-1):
        q*=Fraction(2*r-1,2*r)
    return q

def d_exact(n):
    return (2*n-3)*q_exact(n)

def ell_exact(n):
    return Fraction(2*(n-1),3)+Fraction(4,3)*q_exact(n)

def delta_exact(n):
    q=q_exact(n)
    m=n-1
    return q*Fraction(m*(m-2),3*m*m) + q*q*Fraction(2*m-1,3*m*m)

def cov_exact(n):
    c=Fraction(0)
    for k in range(2,n):
        c+=delta_exact(k)
    return c

def state_laws(nmax=9):
    states={(1,1):Fraction(1)}
    out={}
    for n in range(2,nmax+1):
        ED=EL=EDL=QR=Fraction(0)
        for deg,p in states.items():
            D=deg[0]
            L=sum(d==1 for d in deg)
            ED+=p*D
            EL+=p*L
            EDL+=p*D*L
            QR+=p*(D==1)
        out[n]=(ED,EL,EDL,QR,len(states))
        if n==nmax:
            break
        nxt=defaultdict(Fraction)
        total=2*(n-1)
        for deg,p in states.items():
            for i,d in enumerate(deg):
                nd=list(deg)
                nd[i]+=1
                nd.append(1)
                nxt[tuple(nd)]+=p*Fraction(d,total)
        states=nxt
    return out

def large_cov(n):
    q=1.0
    c=0.0
    for k in range(2,n):
        if k>2:
            # q_k from q_{k-1}; q at loop entry is q_k after previous update below
            pass
        m=k-1
        c += q/(3*m*m)*(m*(m-2)+(2*m-1)*q)
        q *= (1.0-1.0/(2*m))
    return c

def run():
    laws=state_laws(9)
    state_checks=moment_checks=increment_checks=sign_checks=0
    for n,(ED,EL,EDL,QR,ns) in laws.items():
        assert QR==q_exact(n)
        assert ED==d_exact(n)
        assert EL==ell_exact(n)
        cov=EDL-ED*EL
        assert cov==cov_exact(n)
        moment_checks+=4
        state_checks+=ns
        if n<9:
            assert cov_exact(n+1)-cov_exact(n)==delta_exact(n)
            increment_checks+=1
        if n>=4:
            assert cov>0
            sign_checks+=1
    for n in (1000,10000,100000):
        ratio=large_cov(n)/math.sqrt(n)
        target=2/(3*math.sqrt(math.pi))
        assert abs(ratio-target)<0.03
    print(
        "VERIFY_OK "
        f"aggregated_states_checked={state_checks} "
        f"moment_checks={moment_checks} "
        f"increment_checks={increment_checks} "
        f"positive_covariance_checks={sign_checks} "
        "asymptotic_ratio_checks=3"
    )

if __name__=="__main__":
    run()
