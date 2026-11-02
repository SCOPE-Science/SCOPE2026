#!/usr/bin/env python3
"""Exact finite checks for matching erasures of the simplex midpoint Parseval frame.

Uses only Python's standard library. Tests finite cases; the theorem is proved analytically.
"""
from fractions import Fraction as F
from itertools import combinations


def invert(a):
    m = len(a)
    aug = [list(row) + [F(int(i == j)) for j in range(m)]
           for i, row in enumerate(a)]
    for k in range(m):
        pivot = next(i for i in range(k, m) if aug[i][k])
        aug[k], aug[pivot] = aug[pivot], aug[k]
        z = aug[k][k]
        aug[k] = [x / z for x in aug[k]]
        for i in range(m):
            if i != k:
                z = aug[i][k]
                if z:
                    aug[i] = [a - z*b for a, b in zip(aug[i], aug[k])]
    return [row[m:] for row in aug]


def gram_entry(n, e, f):
    return (F(len(set(e).intersection(f))) - F(4, n)) / (n-2)


def profile(n, t):
    return [[(2*i, 2*i+1) for i in range(t)],
            [e for e in combinations(range(n), 2)
             if e not in [(2*i, 2*i+1) for i in range(t)]]]


def formula(n, t, e, f, erased):
    r = {j for j, d in enumerate(erased) if set(e).intersection(d)}
    s = {j for j, d in enumerate(erased) if set(f).intersection(d)}
    c = len(set(e).intersection(f))
    h = len(r.intersection(s))
    B = n*(n-4)+4*t
    return F(((n-4)*c+h)*B - 4*(n-4+len(r))*(n-4+len(s)),
             (n-2)*(n-4)*B)


def norm_theory(n,t):
    L = F(4*(n-3), n)
    if t == 0:
        return L
    if t == 1:
        return L + F((n-4)*(n*n-12*n+24), n*(n-2)**3)
    C = n**3-16*n*n+80*n-112
    D = n**3-14*n*n+68*n-96
    B = n*(n-4)+4*t
    return L + F(2*(n*C-2*t*D), n*(n-4)*(n-2)*B)


def main():
    count=0
    for n in range(9, 17):
        norms=[]
        for t in range(0,n//2+1):
            erased, kept = profile(n,t)
            if not t:
                norms.append(F(4*(n-3),n))
                continue
            H = [[gram_entry(n,a,b) for b in erased] for a in erased]
            A = [[F(int(i==j))-H[i][j] for j in range(t)] for i in range(t)]
            inv = invert(A)
            P = [[gram_entry(n, e, d) for d in erased] for e in kept]
            by_orbit={}
            max_norm=F(0)
            for i,e in enumerate(kept):
                s=sum(bool(set(e).intersection(d)) for d in erased)
                rowsum=F(0)
                for j,f in enumerate(kept):
                    delta=sum(P[i][a]*inv[a][b]*P[j][b]
                              for a in range(t) for b in range(t))
                    x=gram_entry(n,e,f)+delta
                    y=formula(n,t,e,f,erased)
                    assert x==y,(n,t,e,f,x,y)
                    count+=1
                    c=len(set(e).intersection(f))
                    assert x>0 if c>0 else x<0,(n,t,e,f,x)
                    count+=1
                    rowsum+=abs(x)
                if s in by_orbit:
                    assert by_orbit[s]==rowsum
                else:
                    by_orbit[s]=rowsum
                count+=1
                max_norm=max(max_norm,rowsum)
            expected=norm_theory(n,t)
            assert max_norm==expected,(n,t,max_norm,expected,by_orbit)
            count+=1
            norms.append(max_norm)
        if n==9:
            assert norms[0]>norms[1]>norms[2]
            assert all(norms[i]>norms[i+1] for i in range(2,len(norms)-1))
        else:
            assert norms[0]<norms[1]<norms[2]
            assert all(norms[i]>norms[i+1] for i in range(2,len(norms)-1))
        count+=1
    print(f"PASS: {count} exact rational assertions for n=9..16, all matching sizes")


if __name__=='__main__':
    main()
