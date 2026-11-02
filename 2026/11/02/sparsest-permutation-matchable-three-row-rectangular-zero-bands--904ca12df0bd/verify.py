"""Independent exhaustive verification of sparse 3-by-q support classification.
Counts structure matrices with labeled rows and labeled columns, no external packages.
"""
from itertools import combinations_with_replacement
from collections import Counter
from math import factorial,prod

def balanced(columns):
    q=len(columns)
    return all(3*sum(bool(c&X) for c in columns) >=q*X.bit_count() for X in range(1,8))

def formula(q):
    k,r=divmod(q,3)
    if r==0:return q, factorial(q)//factorial(k)**3
    if r==1:
        first=q*factorial(3*k)//factorial(k)**3
        second=0 if k==0 else 3*q*(q-1)*factorial(3*k-1)//(factorial(k-1)*factorial(k)**2)
        return q+2,first+second
    return q+2,3*q*(q-1)*factorial(3*k)//factorial(k)**3

def exhaustive(q):
    counts=Counter()
    for cols in combinations_with_replacement(range(1,8),q):
        if not balanced(cols):continue
        m=Counter(cols); labeled=factorial(q)//prod(factorial(z) for z in m.values())
        counts[sum(c.bit_count() for c in cols)]+=labeled
    s=min(counts)
    return s,counts[s]

if __name__=='__main__':
    for q in range(1,11):
        got=exhaustive(q)
        expected=formula(q)
        assert got==expected,(q,got,expected)
        print(q,got)
    print('ALL_CHECKS_PASSED')
