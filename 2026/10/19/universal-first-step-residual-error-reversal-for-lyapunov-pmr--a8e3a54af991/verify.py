#!/usr/bin/env python3
"""Exact-rational consistency checks for one-step Lyapunov projection formulas.

Requires Python 3.10+ standard library only. Finite tests corroborate the proof;
they are not certificates for the universal statements.
"""
from fractions import Fraction as F
from math import sqrt

checks = 0

def ensure(predicate, msg):
    global checks
    if not predicate:
        raise AssertionError(msg)
    checks += 1


def quantities(eigenvalues, weights):
    lam = list(map(F, eigenvalues))
    w = list(map(F, weights))
    ensure(sum(w) == 1, 'weights')
    ensure(all(x > 0 for x in lam), 'eigenvalues')
    ensure(all(x >= 0 for x in w), 'nonnegative weights')
    a = sum(x*p for x, p in zip(lam,w))
    b2 = sum(x*x*p for x,p in zip(lam,w)) - a*a
    g = 1/(2*a)
    m = a/(2*a*a+b2)
    p = a/(2*(a*a+b2))
    mu = sum(w[i]*w[j]/(lam[i]+lam[j])
             for i in range(len(lam)) for j in range(len(lam)))
    normX2 = sum(w[i]*w[j]/(lam[i]+lam[j])**2
                 for i in range(len(lam)) for j in range(len(lam)))

    def err2(y):
        return normX2 - 2*y*mu + y*y

    def res2(y):
        return (1-2*a*y)**2 + 2*b2*y*y

    return a,b2,g,m,p,mu,err2,res2


def run_general():
    for n in range(2,8):
        for seed in range(1,23):
            eig = [F(1+(11*i+7*seed+i*seed)%23) for i in range(n)]
            nums = [1+((i+3)*(seed+5))%13 for i in range(n)]
            s = sum(nums)
            w = [F(k,s) for k in nums]
            a,b2,g,m,p,mu,e,r = quantities(eig,w)
            ensure(b2 >= 0, 'variance')
            ensure(e(g)>=0 and e(m)>=0 and e(p)>=0, 'nonnegative errors')
            if b2 == 0:
                ensure(g==m==p and g==mu, 'eigenvector equality')
            else:
                ensure(0 < p < m < g < mu, 'strict coefficients/Jensen')
                ensure(e(g) < e(m) < e(p), 'strict error reversal')
                ensure(r(m) < r(p) < r(g), 'strict residual ordering')
                ensure(r(g)==b2/(2*a*a), 'Galerkin residual')
                ensure(r(m)==b2/(2*a*a+b2), 'minimal residual')
                ensure(r(p)==b2*(a*a+2*b2)/(2*(a*a+b2)**2), 'PMR residual')


def run_family():
    for k in range(2,251):
        w = [F(k*k,k*k+1),F(1,k*k+1)]
        a,b2,g,m,p,mu,e,r = quantities([1,k],w)
        ensure(a==F(k*k+k,k*k+1), 'family Rayleigh quotient')
        ensure(b2==F(k*k*(k-1)**2,(k*k+1)**2), 'family variance')
        ensure(g==F(k*k+1,2*k*(k+1)), 'family Galerkin coefficient')
        ensure(p==F(k+1,4*k), 'family PMR coefficient')
        ensure(e(g) < e(m) < e(p), 'family error')
        ensure(r(m)<r(p)<r(g), 'family residual')
    for k in [100,1000,10000]:
        _,_,g,m,p,mu,e,r=quantities([1,k],[F(k*k,k*k+1),F(1,k*k+1)])
        ensure(abs(float(e(g)*k*k)-.75) < 5/k, 'Galerkin error asymptotic')
        ensure(abs(float(e(p))-.0625) < .2/k, 'PMR error limit')
        ensure(abs(float(e(m))-F(1,36)) < .2/k, 'MR error limit')
        ensure(abs(float(r(g))-.5) < 3/k, 'Galerkin residual limit')
        ensure(abs(float(r(p))-.375) < 3/k, 'PMR residual limit')
        ensure(abs(float(r(m))-F(1,3)) < 3/k, 'MR residual limit')
    k=100
    _,_,g,m,p,mu,e,r=quantities([1,k],[F(k*k,k*k+1),F(1,k*k+1)])
    ensure(e(p)>400*e(g), 'unbounded ratio witness (>20 at k=100)')
    ensure(e(m)>100*e(g), 'MR also diverges relative to G')

if __name__ == '__main__':
    run_general()
    run_family()
    print(f'PASS: {checks} deterministic exact-rational assertions')
