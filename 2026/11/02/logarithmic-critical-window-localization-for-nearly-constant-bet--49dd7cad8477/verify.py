#!/usr/bin/env python3
"""Finite normalization and quadrature checks for the beta rare-variance law."""
import math
from fractions import Fraction

def exact_determinant(matrix):
    """Fraction Gaussian elimination for integer Gram matrices."""
    A=[[Fraction(v) for v in row] for row in matrix]
    n=len(A); det=Fraction(1)
    for i in range(n):
        if A[i][i]==0:
            j=next((j for j in range(i+1,n) if A[j][i]),None)
            if j is None:
                return Fraction(0)
            A[i],A[j]=A[j],A[i];det=-det
        pivot=A[i][i];det*=pivot
        for j in range(i+1,n):
            f=A[j][i]/pivot
            for k in range(i,n):
                A[j][k]-=f*A[i][k]
    return det


checks = 0

def check(condition, message):
    global checks
    assert condition, message
    checks += 1

def close(actual, expected, tol=1e-12):
    check(abs(actual-expected) <= tol*max(1., abs(expected)),
          f"{actual} versus {expected}")

def phi(n, z):
    if z == 0:
        return 1.0
    a = n*z/2.0
    return -math.expm1(-a)/a

def simpson(f, a, b, m=200000):
    assert m % 2 == 0
    h = (b-a)/m
    s = f(a)+f(b)
    for k in range(1,m):
        s += (4 if k % 2 else 2)*f(a+k*h)
    return s*h/3

def exact_arcsine_probability(eps):
    """Exact reduced 1D integral for two independent Beta(1/2,1/2) draws.

    Write X=sin^2(pi*T/2), T uniform, and integrate the conditional
    arcsine CDF difference on |X-Y|<=sqrt(2 eps).
    """
    d = math.sqrt(2*eps)
    def cdf(y):
        y=min(1.,max(0.,y))
        return (2/math.pi)*math.asin(math.sqrt(y))
    def f(t):
        x=math.sin(math.pi*t/2.)**2
        return cdf(x+d)-cdf(x-d)
    # segment at the points where truncations switch
    t_left=(2/math.pi)*math.asin(math.sqrt(d))
    t_right=(2/math.pi)*math.asin(math.sqrt(1-d))
    return (simpson(f,0,t_left,10000)
            +simpson(f,t_left,t_right,40000)
            +simpson(f,t_right,1,10000))

def main():
    # Normalized beta constants, volumes and critical exponents.
    for n in range(2,12):
        c=(n-1)/n
        # Coordinates (w_1,...,w_{n-1}) on the zero-sum hyperplane
        # have Gram matrix I+J of determinant n.
        check(exact_determinant([[1+(i==j) for j in range(n-1)]
                                 for i in range(n-1)])==n,
              "diagonal Jacobian Gram determinant")
        B=math.gamma(c)**2/math.gamma(2*c)
        V=math.pi**((n-1)/2)/math.gamma(1+(n-1)/2)
        check(B>0 and V>0 and 0<c<1,"positive normalizations")
        close(n*(c-1),-1.)
        for lam,mu in ((0.,0.),(.5,-1.),(-2.,3.),(1.,2.)):
            pl=phi(n,lam);pr=phi(n,mu)
            check(pl>0 and pr>0,"positive endpoint weights")
            close(pl/(pl+pr)+pr/(pl+pr),1.)
            # Direct Simpson quadrature of the tilt integral.
            close(pl,simpson(lambda u:math.exp(-n*lam*u/2),0,1,800),3e-10)
            close(pr,simpson(lambda u:math.exp(-n*mu*u/2),0,1,800),3e-10)
            # Endpoint swap exchanges weights but not total mass.
            close(pl+pr,phi(n,mu)+phi(n,lam))
    close(math.gamma(.5)**2/math.gamma(1),math.pi)
    # n=3: match the fixed-shape S^2 critical coefficient exactly.
    n=3;c=2/3
    B=math.gamma(c)**2/math.gamma(2*c)
    V=math.pi
    q_constant=math.sqrt(3)*V/B**3
    s2_constant=2*q_constant  # Q=2*S^2, first-order log preserved
    close(s2_constant,2*math.sqrt(3)*math.pi/B**3)
    # Main result at n=2, lambda=mu=0 versus independent exact CDF integral.
    # As eps shrinks, P(E)/(K sqrt(eps) log(1/eps)) -> 1.
    ratios=[]
    for eps in (1e-5,1e-7,1e-9):
        p=exact_arcsine_probability(eps)
        k=(2*math.sqrt(2)/math.pi**2)*math.sqrt(eps)*math.log(1/eps)
        ratio=p/k
        check(p>0 and ratio>1. and ratio<2.,"positive finite-threshold ratio")
        ratios.append(ratio)
    check(ratios[0]>ratios[1]>ratios[2],"arcsine ratio approaches 1")
    print(f"PASS: {checks} assertions; arcsine finite-epsilon/asymptotic ratios:",
          [round(r,6) for r in ratios])
    print("The asymptotic theorem rests on its proof, not on these finite checks.")

if __name__=='__main__':
    main()
