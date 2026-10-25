"""Exact finite checks for age-indexed descendant size second moments."""
import itertools
from collections import Counter
from fractions import Fraction


def compute(n):
    counts = 0
    sums = [0] * (n + 1)
    products = [[0] * (n + 1) for _ in range(n + 1)]
    for parents in itertools.product(*(range(1, j) for j in range(2, n+1))):
        sz = [0] + [1]*n
        parent = [0, 0] + list(parents)
        for j in range(n, 1, -1):
            sz[parent[j]] += sz[j]
        counts += 1
        for i in range(1, n+1):
            si = sz[i]
            sums[i] += si
            for j in range(i, n+1):
                products[i][j] += si * sz[j]
    assert counts == __import__('math').factorial(n-1)
    assertions = 0
    for i in range(1, n+1):
        assert Fraction(sums[i], counts) == Fraction(n, i)
        assertions += 1
        for j in range(i, n+1):
            got = Fraction(products[i][j], counts) - Fraction(sums[i]*sums[j], counts**2)
            target = Fraction(n * (n-i)*(i-1), i*i*(i+1)) if i == j else Fraction(0)
            assert got == target, (n,i,j,got,target)
            assertions += 1
    total_variance = sum((Fraction(n*(n-i)*(i-1),i*i*(i+1)) for i in range(2,n+1)),Fraction(0))
    hn = sum((Fraction(1,k) for k in range(1,n+1)),Fraction(0))
    h2 = sum((Fraction(1,k*k) for k in range(1,n+1)),Fraction(0))
    assert total_variance == 2*n*n-n*hn-n*n*h2
    assertions += 1
    return assertions


if __name__ == '__main__':
    a=0
    for n in range(1,10):
        b=compute(n)
        a+=b
        print(n,b)
    # Pairwise uncorrelated need not mean independent:
    n=4; distribution=Counter()
    for parents in itertools.product(*(range(1,j) for j in range(2,n+1))):
        sz=[0]+[1]*n; p=[0,0]+list(parents)
        for j in range(n,1,-1):sz[p[j]]+=sz[j]
        distribution[sz[2],sz[3]]+=1
    assert distribution[(3,2)] == 1 and sum(distribution.values())==6
    print('VERIFY_OK',a,'exact equality assertions; dependent example validated')
