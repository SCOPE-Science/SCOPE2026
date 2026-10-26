"""Deterministic checks for a finite-interval fractional continuous-time random walk.

Run: python verify_fractional_ctrw.py
Dependencies: Python 3, NumPy, SciPy.
These are finite checks; asymptotic conclusions are proved analytically elsewhere.
"""
import math
import itertools
import numpy as np
from scipy.special import gammaln, gammainc, betaln, betainc
from scipy.optimize import brentq
from scipy.integrate import quad

checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def close(x, y, rel=1e-10, abs_tol=1e-12):
    return abs(x-y) <= abs_tol + rel*max(abs(x), abs(y))

def exact_sides(N, i, a):
    # a is the Laplace transform of one holding time at the reset rate
    xi=math.acosh(1/a)
    left=math.sinh((N-i)*xi)/math.sinh(N*xi)
    right=math.sinh(i*xi)/math.sinh(N*xi)
    return left,right

def linear_sides(N,i,a):
    A=np.eye(N-1)
    for j in range(N-2):
        A[j,j+1]=-a/2
        A[j+1,j]=-a/2
    left=np.zeros(N-1);left[0]=a/2
    right=np.zeros(N-1);right[-1]=a/2
    x=np.linalg.solve(A,left)
    y=np.linalg.solve(A,right)
    return x[i-1],y[i-1]

for N in range(3,19):
    for a in [0.16,0.35,0.65,0.91]:
        for i in range(1,N):
            L,R=exact_sides(N,i,a)
            l,r=linear_sides(N,i,a)
            check(close(L,l,rel=3e-11),f'left resolvent N={N},i={i},a={a}')
            check(close(R,r,rel=3e-11),f'right resolvent N={N},i={i},a={a}')
            check(close(L/(L+R),l/(l+r),rel=2e-11),'splitting')

def path_count(N,i,target,steps):
    out=0
    stack=[(i,0)]
    while stack:
        site,t=stack.pop()
        if t==steps:
            out += int(site==target)
            continue
        if site in (0,N):
            continue
        stack.append((site-1,t+1))
        stack.append((site+1,t+1))
    return out

for N in range(3,11):
    for i in range(1,N):
        for target in [0,N]:
            m=i if target==0 else N-i
            c=m-(int(i==N-1) if target==0 else int(i==1))
            check(path_count(N,i,target,m)==1,'unique shortest path')
            check(path_count(N,i,target,m+1)==0,'parity forbids 1 extra')
            check(path_count(N,i,target,m+2)==c,'first detour count')

# Transform of an exponentially tilted Mittag-Leffler waiting time.
for beta in [0.23,0.42,0.73,0.95]:
    for a in [0.005,0.02,0.11,0.26]:
        for s in [0,0.1,0.7,2.5]:
            rhs=(1+a)/((1+s)**beta+a)
            terms=sum((1+a)*(-a)**(k-1)/(1+s)**(k*beta) for k in range(1,80))
            check(close(rhs,terms,rel=1e-12),'signed Gamma series transform')

# The sharp first-order signed density correction has exactly one sign change.
def gamma_pdf(x,shape):
    return math.exp((shape-1)*math.log(x)-x-gammaln(shape))

for beta in [0.25,0.51,0.79]:
    for m in [1,2,3,5]:
        b=m*beta
        tstar=math.exp((gammaln(b+beta)-gammaln(b))/beta)
        delta=gammainc(b,tstar)-gammainc(b+beta,tstar)
        check(delta>0,'positive TV coefficient')
        check(close(gamma_pdf(tstar,b),gamma_pdf(tstar,b+beta),rel=3e-12),'crossing')
        numeric=0.5*quad(lambda u:abs(gamma_pdf(u,b)-gamma_pdf(u,b+beta)),0,math.inf,epsabs=3e-10)[0]
        check(close(numeric,delta,rel=1e-8,abs_tol=4e-9),'total variation integral')
        for a in [0.035,0.014]:
            # m-fold transform raised to m, expanded in signed Gamma densities.
            # Coefficients for ((1+a)/(z+a))**m, where z=(1+s)^beta.
            from math import comb
            weights=[(1+a)**m * ((-a)**k)*comb(m+k-1,k) for k in range(24)]
            def density(u):
                return sum(weights[k]*gamma_pdf(u,(m+k)*beta) for k in range(len(weights)))
            tv=0.5*quad(lambda u:abs(density(u)-gamma_pdf(u,b)),0,math.inf,epsabs=1e-8,limit=250)[0]
            check(abs(tv/a-m*delta)<0.6*a+0.06*a*m*m,'first-order TV scaling')


