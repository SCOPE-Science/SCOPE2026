"""Reproduce independent numerical and special-function checks of the stated theorem."""
import math
import numpy as np


def qstar(m, d, beta):
    return min(m*d, d+beta)


def exact_second_one_step(m, d, sigma, b):
    if m*d <= 2:
        return math.inf
    return sum(t*t for t in b)/(sigma*sigma*(m*d-2))


def exact_q_one_step_centered(m, d, sigma, b, q):
    if not 0 < q < qstar(m, d, 2):
        return math.inf
    # Log-gamma prevents overflow for all tested dimensions.
    logcoef = (-q/2)*math.log(2*sigma*sigma)
    logcoef += math.lgamma((m*d-q)/2)+math.lgamma((d+2-q)/2)
    logcoef -= math.lgamma(d/2)+math.lgamma((m*d+2-q)/2)
    return math.exp(logcoef)*sum(abs(t)**q for t in b)


def simulate(m, d, b, sigma, n_paths=35000, n_steps=10, seed=20261025):
    rng = np.random.default_rng(seed)
    x = np.zeros((n_paths,d), dtype=float)
    out=[]
    for _ in range(n_steps):
        a=rng.normal(0,sigma,(n_paths,m,d))
        r2=np.sum(a*a,axis=2)
        u=rng.random(n_paths)*np.sum(r2,axis=1)
        sel=np.sum(np.cumsum(r2,axis=1)<u[:,None],axis=1)
        sel=np.minimum(sel,m-1)
        aa=a[np.arange(n_paths),sel]
        bb=np.asarray(b)[sel]
        gain=(bb-np.sum(aa*x,axis=1))/np.sum(aa*aa,axis=1)
        x=x+gain[:,None]*aa
        out.append(float(np.mean(np.sum(x*x,axis=1))))
    return out


def main():
    for m,d in [(1,3),(2,2),(3,1),(5,1),(2,4),(4,3),(6,3),(8,5)]:
        b=[1.0]+[0.0]*(m-1)
        for sigma in (0.5,1.0,2.0):
            expected=exact_second_one_step(m,d,sigma,b)
            actual=exact_q_one_step_centered(m,d,sigma,b,2)
            assert math.isclose(expected,actual,rel_tol=2e-13), (m,d,sigma,expected,actual)
    assert qstar(3,1,2)==3
    assert qstar(2,1,2)==2
    assert qstar(4,1,0)==1
    assert qstar(4,1,2)==3
    assert qstar(2,2,2)==4
    assert qstar(6,3,2)==5
    assert math.isinf(exact_q_one_step_centered(3,1,1,[1,0,0],3))
    assert math.isinf(exact_second_one_step(2,1,1,[1,0]))
    m,d,sigma=6,3,1.
    b=[1.,2.,0.,0.,0.,0.]
    theoretical=exact_second_one_step(m,d,sigma,b)
    expected_limit=d*theoretical
    observed=simulate(m,d,b,sigma)
    rho=1-1/d
    for k in (1,2,4,10):
        benchmark=expected_limit*(1-rho**k)
        assert abs(observed[k-1]-benchmark)<0.075, (k,observed[k-1],benchmark)
    assert abs(observed[-1]-expected_limit)<0.075
    # q=1 gamma moment independently compared to actual single-step sampling.
    benchmark_q1=exact_q_one_step_centered(m,d,sigma,b,1)
    rng=np.random.default_rng(4560)
    n=140000
    a=rng.normal(0,1,(n,m,d))
    r2=(a*a).sum(axis=2)
    choice=np.sum(np.cumsum(r2,axis=1)<rng.random(n)[:,None]*r2.sum(axis=1)[:,None],axis=1)
    choice=np.minimum(choice,m-1)
    one=np.mean(np.abs(np.asarray(b)[choice])/np.sqrt(r2[np.arange(n),choice]))
    assert abs(one-benchmark_q1)<0.025, (one,benchmark_q1)
    print('VERIFY_OK: centered gamma/Dirichlet q=2 identities in 24 parameter regimes; exact critical-boundary cases; independent numerical one-step and 10-step second moments; q=1 formula.')
    print('case m=6,d=3: first-step MSE',theoretical,'stationary MSE',expected_limit,'observed 10-step MSE',observed[-1])
    print('q=1 one-step theoretical',benchmark_q1,'Monte Carlo',one)

if __name__=='__main__':
    main()
