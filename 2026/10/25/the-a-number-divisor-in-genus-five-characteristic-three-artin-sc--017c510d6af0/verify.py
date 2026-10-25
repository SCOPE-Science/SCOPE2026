#!/usr/bin/env python3
"""Exact characteristic-three Cartier checks for the genus-five two-pole family."""
from itertools import product

def rank_mod3(mat):
    a=[list(map(lambda v:v%3,row)) for row in mat]
    m=len(a); n=len(a[0]); j=0
    for i in range(n):
        k=next((k for k in range(j,m) if a[k][i]),None)
        if k is None:continue
        a[j],a[k]=a[k],a[j]
        u=pow(a[j][i],-1,3)
        a[j]=[(u*t)%3 for t in a[j]]
        for t in range(m):
            if t!=j:
                v=a[t][i]
                a[t]=[(x-v*y)%3 for x,y in zip(a[t],a[j])]
        j+=1
        if j==m:break
    return j

def mul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))%3
             for j in range(len(b[0]))] for i in range(len(a))]

def cartier_laurent(poly):
    return {(i+1)//3-1:coeff%3 for i,coeff in poly.items()
            if (i+1)%3==0 and coeff%3}

# Basis ordered dx/x, dx, x dx, y dx/x, y dx.
# The curves satisfy y^3-y=x^4+a*x^2+b*x+c/x.
for a,b,c in product(range(3),range(3),(1,2)):
    f={4:1,2:a,1:b,-1:c}
    # C(y*P dx)=y C(P dx)-C(fP dx), valid by y^3=y+f.
    cf=cartier_laurent(f)
    cfx=cartier_laurent({i-1:v for i,v in f.items()})
    assert cf==({-1:c,0:a} if a else {-1:c})
    assert cfx=={}
    cols=[(1,0,0,0,0),(0,0,0,0,0),(0,0,0,0,0),
          (0,0,0,1,0),(-c,-a,0,0,0)]
    M=[[cols[j][i]%3 for j in range(5)] for i in range(5)]
    assert rank_mod3(M)==(2 if a==0 else 3)
    P=M
    for _ in range(6):P=mul(P,M)
    assert rank_mod3(P)==2

# The only partitions of d+2=7 into e_i>=2 with e_i !=1 mod3.
def partitions(s,low=2):
    if s==0:
        yield ()
    for v in range(low,s+1):
        if v%3!=1:
            for rest in partitions(s-v,v):
                yield (v,)+rest
assert set(partitions(7))=={(2,5),(2,2,3)}

# Canonical divisor from the two lower jumps 4 and 1:
# div(dx)=4 P_infinity+4 P_0.
# Hence v_inf(x,y,dx)=(-3,-4,4), v_0=(3,-1,4).
for i,j in [(-1,0),(0,0),(1,0),(-1,1),(0,1)]:
    assert 4-3*i-4*j>=0
    assert 4+3*i-j>=0
print('VERIFY_OK: all 18 F3 specializations, ranks, p-ranks, pole partitions, regular basis')
