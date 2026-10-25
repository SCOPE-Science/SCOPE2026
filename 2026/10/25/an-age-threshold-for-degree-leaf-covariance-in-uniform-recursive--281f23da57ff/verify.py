"""Exact checks for the degree/leaf covariance of uniform recursive trees.

Run with Python 3.9 or later: python verify.py
This independent enumerator is supplementary to the all-n proof.
"""
from fractions import Fraction
from itertools import product
from math import factorial

checks = 0
def check(actual, expected, context):
    global checks
    checks += 1
    if actual != expected:
        raise AssertionError(f"{context}: {actual} != {expected}")


def theoretical(n, i, j):
    """Covariance(outdegree of vertex i, leaf indicator of vertex j)."""
    if j == 1:
        return Fraction(0)
    if i == j:
        return -Fraction(j-1, n-1) * sum((Fraction(1, t) for t in range(j, n)), Fraction(0))
    m = max(i, j)
    return Fraction(j-1, n-1) * (Fraction(1, m-1) - Fraction(1, n-1))


def total_covariance(n, i):
    if i == 1:
        return Fraction(n-2, 2*(n-1))
    return (Fraction((n-i)*(n-3), 2*(n-1)**2)
            - Fraction(i-1, n-1)*sum((Fraction(1,t) for t in range(i,n)),Fraction(0)))


def enumerate_moments(n):
    out_sums = [0]*n
    leaf_sums = [0]*n
    cross_sums = [[0]*n for _ in range(n)]
    count=0
    for parents in product(*(range(t-1) for t in range(2,n+1))):
        children=[0]*n
        for parent in parents:
            children[parent]+=1
        leaves=[int(z == 0) for z in children]
        count+=1
        for i in range(n):
            out_sums[i]+=children[i]
            leaf_sums[i]+=leaves[i]
            for j in range(n):
                cross_sums[i][j]+=children[i]*leaves[j]
    check(count, factorial(n-1),f"tree count n={n}")
    for i in range(n):
        for j in range(n):
            actual=(Fraction(cross_sums[i][j],count)
                    - Fraction(out_sums[i]*leaf_sums[j],count*count))
            check(actual,theoretical(n,i+1,j+1),f"entry n={n}, i={i+1}, j={j+1}")
        row = (Fraction(sum(cross_sums[i]),count)
               - Fraction(out_sums[i]*sum(leaf_sums),count*count))
        check(row,total_covariance(n,i+1),f"row n={n}, i={i+1}")
    return count

total_trees=0
for n in range(2,10):
    total_trees+=enumerate_moments(n)
for n in range(3,201):
    row=[total_covariance(n,i) for i in range(1,n+1)]
    check(sum(row,Fraction(0)),Fraction(0),f"degree-sum constant {n}")
    check(row[0]>0,True,f"root sign {n}")
    check(row[-1],Fraction(0),f"newest degree zero {n}")
    check(row[-2]<0,True,f"next-newest sign {n}")
    for i in range(2,n-1):
        check(row[i+1]-2*row[i]+row[i-1],Fraction(1,i*(n-1)),f"convexity {n} i={i+1}")
    for i in range(2,n):
        if row[i-1]<=0:
            check(all(v<0 for v in row[i:n-1]),True,f"single crossing {n} i={i}")
print(f"VERIFY_OK {checks} exact assertions; {total_trees} enumerated trees")
