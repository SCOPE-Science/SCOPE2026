"""Reproducibility checks for a balanced alternating-star temporal SIS model.
Run: python verify.py (numpy and scipy required).
Finite tests support, but do not replace, the mathematical proof.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


def adjacency(m, phase):
    n = 2*m+1
    out = np.zeros((n,n), dtype=float)
    group = range(1, m+1) if phase == 0 else range(m+1, 2*m+1)
    for j in group: out[0,j] = out[j,0] = 1.0
    return out


def rho_formula(m, beta, delta, T):
    r = beta*math.sqrt(m)*T
    h = math.acosh((1.0 + math.cosh(r))/2.0)
    return math.exp(2.0*(h-delta*T))


def rhs(A, beta, delta):
    return lambda _, x: -delta*x+beta*(1-x)*(A@x)


def cycle(x, A0, A1, beta, delta, T):
    for A in (A0,A1):
        sol = solve_ivp(rhs(A,beta,delta), (0,T), x, rtol=2e-11, atol=2e-13)
        assert sol.success
        x = sol.y[:,-1]
    return x


def main():
    count = 0
    for m in (1,2,3,4,5,7):
        A0,A1 = adjacency(m,0),adjacency(m,1)
        assert np.array_equal(A0,A0.T) and np.array_equal(A1,A1.T)
        assert np.all(np.diag(A0)==0) and np.all(np.diag(A1)==0)
        for beta in (0.35, 0.7, 1.3):
            for T in (0.12, 0.43, 1.15, 2.65):
                delta=0.81*beta*math.sqrt(m)
                M = expm((beta*A1-delta*np.eye(2*m+1))*T)@expm((beta*A0-delta*np.eye(2*m+1))*T)
                eig = np.linalg.eigvals(M)
                rho = max(abs(eig))
                expected = rho_formula(m,beta,delta,T)
                assert abs(rho-expected) < 2.e-9*max(1.0,expected), (m,beta,T,rho,expected)
                count += 1

    # Analytic transition; average contact map incorrectly predicts extinction.
    m,beta,delta = 1,1.0,0.8
    f=lambda T: math.acosh((1+math.cosh(T))/2) - delta*T
    Tstar=brentq(f,2.0,4.0,xtol=1e-13)
    assert abs(Tstar-3.03490842766049)<2e-11
    assert beta*math.sqrt(m/2)<delta<beta*math.sqrt(m)
    assert rho_formula(m,beta,delta,2.0)<1.0
    assert rho_formula(m,beta,delta,4.0)>1.0

    # Full nonlinear dynamics above threshold and exact phase-locked switch ratio.
    for m in (1,2,3):
        beta=1.0
        delta=0.8*math.sqrt(m)
        T=4.0/math.sqrt(m)
        A0,A1=adjacency(m,0),adjacency(m,1)
        x = np.full(2*m+1,0.65)
        for _ in range(180): x=cycle(x,A0,A1,beta,delta,T)
        assert min(x)>0.0001, (m,x)
        assert np.linalg.norm(cycle(x,A0,A1,beta,delta,T)-x,np.inf)<1e-8
        half = solve_ivp(rhs(A0,beta,delta),(0,T),x,rtol=2e-11,atol=2e-13).y[:,-1]
        group1=float(np.mean(x[1:m+1]))
        group2=float(np.mean(x[m+1:]))
        assert abs(group2/group1-math.exp(delta*T))<3e-7, (m,group1,group2)
        assert abs(half[0]-x[0])<3e-8
        assert np.max(abs(half[1:m+1]-x[m+1:]))<3e-8
        assert np.max(abs(half[m+1:]-x[1:m+1]))<3e-8
        print(f'm={m}, endemic first-leaf={group1:.10f}, other-leaf={group2:.10f}, switch ratio={group2/group1:.10f}')

    print(f'PASS {count} full-matrix spectral comparisons; critical T={Tstar:.12f}; nonlinear phase identities PASS.')

if __name__=='__main__':main()
