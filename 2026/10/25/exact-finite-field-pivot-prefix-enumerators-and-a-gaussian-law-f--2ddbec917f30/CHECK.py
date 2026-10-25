#!/usr/bin/env python3
"""Exact checks for leading-principal-minor renewal formulas over prime finite fields."""
from fractions import Fraction
from itertools import product
from math import prod


def rank_mod(mat, p):
    a = [list(row) for row in mat]
    m=len(a); piv=0
    for j in range(m):
        u=next((i for i in range(piv,m) if a[i][j]%p),None)
        if u is None: continue
        a[piv],a[u]=a[u],a[piv]
        inv=pow(a[piv][j],-1,p)
        a[piv]=[(z*inv)%p for z in a[piv]]
        for i in range(piv+1,m):
            t=a[i][j]%p
            if t:
                a[i]=[(a[i][h]-t*a[piv][h])%p for h in range(m)]
        piv+=1
        if piv==m: break
    return piv


def brute(p,n):
    out={}
    for entries in product(range(p),repeat=n*n):
        mat=[entries[i*n:(i+1)*n] for i in range(n)]
        if rank_mod(mat,p)!=n: continue
        num=sum(rank_mod([row[:k] for row in mat[:k]],p)==k for k in range(1,n+1))
        out[num]=out.get(num,0)+1
    return out


def fraction_model(p,n):
    a=[Fraction(1)]
    for j in range(1,n+1):a.append(a[-1]*(1-Fraction(1,p**j)))
    f=[Fraction(0)]*(n+1)
    for k in range(1,n+1):
        f[k]=a[k]-sum(f[j]*a[k-j] for j in range(1,k))
    v=[[Fraction(0)]*(n+1) for b in range(n+1)]
    v[0][0]=Fraction(1)
    for b in range(1,n+1):
        for k in range(1,n+1):
            v[b][k]=sum(f[j]*v[b-1][k-j] for j in range(1,k+1))
    assert sum(v[b][n] for b in range(1,n+1))==a[n]
    N=prod(p**n-p**j for j in range(n))
    d={b:int(v[b][n]*N/a[n]) for b in range(1,n+1) if v[b][n]}
    assert all(v[b][n]*N/a[n]==d[b] for b in d)
    return d,a,f


def direct_transitions(p,k):
    # Exhaustively compare rank jumps for each rank class of matrices A, k<=2.
    from collections import defaultdict
    tally=defaultdict(lambda:[0,0,0])
    count=defaultdict(int)
    for ent in product(range(p),repeat=k*k):
        A=[ent[i*k:(i+1)*k] for i in range(k)]
        d=k-rank_mod(A,p)
        count[d]+=1
        for last in product(range(p),repeat=2*k+1):
            B=[list(row)+[last[i]] for i,row in enumerate(A)]
            B.append(list(last[k:2*k])+[last[-1]])
            e=k+1-rank_mod(B,p)
            tally[d][e-d+1]+=1
    for d,c in count.items():
        den=c*p**(2*k+1)
        expected={-1:(1-Fraction(1,p**d))**2 if d else Fraction(0),
                  1:Fraction(1,p**(2*d+1))}
        expected[0]=1-expected[-1]-expected[1]
        for change, probability in expected.items():
            assert Fraction(tally[d][change+1],den)==probability,(p,k,d,change)


def main():
    for p,n in [(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3)]:
        b=brute(p,n)
        predicted,_,_=fraction_model(p,n)
        assert b==predicted,(p,n,b,predicted)
        print('PASS matrix distribution',p,n,predicted)
    for p,k in [(2,1),(2,2),(3,1)]:
        direct_transitions(p,k)
        print('PASS rank transitions',p,k)
    for p in (2,3,5,7):
        from decimal import Decimal, localcontext
        with localcontext() as cxt:
            cxt.prec=65
            a=Decimal(1); arr=[a]
            for j in range(1,260):
                a*=1-Decimal(1)/(Decimal(p)**j)
                arr.append(a)
            c=a
            A=sum((v-c for v in arr),Decimal(0))
            var=2*c*A-c*(1-c)
            assert var>0
            print('PASS positive variance',p,'c=',float(c),'sigma2=',float(var))
    print('VERIFY_OK matrix_distributions=7 rank_transitions=3 exact_renewal_identity=PASS positive_variances=4')


if __name__=='__main__':main()
