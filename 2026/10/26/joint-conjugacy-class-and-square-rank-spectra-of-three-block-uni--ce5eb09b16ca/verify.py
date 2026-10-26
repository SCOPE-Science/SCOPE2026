#!/usr/bin/env python3
"""Independent small-prime-field checks for three-block conjugacy/square-rank census.
Public, standalone; Python standard library only. Run: python3 verify.py.
"""
from collections import Counter
from itertools import product


def rank(rows, p):
    rows = [list(x) for x in rows]
    if not rows:
        return 0
    nr, nc = len(rows), len(rows[0])
    t = 0
    for col in range(nc):
        pivot = next((i for i in range(t, nr) if rows[i][col] % p), None)
        if pivot is None:
            continue
        rows[t], rows[pivot] = rows[pivot], rows[t]
        iv = pow(rows[t][col] % p, -1, p)
        rows[t] = [(v * iv) % p for v in rows[t]]
        for i in range(nr):
            if i != t and rows[i][col] % p:
                lam = rows[i][col]
                rows[i] = [(x-lam*y) % p for x, y in zip(rows[i], rows[t])]
        t += 1
        if t == nr:
            break
    return t


def mat(rows, cols, entries):
    return [tuple(entries[i*cols:(i+1)*cols]) for i in range(rows)]


def mm(A, B, p):
    if not A or not B:
        return []
    return [tuple(sum(A[i][h]*B[h][j] for h in range(len(B))) % p
                  for j in range(len(B[0]))) for i in range(len(A))]


def gauss(n,k,q):
    if k<0 or k>n:
        return 0
    t=1
    for i in range(k):
        numerator = q**(n-i)-1
        denominator = q**(k-i)-1
        t=t*numerator//denominator if (t*numerator)%denominator==0 else None
        if t is None:
            # Use rational arithmetic if intermediate division was not integral.
            from fractions import Fraction
            f=Fraction(1)
            for j in range(k):
                f*=Fraction(q**(n-j)-1,q**(k-j)-1)
            return int(f)
    return t


def count_rank(a,b,r,q):
    return gauss(a,r,q)*gauss(b,r,q)*__import__('math').prod(q**r-q**i for i in range(r))


def formula(a,b,c,q):
    z=Counter()
    for r in range(min(a,b)+1):
        xcount=count_rank(a,b,r,q)
        for s in range(min(b,c)+1):
            onto=__import__('math').prod(q**c-q**i for i in range(s))
            for k in range(max(0,r+s-b),min(r,s)+1):
                incidence=(gauss(b-r,s-k,q)*gauss(r,k,q)*q**(k*(b-r-s+k)))
                if not incidence:
                    continue
                t=c*r+a*s-r*s
                z[(t,k)]+=q**(a*c)*xcount*incidence*onto
    return z


def brute(a,b,c,p):
    Xs = [mat(a,b,x) for x in product(range(p),repeat=a*b)]
    Cs = [mat(b,c,y) for y in product(range(p),repeat=b*c)]
    d=a*b+b*c
    z=Counter()
    for X in Xs:
        for C in Cs:
            k=rank(mm(X,C,p),p)
            # Direct matrix of (X',C') -> XC' - X'C from basis variables.
            cols=[]
            for u in range(a):
                for v in range(b):
                    cols.append(tuple(-C[v][j] % p if i==u else 0
                                      for i in range(a) for j in range(c)))
            for u in range(b):
                for v in range(c):
                    cols.append(tuple(X[i][u] % p if j==v else 0
                                      for i in range(a) for j in range(c)))
            assert len(cols)==d
            t=rank(list(zip(*cols)),p)
            z[(t,k)]+=p**(a*c)
    return z


def check():
    cases=[(2,1,1,1),(3,1,1,1),(5,1,1,1),
           (2,1,2,1),(3,1,2,1),(2,2,1,2),(3,2,1,2),
           (2,2,2,2),(3,2,2,2),(2,2,3,2),(2,1,3,2)]
    for p,a,b,c in cases:
        actual=brute(a,b,c,p)
        predicted=formula(a,b,c,p)
        assert actual==predicted, (p,a,b,c,actual,predicted)
        assert sum(actual.values())==p**(a*b+b*c+a*c)
        print('PASS',f'q={p}, (a,b,c)=({a},{b},{c})',
              'elements=',sum(actual.values()),'joint_types=',len(actual))
    q=2
    z=formula(2,2,2,q)
    print('q=2 (a,b,c)=(2,2,2) class_size=16, square rank counts:',
          tuple(z[(4,k)] for k in (0,1,2)))
    assert tuple(z[(4,k)] for k in (0,1,2))==(192,1728,576)
    print('VERIFY_OK')

if __name__=='__main__':
    check()
