#!/usr/bin/env python3
"""Standalone reproducibility checks for an exact classical XY ring criterion.
Uses only standard Python, NumPy and SciPy. Numerical tests are diagnostics, not proof.
"""
import math
import numpy as np
from scipy.optimize import minimize


def energy_from_independent(y, J):
    d = np.r_[y, np.pi - np.sum(y)]
    return float(np.sum(J * (1-np.cos(d))))


def criterion(J):
    idx = int(np.argmin(J))
    m = float(J[idx]); R = float(np.sum(1/np.delete(J,idx)))
    return m, R, idx


def spinwave_test(J):
    m, R, weak = criterion(J)
    weak_other=np.array([i for i in range(len(J)) if i!=weak])
    eps=1e-3
    d=np.zeros(len(J))
    d[weak_other]=eps/J[weak_other]
    d[weak]=np.pi-eps*R
    return np.sum(J*(1-np.cos(d))), 2*m


def numerical_min(J,rng,restarts=10):
    N=len(J)
    minima=[]
    guesses=[np.zeros(N-1)]
    for _ in range(restarts):guesses.append(rng.uniform(-np.pi,np.pi,size=N-1))
    for start in guesses:
        out=minimize(energy_from_independent,start,args=(J,),method='BFGS',
                     options={'gtol':1e-9, 'maxiter':1100})
        minima.append(float(out.fun))
    return min(minima)


def run():
    rng=np.random.default_rng(130721)
    checked=0; sharp=0; unstable=0
    for n in (3,5,7,9):
        for trial in range(24):
            J=np.exp(rng.uniform(-2,2,size=n))
            m,R,_=criterion(J)
            predicted=m*R<=1
            observed=numerical_min(J,rng,9)
            if predicted:
                assert observed >= 2*m-2e-7, (n,J,'false collinear',observed,2*m)
                assert abs(observed-2*m)<2e-6, (n,J,'not attained',observed,2*m)
            else:
                unstable+=1
                pert,baseline=spinwave_test(J)
                if baseline-pert>1e-10:
                    assert observed < baseline-1e-9 or abs(observed-pert)<2e-7,(n,J,'unstable')
                assert observed<=2*m+2e-7
            checked+=1
    for n in (3,5,7,9,11):
        for Jrest in (np.ones(n-1),rng.uniform(.7,2.5,size=n-1)):
            R=float(sum(1/Jrest)); thresh=1/R
            for s in (0.5,1.,1.5):
                J=np.r_[s*thresh,Jrest]
                m,R2,weak=criterion(J)
                assert weak==0 and abs(m*R2-s)<1e-11
                if s<=1:
                    assert abs(numerical_min(J,rng,8)-2*m)<2e-6
                else:
                    assert numerical_min(J,rng,12)<2*m-1e-6
                sharp+=1
    print('PASS',checked,'random weighted rings,',sharp,'at/below/above critical cases;',unstable,'random noncollinear phases')
if __name__=='__main__':run()
