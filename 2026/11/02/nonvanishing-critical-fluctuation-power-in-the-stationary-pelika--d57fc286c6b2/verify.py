"""Exact finite-time tests for the stationary Pelikan covariance formulas.
Run: python verify.py (Python 3, standard library only).
The analytical proof, not finite testing, establishes all-time assertions.
"""
from fractions import Fraction as Q
from math import comb


def conv(a, b, N):
    return [sum((a[k] * b[n-k] for k in range(n+1)), Q(0)) for n in range(N+1)]


def reciprocal(a, N):
    assert a[0] != 0
    out = [1/a[0]]
    for n in range(1, N+1):
        out.append(-sum((a[k]*out[n-k] for k in range(1,n+1)),Q(0))/a[0])
    return out


def gf_coefficients(p, b, N):
    q=1-p; r=q/p; c=2*p+q/2
    lam=[Q(0)]*(N+1)
    for k in range((N+1)//2):
        j=2*k+1
        if j<=N: lam[j]=Q(comb(2*k,k),k+1)*p**(k+1)*q**k
    A=[c**n for n in range(N+1)]
    D=[Q(0)]*(N+1);D[0]=Q(1)
    if N>=1: D[1]=-p*b
    for j in range(2,N+1): D[j]=-q*lam[j-1]
    E=[Q(0)]*(N+1);E[0]=Q(1)
    for j in range(1,N+1): E[j]=-r*lam[j]/2
    AB=conv(A,reciprocal(D,N),N)
    B=[Q(0)]+[p*(b-2)*AB[n-1] for n in range(1,N+1)]
    BE=conv(B,reciprocal(E,N),N)
    return [(1-r)*(A[n]/(1-r/4)+BE[n]) for n in range(N+1)]


def direct_coefficients(p,b,N):
    q=1-p;r=q/p;c=2*p+q/2
    M=3*N+8
    v=[Q(1,2**j) for j in range(M)]
    u=v[:];out=[]
    for n in range(N+1):
        head=sum(((1-r)*r**j*v[j]*u[j] for j in range(n+1)),Q(0))
        tail=(1-r)*c**n*(r/4)**(n+1)/(1-r/4)
        out.append(head+tail)
        if n<N:
            w=[Q(0)]*M
            w[0]=p*b*u[0]+q*u[1]
            for j in range(1,M-1):w[j]=p*u[j-1]+q*u[j+1]
            u=w
    return out


def invariant_moments(p):
    r=(1-p)/p
    m=(1-r)/(1-r/2);s=(1-r)/(1-r/4)
    return m,s


def covariance_formula(p):
    return (2*p-1)*(6*p*p-3*p+1)/(3*(3*p-1)**2*(5*p-1))


def green_kubo_formula(p):
    return (-12*p**4+50*p**3-43*p*p+14*p-1)/((3*p-1)**3*(5*p-1))


def green_kubo_from_poisson(p):
    q=1-p;r=q/p;d=2*p-1
    m,s=invariant_moments(p)
    a=-Q(2)/(3*p-1)
    ej=r/(1-r)
    ejv=(1-r)*(r/2)/(1-r/2)**2
    summed=(a*(s-m*m)-(m/d)*(ejv-m*ej))/4 + a*(s-3*m)/12
    variance=s/Q(3)-m*m/4
    return 2*summed-variance


def test():
    for p in [Q(51,100),Q(3,5),Q(2,3),Q(3,4),Q(4,5),Q(9,10),Q(99,100)]:
        m,s=invariant_moments(p)
        for b in [Q(1),Q(1,2)]:
            N=12
            x=gf_coefficients(p,b,N)
            y=direct_coefficients(p,b,N)
            assert x==y,(p,b,'all-lag resolvent discrepancy')
        f1=gf_coefficients(p,Q(1),12)
        fh=gf_coefficients(p,Q(1,2),12)
        c0=(f1[0]/4+fh[0]/12)-m*m/4
        assert c0==covariance_formula(p)
        assert green_kubo_from_poisson(p)==green_kubo_formula(p)
        assert green_kubo_formula(p)>0
    # The critical equilibrium is degenerate, but the nonzero stationary
    # asymptotic-variance limit is exactly four by polynomial evaluation.
    f=lambda x: (-12*x**4+50*x**3-43*x*x+14*x-1)/((3*x-1)**3*(5*x-1))
    assert f(Q(1,2))==Q(4)
    assert f(Q(1))==Q(1,4)
    print('PASS: 7 rational parameters; 182 exact resolvent/dynamics coefficients;'
          ' invariant variances and Poisson/Green-Kubo identities; endpoint limits')

if __name__=='__main__':test()
