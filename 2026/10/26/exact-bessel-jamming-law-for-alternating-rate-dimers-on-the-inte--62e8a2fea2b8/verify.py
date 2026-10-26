"""Independent checks for two-period irreversible dimer adsorption on the integer chain.
Requires Python 3, scipy, mpmath; no external data.
"""
from fractions import Fraction
from itertools import permutations
from math import exp
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import hyp0f1
import mpmath as mp


def vacancy_exact(alpha, beta):
    nu = alpha/(alpha+beta)
    mu = beta/(alpha+beta)
    h = nu*mu
    return float((h/(2+h))*hyp0f1(nu+2,h)*hyp0f1(mu+2,h))


def cavity_solution(alpha, beta, time):
    nu = mp.mpf(alpha)/(alpha+beta)
    mu = 1-nu
    x = 2*mp.sqrt(nu*mu)
    z = x*mp.exp(-(alpha+beta)*time/2)
    def component(a):
        return x*(z/x)**a*(mp.besselk(a+1,x)*mp.besseli(a,z)+mp.besseli(a+1,x)*mp.besselk(a,z))
    return float(component(nu)),float(component(mu))


def exact_first_edge_path(n, a, b, use_fraction=False):
    rates = [Fraction(a) if use_fraction else float(a), Fraction(b) if use_fraction else float(b)]
    f = [[Fraction(0),Fraction(0)] if use_fraction else [0.0,0.0] for _ in range(n+1)]
    for k in range(2,n+1):
        for s in (0,1):
            den = sum(rates[(s+i)%2] for i in range(k-1))
            num = 0
            for i in range(k-1):
                lam = rates[(s+i)%2]
                num += lam*(1+f[i][s]+f[k-i-2][(s+i)%2])
            f[k][s] = num/den
    return f[n][0]


def explicit_priority_path(n, a, b):
    rates = [Fraction(a) if i%2==0 else Fraction(b) for i in range(n-1)]
    result = Fraction(0)
    for order in permutations(range(n-1)):
        rem = sum(rates)
        pr = Fraction(1)
        occupied = [False]*n
        accepted = 0
        for i in order:
            pr *= rates[i]/rem
            rem -= rates[i]
            if not occupied[i] and not occupied[i+1]:
                occupied[i]=occupied[i+1]=True
                accepted+=1
        result += pr*accepted
    return result


def check():
    mp.mp.dps=40
    # Independently enumerate all edge-arrival orders; two-rate exact first-edge recursion.
    for n in range(2,8):
        for a,b in [(1,1),(1,2),(3,1)]:
            assert exact_first_edge_path(n,a,b,True)==explicit_priority_path(n,a,b),(n,a,b)
    print('Exact finite-path check: 18 independent exhaustive rational priority enumerations PASS')

    # Numerically integrate two independent half-line cavity equations.
    for a,b in [(1.,1.),(1.,2.),(2.,1.),(4.,1.),(1.,0.2),(0.2,1.)]:
        tmax=max(50/min(a,b),50)
        sol=solve_ivp(lambda t,y:(-a*np.exp(-a*t)*y[1],-b*np.exp(-b*t)*y[0]),(0,tmax),(1.,1.),rtol=2e-12,atol=1e-14)
        pred=vacancy_exact(a,b)
        assert abs(sol.y[0,-1]*sol.y[1,-1]-pred)<2e-10,(a,b,pred,sol.y[:,-1])
        for t in (0.1,1.,3.):
            y=solve_ivp(lambda t,x:(-a*np.exp(-a*t)*x[1],-b*np.exp(-b*t)*x[0]),(0,t),(1.,1.),rtol=3e-12,atol=1e-14).y[:,-1]
            exact=cavity_solution(a,b,t)
            assert np.max(np.abs(y-np.array(exact)))<2e-10,(a,b,t,y,exact)
    print('Cavity integration and independently evaluated Bessel solution: 24 comparisons PASS')

    # Compare thermodynamic formula with entirely distinct finite-interval recursion.
    # Boundary discrepancy is O(1/n), not a finite-size identity.
    for a,b in [(1,1),(1,2),(2,1),(1,4),(4,1)]:
        pred=vacancy_exact(a,b)
        old=None
        for n in (128,256,512):
            p=1.-2.*exact_first_edge_path(n,a,b)/n
            assert abs(p-pred)<1.5/n,(a,b,n,p,pred)
            if old is not None:
                assert abs(p-pred)<abs(old-pred),(a,b,n)
            old=p
    print('Thermodynamic jamming law: 15 independent finite-path recursion tests PASS')

    # Exactly solvable symmetric benchmark and weak-minority asymptotics.
    assert abs(vacancy_exact(1,1)-exp(-2))<3e-15
    for eps in (0.01,0.001,0.0001):
        p=vacancy_exact(1,eps)
        approx=eps/2-5*eps*eps/6
        assert abs(p-approx)<2*eps**3
    print('Homogeneous benchmark and second-order weak-minority asymptotic: 4 tests PASS')

if __name__=='__main__': check()
