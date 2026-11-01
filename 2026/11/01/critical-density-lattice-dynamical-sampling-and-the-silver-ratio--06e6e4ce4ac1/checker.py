"""Exact finite consistency tests for nearest-neighbor dynamical sampling.
Uses the Python standard library only. No finite test certifies an infinite limit.
"""
from fractions import Fraction as Q
from math import comb


def matrix(k):
    cols = [j for t in range(k) for j in ((-t, 1+t) if t else (0, 1))]
    rows = [(s, t) for t in range(k) for s in (0, 1)]
    ans = []
    for s, t in rows:
        vals = []
        for j in cols:
            m = t + j - s
            vals.append(Q(comb(t, m//2), 2**t) if 0 <= m <= 2*t and m % 2 == 0 else Q(0))
        ans.append(vals)
    return ans, cols


def determinant(a):
    a = [r[:] for r in a]
    n = len(a)
    d = Q(1)
    for j in range(n):
        pivot = next((i for i in range(j,n) if a[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            a[j],a[pivot]=a[pivot],a[j]
            d=-d
        v=a[j][j]
        d*=v
        for i in range(j+1,n):
            if a[i][j]:
                c=a[i][j]/v
                for h in range(j+1,n):
                    a[i][h]-=c*a[j][h]
                a[i][j]=0
    return d


def cheb(j):
    if j==0:return (1,)
    a=(1,);b=(0,1)
    for n in range(2,j+1):
        c=[0]*(n+1)
        for t,v in enumerate(b):c[t+1]+=2*v
        for t,v in enumerate(a):c[t]-=v
        a,b=b,tuple(c)
    return b

for k in range(1,8):
    m,cols=matrix(k)
    assert abs(determinant(m))==Q(1,2**(k*(k-1)))
    for j in range(1,k):
        c=cheb(j)
        coeff={q:Q(0) for q in cols}
        for t,v in enumerate(c):
            for idx,x in enumerate(m[2*t]):coeff[cols[idx]]+=v*x
        assert all(coeff[pos]==(Q(1,2) if pos in (-j,j) else Q(0)) for pos in cols)
        assert sum(abs(v) for v in c)==abs(sum(v*complex(0,1)**t for t,v in enumerate(c)))
    for ix in range(2*k):
        y=[r[ix] for r in m]
        recovered={0:y[0],1:y[1]}
        for j in range(1,k):
            c=cheb(j)
            recovered[-j]=2*sum(c[t]*y[2*t] for t in range(j+1))-recovered[j]
            recovered[j+1]=2*sum(c[t]*y[2*t+1] for t in range(j+1))-recovered[1-j]
        assert all(recovered[z]==int(z==cols[ix]) for z in cols)
print('CHECK_OK: exact block determinants, Chebyshev inversion, coefficient alternation (k=1..7)')
