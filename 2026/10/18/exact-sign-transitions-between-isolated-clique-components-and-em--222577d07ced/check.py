"""Exact checks for isolated-clique and all-clique cross-covariance.

This script uses only the Python standard library and is standalone.
Run with: python check.py
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def masks(n):
    ed = {(i,j):t for t,(i,j) in enumerate(combinations(range(n),2))}
    data = {}
    for r in range(2,n+1):
        rows=[]
        for A in combinations(range(n),r):
            aset=set(A)
            inside=sum(1<<ed[i,j] for i,j in combinations(A,2))
            cross=sum(1<<ed[min(i,j),max(i,j)] for i in A for j in range(n) if j not in aset)
            rows.append((inside,cross))
        data[r]=rows
    return data


def model_cov(n,r,s,p):
    a=comb(r,2)
    b=comb(s,2)
    m=comb(n,s)-(comb(n-r,s) if n-r>=s else 0)
    c=comb(r,s) if r>=s else 0
    ei=comb(n,r)*p**a*(1-p)**(r*(n-r))
    return ei*(c-m*p**b)

checks=0
for n in (3,4,5,6):
    E=comb(n,2)
    kinds=masks(n)
    for num,den in ((1,2),(2,5)):
        pn=Fraction(num,den)
        z=den**E
        powers=[num**i*(den-num)**(E-i) for i in range(E+1)]
        sumsI={r:0 for r in range(2,n)}
        sumsT={s:0 for s in range(2,n+1)}
        sumsIT={(r,s):0 for r in range(2,n) for s in range(2,n+1)}
        for graph in range(1<<E):
            weight=powers[graph.bit_count()]
            vals={r:sum((graph&inside)==inside and (graph&cross)==0 for inside,cross in kinds[r]) for r in range(2,n)}
            tvals={s:sum((graph&inside)==inside for inside,_ in kinds[s]) for s in range(2,n+1)}
            for r,v in vals.items():
                sumsI[r]+=weight*v
            for s,v in tvals.items():
                sumsT[s]+=weight*v
            for r,v in vals.items():
                for s,w in tvals.items():
                    sumsIT[r,s]+=weight*v*w
        for (r,s),summed in sumsIT.items():
            cov=Fraction(summed,z)-Fraction(sumsI[r]*sumsT[s],z*z)
            assert cov==model_cov(n,r,s,pn),(n,r,s,pn,cov,model_cov(n,r,s,pn))
            checks+=1

# The 7-vertex six-clique thresholds satisfy p_{7;6,6}<p_{7;6,5}.
# Their thirtieth powers are 7^(-2) and (2/7)^3 respectively.
assert Fraction(1,49) < Fraction(8,343)
checks+=1

# Independent exact test of asymptotic leading combinatorial coefficients.
for n in range(3,70):
    for r in range(2,n):
        for s in range(2,r+1):
            m=comb(n,s)-(comb(n-r,s) if n-r>=s else 0)
            assert m>comb(r,s)
            checks+=1
print(f"PASS: {checks} exact checks; full graph enumeration through six vertices.")
