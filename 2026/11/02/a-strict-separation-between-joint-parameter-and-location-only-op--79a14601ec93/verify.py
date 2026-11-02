"""Checks for a three-site Poisson Gaussian-transect design theorem.

Run with Python 3 standard library: python verify.py.  Finite tests supplement
and do not replace the analytic monotonicity and determinant proofs in RESULT.md.
"""
from fractions import Fraction as F
from math import exp, expm1, sqrt, log
from random import Random

N = 0

def check(condition, message):
    global N
    N += 1
    if not condition:
        raise AssertionError(message)

def determinant3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
           -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
           +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

def information(q, u, a, b, wm, wc, wp, sig=1):
    # q represents the wing profile exp(-d^2/(2 sigma^2)); u=d/sigma.
    # Gradient order: x, amplitude, background.  Dimensionful derivative
    # d/dx of A f at x=0 is A*q*(position)/(sigma^2).
    rows = [(-a*q*u/sig,q,1), (0,1,1), (a*q*u/sig,q,1)]
    means = [a*q+b,a+b,a*q+b]
    weights = [wm,wc,wp]
    return [[sum(weights[k]*rows[k][i]*rows[k][j]/means[k]
                 for k in range(3)) for j in range(3)] for i in range(3)]

def h_d(t,beta):
    z=beta*exp(t)
    return 1/t+2/expm1(t)-2*z/(1+z)

def h_c(t,beta):
    z=beta*exp(t)
    return 1/t-1-z/(1+z)

def root(f,lo,hi):
    check(f(lo)>0 and f(hi)<0, 'root not bracketed')
    for _ in range(90):
        mid=(lo+hi)/2
        if f(mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2

def d_value(t,beta):
    return t*(1-exp(-t))**2/(1+beta*exp(t))**2

def c_value(t,beta):
    return t*exp(-t)/(1+beta*exp(t))

def run():
    r=Random(194711)
    # EXACT arithmetic in a formal wing response q and separation u.
    for _ in range(220):
        q=F(r.randint(1,8),r.randint(9,20))
        u=F(r.randint(1,11),r.randint(1,8))
        sig=F(r.randint(1,8),r.randint(1,8))
        a=F(r.randint(1,13),r.randint(1,8))
        b=F(r.randint(1,13),r.randint(1,8))
        wm,wc,wp=[F(r.randint(1,7),r.randint(1,7)) for _ in range(3)]
        M=information(q,u,a,b,wm,wc,wp,sig)
        actual=determinant3(M)
        expected=4*wm*wc*wp*a*a*q*q*u*u*(1-q)**2/(sig*sig*(a+b)*(a*q+b)**2)
        check(actual==expected,'exact Fisher determinant')
        for i in range(3):
            for j in range(3):
                check(M[i][j]==M[j][i], 'Fisher symmetry')
        check(actual>0, 'Fisher nonsingularity')
        # Equal wing exposure is the case where position is orthogonal to nuisances.
        equal=information(q,u,a,b,wm,wc,wm,sig)
        check(equal[0][1]==0 and equal[0][2]==0,'orthogonality')
        check(equal[0][0]==2*wm*a*a*q*q*u*u/(sig*sig*(a*q+b)),
              'position information')
    # Independent smooth derivatives of the two scalar objectives.
    for _ in range(1000):
        beta=exp(r.uniform(-9,9))
        t=r.uniform(.13,12)
        h=1e-6
        dl=(log(d_value(t+h,beta))-log(d_value(t-h,beta)))/(2*h)
        cl=(log(c_value(t+h,beta))-log(c_value(t-h,beta)))/(2*h)
        check(abs(dl-h_d(t,beta))<2e-7,'D derivative')
        check(abs(cl-h_c(t,beta))<2e-7,'c derivative')
    for _ in range(400):
        beta=exp(r.uniform(-12,12))
        dc=root(lambda t:h_d(t,beta),1,25)
        cc=root(lambda t:h_c(t,beta),.5,1)
        check(.5<cc<1<dc,'strict universal D/c separation')
        check(abs(h_d(dc,beta))<2e-14,'D stationary')
        check(abs(h_c(cc,beta))<2e-14,'c stationary')
        check(d_value(dc,beta)>d_value(cc,beta),'D improvement')
        check(c_value(cc,beta)>c_value(dc,beta),'c improvement')
        for t in [1e-4,.3,.5,.9,1,1.25,2,5,14,25]:
            check(d_value(dc,beta)+1e-15>=d_value(t,beta),'D global')
            check(c_value(cc,beta)+1e-15>=c_value(t,beta),'c global')
    # Monotonicity in background and limiting universal bound.
    prev_d=1000
    prev_c=10
    for beta in [1e-8,1e-7,1e-6,1e-5,1e-4,.001,.01,.1,1,10,100,1e4,1e6]:
        dc=root(lambda t:h_d(t,beta),1,30)
        cc=root(lambda t:h_c(t,beta),.5,1)
        check(dc<prev_d and cc<prev_c,'background moves both optima inward')
        prev_d,prev_c=dc,cc
    dc=root(lambda t:h_d(t,1),1,3)
    cc=root(lambda t:h_c(t,1),.5,1)
    check(abs(dc-1.273380149670236)<2e-12,'numeric D example')
    check(abs(cc-.607064681536402)<2e-12,'numeric c example')
    check(abs(d_value(dc,1)/d_value(cc,1)-2.01901049403675)<1e-10,'gain')
    check(abs(c_value(cc,1)/c_value(dc,1)-1.49722769983544)<1e-10,'loss')
    # Independent fractional-exposure positivity/AM-GM spot tests.
    for _ in range(400):
        a,b,c=[r.random()+0.02 for _ in range(3)]
        avg=(a+b+c)/3
        check(a*b*c<=avg**3+1e-13,'exposure product AM-GM')
    print(f'VERIFY_OK assertions={N}')

if __name__=='__main__':
    run()
