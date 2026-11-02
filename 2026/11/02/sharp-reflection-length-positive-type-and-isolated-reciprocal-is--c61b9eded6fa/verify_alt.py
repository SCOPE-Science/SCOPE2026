#!/usr/bin/env python3
"""Exact rational tests for the finite alternating-group cycle kernel theorem.
Requires only the Python 3 standard library. This is finite corroboration, not
an exhaustive proof of the theorem for all group orders.
"""
from fractions import Fraction as F
from math import comb, factorial
from itertools import permutations


def partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    if maximum is None:
        maximum = n
    for part in range(min(n, maximum), 0, -1):
        for rest in partitions(n - part, part):
            yield (part,) + rest


def contents(shape):
    return [j - i for i, length in enumerate(shape) for j in range(length)]


def scalar_even(shape, q):
    p = F(1)
    r = F(1)
    for c in contents(shape):
        p *= 1 + q*c
        r *= 1 - q*c
    return (p+r)/2


def tableau_dimension(shape):
    n = sum(shape)
    h = 1
    for i, length in enumerate(shape):
        for j in range(length):
            h *= length - j + sum(row > j for row in shape[i+1:])
    return factorial(n)//h


def even_sign(p):
    n = len(p)
    inv = sum(p[i] > p[j] for i in range(n) for j in range(i+1,n))
    return inv % 2 == 0


def cycle_count(p):
    n=len(p)
    seen=set(); count=0
    for i in range(n):
        if i not in seen:
            count += 1
            j = i
            while j not in seen:
                seen.add(j)
                j=p[j]
    return count


def symmetric_psd(M):
    """Exact symmetric-elimination PSD check; also returns rank."""
    n=len(M); rank=0
    A=[row[:] for row in M]
    for i in range(n):
        p=A[i][i]
        if p<0:
            return False, rank
        if p==0:
            if any(A[i][j] != 0 for j in range(i+1,n)):
                return False, rank
            continue
        rank+=1
        for j in range(i+1,n):
            if A[j][i]==0: continue
            for k in range(j,n):
                A[j][k] -= A[j][i]*A[i][k]/p
            for k in range(j,n):
                A[k][j]=A[j][k]
        for j in range(i+1,n):
            A[j][i]=A[i][j]=F(0)
    return True, rank


def main():
    tested=0
    for n in range(3, 14):
        m=(n-1)//2
        shapes=list(partitions(n))
        samples={F(0), F(1), F(1,m), F(1,2*m), F(1, m+1)}
        if m>1:
            samples.add((F(1,m)+F(1,m-1))/2)
            samples.update(F(1,k) for k in range(1,m))
        for q in samples:
            actual=all(scalar_even(p,q)>=0 for p in shapes)
            expected=(q<=F(1,m) or (q.numerator == 1 and q.denominator<m))
            assert actual==expected, (n,q,actual,expected)
            tested+=1
        if n in (2*m+1,2*m+2):
            missing = sum(tableau_dimension(p)**2 for p in shapes
                          if len(p)>m and p[0]>m)//2
            if n==2*m+1:
                expect=comb(2*m,m)**2//2
            else:
                fh=comb(2*m+1,m)
                fs=(2*m*m*comb(2*m,m))//(m+1)
                expect=fh**2+fs**2//2
            assert missing==expect, (n,missing,expect)
            assert missing + sum(tableau_dimension(p)**2 for p in shapes
                                 if len(p)<=m or p[0]<=m)//2 == factorial(n)//2
            tested+=1
    # Direct finite group matrices: kernel on A_5 (60x60), exact rational.
    perms=[p for p in permutations(range(5)) if even_sign(p)]
    assert len(perms)==60
    for q,expected_rank,expected_psd in [(F(0),60,True),(F(2,5),60,True),
                                          (F(1,2),42,True),(F(3,5),None,False),
                                          (F(1),1,True)]:
        dist=[]
        for a in perms:
            dist.append([5-cycle_count(tuple(a.index(b[j]) for j in range(5))) for b in perms])
        assert all(d%2==0 for row in dist for d in row)
        M=[[q**d for d in row] for row in dist]
        psd,rank=symmetric_psd(M)
        assert psd==expected_psd,(q,psd)
        if expected_psd:
            assert rank==expected_rank,(q,rank,expected_rank)
        tested+=1
    print('VERIFY_OK exact checks:',tested, '; orders n=3..13, direct matrices on A5')

if __name__=='__main__': main()
