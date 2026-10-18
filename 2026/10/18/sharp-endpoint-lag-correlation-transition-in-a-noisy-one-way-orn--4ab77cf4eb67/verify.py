"""Independent finite-dimensional checks for the feedforward OU lag theorem.
Run: python verify.py
Requires scipy and numpy. All quantities are dimensionless after a=D=1.
"""
import math
import numpy as np
from scipy.linalg import solve_continuous_lyapunov, expm
from scipy.optimize import brentq
from scipy.special import gammaincc, gammaln

def S(m,h):
    # scaled binomial terms in logarithmic form, sum via long double when appropriate
    if m < 100:
        return sum(math.comb(2*j,j)*(h/2)**(2*j) for j in range(m+1))
    from scipy.special import logsumexp
    return math.exp(logsumexp([gammaln(2*j+1)-2*gammaln(j+1)+2*j*math.log(h/2) for j in range(m+1)]))

def lagroot(m):
    def f(lam):
        # e^-lam E_(m-1)(lam) - e^-lam lam^m/m!
        return gammaincc(m,lam)-math.exp(-lam+m*math.log(lam)-gammaln(m+1))
    return brentq(f,1.e-8,3*m,xtol=1.e-11)

def rho_max(m,h):
    lam=lagroot(m)
    log_gain=math.log(2)-lam/2 + m*math.log(lam)-gammaln(m+1)
    return math.exp(m*math.log(h/2)+log_gain-.5*math.log(S(m,h)))

# Independent Lyapunov and matrix exponential checks for n=2..8, three couplings.
count=0
for n in range(2,9):
 for a,D,h in [(0.6,1.1,0.4),(1.3,0.7,1.0),(1.9,2.3,1.5)]:
    g=a*h;m=n-1
    A=-a*np.eye(n)+g*np.diag(np.ones(n-1),-1)
    C=solve_continuous_lyapunov(A,-2*D*np.eye(n))
    c1n=D/a*(h/2)**m
    vnn=D/a*S(m,h)
    assert abs(C[0,n-1]-c1n)<2.e-9*max(1,abs(c1n)), (n,h,'cov')
    assert abs(C[n-1,n-1]-vnn)<2.e-9*max(1,abs(vnn)),(n,h,'var')
    for t in [0,0.17/a,0.5/a,2/a,5/a]:
        lag=(expm(A*t)@C)[n-1,0]
        expected=c1n*math.exp(-a*t)*sum((2*a*t)**j/math.factorial(j) for j in range(m+1))
        assert abs(lag-expected)<2.e-9*max(1,abs(expected)),(n,h,t,'lag',lag,expected)
        rev=(expm(A*t)@C)[0,n-1]
        assert abs(rev-c1n*math.exp(-a*t))<2.e-9*max(1,abs(rev))
        count+=1
print('Lyapunov/exponential formula checks:',count,'PASS')
print('roots lambda, lambda-(2m-2):')
for m in [1,2,3,5,10,20,50,100,250]:
    lam=lagroot(m)
    assert 0<lam<2*m
    print(m,round(lam,10),round(lam-(2*m-2),9))

# Three phase asymptotic coefficients and the critical window.
for h in [.6,1.,1.4]:
 for m in [40,100,250]:
    v=rho_max(m,h)
    if h<1: approx=math.sqrt(2/math.pi)*h**m*(1-h*h)**.25/math.sqrt(m)
    elif h==1: approx=math.pi**(-.25)*m**(-.75)
    else: approx=math.sqrt(2)*math.pi**(-.25)*math.sqrt(1-h**(-2))*m**(-.25)
    print('phase',h,m,'rho',v,'rho/leading',v/approx)
for theta in [-1,0,1.5]:
 for m in [100,250]:
    from scipy.integrate import quad
    I=quad(lambda y:2*math.exp(2*theta*y*y),0,1)[0]
    v=rho_max(m,math.exp(theta/m))
    leading=math.sqrt(2)*math.pi**(-.25)*math.exp(theta)/math.sqrt(I)*m**(-.75)
    print('window',theta,m,v/leading)
print('ALL CHECKS PASS')
