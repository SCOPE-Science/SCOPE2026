"""Independent finite checks for the even-ring capture-time identities.

Requires numpy and scipy. Run: python check_even_flux.py
These finite tests are not a substitute for the all-size trigonometric proof.
"""
from math import pi, sin, cos, atan, sqrt
import numpy as np
from scipy.linalg import solve_continuous_lyapunov
from scipy.optimize import minimize_scalar


def formula(n, J, kappa, phi):
    assert n >= 4 and n % 2 == 0 and J > 0 and kappa > 0
    m = n // 2
    a = (m*m-1)/3
    b = m*m
    return n/kappa + kappa/(32*J*J)*(a/sin(phi/2)**2+b/cos(phi/2)**2)


def optimum(n, J=1):
    m = n // 2
    a = (m*m-1)/3
    b = m*m
    phi = 2*atan((a/b)**0.25)
    kappa = sqrt(32*n)*J/(sqrt(a)+sqrt(b))
    t = sqrt(n/8)*(sqrt(a)+sqrt(b))/J
    return phi, kappa, t


def spectral_sum(n, J, phi):
    e = [2*J*cos((2*pi*k+phi)/n) for k in range(n)]
    return sum(1/(e[j]-e[k])**2 for j in range(n) for k in range(j+1, n))


def analytic_sum(n, J, phi):
    m = n//2
    a = (m*m-1)/3
    b = m*m
    return m*m/(16*J*J)*(a/sin(phi/2)**2+b/cos(phi/2)**2)


def lyapunov_time(n, J, kappa, phi):
    H = np.zeros((n,n), dtype=complex)
    for j in range(n):
        H[(j+1)%n,j] += J*np.exp(1j*phi/n)
        H[j,(j+1)%n] += J*np.exp(-1j*phi/n)
    A = -1j*H
    A[0,0] -= kappa/2
    X = solve_continuous_lyapunov(A,-np.eye(n)/n)
    assert np.max(np.abs(A@X+X@A.conj().T+np.eye(n)/n)) < 1e-9
    return float(np.trace(X).real)


def main():
    spectral_checks=0
    dynamical_checks=0
    optimizer_checks=0
    boundary_checks=0
    for n in range(4, 31, 2):
        for J in [0.7, 1.3]:
            for phi in [0.13, 0.47, 1.12, pi/2, 2.36, 2*pi-0.47]:
                s = spectral_sum(n, J, phi)
                a = analytic_sum(n, J, phi)
                assert abs(s-a) < 2e-7*max(1,abs(a)), (n,J,phi,s,a)
                spectral_checks += 1
        phi, kappa, t = optimum(n,1.3)
        assert abs(formula(n,1.3,kappa,phi)-t) < 3e-11*max(1,t)
        assert phi < pi/2
        res = minimize_scalar(lambda x: formula(n,1.3,kappa,x),bounds=(0.1,pi-0.1),method='bounded', options={'xatol':1e-12})
        assert abs(res.x-phi) < 5e-7,(n,res.x,phi)
        assert formula(n,1.3,kappa,phi) < formula(n,1.3,kappa,pi/2)
        optimizer_checks += 1
        for flux, rank in [(0,n//2+1),(pi,n//2)]:
            e = 2*np.cos((2*pi*np.arange(n)+flux)/n)
            vals=[]
            for v in e:
                if not any(abs(v-w)<1e-9 for w in vals): vals.append(v)
            assert len(vals)==rank,(n,flux,len(vals),rank)
            boundary_checks+=1
    for n in range(4, 13, 2):
        for J in [0.75,1.3]:
            for phi in [0.19,0.55,1.15,pi/2,2.2]:
                for kappa in [0.31,1.7,4.2]:
                    numeric=lyapunov_time(n,J,kappa,phi)
                    predicted=formula(n,J,kappa,phi)
                    assert abs(numeric-predicted)<2e-8*max(1,abs(predicted)),(n,J,phi,kappa,numeric,predicted)
                    dynamical_checks+=1
    print('PASS: direct spectral-gap sums:',spectral_checks)
    print('PASS: independent complex Lyapunov evolution checks:',dynamical_checks)
    print('PASS: flux/loss optimizer checks:',optimizer_checks)
    print('PASS: exceptional-flux distinct-energy counts:',boundary_checks)
    print('ALL CHECKS PASSED')

if __name__=='__main__':
    main()
