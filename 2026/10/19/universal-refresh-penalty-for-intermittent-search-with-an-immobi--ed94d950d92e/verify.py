"""Finite-state independent checks for two-state intermittent search reset formulas.

Requires Python 3, NumPy and SciPy. Run: python active_reset_protocol_check.py
"""
import numpy as np
from scipy.linalg import solve


def active_generator(k, left, right):
    Q = np.zeros((k, k), dtype=float)
    loss = np.zeros(k, dtype=float)
    for j in range(k):
        d = left[j]
        Q[j,j] -= d
        if j > 0:
            Q[j,j-1] += d
        else:
            loss[j] = d
        if j+1 < k:
            u = right[j]
            Q[j,j] -= u
            Q[j,j+1] += u
    return Q, loss


def full_generator(Q, alpha, beta, r, eta, target):
    k=len(Q)
    G=np.zeros((2*k,2*k),dtype=float)
    G[k:, k:]=Q
    for j in range(k):
        G[j,k+j] += alpha
        G[j,j] -= alpha
        G[k+j,j] += beta
        G[k+j,k+j] -= beta
    s=alpha+beta
    pi0=beta/s
    pi1=alpha/s
    for j in range(k):
        for state in (0,1):
            origin=j+k*state
            targets=((target,r*((1-eta)*(state==0)+eta*pi0)),
                     (k+target,r*((1-eta)*(state==1)+eta*pi1)))
            for dest,rate in targets:
                G[origin,dest]+=rate
                G[origin,origin]-=rate
    return G


def verify():
    rng=np.random.default_rng(20261014)
    max_error=0.0
    number=0
    for k in (3,5,7):
        for scenario in range(16):
            left=np.exp(rng.uniform(-0.3,0.3,size=k))
            right=np.exp(rng.uniform(-0.3,0.3,size=k))
            Q,loss=active_generator(k,left,right)
            target=scenario%min(k,3)
            alpha=float(np.exp(rng.uniform(-.5,.5)))
            beta=float(np.exp(rng.uniform(-.5,.5)))
            r=float(np.exp(rng.uniform(-.5,.5)))
            s=alpha+beta
            q=r*(s+r)/(alpha+r)
            B=s/alpha
            F=solve(q*np.eye(k)-Q,loss)[target]
            assert 0<F<1
            active_time=B*(1/F-1)/q
            for eta in (0,.13,.37,.6,.93,1):
                G=full_generator(Q,alpha,beta,r,eta,target)
                mean=solve(-G,np.ones(2*k),assume_a='gen')
                on=mean[k+target]
                off=mean[target]
                predicted_off_on=s/(alpha*(s+r*eta))
                predicted_avg=active_time+beta/(alpha*(s+r*eta))
                predicted_on=active_time
                avg=(beta*off+alpha*on)/s
                for observed,predicted in ((on,predicted_on),
                                            (off-on,predicted_off_on),
                                            (avg,predicted_avg)):
                    error=abs(observed-predicted)
                    max_error=max(max_error,error)
                    assert error < 1e-8*max(1,abs(predicted)), (k,scenario,eta,error)
                    number+=1
    print(f'PASS {number} independent finite-generator comparisons; maximum absolute discrepancy {max_error:.4g}')


if __name__=='__main__':
    verify()
