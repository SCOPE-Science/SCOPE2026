"""Deterministic finite reproducibility checks for coupon occupancy deficit profiles.

The analytical weak convergence proof is in RESULT.md; finite checks alone
cannot establish it.
"""
from __future__ import annotations
from collections import Counter
from itertools import product
from math import factorial, exp, log, isclose
import numpy as np
from scipy.special import gammaincc, gammainccinv
from scipy.stats import poisson, binom

TESTS = 0

def check(condition, label):
    global TESTS
    TESTS += 1
    if not condition:
        raise AssertionError(label)

def quantile(n, m):
    return float(gammainccinv(m, 1.0/n))

def direct_tail(m, u):
    return sum(exp(-u) * u**j / factorial(j) for j in range(m))

# Exact identity: the Gamma survival is the Poisson lower tail.
for m in range(1, 9):
    for u in (0.25, 0.8, 2.4, 6.3):
        check(isclose(direct_tail(m,u),float(gammaincc(m,u)),rel_tol=5e-12,abs_tol=1e-14),f'tail m={m} u={u}')

# Exact small-n multinomial joint law, checked by exhaustive sequences.
for n, N in ((3, 4), (3, 6), (4, 5), (4, 6), (5, 5)):
    table = Counter()
    for seq in product(range(n),repeat=N):
        a=seq.count(0); b=seq.count(1)
        table[a,b]+=1
    for a in range(N+1):
        for b in range(N+1-a):
            r=N-a-b
            exact=factorial(N)*((n-2)**r)/(factorial(a)*factorial(b)*factorial(r))
            check(table[a,b] == exact, f'multinomial n={n} N={N} a={a} b={b}')

# Gamma high quantile, conditional deficit mass and local-hazard checks.
for n, m in ((10_000,4),(100_000,10),(1_000_000,14),(1_000_000,100),
             (1_000_000,1000),(1_000_000,10000)):
    u=quantile(n,m)
    h=1-(m-1)/u
    check(u>m-1 and 0<h<=1, f'positive window n={n} m={m}')
    check(abs(float(gammaincc(m,u))*n-1)<2e-8, f'quantile n={n} m={m}')
    probs=np.asarray([poisson.pmf(m-j,u) for j in range(1,m+1)])
    conditional=probs/probs.sum()
    check(abs(conditional.sum()-1)<1e-10,'conditional normalization')
    for j in range(1,min(m,10)+1):
        exact_ratio = factorial(m-1)/factorial(m-j)/u**(j-1)
        check(isclose(probs[j-1]/probs[0],exact_ratio,rel_tol=5e-8),f'lower tail ratio m={m},j={j}')
    rate=poisson.pmf(m-1,u)/float(gammaincc(m,u))
    check(rate>0,'hazard positive')
    dx=min(.0001,.0001/h)
    finite_difference=-(log(float(gammaincc(m,u+dx)))-log(float(gammaincc(m,u-dx))))/(2*dx)
    check(abs(rate-finite_difference)<.0001, f'quantile hazard m={m}')
    # A finite-sample diagnostic, rather than a claimed asymptotic proof.
    test_lambda=u+0.5/h
    ratio=float(gammaincc(m,test_lambda)/gammaincc(m,u))
    check(.1<ratio<1, 'tail decreases')
    if m<=1000:
        p=np.array([poisson.pmf(m-j,u) for j in range(1,m+1)])
        check(abs(p.sum()-1/n)<1e-8, 'Poisson deficient mass')

# Formula for fixed-draw marginal and Poissonization closeness in the
# crossover regime m ~ alpha log n, where each rare bin receives O(log n).
for n in (1000,10000,100000,1000000):
    for alpha in (0.6,1.0,2.0):
        m=max(2,round(alpha*log(n)))
        u=quantile(n,m)
        h=1-(m-1)/u
        N=int(n*(u+0.4/h))
        for j in (1,2,3):
            if j>m: continue
            bp=binom.pmf(m-j,N,1/n)
            pp=poisson.pmf(m-j,N/n)
            check(abs(bp/pp-1)<.06, f'binomial/Poisson marginal n={n} m={m} j={j}')

print(f'PASS: {TESTS} deterministic assertions')
print('Illustrative asymptotic profile diagnostics (not a proof):')
for n,alpha in ((10**5,0.5),(10**7,1),(10**7,4),(10**7,30)):
    m=round(alpha*log(n));u=quantile(n,m);q=(m-1)/u
    print(f'n={n} m={m} alpha={alpha} u={u:.9f} q_n={q:.9f} h_n={1-q:.9f}')
