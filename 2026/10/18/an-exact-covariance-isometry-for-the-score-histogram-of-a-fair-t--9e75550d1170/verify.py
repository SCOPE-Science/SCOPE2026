"""Exact checks for the Pearson covariance projection in fair tournaments.
Run: python verify.py
Only Python's standard library is required.
"""
from fractions import Fraction as F
from itertools import product
from math import comb


def expected_covariance(n):
    """Exact n-by-n covariance from a shared-game calculation."""
    k = n - 1
    p = [F(comb(k, j), 2 ** k) for j in range(n)]
    a = [F(comb(k - 1, j), 2 ** (k - 1)) if 0 <= j <= k - 1 else F(0) for j in range(n)]
    d = [(a[j-1] if j > 0 else F(0)) - a[j] for j in range(n)]
    return p, d, [[n*(int(i == j)*p[i]-p[i]*p[j])-F(n*k,4)*d[i]*d[j]
                       for j in range(n)] for i in range(n)]


def exhaustive_covariance(n):
    """Enumerate all independent pair orientations, not score sequences."""
    pairs = [(i, j) for i in range(n) for j in range(i+1,n)]
    total = 1 << len(pairs)
    first = [0]*n
    second = [[0]*n for _ in range(n)]
    for b in range(total):
        deg = [0]*n
        for t,(u,v) in enumerate(pairs):
            deg[u if (b>>t)&1 else v] += 1
        h = [0]*n
        for z in deg:
            h[z] += 1
        assert sum(h) == n
        assert sum(j*h[j] for j in range(n)) == n*(n-1)//2
        for i in range(n):
            first[i] += h[i]
            for j in range(n):
                second[i][j] += h[i]*h[j]
    mean = [F(z,total) for z in first]
    cov = [[F(second[i][j],total)-mean[i]*mean[j] for j in range(n)] for i in range(n)]
    return mean,cov,total


def krawtchouk(k,r,j):
    """Coefficient of z^r in (1-z)^j (1+z)^(k-j)."""
    return sum((-1)**t*comb(j,t)*comb(k-j,r-t)
               for t in range(max(0,r-(k-j)),min(j,r)+1))


def test():
    checks=0
    configurations=0
    for n in range(2,9):
        p,d,s = expected_covariance(n)
        assert all(p[j]*F(2*(2*j-(n-1)),n-1)==d[j] for j in range(n)); checks+=n
        assert sum(d) == 0 and sum(p)==1;checks+=2
        assert all(sum(s[i][j] for j in range(n))==0 for i in range(n)); checks+=n
        assert all(sum(j*s[i][j] for j in range(n))==0 for i in range(n));checks+=n
        assert all(sum(s[i][j]/p[j]*s[j][l] for j in range(n))==n*s[i][l]
                   for i in range(n) for l in range(n));checks+=n*n
        assert sum(s[i][i]/p[i] for i in range(n))==n*(n-2);checks+=1
        if n<=6:
            mean,cov,num=exhaustive_covariance(n)
            configurations+=num
            assert all(mean[j]==n*p[j] for j in range(n));checks+=n
            assert all(cov[i][j]==s[i][j] for i in range(n) for j in range(n)); checks+=n*n
            # E Pearson X^2: exact, NOT a chi-square distribution claim.
            assert sum(cov[i][i]/(n*p[i]) for i in range(n))==n-2;checks+=1
        # Exact orthogonality of the binomial Krawtchouk basis, and of its
        # tournament additive statistics for all degrees >= 2.
        kk=[[krawtchouk(n-1,r,j) for j in range(n)] for r in range(n)]
        for r in range(n):
            for t in range(n):
                pop=sum(p[j]*kk[r][j]*kk[t][j] for j in range(n))
                assert pop==(comb(n-1,r) if r==t else 0)
                tournament=sum(s[i][j]*kk[r][i]*kk[t][j]
                               for i in range(n) for j in range(n))
                assert tournament==(n*comb(n-1,r) if r==t and r>=2 else 0)
                checks+=2
        # several nontrivial probes of the sharp residual variance identity.
        for f in ([j*j for j in range(n)], [(-1)**j for j in range(n)],
                  [j**3-2*j for j in range(n)]):
            mean_f=sum(p[j]*f[j] for j in range(n))
            mean_R=F(n-1,2)
            var_f=sum(p[j]*(f[j]-mean_f)**2 for j in range(n))
            cov_fR=sum(p[j]*(f[j]-mean_f)*(j-mean_R) for j in range(n))
            lhs=sum(s[i][j]*f[i]*f[j] for i in range(n) for j in range(n))
            rhs=n*(var_f - cov_fR**2 / F(n-1,4))
            assert lhs==rhs, (n,f,lhs,rhs); checks+=1
    print(f'PASS: {checks} exact identities; {configurations} exhaustively enumerated tournament orientations (n=2..6); symbolic score algebra n=2..8')


if __name__=='__main__':
    test()
