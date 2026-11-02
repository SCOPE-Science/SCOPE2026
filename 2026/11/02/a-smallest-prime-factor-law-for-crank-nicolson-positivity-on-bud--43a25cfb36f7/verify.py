"""Standalone reproducibility tests for the multipartite diffusion claim.

Only the Python standard library is needed. Exact fractions check the full
resolvent; floating-point arithmetic is used solely for diagnostic comparison
of the explicit radical thresholds across many finite partitions.
"""
from fractions import Fraction as F
from math import sqrt, isclose


def partitions(n, minimum=1):
    if n == 0:
        yield ()
        return
    for first in range(minimum, n + 1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def laplacian(parts):
    n = sum(parts)
    group = []
    for j, count in enumerate(parts):
        group.extend([j] * count)
    result = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and group[i] != group[j]:
                result[i][i] += 1
                result[i][j] -= 1
    return result


def invert(matrix):
    n = len(matrix)
    a = [[F(x) for x in row] + [F(i == j) for j in range(n)]
         for i, row in enumerate(matrix)]
    for k in range(n):
        pivot = next(j for j in range(k, n) if a[j][k])
        a[k], a[pivot] = a[pivot], a[k]
        scale = a[k][k]
        a[k] = [v / scale for v in a[k]]
        for j in range(n):
            if j != k:
                factor = a[j][k]
                if factor:
                    a[j] = [x - factor*y for x, y in zip(a[j], a[k])]
    return [row[n:] for row in a]


def return_value(n, a, s):
    return (F(1,n) + F(n-a, a*n*(1+n*s))
            + F(a-1, a*(1+(n-a)*s)))


def sigma(n, a):
    return (a + sqrt(a*a + 4*(n-2)*(n-a))) / (2*(n-2)*(n-a))


def edge_count(parts):
    n = sum(parts)
    return (n*n - sum(a*a for a in parts)) // 2


def smallest_prime_factor(n):
    for x in range(2, n + 1):
        if n % x == 0:
            return x
    raise AssertionError


checks = 0
# Exact matrix inversion: no spectral formula assumed in this test.
for n in range(3, 10):
    for p in partitions(n):
        if len(p) < 2:
            continue
        groups = [i for i,a in enumerate(p) for _ in range(a)]
        L = laplacian(p)
        for s in (F(1, 10), F(1, 3), F(4, 5)):
            A = [[F(i==j) + s*L[i][j] for j in range(n)] for i in range(n)]
            R = invert(A)
            for i in range(n):
                assert R[i][i] == return_value(n, p[groups[i]], s)
                assert sum(R[i]) == 1
                for j in range(n):
                    if i != j:
                        assert R[i][j] > 0
            checks += 1

# Verify the quadratic crossing exactly at rational points on opposite sides.
# A fractional rational bracket is independent of floating spectral routines.
for n in range(3, 85):
    for a in range(1, n//2 + 1):
        z = sigma(n, a)
        lo = F(int(z*10**7)-1,10**7)
        hi = F(int(z*10**7)+2,10**7)
        if lo <= 0:
            continue
        q = lambda x: 1 + a*x - (n-2)*(n-a)*x*x
        assert q(lo)>0 and q(hi)<0
        # Exact inequality behind the derivative/partition comparison.
        D2 = a*a + 4*(n-2)*(n-a)
        assert (n+2)**2*D2 >= n*n*(2*n-a)**2
        checks += 1

# Direct endpoint checks with budget B=1 and full dense matrices.
for n in range(3, 9):
    for p in partitions(n):
        if len(p)<2:continue
        E = edge_count(p)
        a = p[0]
        v = sigma(n,a)
        lower = F(int(v*10**6)-1,10**6)
        upper = F(int(v*10**6)+2,10**6)
        if lower<=0:continue
        L=laplacian(p)
        for s, expected in ((lower,True),(upper,False)):
            A = [[F(i==j)+s*L[i][j] for j in range(n)] for i in range(n)]
            R=invert(A)
            C=[[2*R[i][j]-F(i==j) for j in range(n)] for i in range(n)]
            assert (all(x>=0 for row in C for x in row)) is expected
            # Under conductance B/E, physical step h=2E*s produces the same matrix.
            assert E>0
            checks+=1

# Exhaust every partition through order 18, including nonbalanced families.
for n in range(3,19):
    prime=smallest_prime_factor(n)
    d=n//prime
    best=edge_count((d,)*prime)*sigma(n,d)
    n_ties=0
    for p in partitions(n):
        if len(p)<2:continue
        score=edge_count(p)*sigma(n,p[0])
        assert score < best + 1e-8
        if abs(score-best)<1e-8:
            assert p==(d,)*prime
            n_ties+=1
        checks+=1
    assert n_ties==1

# Broader stress test: for fixed number of parts, the most balanced shape
# maximizes edges; compare every such competitor for n up to 1000.
for n in range(3,1001):
    p=smallest_prime_factor(n)
    d=n//p
    best=edge_count((d,)*p)*sigma(n,d)
    for k in range(2,n+1):
        q,r=divmod(n,k)
        e=(n*n - (k-r)*q*q-r*(q+1)*(q+1))//2
        score=e*sigma(n,q)
        assert score<=best+1e-7*max(1,best)
        if abs(score-best)<1e-9:
            assert k==p and r==0
        checks+=1

print('VERIFY_OK',checks)
