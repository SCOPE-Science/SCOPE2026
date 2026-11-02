"""Independent finite-state and asymptotic checks for post-loss coupon retention.

Requires Python 3 standard library only. It does not certify infinite limits;
those are established by the accompanying analytic proof.
"""
from fractions import Fraction
from math import comb, exp, expm1, log, log1p, isfinite


def transition(n, p):
    """Exact cardinality-chain transition matrix."""
    q = 1-p
    out = [[Fraction(0) for _ in range(n+1)] for __ in range(n+1)]
    for k in range(n+1):
        for s, w in ((k, Fraction(k,n)), (k+1, Fraction(n-k,n))):
            if not w:
                continue
            for j in range(s+1):
                out[k][j] += w * comb(s,j) * q**j * p**(s-j)
    return out


def solve(A,b):
    """Exact fraction Gaussian elimination without numerical libraries."""
    N = len(A)
    aa = [list(map(Fraction, A[i]))+[Fraction(b[i])] for i in range(N)]
    for j in range(N):
        pivot = next(i for i in range(j,N) if aa[i][j] != 0)
        aa[j],aa[pivot]=aa[pivot],aa[j]
        z=aa[j][j]
        for l in range(j,N+1):
            aa[j][l]/=z
        for i in range(N):
            if i==j:continue
            z=aa[i][j]
            if not z:continue
            for l in range(j,N+1):
                aa[i][l]-=z*aa[j][l]
    return [aa[i][N] for i in range(N)]


def stationary(n,p):
    P=transition(n,p)
    A=[[P[i][j] - int(i==j) for i in range(n+1)] for j in range(n+1)]
    A[n]=[Fraction(1)]*(n+1)
    b=[Fraction(0)]*n+[Fraction(1)]
    return solve(A,b)


def subset_moments(n,p):
    q=1-p
    out=[Fraction(1)]
    for k in range(1,n+1):
        out.append(out[-1]*k*q**k/(n*(1-q**k)+k*q**k))
    return out


def invert_moments(n,m):
    return [comb(n,j)*sum((-1)**r * comb(n-j,r)*m[j+r]
                           for r in range(n-j+1)) for j in range(n+1)]


def product(n,p):
    q=1-p
    m=Fraction(1)
    for k in range(1,n+1):
        m*=k*q**k/(n*(1-q**k)+k*q**k)
    return m


def quad(f,N=8000):
    """Composite Simpson quadrature on [0,1]."""
    assert N%2==0
    s=f(0.0)+f(1.0)
    for k in range(1,N):
        s+=(4 if k%2 else 2)*f(k/N)
    return s/(3*N)


def f(c,x):
    if x==0:return -log1p(c)
    return -log1p(expm1(c*x)/x)


def deriv(c,x):
    if x==0:return -c*c/(2*(1+c))  # correction integrand, not raw derivative
    return -c*c*x*exp(c*x)/(2*(x+expm1(c*x)))


def rate_and_constant(c):
    I=-quad(lambda x:f(c,x))
    logA=(log1p(c)-c)/2+quad(lambda x:deriv(c,x))
    return I, exp(logA)


def log_stationary_product(n,c):
    lam=-n*log1p(-c/n)
    return sum(f(lam,k/n) for k in range(1,n+1))


def run():
    checks=0
    for n in range(1,9):
        for p in (Fraction(1,2),Fraction(1,3),Fraction(2,5)):
            s=stationary(n,p)
            checks+=1;assert sum(s)==1
            checks+=1;assert all(z>0 for z in s)
            checks+=1;assert s[n]==product(n,p),(n,p)
            moments=subset_moments(n,p)
            for k in range(n+1):
                actual=sum(s[j]*Fraction(comb(j,k),comb(n,k)) for j in range(k,n+1))
                checks+=1;assert moments[k]==actual
            recovered=invert_moments(n,moments)
            checks+=1;assert recovered==s
            m=sum(Fraction(j)*s[j] for j in range(n+1))
            checks+=1;assert m==n*(1-p)/(1-p+n*p)
            P=transition(n,p)
            for k in range(n+1):
                checks+=1;assert sum(P[k])==1
                checks+=1;assert all(x>=0 for x in P[k])
                checks+=1;assert sum(s[j]*P[j][k] for j in range(n+1))==s[k]
    for c in (0.2,0.5,1.,2.,3.):
        I,A=rate_and_constant(c)
        checks+=1;assert log1p(c)<I<c
        checks+=1;assert 0<A<1
        for n in (30,50,100,200,500):
            if n<=c:continue
            rat=exp(log_stationary_product(n,c)+n*I)
            checks+=1;assert abs(rat/A-1)<12/n,(c,n,rat,A)
        # Numerically check a convergence rate, beyond the finite exact tests
        r200=exp(log_stationary_product(200,c)+200*I)
        r500=exp(log_stationary_product(500,c)+500*I)
        checks+=1;assert abs(r500/A-1)<abs(r200/A-1)
    print('Exact and numerical assertions passed:', checks)
    for c in (0.2,1.,3.):
        I,A=rate_and_constant(c)
        print(f'c={c:g} I={I:.12f} A={A:.12f} naive_rate={log1p(c):.12f}')

if __name__=='__main__':run()
