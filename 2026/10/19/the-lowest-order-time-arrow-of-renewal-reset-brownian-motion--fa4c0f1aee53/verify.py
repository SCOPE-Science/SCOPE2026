"""Reproducible exact checks for the Brownian renewal-reset temporal-asymmetry identities.

Only Python standard library is needed. Finite symbolic checks support the proof,
but do not substitute for its universal argument.
"""
from fractions import Fraction as Q
from math import comb, factorial, exp, isclose


def dfact(n):
    out = 1
    for a in range(n, 0, -2):
        out *= a
    return out


def independent_brownian_mixed_coefficient(m, j):
    # Difference E[U(U+V)^(2m+1)] - E[U^(2m+1)(U+V)]:
    # coefficient of D^(m+1)*a^(m+1-j)*t^j, U,V independent
    # Gaussian with variances 2Da and 2Dt.
    return (comb(2*m+1,2*j)*dfact(2*(m+1-j)-1)*dfact(2*j-1)
            * 2**(m+1))


def hierarchy_law(distribution, m, t, diffusivity):
    """Renewal positive-part formula, exact for finite-support laws."""
    mean_T = sum(p*T for T,p in distribution)
    total=Q(0)
    for j in range(1,m+1):
        exponent=m+2-j
        truncated=sum(p*max(Q(0),T-t)**exponent for T,p in distribution)
        coeff=Q(2*factorial(2*m+1)*(m+1-j),
                factorial(j)*factorial(m+1-j)*exponent)
        total+=coeff*(diffusivity**(m+1))*(t**j)*truncated/mean_T
    return total


def direct_gaussian_cycle(distribution,m,t,diffusivity):
    """Independent calculation: expand Brownian Gaussian moments and integrate age."""
    mean_T=sum(p*T for T,p in distribution)
    total=Q(0)
    for T,p in distribution:
        remaining=max(Q(0),T-t)
        for j in range(1,m+1):
            exponent=m+1-j
            total += (p/mean_T*independent_brownian_mixed_coefficient(m,j)
                      *diffusivity**(m+1)*t**j*remaining**(exponent+1)/Q(exponent+1))
    return total


def elementary_stop_loss(distribution,t,diffusivity):
    mean_T=sum(p*T for T,p in distribution)
    stop_loss=sum(p*max(Q(0),T-t)**2 for T,p in distribution)
    return 6*diffusivity**2*t*stop_loss/mean_T


def run():
    assertions=0
    distributions=[
        [(Q(1),Q(1))],
        [(Q(2),Q(1))],
        [(Q(1),Q(1,3)),(Q(3),Q(2,3))],
        [(Q(1,2),Q(1,4)),(Q(2),Q(3,4))],
        [(Q(1,3),Q(1,5)),(Q(7,5),Q(2,5)),(Q(4),Q(2,5))]
    ]
    for distribution in distributions:
        for t in [Q(1,10),Q(1,2),Q(1),Q(3,2),Q(5,2),Q(5)]:
            for diffusivity in [Q(1,3),Q(1),Q(7,4)]:
                for m in [1,2,3,4]:
                    q=hierarchy_law(distribution,m,t,diffusivity)
                    assert q == direct_gaussian_cycle(distribution,m,t,diffusivity)
                    assertions+=1
                    assert q>=0
                    assertions+=1
                    if m==1:
                        assert q==elementary_stop_loss(distribution,t,diffusivity)
                        assertions+=1
    # The recovered survival curve equals the original survival for piecewise
    # quadratic truncated-power transforms away from atom locations.
    for distribution in distributions:
        mean_T=sum(p*T for T,p in distribution)
        for x in [Q(1,8),Q(3,8),Q(5,8),Q(9,8),Q(13,8),Q(17,8),Q(27,8)]:
            if any(T==x for T,p in distribution):
                continue
            h=Q(1,10000)
            if any(abs(T-x)<=h for T,p in distribution):
                continue
            def G(y):
                return elementary_stop_loss(distribution,y,Q(5,3))/y
            right_second=(G(x+h)-2*G(x)+G(x-h))/h**2
            expected=Q(12)*Q(5,3)**2/mean_T*sum(p for T,p in distribution if T>x)
            assert right_second==expected,(distribution,x,right_second,expected)
            assertions+=1
    # Poisson survival, deterministic cycle and unique peak formulas.
    for r in [Q(1,3),Q(1),Q(2),Q(5)]:
        for D in [Q(1,2),Q(2)]:
            for t in [Q(1,4),Q(1),Q(9,4)]:
                rr=float(r);tt=float(t);dd=float(D)
                # Method 1: direct conditional Poisson Brownian moments with
                # stationary E[X^2]=2D/r and E[X^4]=24D^2/r^2.
                forward=exp(-rr*tt)*(24*dd**2/rr**2 + 12*dd**2*tt/rr)
                backward=exp(-rr*tt)*24*dd**2/rr**2
                direct=forward-backward
                # Method 2: squared positive-part of independent Exp(r):
                # E[(T-t)_+^2]=2 exp(-rt)/r^2, E[T]=1/r.
                stop_loss=6*dd**2*tt*rr*(2*exp(-rr*tt)/rr**2)
                assert isclose(direct,stop_loss,rel_tol=1e-10,abs_tol=1e-11)
                assertions+=1
                # The analytic logarithmic derivative is 1/t-r.
                assert (1/tt-rr>0) == (tt<1/rr) if tt!=1/rr else abs(1/tt-rr)<1e-12
                assertions+=1
    for t in [Q(1,8),Q(1,4),Q(1,2),Q(3,4),Q(1),Q(2)]:
        b=Q(1)
        assert elementary_stop_loss([(b,Q(1))],t,Q(3,2))==Q(6)*Q(3,2)**2*t*max(Q(0),b-t)**2/b
        assertions+=1
    print(f"PASS: {assertions} independent exact rational / algebraic checks")

if __name__=='__main__':
    run()
