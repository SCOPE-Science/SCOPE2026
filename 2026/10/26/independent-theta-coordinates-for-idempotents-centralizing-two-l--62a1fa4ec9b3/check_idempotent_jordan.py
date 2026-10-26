#!/usr/bin/env python3
"""Independent finite-field exhaustive test of the claimed centralizer idempotent spectrum.
Requires Python 3 only; no external dependencies. No mathematical assertions are read from output files.
"""
from collections import Counter
from math import prod


def phi(q,k):
    from fractions import Fraction
    return prod((1-Fraction(1,q**h) for h in range(1,k+1)),start=__import__('fractions').Fraction(1))


def D(a,b,x,y):
    return a*x*x+b*y*y+2*a*x*y


def pred(q,a,b,m):
    from fractions import Fraction
    au=lambda x,y:Fraction(q**D(a,b,x,y))*phi(q,x)*phi(q,y)
    root=au(m,m)
    return {(r,s):int(root/(au(r,s)*au(m-r,m-s))) for r in range(m+1) for s in range(m+1)}


def j2(a,b,m):
    lengths=[a]*m+[b]*m
    n=sum(lengths); x=0; p=0
    for length in lengths:
        for i in range(length-1):x|=1<<((p+i)*n+p+i+1)
        p+=length
    return n,x


def rank2(x,n):
    basis={}; count=0
    for i in range(n):
        v=(x>>(i*n))&((1<<n)-1)
        while v:
            k=v.bit_length()-1
            if k in basis:v^=basis[k]
            else:
                basis[k]=v;count+=1;break
    return count


def mul2(a,b,n):
    mask=(1<<n)-1; out=0
    for i in range(n):
        v=(a>>(i*n))&mask; row=0
        while v:
            bit=v&-v; k=bit.bit_length()-1
            row^=(b>>(k*n))&mask;v-=bit
        out|=row<<(i*n)
    return out


def centralizer_basis2(n,j):
    equations=[]
    # basis vector for each matrix entry; linear commutator constraints
    for i in range(n):
        for k in range(n):
            coeff=0
            for h in range(n):
                if j&(1<<(h*n+k)):
                    coeff^=1<<(i*n+h)
                if j&(1<<(i*n+h)):
                    coeff^=1<<(h*n+k)
            if coeff:equations.append(coeff)
    pivots={}
    for row in equations:
        while row:
            p=(row&-row).bit_length()-1
            if p in pivots:row^=pivots[p]
            else:pivots[p]=row;break
    free=[i for i in range(n*n) if i not in pivots]
    ans=[]
    for v in free:
        x=1<<v
        for p in sorted(pivots,reverse=True):
            if (x&pivots[p]).bit_count()%2:x^=1<<p
        assert mul2(x,j,n)==mul2(j,x,n)
        ans.append(x)
    return ans


def exhaustive2(a,b,m):
    n,j=j2(a,b,m); bases=centralizer_basis2(n,j)
    lim=1<<len(bases)
    assert len(bases)==D(a,b,m,m)
    current=0; seen=Counter()
    jp=1 if False else sum(1<<(i*n+i) for i in range(n))
    for _ in range(a):jp=mul2(jp,j,n)
    for index in range(lim):
        if index:
            delta=(index&-index).bit_length()-1
            current^=bases[delta]
        if mul2(current,current,n)!=current:continue
        s_num=rank2(mul2(jp,current,n),n)
        assert s_num%(b-a)==0
        s=s_num//(b-a)
        r_num=rank2(current,n)-b*s
        assert r_num%a==0
        r=r_num//a
        assert 0<=r<=m and 0<=s<=m
        seen[(r,s)]+=1
    expectation=pred(2,a,b,m)
    assert dict(seen)==expectation,(a,b,m,dict(seen),expectation)
    return lim,sum(seen.values()),dict(sorted(seen.items()))


def mulp(A,B,n,p):
    return tuple(sum(A[i*n+h]*B[h*n+j] for h in range(n))%p for i in range(n) for j in range(n))

def rankp(A,n,p):
    M=[list(A[i*n:(i+1)*n]) for i in range(n)]; r=0
    for c in range(n):
        t=next((i for i in range(r,n) if M[i][c]%p),None)
        if t is None:continue
        M[r],M[t]=M[t],M[r]
        inv=pow(M[r][c],-1,p)
        M[r]=[(v*inv)%p for v in M[r]]
        for i in range(r+1,n):
            h=M[i][c]
            if h:M[i]=[(v-h*w)%p for v,w in zip(M[i],M[r])]
        r+=1
    return r

def exhaustive_odd_prime(p,a,b,m):
    n,jbits=j2(a,b,m)
    j=tuple((jbits>>i)&1 for i in range(n*n))
    jpow=tuple(int(i==k) for i in range(n) for k in range(n))
    for _ in range(a):jpow=mulp(jpow,j,n,p)
    c=Counter();cen=0
    from itertools import product
    for A in product(range(p),repeat=n*n):
        if mulp(A,j,n,p)!=mulp(j,A,n,p):continue
        cen+=1
        if mulp(A,A,n,p)!=A:continue
        s0=rankp(mulp(jpow,A,n,p),n,p)
        assert s0%(b-a)==0
        s=s0//(b-a)
        r0=rankp(A,n,p)-b*s
        assert r0%a==0
        r=r0//a
        c[(r,s)]+=1
    assert cen==p**D(a,b,m,m)
    expectation=pred(p,a,b,m)
    assert dict(c)==expectation,(p,a,b,m,dict(c),expectation)
    return cen,sum(c.values()),dict(sorted(c.items()))


def main():
    cases=[]
    for a,b,m in [(1,2,1),(1,3,1),(2,3,1),(1,2,2)]:
        n,tot,c=exhaustive2(a,b,m)
        cases.append((2,a,b,m,n,tot,c))
        print('GF(2) a,b,m=',a,b,m,'centralizer=',n,'idempotents=',tot,'spectrum=',c)
    n,tot,c=exhaustive_odd_prime(3,1,2,1)
    cases.append((3,1,2,1,n,tot,c))
    print('GF(3) a,b,m=',1,2,1,'centralizer=',n,'idempotents=',tot,'spectrum=',c)
    print('ALL_TWO_LENGTH_IDEMPOTENT_SPECTRA_PASSED cases=%d centralizer_elements=%d idempotents=%d' %(len(cases),sum(c[4] for c in cases),sum(c[5] for c in cases)))

if __name__=='__main__':main()
