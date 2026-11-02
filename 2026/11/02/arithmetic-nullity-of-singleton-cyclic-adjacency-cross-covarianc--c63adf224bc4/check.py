#!/usr/bin/env python3
"""Exact checks for cyclic singleton/equal-block covariance and its nullity.
Standard-library only. These checks are finite; the all-n proof is in RESULT.md.
"""
from fractions import Fraction
from math import gcd


def bell_numbers(nmax):
    b=[1]
    from math import comb
    for n in range(nmax):
        b.append(sum(comb(n,j)*b[j] for j in range(n+1)))
    return b


def partitions_rg(n):
    # Each restricted-growth word represents one unlabeled set partition.
    def rec(word, mx):
        if len(word)==n:
            yield tuple(word)
            return
        for x in range(mx+2):
            word.append(x)
            yield from rec(word,max(mx,x))
            word.pop()
    yield from rec([0],0)


def rank_rational(a):
    a=[[Fraction(z) for z in row] for row in a]
    m=len(a); n=len(a[0]); r=0
    for c in range(n):
        pivot=next((i for i in range(r,m) if a[i][c]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        x=a[r][c]
        a[r]=[t/x for t in a[r]]
        for i in range(r+1,m):
            x=a[i][c]
            if x:
                a[i]=[a[i][j]-x*a[r][j] for j in range(n)]
        r+=1
        if r==m:break
    return r


def main():
    b=bell_numbers(100)
    assertions=0
    # Bell-number ratio bounds used in the analytic proof.
    for n in range(3,100):
        assert b[n-2]*b[n]>b[n-1]**2; assertions+=1
        assert (n-1)*b[n-2]*b[n]<=n*b[n-1]**2; assertions+=1
        assert (n-2)*b[n-2]*b[n]<n*b[n-1]**2; assertions+=1
    for n in range(3,10):
        rows=list(partitions_rg(n))
        N=b[n]
        assert len(rows)==N; assertions+=1
        pcount=[0]*n
        for w in rows:
            sizes=[w.count(j) for j in set(w)]
            for i in range(n):
                if sizes[w[i]]==1:pcount[i]+=1
        for i in range(n):
            assert pcount[i]==b[n-1]; assertions+=1
        for d in range(1,n):
            acount=[0]*n
            joint=[[0]*n for _ in range(n)]
            for w in rows:
                sizes=[0]*n
                for x in w:sizes[x]+=1
                singles=[sizes[w[i]]==1 for i in range(n)]
                for j in range(n):
                    if w[j]==w[(j+d)%n]:
                        acount[j]+=1
                        for i in range(n):
                            if singles[i]: joint[i][j]+=1
            for j in range(n):
                assert acount[j]==b[n-1];assertions+=1
            cn=[]
            for i in range(n):
                row=[]
                for j in range(n):
                    touches=i==j or i==(j+d)%n
                    predicted=0 if touches else b[n-2]
                    assert joint[i][j]==predicted; assertions+=1
                    v=N*joint[i][j]-pcount[i]*acount[j]
                    v2=(0 if touches else b[n-2]*N)-b[n-1]**2
                    assert v==v2;assertions+=1
                    row.append(v)
                cn.append(row)
            g=gcd(n,d)
            expected=n-g if (n//g)%2==0 else n
            assert rank_rational(cn)==expected; assertions+=1
            rowsum=(n-2)*b[n-2]*N-n*b[n-1]**2
            assert rowsum<0;assertions+=1
            for row in cn:
                assert sum(row)==rowsum;assertions+=1
    print('PASS: %d exact assertions; all set partitions n=3..9, all displacements, Bell bounds n=3..99.'%assertions)
    for d in (1,2,3):
        n=6;g=gcd(n,d)
        print('n=%d d=%d exact cross-covariance rank=%d'%(n,d,n-g if (n//g)%2==0 else n))

if __name__=='__main__':main()
