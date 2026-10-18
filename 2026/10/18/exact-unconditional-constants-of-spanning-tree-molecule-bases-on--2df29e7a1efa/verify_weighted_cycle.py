"""Independent rational dual-polytope checks for weighted-cycle edge bases.

Usage: python3 verify_weighted_cycle.py
No nonstandard dependencies.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def dual_vertices(w):
    """All possible vertices of {y : sum y=0, |y_i|<=w_i}."""
    n = len(w)
    out = set()
    for free in range(n):
        idx = [i for i in range(n) if i != free]
        for signs in product((-1, 1), repeat=n-1):
            y = [F(0)] * n
            for i, sign in zip(idx, signs):
                y[i] = sign*w[i]
            y[free] = -sum(y)
            if abs(y[free]) <= w[free]:
                out.add(tuple(y))
    return sorted(out)


def direct_unconditional_constant(w, omit):
    """Exact dual-polytope operator norm, with no quotient median calculation."""
    vertices = dual_vertices(w)
    n = len(w)
    result = F(1)
    for signs in product((-1, 1), repeat=n-1):
        coeff = list(signs)
        for v in vertices:
            numer = abs(sum(s*v[i] for s,i in zip(coeff, (j for j in range(n) if j!=omit))))
            result = max(result, numer / w[omit])
    return result


def claimed_constant(w, omit):
    other = [w[i] for i in range(len(w)) if i != omit]
    S = sum(other)
    discrepancy = min(abs(sum(s*a for s,a in zip(signs,other))) for signs in product((-1,1),repeat=len(other)))
    return min(S, w[omit]+S-discrepancy)/w[omit]


def main():
    rng = Random(100123)
    checked = 0
    for n, trials in ((3,20),(4,20),(5,15),(6,8),(7,3)):
        for _ in range(trials):
            w = [F(rng.randrange(1,15),rng.randrange(1,5)) for i in range(n)]
            while 2*max(w)>sum(w):
                w=[v+F(10) for v in w]
            for k in range(n):
                a = direct_unconditional_constant(w,k)
                b = claimed_constant(w,k)
                assert a == b,(n,w,k,a,b)
                checked+=1
    # Exact unit-weight profiles.
    for n in range(3,9):
        w=[F(1)]*n
        assert claimed_constant(w,n-1)==F(n-1)
    # Integer edge sets encode instances of the PARTITION decision problem.
    for a in ((1,1,2,2),(2,4,6),(2,2,2,2,2),(2,3,5,7,9),(1,1,1,1,1,1)):
        w=[F(2*x) for x in a]+[F(1)]
        assert 2*max(w)<=sum(w)
        optimum=claimed_constant(w,len(w)-1)
        threshold=sum(w[:-1])/w[-1]
        is_partitionable=any(sum(s*x for s,x in zip(sign,a))==0 for sign in product((-1,1),repeat=len(a)))
        assert (optimum==threshold)==is_partitionable
    print('PASS exact dual-polytope independent comparisons:',checked)
    print('PASS unit cycles 3 through 8 and integer partition witnesses')

if __name__=='__main__':
    main()
