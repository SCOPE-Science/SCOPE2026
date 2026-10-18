#!/usr/bin/env python3
"""Exact polynomial certificate for a three-patch occupancy process.

All operations use only the Python standard library, with integer coefficients.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction

ONE={(0,0,0):1}; ZERO={}; X={(1,0,0):1}; R={(0,1,0):1}; Z={(0,0,1):1}

def add(a,b,sign=1):
    d=a.copy()
    for power,c in b.items():
        q=d.get(power,0)+sign*c
        if q:d[power]=q
        else:d.pop(power,None)
    return d

def scale(a,k):
    return {power:k*c for power,c in a.items() if k*c}

def mul(a,b):
    if not a or not b:return {}
    d=defaultdict(int)
    for (a1,a2,a3),av in a.items():
        for (b1,b2,b3),bv in b.items():
            d[(a1+b1,a2+b2,a3+b3)]+=av*bv
    return {power:c for power,c in d.items() if c}

def sum_poly(items):
    q={}
    for item in items:q=add(q,item)
    return q

def determinant(M):
    n=len(M)
    @lru_cache(maxsize=None)
    def f(mask):
        if not mask:return ONE
        row=mask.bit_count()-1
        out={}
        # in mask, the newest row receives column j
        for j in range(n):
            if not ((mask>>j)&1):continue
            sign=-1 if (mask>>(j+1)).bit_count()%2 else 1
            term=mul(f(mask^(1<<j)),M[row][j])
            out=add(out,term,sign)
        return out
    return f((1<<n)-1)

def matrix(protected):
    states=list(range(1,8)); index={state:k for k,state in enumerate(states)}
    A=[[{} for _ in states] for _ in states]
    for state in states:
        i=index[state]
        A[i][i]=add(A[i][i],Z)
        for j in range(3):
            bit=1<<j
            if state&bit:
                new=state^bit
                rate=R if j==protected else ONE
            else:
                new=state|bit
                neighbors=sum(1 for k in (j-1,j+1) if 0<=k<3 and state&(1<<k))
                rate=scale(X,neighbors)
            if new==state or not rate:continue
            A[i][i]=add(A[i][i],rate)
            if new:
                A[i][index[new]]=add(A[i][index[new]],rate,-1)
    return A

def cramer_last(M):
    N=[[value.copy() for value in row] for row in M]
    for i in range(len(M)):N[i][-1]=ONE
    return determinant(N)

def divide_XR_one_minus_R(p):
    # Coefficientwise exact division by X R (1-R).
    by_group=defaultdict(dict)
    for (a,b,c),value in p.items():
        if a<1 or b<1:raise AssertionError('missing X R factor')
        by_group[(a-1,c)][b-1]=value
    result={}
    for (a,c),coeffs in by_group.items():
        last=max(coeffs)
        carry=0
        for b in range(last+1):
            carry+=coeffs.get(b,0)
            if b<last and carry:result[(a,b,c)]=carry
        if carry:raise AssertionError('not divisible by 1-R')
    return result

def poly_eval(poly,L,r,z):
    return sum(c*(L**a)*(r**b)*(z**d) for (a,b,d),c in poly.items())

def check():
    mid=matrix(1);end=matrix(0)
    dm=determinant(mid);de=determinant(end)
    nm=cramer_last(mid);ne=cramer_last(end)
    p=add(mul(nm,de),mul(ne,dm),-1)
    cert=divide_XR_one_minus_R(p)
    assert cert and all(isinstance(v,int) and v>0 for v in cert.values())
    assert len(cert)==159 and min(cert.values())==2 and max(cert.values())==19670
    assert max(sum(power) for power in cert)==8
    # Reconstruct the full cross-multiplied identity exactly.
    assert p==mul(mul(mul(X,R),add(ONE,R,-1)),cert)
    # Independent exact scalar linear-system computation by rational Gaussian elimination.
    def solve_rational(m,b):
        n=len(m)
        A=[[Fraction(v) for v in row]+[Fraction(b[i])] for i,row in enumerate(m)]
        for k in range(n):
            pivot=next(i for i in range(k,n) if A[i][k])
            A[k],A[pivot]=A[pivot],A[k]
            c=A[k][k];A[k]=[v/c for v in A[k]]
            for i in range(k+1,n):
                c=A[i][k]
                if c:A[i]=[v-c*w for v,w in zip(A[i],A[k])]
        x=[Fraction(0)]*n
        for i in range(n-1,-1,-1):x[i]=A[i][-1]-sum(A[i][j]*x[j] for j in range(i+1,n))
        return x
    for ll,rr,zz in [(Fraction(1),Fraction(1,2),Fraction(0)),
                     (Fraction(1),Fraction(1,2),Fraction(1)),
                     (Fraction(2,3),Fraction(3,4),Fraction(3,5)),
                     (Fraction(3),Fraction(5,4),Fraction(1,2))]:
        exact=[]
        for M,D,N in [(mid,dm,nm),(end,de,ne)]:
            m=[[poly_eval(v,ll,rr,zz) for v in row] for row in M]
            x=solve_rational(m,[1]*7)[-1]
            assert x==poly_eval(N,ll,rr,zz)/poly_eval(D,ll,rr,zz)
            exact.append(x)
        lhs=exact[0]-exact[1]
        rhs=poly_eval(p,ll,rr,zz)/(poly_eval(dm,ll,rr,zz)*poly_eval(de,ll,rr,zz))
        assert lhs==rhs
        if ll>0 and rr!=1: assert lhs*(1-rr)>0
    assert poly_eval(nm,Fraction(1),Fraction(1,2),0)/poly_eval(dm,Fraction(1),Fraction(1,2),0)==Fraction(851,182)
    assert poly_eval(ne,Fraction(1),Fraction(1,2),0)/poly_eval(de,Fraction(1),Fraction(1,2),0)==Fraction(1599,370)
    print('PASS: seven-state CTMC exact determinant identity; 159 strictly positive certificate coefficients;')
    print('max certificate degree 8, min coefficient 2, max coefficient 19670;')
    print('four independent rational Gaussian-elimination checks, including zero and positive discounts;')
    print('exact means at colonization 1, protected death rate 1/2: 851/182 and 1599/370.')

if __name__=='__main__':check()
