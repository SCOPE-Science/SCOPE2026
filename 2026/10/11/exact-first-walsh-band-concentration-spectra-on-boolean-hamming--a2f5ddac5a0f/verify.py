"""Direct exact finite-size checks for the first-Walsh-band Hamming-ball concentration theorem.

Requires Python 3 standard library; no source paper or external data required.
"""
from math import comb, sqrt, pi, erf, exp
from fractions import Fraction
from itertools import product


def binom(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def formula(n, r):
    p = Fraction(sum(binom(n, k) for k in range(r+1)), 2**n)
    s = Fraction(binom(n-1, r), 2**n)
    t = Fraction(binom(n-2, r)-binom(n-2, r-1), 2**n)
    return p, s, t


def brute(n,r):
    G=[[0]*(n+1) for _ in range(n+1)]
    for eps in product(range(2),repeat=n):
        if sum(eps)>r:continue
        x=[1]+[1-2*z for z in eps]
        for i in range(n+1):
            for j in range(n+1): G[i][j]+=x[i]*x[j]
    return [[Fraction(v,2**n) for v in row] for row in G]


def predicted(n,r):
    p,s,t=formula(n,r)
    return [[p if i==j else s if i==0 or j==0 else t for j in range(n+1)]for i in range(n+1)]


def matmul(A,B):
    d=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(d)) for j in range(d)] for i in range(d)]


def polynomial_mul(a,b):
    result=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):result[i+j]+=x*y
    return result


def charpoly_from_traces(G):
    # Coefficients ascending in the indeterminate.
    d=len(G)
    identity=[[Fraction(i==j) for j in range(d)] for i in range(d)]
    power=identity
    traces=[]
    for k in range(1,d+1):
        power=matmul(power,G)
        traces.append(sum(power[i][i] for i in range(d)))
    # p(X)=X^d+c_1 X^{d-1}+...+c_d; Newton recurrence.
    c=[Fraction(1)]
    for k in range(1,d+1):
        c.append(-sum(c[k-j]*traces[j-1] for j in range(1,k+1))/k)
    return list(reversed(c))


def predicted_charpoly(n,r):
    p,s,t=formula(n,r)
    poly=[Fraction(1)]
    for j in range(n-1):poly=polynomial_mul(poly,[-(p-t),Fraction(1)])
    radial=[p*(p+(n-1)*t)-n*s*s,-(2*p+(n-1)*t),Fraction(1)]
    return polynomial_mul(poly,radial)


def test_finite():
    cases=0
    for n in range(3,9):
        for r in range(n+1):
            G=brute(n,r)
            assert G==predicted(n,r),(n,r)
            assert charpoly_from_traces(G)==predicted_charpoly(n,r),(n,r)
            p,s,t=formula(n,r)
            if 1<=r<=n-2:
                assert abs(t)<s
                assert p-t>0
                # The 2x2 radial block is nonsingular (positive definite).
                assert p*(p+(n-1)*t)-n*s*s>0
            if n%2 and r==(n-1)//2:
                assert p==Fraction(1,2) and t==0
            cases+=1
    return cases


def test_halfball():
    prev=None
    for n in range(3,201,2):
        p,s,t=formula(n,(n-1)//2)
        c2=Fraction(n)*s*s
        assert Fraction(0)<c2<Fraction(1,4)
        if prev is not None:
            assert c2<prev
            # Identity: c_n^2/c_(n-2)^2=1-(n-1)^(-2).
            assert c2/prev==1-Fraction(1,(n-1)**2)
        prev=c2
    return 99


def gaussian(z):
    Phi=(1+erf(z/sqrt(2)))/2
    phi=exp(-z*z/2)/sqrt(2*pi)
    lo=Phi-z*phi/2-phi*sqrt(1+z*z/4)
    hi=Phi-z*phi/2+phi*sqrt(1+z*z/4)
    return lo,Phi,hi


def eigs(n,r):
    p,s,t=formula(n,r)
    p,s,t=map(float,(p,s,t))
    center=p+(n-1)*t/2
    d=sqrt(((n-1)*t/2)**2+n*s*s)
    return center-d,p-t,center+d


def test_gaussian():
    for z in [-1.0,0.0,0.8]:
        n=1601
        r=int((n+z*sqrt(n))/2)
        expect=gaussian(z)
        got=eigs(n,r)
        assert max(abs(a-b) for a,b in zip(got,expect)) <0.02,(z,got,expect)
    return 3


if __name__=='__main__':
    print('VERIFY_OK', 'finite_cases=',test_finite(),'exact_monotone_cases=',test_halfball(), 'gaussian_checks=',test_gaussian())
