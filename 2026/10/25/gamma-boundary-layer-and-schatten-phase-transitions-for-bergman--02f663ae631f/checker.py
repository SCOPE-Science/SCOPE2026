#!/usr/bin/env python3
"""Independent numerical checks for weighted Bergman cutoff commutator formulas.
This code checks finite-dimensional identities and boundary asymptotic predictions;
it is not a proof of infinite-dimensional limit theorems.
"""
import math
import numpy as np
from scipy.special import gammaln, betainc, beta as beta_function
from scipy.integrate import quad

count = 0

def check(cond, msg):
    global count
    if not cond: raise AssertionError(msg)
    count += 1

def coeff(k,beta):
    return math.exp(gammaln(k+beta+1)-gammaln(beta)-gammaln(k+2)+0.5*(math.log(k+1)-math.log(k+beta+1)))

def spectrum(beta,eps,N):
    ks=np.arange(N,dtype=np.float64)
    lg=beta*math.log(eps)+(ks+1)*math.log1p(-eps) + gammaln(ks+beta+1)-gammaln(beta)-gammaln(ks+2)+0.5*np.log((ks+1)/(ks+beta+1))
    return np.exp(lg)

for beta in (0.25,0.7,1.,1.25,2.,3.5):
    for x in (0.14,0.47,0.83):
        a,b=beta,x
        for k in range(17):
            L=betainc(k+1,beta,x)
            L1=betainc(k+2,beta,x)
            delta=L-L1
            w=math.sqrt((k+1)/(k+beta+1))
            candidate=(1-x)**beta*x**(k+1)*coeff(k,beta)
            check(abs(delta*w-candidate)<4e-13, f'beta integral {beta} {x} {k}')
        # Matrix commutator in normalized monomial coordinates:
        N=13
        t=np.array([betainc(k+1,beta,x) for k in range(N)])
        shift=np.zeros((N,N))
        for k in range(N-1): shift[k+1,k]=math.sqrt((k+1)/(k+beta+1))
        diag=np.diag(t)
        comm=diag@shift-shift@diag
        observed=np.linalg.svd(comm,compute_uv=False)
        expected=np.r_[spectrum(beta,1-x,N-1),0]
        check(np.allclose(np.sort(observed),np.sort(expected),atol=1e-12,rtol=1e-12), f'matrix {beta} {x}')

# Asymptotics: numerical convergence with decreasing eps on both sides of critical lines.
for beta,p,eps in [(0.3,2,0.002),(0.5,2,0.001),(0.8,2,0.001),
                   (1,1,0.0005),(1.4,1,0.0008),(0.3,0.6,0.0008),
                   (1.5,3,0.001),(0.6,3,0.0008)]:
    sk=spectrum(beta,eps, int(math.ceil(42/eps)))
    observed=float(np.sum(sk**p))
    a=p*(beta-1)
    if a> -1:
        predicted=eps**(p-1)*math.gamma(a+1)/(p**(a+1)*math.gamma(beta)**p)
    elif abs(a+1)<1e-9:
        predicted=eps**(p-1)*math.log(1/eps)/math.gamma(beta)**p
    else:
        C=np.array([coeff(k,beta) for k in range(120000)])
        predicted=eps**(p*beta)*float(np.sum(C**p))
    print('ASYM',beta,p,eps,'ratio',round(observed/predicted,7));check(abs(observed/predicted-1)<0.5, f'Schatten {beta=} {p=} {eps=} {observed/predicted=}')

for beta,eps in [(0.25,0.0008),(0.85,0.0008),(1,0.0008),(1.3,0.0008),(3,0.0008)]:
    sk=spectrum(beta,eps,int(math.ceil(45/eps)))
    norm=float(np.max(sk))
    if beta<1:
        pred=eps**beta*max(coeff(k,beta) for k in range(20000))
    elif beta==1:
        pred=eps
    else:
        pred=eps*(beta-1)**(beta-1)*math.exp(-(beta-1))/math.gamma(beta)
    print('OP',beta,eps,'ratio',round(norm/pred,7));check(abs(norm/pred-1)<0.08,f'opnorm {beta} {norm/pred}')
    print('TRACE',beta,eps,'mass',round(sum(sk),7));check(abs(sum(sk)-1)<0.23, f'trace escape {beta} {sum(sk)}')

# Exact unweighted modal threshold of the successive-weight ratio.
for eps in (0.2,0.04,0.003,0.0007):
    sk=spectrum(1,eps,int(math.ceil(8/eps)))
    k=int(np.argmax(sk))
    K=(2*eps-eps*eps)**(-0.5)
    check(abs((k+2)-K)<2.1, f'critical mode {eps} {k} {K}')
# Separate quadrature check, not using the special-function CDF evaluator.
for beta in (0.25, 1., 1.7):
    for x in (0.19, 0.63):
        for k in range(6):
            I = quad(lambda t: t**k * (1-t)**(beta-1), 0, x, epsabs=2e-13)[0]/beta_function(k+1,beta)
            check(abs(I-betainc(k+1,beta,x))<3e-12, 'quadrature beta identity')
            exact = (betainc(k+1,beta,x)-betainc(k+2,beta,x))*math.sqrt((k+1)/(k+beta+1))
            check(abs(exact - (1-x)**beta*x**(k+1)*coeff(k,beta))<3e-12,'beta recurrence')
for beta in (0.25,1.,2.5):
    for eps in (0.2,0.02):
        mass=float(np.sum(spectrum(beta,eps,int(math.ceil(43/eps)))))
        check(0<mass<1-eps**beta, 'strict trace-norm bound')
print(f'PASS {count} assertions, finite dimensional formulae and asymptotic convergence tests')
