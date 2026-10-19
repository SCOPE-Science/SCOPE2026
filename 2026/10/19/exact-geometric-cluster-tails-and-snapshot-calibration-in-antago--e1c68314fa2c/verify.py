"""Numerical and finite-chain checks of the one-attempt antagonistic adsorption cluster theorem.

Run with Python 3.10 or later: python verify.py
No third-party packages required. Finite-chain results are independent calculations,
not proofs of infinite-lattice assertions.
"""
from functools import lru_cache
from math import cosh, exp, sqrt, sinh, isclose

N_ASSERTIONS = 0

def check(condition, description):
    global N_ASSERTIONS
    N_ASSERTIONS += 1
    if not condition:
        raise AssertionError(description)

def qa(u,p):
    b = 1-p
    g = sqrt(p*b)
    return cosh(g*u)-b/g*sinh(g*u)

def qb(u,p):
    b = 1-p
    g = sqrt(p*b)
    return cosh(g*u)-p/g*sinh(g*u)

def jac(u,p):
    b=1-p
    g=sqrt(p*b)
    return sinh(g*u)/g-b*(cosh(g*u)-1)/(g*g)

def simpson(f,t,n=1000):
    assert n%2==0
    h=t/n
    return h/3*(f(0)+f(t)+4*sum(f(h*i) for i in range(1,n,2))+
                 2*sum(f(h*i) for i in range(2,n,2)))

def rho_source(t,p):
    b=1-p
    g=sqrt(p*b)
    theta=sqrt(p/b)
    return (2*theta+(theta**2-1)*2*g*t+(theta**2+1)*sinh(2*g*t)
            -2*theta*cosh(2*g*t))/(4*theta)

def block(t,p,m):
    assert m>=2
    return p**m * t**(m-2)*jac(t,p)**2

def cluster(t,p,m):
    if m==1:
        return rho_source(t,p)-2*block(t,p,2)+block(t,p,3)
    return block(t,p,m)-2*block(t,p,m+1)+block(t,p,m+2)

def finite_chain_probability(n,start,m,p,t):
    """Exact finite-chain expectation, computed by averaging all random trial orders,
    all independent A/B marks and independent Bernoulli(t) attempt activity.
    This dynamic program does NOT assume the infinite-line boundary law.
    """
    assert 0<p<1 and 0<t<=1 and n>=start+m
    full=(1<<n)-1
    target=((1<<m)-1)<<start
    nbr=tuple(((1<<(i-1)) if i>0 else 0)|
              ((1<<(i+1)) if i<n-1 else 0) for i in range(n))
    @lru_cache(None)
    def visit(left,A,B):
        if not left:
            return 1. if A&target==target else 0.
        remaining=left.bit_count()
        total=0.
        bits=left
        while bits:
            bit=bits&-bits
            bits-=bit
            i=bit.bit_length()-1
            new_left=left^bit
            vacant=visit(new_left,A,B)
            choice_A=visit(new_left,A|bit,B) if not(B&nbr[i]) else vacant
            choice_B=visit(new_left,A,B|bit) if not(A&nbr[i]) else vacant
            total+=(1-t)*vacant+t*(p*choice_A+(1-p)*choice_B)
        return total/remaining
    result=visit(full,0,0)
    return result,visit.cache_info().currsize

def main():
    for p in (0.08,0.17,0.3,0.5,0.7,0.83,0.92):
        for t in (0.07,0.2,0.4,0.65,0.85,1.0):
            a,b=qa(t,p),qb(t,p)
            check(0<a<1,'one-sided A nonblocking probability')
            check(0<b<1,'one-sided B nonblocking probability')
            delta=1.e-6
            check(abs((qa(t+delta,p)-qa(t-delta,p))/(2*delta)+(1-p)*qb(t,p))<2.e-8,
                  'A half-line survival ODE')
            check(abs((qb(t+delta,p)-qb(t-delta,p))/(2*delta)+p*qa(t,p))<2.e-8,
                  'B half-line survival ODE')
            J=simpson(lambda u:qa(u,p),t)
            K=simpson(lambda u:qa(u,p)**2,t)
            check(abs(J-jac(t,p))<2.e-10,'integrated half-line law')
            check(abs(p*K-rho_source(t,p))<2.e-10,'published one-point law')
            check(J>K>0,'adjacent same-color clustering')
            for m in range(2,10):
                left=block(t,p,m)
                check(left>0,'positive monochromatic block')
                check(abs(block(t,p,m+1)/left-p*t)<5.e-13,
                      'block geometric tail')
                intensity=cluster(t,p,m)
                check(abs(intensity-p**m*t**(m-2)*J**2*(1-p*t)**2)<2.e-10,
                      'maximal block intensity')
                check(intensity>0,'positive cluster density')
            d1=cluster(t,p,1)
            check(d1>0,'singleton intensity')
            check(abs(d1+block(t,p,2)*(2-p*t)-rho_source(t,p))<2.e-12,
                  'run-length mass bookkeeping')
            check(abs(cluster(t,p,3)/cluster(t,p,2)-p*t)<5.e-13,
                  'A cluster ratio identifies p*t')
            check(abs(cluster(t,1-p,3)/cluster(t,1-p,2)-(1-p)*t)<5.e-13,
                  'B cluster ratio identifies (1-p)*t')
            check(abs(cluster(t,p,3)/cluster(t,p,2)+
                      cluster(t,1-p,3)/cluster(t,1-p,2)-t)<5.e-13,
                  'inverse calibration time')
    tests=(
        (0.2,1.0,2),(0.5,0.6,2),(0.8,0.8,3),(0.5,1.0,4),
        (0.5,1.0,2),
    )
    for p,t,m in tests:
        n=m+8 # four outside sites on each side
        direct, states=finite_chain_probability(n,4,m,p,t)
        analytic=block(t,p,m)
        check(abs(direct-analytic)<5.e-4,
              'finite-chain dynamic program approaches infinite-lattice formula')
        print('Finite chain: p=%.2f t=%.2f m=%s states=%s direct=%.12g infinite=%.12g'
              %(p,t,m,states,direct,analytic))
    check(abs(rho_source(1,0.5)-(1-exp(-1))/2)<1.e-12,
          'symmetric benchmark')
    print('PASS: %s independent assertions/equality/positivity tests'%N_ASSERTIONS)

if __name__=='__main__':
    main()
