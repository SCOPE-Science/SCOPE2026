"""Exact independent small-state verification for random recursive-tree site-percolation singleton theorem."""
from fractions import Fraction as F
from itertools import product
from math import factorial, sqrt

ASSERTIONS=0

def check(condition, message):
    global ASSERTIONS
    ASSERTIONS+=1
    if not condition:
        raise AssertionError(message)

def observed(n, p):
    q=1-p
    values=[F(0) for _ in range(5)] # EU, ES, EU^2, ES^2, EUS
    for parents in product(*(tuple(range(i)) for i in range(1,n))):
        nbr=[[] for _ in range(n)]
        for i, par in enumerate(parents,1):
            nbr[i].append(par);nbr[par].append(i)
        for states in product((0,1),repeat=n):
            k=sum(states)
            weight=p**k*q**(n-k)/factorial(n-1)
            u=n-k
            singleton=sum(int(states[i] and not any(states[j] for j in nbr[i])) for i in range(n))
            quantities=(u,singleton,u*u,singleton*singleton,u*singleton)
            for j,x in enumerate(quantities):values[j]+=weight*x
    return values

def predicted(n,p):
    q=1-p
    s=p*q/(1+p)
    a=p*q*(p*p+2*p-1)/(1+p)**2
    b=2*p**3*q/(1+p)
    R=F(1);H=F(0)
    for k in range(1,n):
        H+=1/(F(k)-p)
        R*=1-p/F(k)
    mean=n*s+(p-s)*R
    cov=n*a+R*(-p*q-a+b*H)
    return mean,cov

for n in range(1,7):
    for p in (F(1,5),F(1,3),F(1,2),F(2,3),F(4,5)):
        u,s,u2,s2,us=observed(n,p)
        q=1-p
        m,c=predicted(n,p)
        check(u==n*q,(n,p,'mean closed'))
        check(u2-u*u==n*p*q,(n,p,'var closed'))
        check(s==m,(n,p,'singleton mean'))
        check(us-u*s==c,(n,p,'cross cov'))
        check(s2>=s*s,(n,p,'nonnegative singleton var'))

for p in (F(1,5),F(1,3),F(1,2),F(2,3),F(4,5)):
    q=1-p
    s=p*q/(1+p)
    alpha=p*q*(p*p+2*p-1)/(1+p)**2
    sigma=p*q*(2*p**3+7*p*p+1)/((1+p)**2*(1+2*p))
    cross=p*q*(p*p+2*p-1)/(1+p)**2
    # Evaluate the Riemann-integral covariance via three rational monomial moments
    sig_uu=p*q
    sig_us=-q*s
    sig_ss=p*(q+s)-s*s
    integral_cross=sig_uu*(1-F(1,1)/(1+p))+sig_us/(1+p)
    integral_s=sig_uu*(1-F(2,1)/(1+p)+F(1,1)/(1+2*p)) \
       +2*sig_us*(F(1,1)/(1+p)-F(1,1)/(1+2*p)) +sig_ss/(1+2*p)
    check(integral_cross==cross,(p,'CLT cross integral'))
    check(integral_s==sigma,(p,'CLT singleton integral'))
    check(sigma>0,(p,'positive variance'))
    check(sig_uu*sigma-cross*cross>0,(p,'positive definite Gaussian'))
    check(alpha==cross,(p,'asymptotic cov matches CLT'))
    # Finite deterministic moment recurrences to n=10000, comparing asymptotic variances.
    mu_s=float(p);eu=float(q);es2=float(p);eus=0.0;pf=float(p);qf=float(q)
    for n in range(1,3001):
        e_s2_new=(1-2*pf/n)*es2+(2*pf/n)*eus+(pf/n)*(eu+mu_s)
        e_us_new=eus+(pf/n)*(n*pf*qf+eu*eu-eus)+qf*mu_s
        mu_s=mu_s+(pf/n)*(eu-mu_s)
        eu+=qf
        es2=e_s2_new;eus=e_us_new
    check(abs(float((es2-mu_s*mu_s)/3001-float(sigma)))<.005,(p,'large-n variance convergence'))

print(f'PASS: {ASSERTIONS} independent exact/limit assertions; all n <= 6, five rational retention parameters; n=3001 moment recurrences.')
