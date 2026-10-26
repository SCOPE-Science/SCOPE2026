"""Exact and numerical checks of one-row interpolation in Krylov residual minimization."""
from fractions import Fraction as F
from math import sqrt, hypot
import random


def matvec(A,u):
    return [sum(A[i][j]*u[j] for j in range(len(u))) for i in range(len(u))]

def norm(v):return sqrt(sum(x*x for x in v))
def rank_one(n,lo,hi,rho):
    u=[1/sqrt(n)]*n
    c=1/sqrt(n); s=sqrt(1-c*c)
    w=[((1 if i==0 else 0)-c*u[i])/s for i in range(n)]
    z=[sqrt(rho)*u[i]-sqrt(1-rho)*w[i] for i in range(n)]
    A=[[(lo if i==j else 0)+(hi-lo)*z[i]*z[j] for j in range(n)] for i in range(n)]
    return A,u

def ratio(A,r):
    ar=matvec(A,r)
    i=max(range(len(r)), key=lambda i:abs(r[i]))
    if ar[i]==0:return float('inf')
    alpha=r[i]/ar[i]
    return norm([r[j]-alpha*ar[j] for j in range(len(r))])/norm(r)

def envelope(n,lo,hi):
    q=(hi-lo)/(2*sqrt(hi*lo)); s=sqrt(n-1)
    return (sqrt(n)*q/(1-s*q) if s*q<1 else float('inf'))

def tests():
    count=0
    for n,lo,hi in [(2,1,2),(2,1,4),(3,1,2),(4,1,1.5),(9,1,1.2),(20,1,1.1)]:
        A,r=rank_one(n,lo,hi,lo/(lo+hi)); observed=ratio(A,r); bound=envelope(n,lo,hi)
        assert abs(observed-bound)<2e-12,(n,observed,bound)
        count+=1
    # Rational exact witness, A has eigenvalues 1 and 4; the first DEIM row is tied.
    A=[[F(13,10),F(-9,10)],[F(-9,10),F(37,10)]]
    r=[F(1),F(1)]; ar=matvec(A,r); alpha=r[0]/ar[0]
    new=[r[j]-alpha*ar[j] for j in range(2)]
    assert (alpha,new)==(F(5,2),[F(0),F(-6)])
    assert sum(x*x for x in new)/sum(x*x for x in r)==F(18)
    count+=1
    # Distinct maximal coordinate perturbation converges to the same sharp value.
    for eps in [1e-2,1e-3,1e-4,1e-5]:
        Af,rv=rank_one(2,1,4,1/5)
        actual=ratio(Af,[rv[0]*(1+eps),rv[1]])
        assert actual<envelope(2,1,4)*(1+1e-9)
        if eps==1e-5:assert abs(actual-envelope(2,1,4))<3e-4
        count+=1
    # Explicit blow-up as an eigenvector rotation tends to a zero sampled denominator.
    for n,hi in [(2,6),(3,4),(5,3)]:
        best=0
        for j in range(1,20001):
            rho=j/20001
            A,r=rank_one(n,1,hi,rho)
            best=max(best,ratio(A,r))
        assert best>50,(n,hi,best)
        count+=1
    rng=random.Random(491)
    for n in [2,3,5,9]:
        for hi in [1.01,1.05,1.3,1.8,2.5,4]:
            bound=envelope(n,1,hi)
            if not (bound<float('inf')):continue
            for _ in range(100):
                z=[rng.gauss(0,1) for j in range(n)]; z=[x/norm(z) for x in z]
                A=[[(1.0 if i==j else 0)+(hi-1)*z[i]*z[j] for j in range(n)] for i in range(n)]
                r=[rng.uniform(-1,1) for j in range(n)]
                assert ratio(A,r) <=bound+1e-8,(n,hi,ratio(A,r),bound)
                count+=1
    print('PASS',count)
if __name__=='__main__':tests()
