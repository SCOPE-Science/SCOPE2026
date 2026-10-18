"""Finite diagnostics for an optimal logistic-network diameter comparison.

Run with Python 3; only its standard library is needed. Analytic arguments
in RESULT.md establish the theorem. Sampling does not constitute a proof.
"""
import math
import random


def logistic(z):
    if z >= 0:
        return 1.0 / (1.0 + math.exp(-z))
    w = math.exp(z)
    return w / (1.0 + w)


def dobrushin(W):
    return max(sum(abs(a-b) for a,b in zip(W[i],W[j])) / 2
               for i in range(len(W)) for j in range(len(W)))


def rhs_components(W, x, beta, H):
    return [-xx + logistic(H + beta * sum(w*v for w,v in zip(row,x)))
            for xx,row in zip(x,W)]


def rk4_step(f, t, x, h):
    a = f(t,x)
    b = f(t+h/2,x+h*a/2)
    c = f(t+h/2,x+h*b/2)
    d = f(t+h,x+h*c)
    return x + h*(a+2*b+2*c+d)/6


def root_bisection(f, lo, hi, repeats=80):
    assert f(lo)>0 and f(hi)<0
    for _ in range(repeats):
        mid=(lo+hi)/2
        if f(mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2


def check():
    rand = random.Random(20260905)
    tested = 0
    for n in range(2, 10):
        for case in range(500):
            W = []
            for _ in range(n):
                weights = [rand.expovariate(1.0) for _ in range(n)]
                W.append([z/sum(weights) for z in weights])
            x = [rand.random() for _ in range(n)]
            beta = 25.0 * rand.random()
            H = 12.0 * rand.random() - 6.0
            d = dobrushin(W)
            R = max(x)-min(x)
            velocities = rhs_components(W, x, beta, H)
            max_i = [i for i in range(n) if x[i]==max(x)]
            min_i = [j for j in range(n) if x[j]==min(x)]
            actual = max(velocities[i]-velocities[j]
                         for i in max_i for j in min_i)
            envelope = -R + math.tanh(beta*d*R/4)
            assert actual<=envelope+4e-14,(n,case,actual,envelope)
            tested += 1

    exact=0
    for _ in range(1500):
        d=rand.random()
        beta=25*rand.random()
        R=rand.random()
        W=[[(1+d)/2,(1-d)/2],[(1-d)/2,(1+d)/2]]
        x=[(1+R)/2,(1-R)/2]
        f=rhs_components(W,x,beta,-beta/2)
        lhs=f[0]-f[1]
        rhs=-R+math.tanh(beta*d*R/4)
        assert abs(lhs-rhs)<2e-14
        exact+=1

    critical=[]
    for initial in [0.1,0.4,0.8]:
        R=initial
        table=[]
        for k in range(1,100001):
            R=rk4_step(lambda t,r:-r+math.tanh(r), k-1, R, 1.0)
            if k in (10000,30000,100000):table.append((k,k*R*R))
        assert abs(table[-1][1]-1.5)<0.02,table
        critical.append((initial,table))

    roots=[]
    for a in [1.01,1.2,2.0,5.0]:
        f=lambda r:-r+math.tanh(a*r)
        z=root_bisection(f,1e-8,1.0)
        assert 0<z<1 and -1+a*(1-z*z)<0
        roots.append((a,z))

    print('random Dini-envelope checks:',tested)
    print('two-node exact-saturation checks:',exact)
    print('critical t R(t)^2 diagnostics:',critical)
    print('supercritical asymmetric amplitudes:',roots)
    print('PASS; finite diagnostics are not a proof')


if __name__=='__main__':check()
