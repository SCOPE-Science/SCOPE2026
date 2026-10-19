"""Independent finite-system identities and asymptotic consistency checks.
Run with Python 3 standard library: python3 verify_bath_gradient.py.
Numerical sampling is not a proof of limiting claims.
"""
from fractions import Fraction as F
from math import comb, exp, gamma, lgamma, log, pi, sqrt

checks = 0

def require(test, description):
    global checks
    if not test:
        raise AssertionError(description)
    checks += 1

def covariance_exact_rational(n, k, D, beta):
    """Exact rational covariance for nonnegative integer beta."""
    C = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(1, n+1):
        for j in range(i, n+1):
            d = j-i
            z = sum((F(1, j+m)**beta) * F(comb(2*m+d, m), 2**(2*m+d)) / k**(2*m+d)
                    for m in range(n-j+1))
            C[i-1][j-1] = C[j-1][i-1] = D*z/k
    return C

for n in range(2, 9):
    for k in (F(4,5), F(1), F(6,5)):
        for beta in (0,1,2):
            C = covariance_exact_rational(n, k, F(3,4), beta)
            for i in range(n):
                for j in range(n):
                    residue = -2*k*C[i][j] + (C[i+1][j] if i+1<n else 0) + (C[i][j+1] if j+1<n else 0)
                    if i == j:
                        residue += 2*F(3,4)*F(1,i+1)**beta
                    require(residue == 0, 'Exact Lyapunov identity')

def cov_float(n,i,j,k,beta,D=1.):
    if i>j:i,j=j,i
    d=j-i
    out=0.
    for m in range(n-j+1):
        # Log-gamma permits large finite systems without overflowing combinatorial coefficients.
        logprob=lgamma(2*m+d+1)-lgamma(m+1)-lgamma(m+d+1)-(2*m+d)*log(2.)
        out += (j+m)**(-beta)*exp(logprob-(2*m+d)*log(k))
    return D*out/k

def K_kernel(h,lam,beta,D=1.,bins=180000):
    # Midpoint quadrature with t=z^4. For beta=.25, the transformed integrand is bounded at z=0.
    acc=0.
    for j in range(bins):
        z=(j+.5)/bins
        t=z**4
        acc += 4*z**(1-4*beta)*exp(-2*lam*t-h*h/(4*t))
    return D*acc/(bins*sqrt(pi))

for beta in (0.,.25):
    for lam in (0., .6, -0.3):
        for h in (0., .8):
            expected=K_kernel(h,lam,beta,bins=18000)
            for n in ((1800,7200) if beta==0. else (7200,28800)):
                i=1
                j=1+int(h*sqrt(n))
                obs=(n**(beta-.5))*cov_float(n,i,j,1+lam/n,beta)
                # Finite-size convergence can be slow at positive beta.
                err=abs(obs-expected)
                require(err < .14, f'critical kernel n={n}, beta={beta}, lambda={lam}, h={h}, obs={obs}, exp={expected}')

def v_variance(n,beta):
    p=1.; ans=0.
    for m in range(n):
        ans+=p/(m+1)**beta
        p*= (2*m+1)/(2*m+2)
    return ans

for beta,n,tol in ((0.,50000,.01),(.2,200000,.08),(.4,200000,.25)):
    target=(1/sqrt(pi))/(.5-beta)*n**(.5-beta)
    require(abs(v_variance(n,beta)/target-1)<tol, f'variance power, beta={beta}')
require(abs((v_variance(200000,.5)-v_variance(100000,.5))/(log(2)/sqrt(pi))-1)<.001,'borderline logarithmic increment')
for beta in (.75,1.,2.):
    require(v_variance(200000,beta)>v_variance(100000,beta), 'bounded monotone variance')
    require(v_variance(200000,beta)<1 + gamma(beta+.5) * 6, 'finite bound loose check')
for beta in (0., .2, .4):
    h=.001
    K0=K_kernel(0.,.7,beta)
    Kh=K_kernel(h,.7,beta)
    coeff=gamma(beta+.5)/(sqrt(pi)*(.5-beta)*2**(1-2*beta))
    actual=(K0-Kh)/(h**(1-2*beta))
    require(abs(actual/coeff-1)<.035,f'local roughness beta={beta}, actual={actual}, expected={coeff}')
print(f'PASS {checks} deterministic assertions; exact finite Lyapunov residuals and asymptotic spot checks.')
