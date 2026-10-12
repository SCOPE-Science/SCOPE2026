"""Reproduce mixed third-cumulant identities for disjoint component types."""
from fractions import Fraction
from itertools import combinations
from math import factorial
from decimal import Decimal, getcontext


def empirical(n, p):
    edges = list(combinations(range(n), 2))
    numer = [0] * 7
    denominator = p.denominator ** len(edges)
    for mask in range(1 << len(edges)):
        adj = [0] * n
        m = 0
        for j, (u, v) in enumerate(edges):
            if (mask >> j) & 1:
                adj[u] |= 1 << v
                adj[v] |= 1 << u
                m += 1
        seen = 0
        comps = []
        for u in range(n):
            if (seen >> u) & 1:
                continue
            queue = [u]
            seen |= 1 << u
            for v in queue:
                for w in range(n):
                    if (adj[v] >> w) & 1 and not ((seen >> w) & 1):
                        seen |= 1 << w
                        queue.append(w)
            e = sum(adj[v].bit_count() for v in queue) // 2
            comps.append((len(queue), e))
        a = sum(k == 1 for k, e in comps)
        b = sum(k == 2 for k, e in comps)
        c = sum(k == 3 and e == 2 for k, e in comps)
        val = [a, b, c, a*b, a*c, b*c, a*b*c]
        w = p.numerator ** m * (p.denominator - p.numerator) ** (len(edges)-m)
        for j, x in enumerate(val):
            numer[j] += w*x
    return [Fraction(x, denominator) for x in numer]


def factor(n, sizes):
    if sum(sizes) > n:
        return Fraction(0)
    x = Fraction(1)
    for s in sizes:
        x *= factorial(n-s)
    x /= factorial(n) ** (len(sizes)-1) * factorial(n-sum(sizes))
    return x


def predicted(m, n, p):
    a,b,c,ab,ac,bc,abc = m
    q = 1-p
    mu=[a,b,c]
    sizes=[1,2,3]
    joint=[]
    for ids in ((0,1),(0,2),(1,2),(0,1,2)):
        ss=[sizes[i] for i in ids]
        cross=sum(sizes[i]*sizes[j] for i,j in combinations(ids,2))
        e=Fraction(1)
        for i in ids:
            e*=mu[i]
        joint.append(e * factor(n,ss) / q**cross)
    assert [ab,ac,bc,abc]==joint,(m,joint)
    cumulant=abc-ab*c-ac*b-bc*a+2*a*b*c
    normalized=cumulant/(a*b*c)
    rhs = factor(n,[1,2,3])/q**(1*2+1*3+2*3) - (factor(n,[1,2])/q**2 + factor(n,[1,3])/q**3 + factor(n,[2,3])/q**6) + 2
    assert normalized == rhs
    return cumulant


def R(n, sizes):
    result = Decimal(1)
    occupied = 0
    for k in sizes:
        for j in range(k):
            result *= Decimal(n-occupied-j)/Decimal(n-j)
        occupied += k
    return result


def analytic_F(n, a, b, c, lam):
    q = Decimal(1) - lam / Decimal(n)
    return R(n,[a,b,c])*q**(-(a*b+a*c+b*c)) - sum(
        R(n,[i,j])*q**(-i*j) for i,j in ((a,b),(a,c),(b,c))
    ) + 2


def run():
    n=6
    checks=0
    for p in (Fraction(1,5),Fraction(1,2),Fraction(4,5)):
        mom=empirical(n,p)
        predicted(mom,n,p)
        checks+=5
    getcontext().prec=75
    asym=0
    for n in (10000,50000):
        for sizes in ((1,2,3),(1,2,4),(2,3,4),(2,2,2)):
            a,b,c=sizes
            for lam in (Decimal('0.2'),Decimal('0.7'),Decimal('1'),Decimal('1.3'),Decimal('2')):
                left=n*n*analytic_F(n,a,b,c,lam)
                target=a*b*c*((a+b+c)*(lam-1)**2-1)
                assert abs(left-target) < Decimal('0.15'),(sizes,lam,left,target)
                asym+=1
    for n in (30,100,1000):
        a,b,c=1,2,3
        s=a+b+c
        delta=Decimal('0.10')
        lo=1-1/Decimal(s).sqrt()
        hi=1+1/Decimal(s).sqrt()
        assert analytic_F(n,a,b,c,lo-delta)>0
        assert analytic_F(n,a,b,c,lo+delta)<0
        assert analytic_F(n,a,b,c,hi-delta)<0
        assert analytic_F(n,a,b,c,hi+delta)>0
    print('VERIFY_OK exact_moments=%d enumerated_graphs=%d asymptotic_checks=%d signs=12'%(checks,2**15,asym))


if __name__ == '__main__':
    run()
