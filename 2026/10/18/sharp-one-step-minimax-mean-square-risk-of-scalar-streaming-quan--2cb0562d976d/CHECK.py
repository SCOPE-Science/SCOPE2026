"""Reproduce exact scalar quantile-Kaczmarz worst-case risks and tail law.

Python 3 standard library only. This checks finite instances, not the infinite theorem.
"""
from itertools import product
from math import comb, exp, log, sqrt


def tail(n, p, j):
    if j <= 0:
        return 1.0
    if j > n:
        return 0.0
    return sum(comb(n, i) * p**i * (1-p)**(n-i)
               for i in range(j, n+1))


def bound(D, beta, q, B):
    assert D >= 1 and 0 < beta < 1 and 0 < q < 1 and B >= 2
    k = max(1, int(q * D))
    return ((1-beta) * tail(D, beta, k)
            + 4*beta + beta*(B*B-4)*tail(D, beta, D-k+1))


def direct_extremum(D, k, J, B, update_corrupt):
    """Exhaust all endpoint and kink values of the corruption choices."""
    vals = (-B, 0, 1, 2, B)
    greatest = -1.0
    for z in product(vals, repeat=J):
        quantile = sorted([abs(1-v) for v in z] + [1]*(D-J))[k-1]
        for v in vals if update_corrupt else (0,):
            new_e = v if abs(1-v) <= quantile else 1
            greatest = max(greatest, new_e*new_e)
    return greatest


def full_enumerated_expectation(D, beta, q, B):
    k = max(1, int(q*D))
    risk = 0.0
    for J in range(D+1):
        weight = comb(D, J) * beta**J * (1-beta)**(D-J)
        worst_clean = direct_extremum(D, k, J, B, False)
        worst_bad = direct_extremum(D, k, J, B, True)
        assert worst_clean == (1 if J >= k else 0)
        assert worst_bad == (B*B if J > D-k else 4)
        risk += weight * ((1-beta)*worst_clean + beta*worst_bad)
    return risk


def kl(a, p):
    return a*log(a/p)+(1-a)*log((1-a)/(1-p))


def main():
    n=0
    for D in range(1, 7):
        for q in (0.21, 0.50, 0.80):
            for beta in (0.05, 0.20):
                for B in (2, 5):
                    r1 = bound(D, beta, q, B)
                    r2 = full_enumerated_expectation(D, beta, q, B)
                    assert abs(r1-r2)<1e-11, (D, beta, q, B, r1, r2)
                    n+=1
    print('Exact conditional extremizers and binomial averages:',n,'passed')
    for beta in (0.07, 0.2, 0.249):
        assert 4*beta < 1
        assert bound(1000,beta,0.50,3) < 1
    for beta in (0.25, 0.4):
        for D in (1,3,7,15,50):
            assert bound(D,beta,0.5,2) >= 1-1e-12
    print('Sharp quarter-corruption boundary: passed')
    beta, q = 0.1,0.5
    I=kl(1-q,beta)
    cvals=[]
    for D in (30,40,60,80,120):
        k=max(1,int(q*D))
        C=tail(D,beta,D-k+1)
        cvals.append(C*sqrt(D)*exp(D*I))
    assert min(cvals)>0.07 and max(cvals)<3, cvals
    print('Binomial lattice-tail normalization (finite check):',cvals)
    for B in (10,100,1000,10000,1000000):
        D=1
        while bound(D,beta,q,B)>=1:
            D+=1
        pred=(2*log(B)-0.5*log(log(B)))/I
        assert abs(D-pred)<20,(B,D,pred)
        print('Amplitude:',B,'minimum D:',D,'two-term center:',round(pred,3))
    print('ALL CHECKS PASSED')


if __name__ == '__main__':
    main()
