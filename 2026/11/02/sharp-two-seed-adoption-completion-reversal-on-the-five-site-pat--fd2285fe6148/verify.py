"""Reproduce exact small-path Bass adoption completion-time identities.

Python 3.9+; standard library only.  All polynomial comparisons are exact.
"""
from functools import lru_cache
from fractions import Fraction
from itertools import combinations


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def neg(a):
    return tuple(-v for v in a)


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c)


def product(*p):
    v = (1,)
    for q in p:
        v = mul(v, q)
    return v


def ratadd(u, v):
    return (add(mul(u[0],v[1]),mul(v[0],u[1])),mul(u[1],v[1]))


def ratmul(u,v):
    return mul(u[0],v[0]),mul(u[1],v[1])


def ratdivpoly(u,p):
    return u[0],mul(u[1],p)


def ratpoly(p):
    return p,(1,)


def equal(u,v):
    return sub(mul(u[0],v[1]),mul(v[0],u[1])) == (0,)


def P(*a):
    return tuple(a)


def S(n):
    @lru_cache(None)
    def t(mask):
        if mask == (1<<n)-1:
            return ratpoly(P(0))
        transitions = []
        for i in range(n):
            if not (mask>>i)&1:
                k = int(i>0 and bool(mask & (1<<(i-1)))) + int(i<n-1 and bool(mask & (1<<(i+1))))
                transitions.append((i,P(1,k)))
        result = ratpoly(P(1))
        total_rate = P(0)
        for i, rate in transitions:
            result = ratadd(result,ratmul(ratpoly(rate),t(mask | (1<<i))))
            total_rate = add(total_rate,rate)
        return ratdivpoly(result,total_rate)
    return lambda pair: t(sum(1<<i for i in pair))


def as_ratio(num, *factors):
    return (num,product(*factors))


def check_symbolic():
    total=0
    d=S(5)
    # Representatives of all ten two-seed configurations under reflection.
    formulas={
      (0,1): as_ratio(P(44,180,261,158,36),P(2,),P(1,1),P(2,1),P(3,1),P(1,2),P(2,3)),
      (0,2): as_ratio(P(44,156,185,74),P(6,),P(1,1),P(2,1),P(1,2),P(2,3)),
      (0,3): as_ratio(P(22,67,52),P(6,),P(1,1),P(1,2),P(2,3)),
      (0,4): as_ratio(P(11,12),P(2,),P(1,2),P(3,2)),
      (1,2): as_ratio(P(44,200,325,221,54),P(2,),P(1,1),P(2,1),P(1,2),P(3,2),P(2,3)),
      (1,3): as_ratio(P(22,99,150,76),P(2,),P(1,1),P(1,2),P(2,3),P(3,4)),
    }
    for pair,formula in formulas.items():
        assert equal(d(pair),formula),pair
        total+=1
    for pair in combinations(range(5),2):
        reflected=tuple(sorted(4-j for j in pair))
        assert equal(d(pair),d(reflected)),pair
        total+=1
    # Rational differences against the two only possible optimizers.
    posdif={
      ((0,1),(0,3)): as_ratio(P(0,28,114,147,56),P(6,),P(1,1),P(2,1),P(3,1),P(1,2),P(2,3)),
      ((0,2),(0,3)): as_ratio(P(0,0,7,11),P(3,),P(1,1),P(2,1),P(1,2),P(2,3)),
      ((1,2),(0,3)): as_ratio(P(0,44,150,165,58),P(6,),P(1,1),P(2,1),P(1,2),P(3,2),P(2,3)),
      ((1,3),(0,3)): as_ratio(P(0,4,5),P(3,),P(1,1),P(2,3),P(3,4)),
      ((0,1),(0,4)): as_ratio(P(0,44,168,236,151,36),P(2,),P(1,1),P(2,1),P(3,1),P(1,2),P(3,2),P(2,3)),
      ((0,2),(0,4)): as_ratio(product(P(0,1),P(4,5),P(4,13,8)),P(6,),P(1,1),P(2,1),P(1,2),P(3,2),P(2,3)),
      ((1,2),(0,4)): as_ratio(P(0,10,30,28,9),P(1,1),P(2,1),P(1,2),P(3,2),P(2,3)),
      ((1,3),(0,4)): as_ratio(P(0,16,53,48,8),P(2,),P(1,1),P(1,2),P(3,2),P(2,3),P(3,4)),
    }
    for (c,e),expected in posdif.items():
        actual=ratadd(d(c),ratmul(ratpoly(P(-1)),d(e)))
        assert equal(actual,expected),(c,e)
        # Every numerator coefficient is nonnegative and is not identically zero.
        assert all(v>=0 for v in expected[0]) and any(v>0 for v in expected[0])
        total+=2
    # The sole competing pair has an explicitly factored sign polynomial.
    actual=ratadd(d((0,4)),ratmul(ratpoly(P(-1)),d((0,3))))
    expected=as_ratio(P(0,-8,-11,4),P(6,),P(1,1),P(1,2),P(3,2),P(2,3))
    assert equal(actual,expected)
    total+=1
    # Lower-order paths never undergo the five-node seed-choice reversal.
    d3=S(3)
    assert equal(ratadd(d3((0,1)),ratmul(ratpoly(P(-1)),d3((0,2)))),
      as_ratio(P(0,1),P(1,1),P(1,2)))
    total+=1
    d4=S(4)
    cases={
      (0,1):as_ratio(P(0,3,4),P(2,),P(1,1),P(2,1),P(1,2)),
      (0,2):as_ratio(P(0,1),P(2,),P(1,1),P(2,3)),
      (1,2):as_ratio(P(0,1),P(1,1),P(1,2)),
    }
    for pair,expected in cases.items():
        actual=ratadd(d4(pair),ratmul(ratpoly(P(-1)),d4((0,3))))
        assert equal(actual,expected),pair
        total+=1
    return total


def check_independent_evaluations():
    total=0
    for n in (3,4,5):
        symbolic=S(n)
        for q in (Fraction(1,100),Fraction(1,3),Fraction(1),Fraction(2),Fraction(3),Fraction(4),Fraction(10),Fraction(100)):
            from fractions import Fraction as Q
            @lru_cache(None)
            def f(mask):
                if mask == (1<<n)-1:return Q(0)
                rr=[]
                for j in range(n):
                    if not(mask>>j&1):
                        k=sum(bool(mask & (1<<k)) for k in (j-1,j+1) if 0<=k<n)
                        rr.append((j,1+q*k))
                return (1+sum(r*f(mask|1<<j) for j,r in rr))/sum(r for j,r in rr)
            for pair in combinations(range(n),2):
                symbolic_ratio=symbolic(pair)
                def val(poly): return sum(c*q**j for j,c in enumerate(poly))
                assert f(sum(1<<j for j in pair)) == val(symbolic_ratio[0])/val(symbolic_ratio[1])
                total+=1
    return total


if __name__=='__main__':
    a=check_symbolic()
    b=check_independent_evaluations()
    print('PASS: %d symbolic identities/positivity statements and %d independent exact-rational cross-checks.'%(a,b))