# Rescaling-invariant time-share law: for two shortest hops the finite-rate
# share distribution is a signed Beta mixture, not exactly Beta(beta,beta).
def beta_pdf(u,x,y):
    return math.exp((x-1)*math.log(u)+(y-1)*math.log1p(-u)-betaln(x,y))
for beta in [0.28,0.53,0.82]:
    A=math.exp(gammaln(beta)+gammaln(3*beta)-2*gammaln(2*beta))
    def shape(u): return 2-A*(u**beta+(1-u)**beta)
    check(shape(1e-8)>0 and shape(0.5)<0,'nonconstant shape correction')
    root=brentq(shape,1e-9,0.5-1e-9)
    # Exact coefficient 1/2 E|shape(U)| via symmetry and zero mean.
    coeff=2*quad(lambda u:shape(u)*beta_pdf(u,beta,beta),0,root,epsabs=1e-10)[0]
    check(coeff>0,'strict share TV coefficient')
    for a in [0.015,0.006]:
        K=8
        weights=[(1+a)*(-a)**j for j in range(K)]
        def finite_share(u):
            return sum(weights[j]*weights[k]*beta_pdf(u,(j+1)*beta,(k+1)*beta) for j in range(K) for k in range(K))
        tv=0.5*quad(lambda u:abs(finite_share(u)-beta_pdf(u,beta,beta)),0,1,epsabs=1e-8,limit=200)[0]
        check(abs(tv/a-coeff)<0.04+0.12*a,'share TV asymptotic')
        check(abs(quad(finite_share,0,1,epsabs=1e-8)[0]-1)<1e-8,'share density normalization')


# General shape correction is normalized and nonconstant for m >= 2.
for beta in [0.2,0.47,0.73,0.99]:
    for m in [2,3,4,7]:
        A=math.exp(gammaln(beta)+gammaln((m+1)*beta)-gammaln(2*beta)-gammaln(m*beta))
        # Dirichlet marginal beta-moment from the beta-gamma identity.
        e_moment=math.exp(gammaln(2*beta)+gammaln(m*beta)-gammaln(beta)-gammaln((m+1)*beta))
        check(close(A*m*e_moment,m,rel=3e-12),'zero-mean share signed correction')
        center=m*(1/m)**beta
        edge=(1-(m-1)*1e-8)**beta+(m-1)*1e-8**beta
        check(A*edge<m<A*center,'positive and negative correction regions')

# For memoryless exponential waiting, conditional shortest-path time shares
# are exactly uniform Dirichlet, so only nonshortest paths cause TV error.
for N in range(4,15):
    for i in range(1,N):
        for target in [0,N]:
            m=i if target==0 else N-i
            if m<2: continue
            c=m-(int(i==N-1) if target==0 else int(i==1))
            for h in [0.03,0.06,0.1]:
                L,R=exact_sides(N,i,h)
                side=L if target==0 else R
                shortest=(h/2)**m
                nonshort=1-shortest/side
                check(abs(nonshort/(h*h)-c/4)<2*h*h*(1+m*m),'memoryless detour TV coefficient')

# Critical mesh crossover of exact splitting probabilities.
for lam in [0.03,0.15,0.7,1.5,4.0]:
    xi=math.acosh(1+lam)
    check(xi<math.sqrt(2*lam),'lattice exponent lies below continuum exponent')
    for N in [160,200,250]:
        a=1/(1+lam)
        for j in [-3,-1,0,1,3]:
            i=N//2+j
            L,R=exact_sides(N,i,a)
            logistic=1/(1+math.exp(2*j*xi))
            check(close(L/(L+R),logistic,rel=1e-9,abs_tol=1e-11),'logistic layer')

print(f'PASS: {checks} deterministic comparisons')
