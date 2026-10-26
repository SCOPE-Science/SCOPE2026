#!/usr/bin/env python3
"""Independent enumeration and closed-form checks for class-two free associative algebras.
Run: python3 verify_free2.py
Uses prime base fields for exhaustive checks; algebraic formula holds for prime powers.
"""
from itertools import combinations, product
from fractions import Fraction
from collections import Counter


def gauss(n,k,q):
    if k<0 or k>n:return 0
    x=Fraction(1)
    for i in range(k):x*=Fraction(q**n-q**i,q**k-q**i)
    assert x.denominator==1
    return int(x)


def profile_formula(r,q,ideal):
    m=r*r
    result=Counter()
    by_u=Counter()
    for u in range(r+1):
        b=(2*r*u-u*u) if ideal else u*u
        for t in range(b,m+1):
            count=gauss(r,u,q)*gauss(m-b,t-b,q)*q**(u*(m-t))
            result[u+t]+=count
            by_u[u]+=count
    return result,by_u


def rref_subspaces(n,q):
    for k in range(n+1):
        for pivs in combinations(range(n),k):
            free=[(i,j) for i,p in enumerate(pivs) for j in range(p+1,n) if j not in pivs]
            for vals in product(range(q),repeat=len(free)):
                rows=[[0]*n for _ in range(k)]
                for i,p in enumerate(pivs):rows[i][p]=1
                for (i,j),v in zip(free,vals):rows[i][j]=v
                yield k,tuple(pivs),tuple(tuple(row) for row in rows)


def contains(x,pivs,rows,q):
    y=list(x)
    for p,row in zip(pivs,rows):
        if a:=y[p]:
            for j in range(p,len(y)):
                y[j]=(y[j]-a*row[j])%q
    return not any(y)


def multiply(x,y,r,q):
    z=[0]*(r+r*r)
    for i in range(r):
        for j in range(r):
            z[r+i*r+j]=x[i]*y[j]%q
    return tuple(z)


def profile_exhaustive(r,q):
    n=r+r*r
    basis=[tuple(int(i==j) for i in range(n)) for j in range(n)]
    sub=Counter(); ideal=Counter(); by_u_sub=Counter(); by_u_ideal=Counter()
    count=0
    for k,pivs,rows in rref_subspaces(n,q):
        count+=1
        # The projection onto V has rank k - dim(S cap W).
        # Since W consists of elements with zero V part, this is the span rank of initial coordinates.
        projected=[tuple(row[:r]) for row in rows]
        u=0; basisproj=[]
        for v in projected:
            w=list(v)
            for pivot,lead in basisproj:
                if w[pivot]:
                    t=w[pivot]
                    w=[(x-t*y)%q for x,y in zip(w,lead)]
            pivot=next((i for i,x in enumerate(w) if x),None)
            if pivot is not None:
                inv=pow(w[pivot],-1,q)
                w=[x*inv%q for x in w]
                basisproj.append((pivot,w));basisproj.sort()
                u+=1
        subok=all(contains(multiply(x,y,r,q),pivs,rows,q) for x in rows for y in rows)
        idealok=all(contains(multiply(x,y,r,q),pivs,rows,q) and contains(multiply(y,x,r,q),pivs,rows,q) for x in rows for y in basis)
        if subok:sub[k]+=1;by_u_sub[u]+=1
        if idealok:ideal[k]+=1;by_u_ideal[u]+=1
    assert count==sum(gauss(n,k,q) for k in range(n+1))
    return (sub,by_u_sub),(ideal,by_u_ideal),count


def main():
    for r,q in [(1,2),(1,3),(2,2),(2,3)]:
        exsub,exideal,ambient=profile_exhaustive(r,q)
        fosub=profile_formula(r,q,False); foideal=profile_formula(r,q,True)
        assert exsub==fosub,(r,q,'sub',exsub,fosub)
        assert exideal==foideal,(r,q,'ideal',exideal,foideal)
        print('OK',{'r':r,'q':q,'ambient_subspaces':ambient,'subalgebras':sum(exsub[0].values()),'ideals':sum(exideal[0].values()),'projection_counts':dict(sorted(exsub[1].items())),'sub_dimension_profile':dict(sorted(exsub[0].items()))})
    # Algebraic formula sanity and asymptotic diagnostics (not proof of the limit).
    for q in (2,3,4):
        for r in (3,4,5,8):
            sub,byu=profile_formula(r,q,False)
            ideal,byuide=profile_formula(r,q,True)
            G=sum(gauss(r*r,k,q) for k in range(r*r+1))
            assert byu[0]==G
            assert byu[1]==gauss(r,1,q)*(G-sum(gauss(r*r-1,k,q) for k in range(r*r)))
            assert byuide[0]==G
            print('FORMULA',q,r,'sub_vs_line',(float(Fraction(byu[1],sum(sub.values())))),'ideal_in_center',float(Fraction(G,sum(ideal.values()))),'scaled_ratio',float(Fraction(sum(ideal.values()),sum(sub.values()))*gauss(r,1,q)))
    print('ALL CHECKS PASSED')

if __name__=='__main__': main()
