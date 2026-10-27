"""Exact independent enumeration for the Latin-square isotopy ascent moment law.

Uses integers and rational arithmetic; no external dependencies.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial


def intercalates(A):
    n = len(A)
    return sum(
        A[r][c] == A[s][d] and A[r][d] == A[s][c]
        for r in range(n) for s in range(r+1,n)
        for c in range(n) for d in range(c+1,n)
    )


def moments(A):
    n = len(A)
    P = list(permutations(range(n)))
    total = total2 = 0
    for row in P:
        edges = [(A[row[i]][j], A[row[i+1]][j])
                 for i in range(n-1) for j in range(n)]
        for sym in P:
            v = sum(sym[a] < sym[b] for a,b in edges)
            total += v
            total2 += v*v
    m = Fraction(total,factorial(n)**2)
    var = Fraction(total2,factorial(n)**2)-m*m
    return m,var


def reduced(n):
    sq = [[j for j in range(n)]]+[[0]*n for _ in range(n-1)]
    columns = [1<<j for j in range(n)]
    def visit(i,j):
        if i==n:
            yield tuple(tuple(row) for row in sq)
            return
        if j==n:
            yield from visit(i+1,0)
            return
        choices = [i] if j==0 else range(n)
        for v in choices:
            if (columns[j]>>v)&1 or v in sq[i][:j]:
                continue
            sq[i][j]=v
            columns[j]|=1<<v
            yield from visit(i,j+1)
            columns[j]^=1<<v
    yield from visit(1,0)


def verify(A):
    n=len(A)
    assert all(sorted(row)==list(range(n)) for row in A)
    assert all(sorted(A[r][c] for r in range(n))==list(range(n)) for c in range(n))
    mean,var=moments(A)
    expected=Fraction(n*(n-1),2)
    predicted=Fraction(n*(n+1),12)-Fraction((n+1)*intercalates(A),3*n*(n-1))
    assert mean==expected and var==predicted,(A,mean,var,predicted)
    return intercalates(A),var


def cyclic(n):
    return [[(i+j)%n for j in range(n)] for i in range(n)]


if __name__=='__main__':
    from collections import Counter
    print('cyclic and elementary-two group tests:')
    for n in (2,3,4,5,6):
        t,v=verify(cyclic(n))
        print('cyclic',n,'intercalates',t,'variance',v)
    for n in (4,):
        A=[[i^j for j in range(n)] for i in range(n)]
        t,v=verify(A)
        print('elementary abelian 2-group',n,'intercalates',t,'variance',v)
    counts=Counter()
    checked=0
    for A in reduced(5):
        t,v=verify(A)
        counts[(t,str(v))]+=1
        checked+=1
    assert checked==56
    print('all 56 reduced order-five Latin squares:')
    for key,multiplicity in sorted(counts.items()):
        print('I,variance,count',key[0],key[1],multiplicity)
    print('EXACT_ORBIT_MOMENTS_VERIFIED')
