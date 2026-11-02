#!/usr/bin/env python3
"""Independent exhaustive finite-field tests of 3-block radical-ring brace claims."""
from itertools import product
from collections import Counter
from math import prod

def mats(a,b,q):
    return list(product(range(q),repeat=a*b))

def mm(X,Y,a,b,c,q):
    return tuple(sum(X[i*b+k]*Y[k*c+j] for k in range(b))%q for i in range(a) for j in range(c))

def sub(A,B,q): return tuple((a-b)%q for a,b in zip(A,B))

def add(A,B,q): return tuple((a+b)%q for a,b in zip(A,B))

def rank(A,m,n,q):
    B=[list(A[i*n:(i+1)*n]) for i in range(m)]
    rr=0
    for col in range(n):
        piv=next((i for i in range(rr,m) if B[i][col]%q),None)
        if piv is None:continue
        B[rr],B[piv]=B[piv],B[rr]
        mult=pow(B[rr][col],-1,q)
        B[rr]=[(mult*x)%q for x in B[rr]]
        for i in range(m):
            if i!=rr:
                f=B[i][col]
                B[i]=[(x-f*y)%q for x,y in zip(B[i],B[rr])]
        rr+=1
        if rr==m:break
    return rr

def gauss(n,k,q):
    if k<0 or k>n:return 0
    from fractions import Fraction
    out=Fraction(1)
    for i in range(k): out*=Fraction(q**(n-i)-1,q**(k-i)-1)
    assert out.denominator==1
    return int(out)

def rank_matrices(m,n,k,q):
    return gauss(m,k,q)*prod(q**n-q**i for i in range(k))

def fiber(r,s,t,q,k,d):
    # Number of (P,Q) with P in M(r,d), Q in M(d,t), PQ = fixed rank-k C.
    return sum(gauss(r-k,a-k,q)*prod(q**d-q**i for i in range(a))*q**((d-a)*t)
               for a in range(k,min(r,d)+1))

def test(r,s,t,q):
    Xs=mats(r,s,q); Ys=mats(s,t,q)
    Cs=mats(r,t,q); zr=(0,)*(r*t)
    SX={X:rank(X,r,s,q) for X in Xs}
    SY={Y:rank(Y,s,t,q) for Y in Ys}
    XP={(X,V):mm(X,V,r,s,t,q) for X in Xs for V in Ys}
    counts=Counter()
    product_counts=Counter(XP.values())
    for X in Xs:
        for Y in Ys:
            a=SX[X]; b=SY[Y]
            brace=group=0
            for U in Xs:
                for V in Ys:
                    C=sub(XP[X,V],XP[U,Y],q)
                    counts[C]+=1
                    if XP[X,V]==zr and XP[U,Y]==zr:brace+=1
                    if C==zr:group+=1
            assert brace==q**(r*(s-b)+t*(s-a)),(r,s,t,q,a,b,brace)
            assert group==q**(r*s+s*t-a*t-r*b+a*b),(r,s,t,q,a,b,group)
    for C in Cs:
        k=rank(C,r,t,q)
        assert counts[C]==fiber(r,s,t,q,k,2*s),(r,s,t,q,C,counts[C],fiber(r,s,t,q,k,2*s))
        assert product_counts[C]==fiber(r,s,t,q,k,s),(r,s,t,q,C,product_counts[C],fiber(r,s,t,q,k,s))
    N=q**(r*s+s*t)
    p0=product_counts[zr]/N
    pb=counts[zr] # need brace count sum separately, derive from p0
    pb_actual=sum(1 for X in Xs for Y in Ys for U in Xs for V in Ys if XP[X,V]==zr and XP[U,Y]==zr)
    assert pb_actual==product_counts[zr]**2
    assert counts[zr]>=pb_actual
    assert sum(counts.values())==N*N
    assert sum(product_counts.values())==N
    # All rank fibers nonempty exactly for rank<=2s
    assert all((counts[C]>0)==(rank(C,r,t,q)<=2*s) for C in Cs)
    print('CHECK_OK',q,(r,s,t),'group_0',counts[zr],'brace_0',pb_actual,
          'p0_num',product_counts[zr], 'rank_fibers',sorted({rank(C,r,t,q):counts[C] for C in Cs}.items()))

def test_width():
    r,s,t,q=3,1,3,2
    Xs=mats(r,s,q); Ys=mats(s,t,q); Cs=mats(r,t,q)
    products={mm(X,Y,r,s,t,q) for X in Xs for Y in Ys}
    commutators={sub(A,B,q) for A in products for B in products}
    assert all((C in products)==(rank(C,r,t,q)<=s) for C in Cs)
    assert all((C in commutators)==(rank(C,r,t,q)<=2*s) for C in Cs)
    two={add(A,B,q) for A in commutators for B in commutators}
    assert set(Cs)==two
    assert any(rank(C,r,t,q)==3 for C in Cs if C not in commutators)
    print('WIDTH_OK','products',len(products),'commutators',len(commutators),'two',len(two))

if __name__=='__main__':
    for case in [(1,1,1,2),(1,1,1,3),(1,1,1,5),(2,1,2,2),
                 (2,1,2,3),(1,2,1,2),(2,1,3,2),(3,1,3,2)]:test(*case)
    test_width()
    print('VERIFY_OK')
