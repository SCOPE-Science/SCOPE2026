#!/usr/bin/env python3
import math

def fwer_product(alpha, gammas):
    surv = 1.0
    for g in gammas:
        surv /= (1.0 + alpha*g)
    return 1.0 - surv

def fwer_recursion(alpha, gammas):
    reach = 1.0
    reject = 0.0
    for g in gammas:
        r = alpha*g/(1.0 + alpha*g)
        s = 1.0/(1.0 + alpha*g)
        reject += reach*r
        reach *= s
    return reject, reach

def main():
    for alpha in (0.05, 0.2, 0.7):
        for gammas in ([1.0], [0.5,0.5], [0.2,0.3,0.5], [0.1]*10):
            p = fwer_product(alpha, gammas)
            r, surv = fwer_recursion(alpha, gammas)
            assert abs(p-r) < 2e-15
            assert abs((1-p)-surv) < 2e-15
            assert p + 1e-15 >= alpha/(1+alpha)
            assert p < 1-math.exp(-alpha) + 1e-15
    alpha = 0.2
    target = 1.0 - math.sqrt(6*alpha)/math.sinh(math.sqrt(6*alpha))
    quoted = 0.17515476014878684
    assert abs(target-quoted) < 5e-16
    for n in (10, 100, 1000, 10000):
        gammas = [6.0/(math.pi**2*j*j) for j in range(1,n+1)]
        trunc = fwer_product(alpha, gammas)
        assert trunc < target
    gammas = [6.0/(math.pi**2*j*j) for j in range(1,200000)]
    trunc = fwer_product(alpha, gammas)
    assert 0.0 < target-trunc < 8e-7
    for n in (1,2,10,100,10000):
        diffuse = 1.0-(1.0+alpha/n)**(-n)
        assert diffuse >= alpha/(1+alpha)-1e-15
        assert diffuse < 1.0-math.exp(-alpha)+1e-15
    assert abs((1.0-(1.0+alpha/1000000)**(-1000000))-(1.0-math.exp(-alpha))) < 3e-8
    print('VERIFY_OK')
if __name__ == '__main__':
    main()
