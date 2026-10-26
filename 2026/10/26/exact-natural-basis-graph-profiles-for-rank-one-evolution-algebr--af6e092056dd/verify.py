#!/usr/bin/env python3
"""Exact checks of finite-field rank-one-algebra natural-basis graph frequencies.
No external dependencies; fields tested: F_3, F_5, F_7 and F_9.
"""
from itertools import product
from math import comb
from collections import defaultdict
from fractions import Fraction


def field(q):
    if q == 9:
        def add(x,y):return (x%3+y%3)%3 + 3*((x//3+y//3)%3)
        def mul(x,y):return ((x%3)*(y%3)+2*(x//3)*(y//3))%3 + 3*(((x%3)*(y//3)+(x//3)*(y%3))%3)
        def neg(x):return ((-(x%3))%3)+3*((-(x//3))%3)
    else:
        def add(x,y):return (x+y)%q
        def mul(x,y):return (x*y)%q
        def neg(x):return (-x)%q
    def power(a,m):
        r=1
        while m:
            if m&1:r=mul(r,a)
            a=mul(a,a);m//=2
        return r
    def chi(a):return 0 if a==0 else (1 if power(a,(q-1)//2)==1 else -1)
    return add,mul,neg,chi


def closed(q,n,c,d,chi):
    eps=chi((-1)%q if q!=9 else 2)
    def A(k):
        return (((q-1)**k+(q-1)*(-1)**k)//q if c==0
                else ((q-1)**k-(-1)**k)//q)
    h=n//2
    b=((q-1 if c==0 else -1)*eps**h*q**(h-1) if n%2==0
       else (0 if c==0 else chi(c)*eps**h*q**h))
    T=q**(n-1)-int(c==0)+d*b
    cnt={k:comb(n,k)*A(k) for k in range(1,n)}
    cnt[n]=A(n)+d*b
    assert sum(cnt.values())==T
    return cnt,T


def run_table(q,n):
    add,mul,neg,chi=field(q)
    qels=range(q)
    groups=defaultdict(lambda:[defaultdict(int),0])
    for b in product(range(1,q),repeat=n):
        d=1
        for x in b:d*=chi(x)
        for w in product(qels,repeat=n):
            if not any(w):continue
            c=0
            for x,y in zip(b,w):c=add(c,mul(x,mul(y,y)))
            k=sum(bool(y) for y in w)
            groups[c,d][0][k]+=1
            groups[c,d][1]+=1
    for (c,d),(obs,total) in groups.items():
        expected,T=closed(q,n,c,d,chi)
        expected_factor=(q-1)**n//2
        assert total==expected_factor*T,(q,n,c,d,total,expected_factor*T)
        for k in range(1,n+1):
            assert obs[k]==expected_factor*expected[k],(q,n,c,d,k,obs[k],expected[k])
    return len(groups)


def rank_rows(vectors,q):
    v=[list(x) for x in vectors if any(x)]
    r=0
    for j in range(len(v[0])):
        piv=next((i for i in range(r,len(v)) if v[i][j]),None)
        if piv is None:continue
        v[r],v[piv]=v[piv],v[r]
        inv=pow(v[r][j],-1,q)
        v[r]=[(z*inv)%q for z in v[r]]
        for i in range(len(v)):
            if i!=r:
                a=v[i][j]
                v[i]=[(x-a*y)%q for x,y in zip(v[i],v[r])]
        r+=1
        if r==len(v):break
    return r


def actual_orthogonal_bases(q,diag,v):
    n=len(diag)
    # count graph profiles among all ordered orthogonal bases in the fixed form
    add,mul,neg,chi=field(q)
    assert q!=9
    valid=defaultdict(int)
    basis_count=0
    for basis in product(product(range(q),repeat=n),repeat=n):
        if any(all(x==0 for x in row) for row in basis):continue
        if rank_rows(basis,q)<n:continue
        squares=[sum(diag[j]*row[j]*row[j] for j in range(n))%q for row in basis]
        if any(s==0 for s in squares):continue
        if any(sum(diag[k]*basis[i][k]*basis[j][k] for k in range(n))%q
                for i in range(n) for j in range(i)):continue
        # v equals sum_i coordinate_i * basis[i]; solve via dot products
        coords=[sum(diag[j]*v[j]*basis[i][j] for j in range(n))*pow(squares[i],-1,q)%q for i in range(n)]
        assert all(sum(coords[i]*basis[i][j] for i in range(n))%q==v[j]%q for j in range(n))
        valid[sum(x!=0 for x in coords)]+=1
        basis_count+=1
    c=sum(diag[j]*v[j]*v[j] for j in range(n))%q
    d=1
    for x in diag:d*=chi(x)
    exp,T=closed(q,n,c,d,chi)
    for k in range(1,n+1):assert Fraction(valid[k],basis_count)==Fraction(exp[k],T),(q,diag,v,k,valid,exp,T)
    return basis_count


def main():
    runs=0;profiles=0
    for q,nmax in [(3,5),(5,4),(7,4),(9,3)]:
        for n in range(2,nmax+1):
            groups=run_table(q,n)
            print('TABLE_OK',q,n,'parameter_types',groups)
            runs+=1;profiles+=groups
    bases=[(3,[1,2],[1,0]),(3,[1,1,1],[1,0,0]),(3,[1,1,2],[1,1,0]),(5,[1,1],[1,0])]
    for q,diag,v in bases:
        k=actual_orthogonal_bases(q,diag,v)
        print('ACTUAL_BASES_OK',q,diag,v,k)
    print('VERIFY_OK table_cases=',runs,'parameter_types=',profiles,'actual_form_cases=',len(bases))

if __name__=='__main__':main()
