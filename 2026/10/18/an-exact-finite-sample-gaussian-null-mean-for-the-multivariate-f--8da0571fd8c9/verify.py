"""Independent numerical checks for an exact finite-sample Gaussian null mean.

Requires numpy and scipy. The finite-sample theorem is established analytically;
these tests compare two independent ways of evaluating its quantities.
"""
from math import pi, sqrt
import numpy as np
from scipy.integrate import quad
from scipy.special import beta as beta_fn, hyp1f1, poch


def laplace_moment(n, d, j, t):
    alpha, beta = d / 2, (n - 1) / 2
    return poch(alpha, j) / poch(beta, j) * hyp1f1(alpha + j, beta + j, -t)


def exact_mean(n, d, a):
    assert 1 <= d <= n - 1 and a > 0
    mm = lambda j, t: laplace_moment(n, d, j, t)
    first = n * (pi / (a + 1))**(d / 2) * d / (2*(a + 1))
    second = -2 * (2*pi / (2*a + 1))**(d/2) * n*(n-1) / (2*a + 1) * mm(1, (n-1)/(4*a+2))
    third = (pi/a)**(d/2)*(d+(n-1)/2*(d*mm(0,n/(2*a))-(n+1)*mm(1,n/(2*a))))
    return first + second + third


def raw_statistic(sample, a):
    n,d=sample.shape
    y=sample-sample.mean(axis=0)
    # Cholesky whitening preserves all pairwise inner products and distances.
    L=np.linalg.cholesky((y.T@y)/n)
    y=y@np.linalg.inv(L.T)
    G=y@y.T
    h=np.diag(G)
    D=np.maximum(h[:,None]+h[None,:]-2*G,0)
    first=n*(pi/(a+1))**(d/2)*d/(2*(a+1))
    second=-2*(2*pi/(2*a+1))**(d/2)*np.sum(h*np.exp(-h/(4*a+2)))/(2*a+1)
    third=(pi/a)**(d/2)*np.sum(G*np.exp(-D/(4*a)))/n
    return first+second+third


def main():
    checks=0
    # Independent beta-integral check of the confluent hypergeometric moments.
    for n,d in ((5,2),(7,3),(11,4),(15,2)):
        alpha=d/2; b=(n-d-1)/2
        for j in (0,1,2):
            for t in (0.1,0.9,2.4):
                numer=quad(lambda z: z**(alpha+j-1)*(1-z)**(b-1)*np.exp(-t*z),0,1,epsabs=1e-11)[0]/beta_fn(alpha,b)
                rhs=laplace_moment(n,d,j,t)
                assert abs(numer-rhs)<2e-9,(n,d,j,t,numer,rhs)
                checks+=1
    # The minimal sample n=d+1 always gives a regular simplex after whitening.
    rng=np.random.default_rng(20261014)
    for d,a in ((2,0.5),(3,1.2),(4,2.0)):
        n=d+1; rhs=exact_mean(n,d,a)
        for _ in range(20):
            observed=raw_statistic(rng.standard_normal((n,d)),a)
            assert abs(observed-rhs)<1e-8,(n,d,a,observed,rhs)
            checks+=1
    # Independent Gaussian-sampling verification of several nondegenerate means.
    configurations=((5,2,1.3),(7,3,2.0),(8,2,0.6),(10,3,1.0),(12,4,2.0))
    for n,d,a in configurations:
        vals=np.array([raw_statistic(rng.standard_normal((n,d)),a) for _ in range(1600)])
        se=vals.std(ddof=1)/sqrt(len(vals))
        err=abs(vals.mean()-exact_mean(n,d,a))
        assert err<6.0*se+0.02,(n,d,a,vals.mean(),exact_mean(n,d,a),se)
        checks+=1
    print('PASS',checks,'independent beta-integral, exact-simplex and Monte Carlo comparisons')
    print('Example: E[T_{5,2,1}] =',format(exact_mean(5,2,1),'.14g'))

if __name__=='__main__':main()
