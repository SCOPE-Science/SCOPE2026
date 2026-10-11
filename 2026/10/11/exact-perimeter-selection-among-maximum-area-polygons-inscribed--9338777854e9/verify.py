"""Standalone finite numerical diagnostics for ellipse polygon perimeter phases.

Only finite diagnostics; the all-parameter result requires the analytic proof.
Run with: python3 verify.py
"""
import math
import random

PI = math.pi


def perimeter(a, b, n, theta):
    return sum(math.hypot(
        a*(math.cos(theta+2*PI*(j+1)/n)-math.cos(theta+2*PI*j/n)),
        b*(math.sin(theta+2*PI*(j+1)/n)-math.sin(theta+2*PI*j/n))
    ) for j in range(n))


def normalized_parameter(n, theta):
    q = n//math.gcd(n,2)
    phi=theta+PI/n-PI/2
    return (-1)**q*math.cos(2*q*phi)


def cheby_and_derivative(n, z):
    t0,t1=1.0,z
    d0,d1=0.0,1.0
    if n == 0:
        return t0,d0
    if n == 1:
        return t1,d1
    for _ in range(2,n+1):
        t0,t1=t1,2*z*t1-t0
        d0,d1=d1,2*t0+2*z*d1-d0
    return t1,d1


def derivative_integral(a,b,n,c,parts=5000):
    q=n//math.gcd(n,2)
    multiplicity=n//q
    w=2*multiplicity*math.sin(PI/n)
    alpha=(a*a+b*b)/2
    beta=(a*a-b*b)/2
    def term(t):
        if t == 0 or t == 1: return 0.0
        s=t/(1-t)
        z=(s+alpha)/beta
        T,D=cheby_and_derivative(q,z)
        return math.sqrt(s)*D/(T-c)**2/(1-t)**2
    dx=1/parts
    result=term(0)+term(1)
    for k in range(1,parts):
        result+=(4 if k%2 else 2)*term(k*dx)
    return -w/(PI*beta)*result*dx/3


def theta_at_c(n,c):
    # cos(2q phi)=(-1)^q c
    q=n//math.gcd(n,2)
    phi=math.acos((-1)**q*c)/(2*q)
    return phi-PI/n+PI/2


def main():
    tests=0
    rng=random.Random(17032011)
    # Independent Euclidean vertex-length implementation versus grouped expression.
    for n in range(3,25):
        q=n//math.gcd(n,2)
        multiplicity=n//q
        for _ in range(150):
            a=1.05+5*rng.random(); b=a*(0.05+0.9*rng.random())
            theta=2*PI*rng.random()
            alpha=(a*a+b*b)/2; beta=(a*a-b*b)/2
            phi=theta+PI/n-PI/2
            rhs=2*multiplicity*math.sin(PI/n)*sum(math.sqrt(alpha+beta*math.cos(2*phi+2*PI*j/q)) for j in range(q))
            lhs=perimeter(a,b,n,theta)
            assert math.isclose(lhs,rhs,rel_tol=8e-13,abs_tol=1e-11),(a,b,n,theta,lhs,rhs)
            tests+=1
    # Grid phase ordering, and a numerical finite-difference derivative-versus-integral comparison.
    for n in [3,4,5,6,7,8,9,10]:
        for a,b in [(2.0,1.0),(3.0,0.4),(1.4,1.0)]:
            vals=[perimeter(a,b,n,theta_at_c(n,-1+2*k/40)) for k in range(41)]
            # Strict phase drop resolvable by machine precision in these cases.
            for x,y in zip(vals,vals[1:]):
                assert x>y+1e-11,(n,a,b,x,y)
                tests+=1
            for c in [-0.6,0,0.6]:
                h=1e-3
                p0=perimeter(a,b,n,theta_at_c(n,c-h))
                p1=perimeter(a,b,n,theta_at_c(n,c+h))
                finite=(p1-p0)/(2*h)
                exact=derivative_integral(a,b,n,c)
                assert exact<0,(n,a,b,c,exact)
                assert abs(finite-exact) < max(3e-7,1.5e-3*abs(exact)), (n,a,b,c,finite,exact)
                tests+=1
    # Cubature of root product identity and logarithmic derivative.
    for q in range(2,14):
        for _ in range(100):
            z=1.001+2*rng.random()
            psi=2*PI*rng.random()
            prod=math.prod(z+math.cos(psi+2*PI*j/q) for j in range(q))
            T,D=cheby_and_derivative(q,z)
            c=(-1)**q*math.cos(q*psi)
            exp=2**(1-q)*(T-c)
            assert math.isclose(prod,exp,rel_tol=3e-9,abs_tol=3e-8),(q,z,psi,prod,exp)
            direct=sum(1/(z+math.cos(psi+2*PI*j/q)) for j in range(q))
            analytic=D/(T-c)
            assert math.isclose(direct,analytic,rel_tol=5e-8,abs_tol=1e-8),(q,z,psi,direct,analytic)
            tests+=2
    print('VERIFY_OK',tests)

if __name__=='__main__': main()
