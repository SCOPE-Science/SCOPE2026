#!/usr/bin/env python3
"""Exact minimal total-domination EGF and exhaustive small rook-board verification."""
from collections import Counter
from fractions import Fraction
from math import factorial


def add(A, B):
    out = dict(A)
    for key, val in B.items():
        out[key] = out.get(key, Fraction(0)) + val
        if not out[key]:
            del out[key]
    return out


def mul(A, B, max_r, max_c):
    out = {}
    for (a,b,k),x in A.items():
        for (c,d,l),y in B.items():
            if a+c <= max_r and b+d <= max_c:
                key = (a+c,b+d,k+l)
                out[key] = out.get(key, Fraction(0)) + x*y
    return {k:v for k,v in out.items() if v}


def exp_poly(P, max_r, max_c):
    power={(0,0,0): Fraction(1)}
    out=dict(power)
    for j in range(1,(max_r+max_c)//3+1):
        power=mul(power,P,max_r,max_c)
        if not power:break
        out=add(out,{k:v/Fraction(factorial(j)) for k,v in power.items()})
    return out


def species_polynomial(m,n):
    row={}
    for k in range(2,m+1):
        row[(k,1,k)]=Fraction(1,factorial(k))
    row[(1,2,2)]=Fraction(1,2)
    for k in range(2,min(n,m-1)+1):
        row[(k+1,k,2*k)]=Fraction(1,factorial(k))
    col={(b,a,k):v for (a,b,k),v in row.items() if b<=m and a<=n}
    # For rectangular boards, transpose generators must use independent constraints;
    # extra terms in row exceeding original bounds can never contribute.
    for k in range(2,n+1):
        col[(1,k,k)]=Fraction(1,factorial(k))
    col[(2,1,2)]=Fraction(1,2)
    for k in range(2,min(m,n-1)+1):
        col[(k,k+1,2*k)]=Fraction(1,factorial(k))
    full={(1,2,2):Fraction(1,2),(2,1,2):Fraction(1,2)}
    iso_cols={(0,k,0):Fraction(1,factorial(k)) for k in range(1,n+1)}
    iso_rows={(k,0,0):Fraction(1,factorial(k)) for k in range(1,m+1)}
    E=add(add(mul(iso_cols,exp_poly(row,m,n),m,n),mul(iso_rows,exp_poly(col,m,n),m,n)),exp_poly(full,m,n))
    return {k:int(v*factorial(m)*factorial(n)) for (i,j,k),v in E.items() if i==m and j==n}


def total(mask,m,n):
    rows=[0]*m; cols=[0]*n
    for i in range(m):
        for j in range(n):
            if mask>>(i*n+j)&1:
                rows[i]+=1; cols[j]+=1
    if 0 in rows and 0 in cols:return False
    for i in range(m):
        for j in range(n):
            if mask>>(i*n+j)&1 and rows[i]+cols[j]<3:
                return False
    return True


def brute(m,n):
    out=Counter()
    for mask in range(1<<(m*n)):
        if not total(mask,m,n):continue
        if all(not total(mask^(1<<k),m,n) for k in range(m*n) if mask>>k&1):
            out[mask.bit_count()]+=1
    return dict(out)


def main():
    boards=((2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(3,3),(3,4),(3,5),(4,4))
    processed=0
    for m,n in boards:
        a=species_polynomial(m,n)
        b=brute(m,n)
        assert a==b,(m,n,a,b)
        processed+=1<<(m*n)
    known={(3,3):51,(3,4):97,(4,4):368,(4,5):2229,(5,5):7310,(5,6):44491,(6,6):301572}
    for (m,n),val in known.items():
        assert sum(species_polynomial(m,n).values())==val,(m,n,species_polynomial(m,n),val)
    print('VERIFY_OK board_shapes=',len(boards),'brute_subsets=',processed,'prior_table_totals=',len(known))
    for m,n in [(2,4),(3,3),(3,4),(4,4),(4,5),(5,5)]:
        print('POLY',m,n,sorted(species_polynomial(m,n).items()))
if __name__=='__main__':main()
