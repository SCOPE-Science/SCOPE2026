"""Exact finite checks for descent-indicator covariance in uniform involutions.

This finite verifier complements, rather than replaces, the unrestricted proof.
Run with Python 3: python check.py
"""
from fractions import Fraction
from collections import defaultdict
from math import factorial


def involutions(items):
    if not items:
        yield ()
        return
    first, *tail = items
    for rest in involutions(tuple(tail)):
        yield ((first, first),) + rest
    for idx, other in enumerate(tail):
        for rest in involutions(tuple(tail[:idx] + tail[idx + 1:])):
            yield ((first, other),) + rest


def falling(a, r):
    ans = 1
    for j in range(r):
        ans *= a - j
    return ans


def pair_ratio(n, f, removed, fixed_removed):
    """I(n-removed,f-fixed_removed)/I(n,f); zero if parameters impossible."""
    k = (removed - fixed_removed) // 2
    if (removed - fixed_removed) % 2 or k < 0 or f < fixed_removed:
        return Fraction(0)
    if n - f < 2*k or n < removed:
        return Fraction(0)
    num = falling(f, fixed_removed)
    for j in range(k):
        num *= n - f - 2*j
    return Fraction(num, falling(n, removed))


def closed(n, f):
    assert n >= 4 and 0 <= f <= n and (n-f)%2 == 0
    r20 = pair_ratio(n,f,2,0)
    r22 = pair_ratio(n,f,2,2)
    r40 = pair_ratio(n,f,4,0)
    r42 = pair_ratio(n,f,4,2)
    r44 = pair_ratio(n,f,4,4)
    r33 = pair_ratio(n,f,3,3)
    a2=(1-r20+r22)/2
    a3=(1-3*r20+3*r22+2*r33)/6
    a22=(1-2*r20+3*r40+2*r22-2*r42+r44)/4
    p=1-a2
    cov=a22-a2*a2
    b=(2*n-3)*f**3-n*f*f+n*n*f-n*n*(n-2)
    target=Fraction((f-n)*b,2*n*n*(n-3)*(n-2)*(n-1)**2)
    assert cov==target
    return p, a3, a22, target


def brute(n):
    stats=defaultdict(lambda: [0,[0]*(n-1),[[0]*(n-1) for _ in range(n-1)]])
    for pairs in involutions(tuple(range(n))):
        p=list(range(n)); f=0
        for a,b in pairs:
            p[a]=b; p[b]=a
            if a==b: f+=1
        desc=[int(p[j]>p[j+1]) for j in range(n-1)]
        vals=stats[f]; vals[0]+=1
        for i in range(n-1):
            vals[1][i]+=desc[i]
            for j in range(i+1,n-1):
                vals[2][i][j]+=desc[i]*desc[j]
    comparisons=0
    for f,(count,ones,twos) in stats.items():
        predicted=factorial(n)//(2**((n-f)//2)*factorial((n-f)//2)*factorial(f))
        assert count==predicted
        comparisons+=1
        p,a3,a22,cov=closed(n,f)
        for i in range(n-1):
            assert Fraction(ones[i],count)==p
            comparisons+=1
            for j in range(i+1,n-1):
                both=Fraction(twos[i][j],count)
                if j==i+1:
                    assert both==1-2*(1-p)+a3
                else:
                    assert both-p*p==cov
                    assert both==1-2*(1-p)+a22
                comparisons+=1
    return comparisons, sum(v[0] for v in stats.values())


def main():
    comparisons=0; total=0
    for n in range(4,12):
        checks, count=brute(n)
        print('n',n,'involutions',count,'exact comparisons',checks)
        comparisons+=checks; total+=count
    for n in range(4,101):
        for f in range(n%2,n+1,2):
            closed(n,f)
            comparisons+=1
    print('PASS:',comparisons,'exact comparisons,',total,'involutions enumerated; analytic proof required for arbitrary n')


if __name__=='__main__':
    main()
