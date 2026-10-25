"""Standalone numerical and exact combinatorial checks of hypergraphic width identities.

Run with: python width_checker.py
No simulation is used as a substitute for an asymptotic proof.
"""
from itertools import combinations
from functools import lru_cache
from math import comb, pi, sqrt, asin
import numpy as np
from scipy.integrate import quad
from scipy.special import ndtr


def binom(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def complete_width(values, k):
    z = np.sort(np.array(values, dtype=float))
    m = len(z)
    return sum(z[j]*(binom(j,k-1)-binom(m-j-1,k-1)) for j in range(m))


def star_width(hub, leaves, k):
    z = np.sort(np.array(leaves, dtype=float))
    n=len(z)
    b=int(np.searchsorted(z,hub,side='left'))
    return (hub*(binom(b,k-1)-binom(n-b,k-1))
           +sum(z[j]*binom(j,k-2) for j in range(b,n))
           -sum(z[j]*binom(n-1-j,k-2) for j in range(b)))


def range_value(values):
    return max(values)-min(values)


def Phi(z):
    return float(ndtr(z))


def Fprime(z,k):
    p=Phi(z)
    return p**(k-1)-(1-p)**(k-1)


@lru_cache(None)
def Fzero(k):
    return 2*quad(lambda t: 1-Phi(t)**(k-1),0,10,epsabs=1e-11)[0]


def F(z,k):
    v=abs(float(z))
    return Fzero(k)+quad(lambda t: Fprime(t,k),0,v,epsabs=1e-11)[0]


def mu(k):
    return 2*quad(lambda t:1-Phi(t)**k-(1-Phi(t))**k,0,10,epsabs=1e-11)[0]


def integrand(z,k,m):
    return np.exp(-z*z/2)/np.sqrt(2*pi)*F(z,k)**m


def constants(k):
    nodes,weights=np.polynomial.hermite.hermgauss(80)
    zz=nodes*sqrt(2)
    ff=np.array([F(z,k) for z in zz])
    ww=weights/sqrt(pi)
    first=float(np.dot(ww,ff))
    second=float(np.dot(ww,ff**2))
    v=second-first*first
    m=mu(k)
    tau2=k*k*v-m*m/2
    cov=float(np.dot(ww,ff*(zz**2-1)))
    return m,first,second,v,tau2,cov


def verify():
    rng=np.random.default_rng(20261020)
    tested=0
    for k in (4,5,6):
        for n in range(k,10):
            for _ in range(45):
                z=rng.standard_normal(n+1)
                direct_c=sum(range_value(z[list(T)]) for T in combinations(range(n+1),k))
                direct_s=sum(range_value([z[0]]+[z[i] for i in T]) for T in combinations(range(1,n+1),k-1))
                s=star_width(z[0],z[1:],k)
                c=complete_width(z,k)
                assert np.isclose(direct_c,c,rtol=1e-11,atol=1e-9),(k,n,direct_c,c)
                assert np.isclose(direct_s,s,rtol=1e-11,atol=1e-9),(k,n,direct_s,s)
                tested+=2
    print('EXACT_SUPPORT_OK',tested)
    for k in (4,5):
        m,first,second,var,tau2,cov=constants(k)
        assert abs(first-m)<5e-8
        assert abs(cov-m/k)<5e-8
        assert var>0 and tau2>0
        print('CONSTANTS',k,'mu',m,'Fzero',Fzero(k),'varF',var,'sphere_tau2',tau2,'cov',cov)
    mu4_expected=3/sqrt(pi)+(6/(pi*sqrt(pi)))*asin(1/3)
    assert abs(mu(4)-mu4_expected)<1e-9
    print('MU4_CLOSED_FORM_OK',mu4_expected)
    print('CHECKER_OK')

if __name__=='__main__':
    verify()

def simulate_directions(k=4, n=180, repetitions=4000, seed=9345):
    rng=np.random.default_rng(seed)
    complete=[];star=[]
    for _ in range(repetitions):
        z=rng.standard_normal(n+1)
        centered=z-z.mean()
        factor=sqrt(n)/np.linalg.norm(centered)
        complete.append(factor*complete_width(z,k)/comb(n+1,k))
        star.append(factor*star_width(z[0],z[1:],k)/comb(n,k-1))
    v=np.array(complete); s=np.array(star)
    print('DIRECTIONAL_TEST',k,'dimension',n,'draws',repetitions,
          'complete_mean',np.mean(v),'complete_CLT_variance',n*np.var(v),
          'star_mean',np.mean(s),'star_variance',np.var(s))

if __name__ == '__main__':
    simulate_directions()
