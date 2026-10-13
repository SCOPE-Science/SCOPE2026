from fractions import Fraction
from math import comb, factorial

def H(n):
    return sum((Fraction(1,k) for k in range(1,n+1)), Fraction(0))

def binomial_harmonic_checks(N=400):
    checks=0
    for m in range(1,N+1):
        lhs=sum((Fraction(((-1)**(j+1))*comb(m,j),j) for j in range(1,m+1)),Fraction(0))
        assert lhs==H(m)
        checks+=1
    return checks

def egf_coeff_checks(N=300):
    # Check e^{-x} sum_{m>=1} H_m x^m/m! = Ein(x)
    # coefficient of x^r in Ein(x) is (-1)^(r+1)/(r*r!)
    checks=0
    for r in range(1,N+1):
        lhs=Fraction(0)
        for m in range(1,r+1):
            lhs += H(m)*Fraction((-1)**(r-m), factorial(m)*factorial(r-m))
        rhs=Fraction((-1)**(r+1), r*factorial(r))
        assert lhs==rhs
        checks+=1
    return checks

def covariance_series_checks(N=300):
    # If F(x)=Ein(x), C(x)/t = [1-e^{-x}-F(x)]/x.
    # Independently compare with x d/dx [F(x)/x].
    checks=0
    # f_r coefficient of x^r in Ein, r>=1
    f={r:Fraction((-1)**(r+1),r*factorial(r)) for r in range(1,N+2)}
    # coefficient at x^k of score expression x d/dx(F/x)
    for k in range(1,N):
        # F/x has coefficient f[k+1] at x^k, derivative* x gives k*f[k+1]
        score=k*f[k+1]
        # numerator 1-e^-x-F has coefficient for x^(k+1):
        r=k+1
        numer=Fraction((-1)**(r+1),factorial(r)) - f[r]
        direct=numer
        assert score==direct
        checks+=1
    return checks

def sign_checks(N=500):
    # Coefficient-free discrete check: H_m/m is strictly decreasing.
    checks=0
    prev=H(1)
    for m in range(2,N+1):
        cur=H(m)/m
        assert cur < prev
        prev=cur
        checks+=1
    return checks

def run():
    a=binomial_harmonic_checks()
    b=egf_coeff_checks()
    c=covariance_series_checks()
    d=sign_checks()
    print("VERIFY_OK")
    print(f"binomial_harmonic_checks={a}")
    print(f"egf_coefficient_checks={b}")
    print(f"covariance_series_checks={c}")
    print(f"conditional_monotonicity_checks={d}")

if __name__=="__main__":
    run()
