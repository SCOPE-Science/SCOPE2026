"""Independent exact-arithmetic checks for uniform spacing/sample-variance covariance.

Requires Python 3 standard library only. These finite checks supplement the
all-sample-size proof; they do not establish an infinite theorem themselves.
"""

from fractions import Fraction
from math import factorial, isqrt


def formula(n: int, r: int) -> Fraction:
    assert n >= 2 and 0 <= r <= n
    return Fraction(6*r*(n-r)-n*(n-1), 6*n*(n-1)*(n+1)*(n+3))


def dirichlet_monomial(moment_indices, M):
    """E product(G_j): Dirichlet(1,...,1), M coordinates.

    Multiplicity factorial formula gives an independent expansion into
    individual monomials; no conditional spacing lemma is used here.
    """
    counts = {}
    for j in moment_indices:
        counts[j] = counts.get(j, 0) + 1
    numerator = 1
    for amount in counts.values():
        numerator *= factorial(amount)
    denominator = 1
    for i in range(len(moment_indices)):
        denominator *= M+i
    return Fraction(numerator, denominator)


def direct_covariance(n: int, r: int) -> Fraction:
    """Expand unbiased sample variance into ordered-pair gap monomials.

    O(n^4) ordered terms: deliberately independent of closed formula and
    of the analytic pair-overlap covariance simplification.
    """
    M=n+1
    q=Fraction(0)
    gq=Fraction(0)
    for a in range(1,n+1):
        for b in range(a+1,n+1):
            for i in range(a,b):
                for j in range(a,b):
                    q+=dirichlet_monomial((i,j),M)
                    gq+=dirichlet_monomial((r,i,j),M)
    scale=n*(n-1)
    return (gq-Fraction(q,M))/scale


def run():
    checks=0
    for n in range(2,19):
        all_cov=Fraction(0)
        for r in range(n+1):
            observed=direct_covariance(n,r)
            expected=formula(n,r)
            assert observed == expected,(n,r,observed,expected)
            all_cov+=expected
            checks+=1
        assert all_cov==0,('simplex sum of gaps',n)
        checks+=1
        # Check full all-size sign classification for every tested rank.
        for r in range(n+1):
            numerator=6*r*(n-r)-n*(n-1)
            assert (formula(n,r)>0)-(formula(n,r)<0) == ((numerator>0)-(numerator<0))
            checks+=1

    # Pell roots: x+y sqrt(3)=(2+sqrt(3))^k, n=x-1, r=(n+-y)/2.
    x,y=1,0
    predicted=set()
    for k in range(1,13):
        x,y=2*x+3*y,x+2*y
        n=x-1
        assert x*x-3*y*y==1
        if k>=2:
            assert n>y and (n-y)%2==0
            lo,hi=(n-y)//2,(n+y)//2
            assert formula(n,lo)==0 and formula(n,hi)==0
            predicted.update([(n,lo),(n,hi)])
        checks+=1
    # Exhaustive arithmetic zero-index check across small sample sizes.
    for n in range(2,2001):
        disc=n*(n+2)
        # Pell iff disc/3 a perfect square with correct gap parity.
        is_pell = disc%3==0 and isqrt(disc//3)**2==disc//3
        hits=[r for r in range(n+1) if 6*r*(n-r)==n*(n-1)]
        assert (len(hits)==2)==is_pell,(n,hits)
        if hits:
            assert set(hits)=={r for N,r in predicted if N==n}
        checks+=1
    return checks


if __name__=='__main__':
    result=run()
    print(f'PASS: {result} exact-arithmetic checks including full-gap direct moments, symmetry, and Pell zero ranks')
