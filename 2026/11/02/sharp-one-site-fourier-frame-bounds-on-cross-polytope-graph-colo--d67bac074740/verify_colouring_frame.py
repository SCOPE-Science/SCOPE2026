#!/usr/bin/env python3
"""Reproduce finite combinatorial and character-Gram checks for a pair-partite colouring frame.
Standard library only. This is verification evidence, not a substitute for the all-parameter proof.
"""
import cmath
import math
from fractions import Fraction


def falling(q, k):
    if k < 0 or k > q:
        return 0
    z = 1
    for j in range(k):
        z *= q-j
    return z


def count(m, q):
    return sum(math.comb(m, s)*falling(q, 2*m-s) for s in range(m+1))


def p_equal(m, q):
    return Fraction(q*count(m-1, q-1), count(m, q))


def levels(m, q):
    p = p_equal(m,q)
    anti = q*(1-p)/Fraction(q-1)
    split = q*(1+p)/Fraction(q-1)
    total = (q*(1+p)-2*m)/Fraction(q-1)
    return anti, split, total


def colourings(m,q):
    def recurse(j, used, col):
        if j == m:
            yield tuple(col)
            return
        available=[v for v in range(q) if v not in used]
        for a in available:
            for b in available:
                yield from recurse(j+1,used|{a,b},col+[a,b])
    yield from recurse(0, set(), [])


def assert_block(m,q):
    p=p_equal(m,q)
    r=(q*p-1)/Fraction(q-1)
    z=Fraction(-1,q-1)
    n=2*m
    matrix=[[Fraction(1) if i==j else (r if i//2==j//2 else z)
             for j in range(n)] for i in range(n)]
    anti,split,total=levels(m,q)
    vectors=[]
    for i in range(m):
        v=[0]*n
        v[2*i]=1;v[2*i+1]=-1
        vectors.append((v,anti))
    for i in range(m-1):
        v=[0]*n
        v[2*i]=v[2*i+1]=1
        v[-2]=v[-1]=-1
        vectors.append((v,split))
    vectors.append(([1]*n,total))
    for v,eig in vectors:
        for i in range(n):
            lhs=sum(matrix[i][j]*v[j] for j in range(n))
            assert lhs==eig*v[i],(m,q,i,lhs,eig)
    assert (anti*m+split*(m-1)+total)==2*m
    assert count(m,q)==q*count(m-1,q-1)+q*(q-1)*count(m-1,q-2)
    if q==m:
        assert anti==total==0 and split==Fraction(2*m,m-1)
    else:
        assert anti>0 and split>0 and total>0
        assert split>max(anti,total,1)
        if q==m+1:
            assert p==Fraction(m,m+1)
            assert anti==total==Fraction(1,m)
            assert split==Fraction(2*m+1,m)
            assert split/min(anti,total)==2*m+1


def sample_checks(m,q):
    samples=list(colourings(m,q))
    assert len(samples)==count(m,q)
    p=p_equal(m,q)
    n=2*m
    alpha=Fraction(-1,q-1)
    r=(q*p-1)/Fraction(q-1)
    root=[cmath.exp(2j*math.pi*t/q) for t in range(q)]
    moment=[[0j]*n for _ in range(n)]
    for col in samples:
        for i in range(n):
            for j in range(n):
                moment[i][j]+=root[col[i]]*root[-col[j]%q]
    for i in range(n):
        for j in range(n):
            expected=1 if i==j else (r if i//2==j//2 else alpha)
            assert abs(moment[i][j]/len(samples)-float(expected))<1e-9,(m,q,i,j)
    # Character cross-frequencies on the actual sample, not just moments at frequency one.
    for a,b in [(1,2),(1,q-1)] if q>2 else []:
        if a==b:
            continue
        for i,j in [(0,0),(0,1),(0,2),(1,3)]:
            z=sum(root[a*col[i]%q]*root[-b*col[j]%q] for col in samples)/len(samples)
            assert abs(z)<1e-9,(m,q,a,b,i,j,z)
    return len(samples)



def full_fourier_gram_check(m,q):
    """Build every character column directly on the enumerated sample set."""
    samples=list(colourings(m,q))
    dims=[None]+[(v,a) for v in range(2*m) for a in range(1,q)]
    d=len(dims)
    root=[cmath.exp(2j*math.pi*t/q) for t in range(q)]
    sums=[[0j]*d for _ in range(d)]
    for col in samples:
        x=[1+0j]+[root[(a*col[v])%q] for v,a in dims[1:]]
        for i in range(d):
            xi=x[i]
            for j in range(d):
                sums[i][j]+=xi*x[j].conjugate()
    pp=p_equal(m,q)
    for i,(si) in enumerate(dims):
        for j,(sj) in enumerate(dims):
            if si is None or sj is None:
                expected=1 if si is None and sj is None else 0
            else:
                u,a=si;v,b=sj
                if a!=b:
                    expected=0
                elif u==v:
                    expected=1
                elif u//2==v//2:
                    expected=(q*pp-1)/Fraction(q-1)
                else:
                    expected=Fraction(-1,q-1)
            assert abs(sums[i][j]/len(samples)-float(expected))<2e-9,(m,q,i,j)
    return d*d

def main():
    tested=0
    for m in range(3,18):
        for q in range(m, min(m+18,28)):
            assert_block(m,q)
            tested+=1
    cases=[(3,3),(3,4),(3,5),(4,4),(4,5),(4,6),(5,5),(5,6)]
    totals=[]
    for m,q in cases:
        totals.append((m,q,sample_checks(m,q)))
    full_assertions=sum(full_fourier_gram_check(m,q) for m,q in [(3,4),(3,5),(4,5),(4,6)])
    # Exact rational high-palette convergence consistency.
    for m in range(3,12):
        for q in [50,100,250,500]:
            p=p_equal(m,q)
            a,b,c=levels(m,q)
            assert p>Fraction(1,q)
            assert a<1<b
            assert c>0
            assert abs(float((b/min(a,c)-1)*q)-2*m)<20*m*m/q
    print('PASS:',tested,'exact Gram block and chromatic recursion cases;')
    print('PASS: direct colourings (m,q,count)=',totals)
    print('PASS:',full_assertions,'direct full-complex-Fourier Gram entries')
    print('PASS: all spectral ranks, first-extra-colour sharp bounds, high-palette consistency')

if __name__=='__main__':
    main()
