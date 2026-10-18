#!/usr/bin/env python3
"""Exhaustive checks of idempotent-count moments for random invertible structure matrices.
Uses only Python's standard library and the field models listed below.
"""
from fractions import Fraction
from itertools import product
from math import comb
from collections import Counter

# Field represented in radix p with polynomial basis, reduction modulus
# x^f + a_(f-1)x^(f-1) + ... + a_0.
FIELDS = {
    2: (2, 1, (0, 1)),  # x+1
    3: (3, 1, (0, 1)),
    4: (2, 2, (1, 1, 1)),
    5: (5, 1, (0, 1)),
    7: (7, 1, (0, 1)),
    8: (2, 3, (1, 1, 0, 1)),
    9: (3, 2, (1, 0, 1)),
}

def field(q):
    p, f, coeff = FIELDS[q]
    def digits(z):
        ans = []
        for _ in range(f):
            ans.append(z % p)
            z //= p
        return ans
    ds = [digits(i) for i in range(q)]
    add = [[sum(((ds[a][i]+ds[b][i])%p)*p**i for i in range(f)) for b in range(q)] for a in range(q)]
    mul = []
    for a in range(q):
        row = []
        for b in range(q):
            pol = [0]*(2*f-1)
            for i, ai in enumerate(ds[a]):
                for j, bj in enumerate(ds[b]):
                    pol[i+j] += ai*bj
            for j in range(2*f-2, f-1, -1):
                c = pol[j]%p
                for k in range(f):
                    pol[j-f+k] -= c*coeff[k]
            row.append(sum((pol[i]%p)*p**i for i in range(f)))
        mul.append(row)
    neg = [sum(((-ds[a][i])%p)*p**i for i in range(f)) for a in range(q)]
    inv = [0]*q
    for a in range(1,q):
        inv[a] = next(b for b in range(1,q) if mul[a][b]==1)
    return add,mul,neg,inv

def invertible(mat, n, add, mul, neg, inv):
    A = [list(mat[i*n:(i+1)*n]) for i in range(n)]
    for j in range(n):
        k = next((k for k in range(j,n) if A[k][j]),None)
        if k is None: return False
        A[j],A[k]=A[k],A[j]
        s=inv[A[j][j]]
        A[j]=[mul[s][v] for v in A[j]]
        for i in range(j+1,n):
            t=A[i][j]
            if t:
                for h in range(j,n):
                    A[i][h]=add[A[i][h]][neg[mul[t][A[j][h]]]]
    return True

def predicted(q,n):
    if n==1: return Fraction(0)
    if q%2==0: return Fraction(1)
    bad=(q-1)*((2*q-1)**n-2*q**n+1)//2
    return Fraction(1)-Fraction(bad,(q**n-1)*(q**n-q))

def gaussian2(n,k):
    if k < 0 or k > n:
        return 0
    a = 1
    for i in range(k):
        a = Fraction(a*(2**(n-i)-1), 2**(k-i)-1)
    assert a.denominator == 1
    return int(a)

def gl2(n):
    out = 1
    for i in range(n):
        out *= (2**n - 2**i)
    return out

def binary_distribution(n):
    """P(number of nonzero idempotents = 2**r-1), 0<=r<=n."""
    return {2**r-1: sum(((-1)**(k-r)) * 2**((k-r)*(k-r-1)//2) * Fraction(gaussian2(k,r),gl2(k)) for k in range(r,n+1)) for r in range(n+1)}

def verify(q,n):
    add,mul,neg,inv=field(q)
    xs = list(product(range(q), repeat=n))
    sq=[tuple(mul[z][z] for z in x) for x in xs]
    nGL=first=second=0
    histogram=Counter()
    for a in product(range(q), repeat=n*n):
        if not invertible(a,n,add,mul,neg,inv):continue
        nGL+=1
        count=0
        for x,xsq in zip(xs,sq):
            if not any(x): continue
            if all(sumcheck(a,i,n,xsq,x[i],add,mul) for i in range(n)):
                count+=1
        first+=count
        second+=count*(count-1)
        histogram[count]+=1
    assert Fraction(first,nGL)==1,(q,n,'mean',first,nGL)
    got=Fraction(second,nGL)
    expect=predicted(q,n)
    assert got==expect,(q,n,'factorial_second',got,expect)
    if q%2 == 0:
        expected_hist = binary_distribution(n)
        assert {z: Fraction(c,nGL) for z,c in histogram.items()} == {z:v for z,v in expected_hist.items() if v}, (q,n, histogram, expected_hist)
    return f'GF({q}) n={n}: GL={nGL}, mean=1, second_factorial={got}, variance={got}, hist={dict(sorted(histogram.items()))}' 

def sumcheck(a,i,n,xsq,expected,add,mul):
    v=0
    for j in range(n):
        v=add[v][mul[a[i*n+j]][xsq[j]]]
    return v==expected

if __name__=='__main__':
    configs=[(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(5,2),(7,2),(8,2),(9,2)]
    for q,n in configs:print(verify(q,n))
    print('VERIFY_OK:',len(configs),'complete matrix and idempotent enumerations')
