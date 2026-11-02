"""Independent exact integer certificate for sharp path 1-variation, N=5,6.
Run: python3 path_maximal_independent.py (Python standard library only).
"""
from itertools import combinations
from math import gcd
from functools import reduce

S=60

def det3(a,b,c,d,e,f,g,h,i):
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

def determinant(m):
    if len(m)==3:
        return det3(*[v for row in m for v in row])
    return sum((1 if j%2==0 else -1)*m[0][j]
               *det3(*[m[r][c] for r in (1,2,3) for c in range(4) if c!=j])
               for j in range(4))

def verify(n):
    A=[];H=set()
    for i in range(n):
        row=[]
        for radius in range(max(i,n-i-1)+1):
            B=[v for v in range(n) if abs(i-v)<=radius]
            coeff=tuple((S//len(B))*sum(v>j for v in B) for j in range(n-1))
            if coeff not in row:row.append(coeff)
        A.append(row)
        for a,b in combinations(row,2):
            delta=tuple(u-v for u,v in zip(a,b))
            g=reduce(gcd,delta,0)
            if g:
                normal=tuple(v//g for v in delta)
                if next(v for v in normal if v)<0:
                    normal=tuple(-v for v in normal)
                H.add(normal)
    for j in range(n-1):
        e=[0]*(n-1);e[j]=1;H.add(tuple(e))
    assert len(H)==(27 if n==5 else 46)
    tuples=rank_full=rays=ties=0
    for rows in combinations(sorted(H),n-2):
        tuples+=1
        x=tuple((-1 if omit%2 else 1)*determinant(tuple(tuple(row[j] for j in range(n-1) if j!=omit) for row in rows)) for omit in range(n-1))
        L=sum(abs(v) for v in x)
        if L==0:continue
        rank_full+=1
        for sgn in (1,-1):
            u=tuple(sgn*v for v in x)
            m=[max(sum(a*b for a,b in zip(v,u)) for v in row) for row in A]
            upper=sum(abs(m[k+1]-m[k]) for k in range(n-1))
            assert n*upper<=(n-1)*S*L,(n,u,upper,L)
            ties+= n*upper==(n-1)*S*L
            rays+=1
    assert tuples==(2925 if n==5 else 163185)
    if n==6:assert (rank_full,rays,ties)==(151429,302858,7268)
    print('PYTHON_CERTIFICATE_OK',n,len(H),tuples,rank_full,rays,ties)

verify(5)
verify(6)
