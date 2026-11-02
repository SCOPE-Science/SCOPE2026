#!/usr/bin/env python3
"""Independent GF(7) exhaustive check (not a geometric/algebraic-closure proof)."""
from itertools import product

P=7

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b): c[i+j]=(c[i+j]+v*w)%P
    return c

def det(A):
    A=[row[:] for row in A]
    n=len(A); r=1
    for i in range(n):
        pivot=next((j for j in range(i,n) if A[j][i]),None)
        if pivot is None:return 0
        if pivot!=i: A[i],A[pivot]=A[pivot],A[i];r=-r
        z=A[i][i];r=r*z%P;inv=pow(z,-1,P)
        for j in range(i+1,n):
            m=A[j][i]*inv%P
            if m:
                for k in range(i,n): A[j][k]=(A[j][k]-m*A[i][k])%P
    return r%P

def res_monic_quintic(f):
    deriv=[((i+1)*f[i+1])%P for i in range(5)]
    # Rows of Sylvester matrix for degrees (5,4), in descending-power order.
    f=f[::-1]; g=deriv[::-1]
    A=[]
    for shift in range(4): A.append([0]*shift+f+[0]*(3-shift))
    for shift in range(5): A.append([0]*shift+g+[0]*(4-shift))
    return det(A)

def det3(H):
    return (H[0][0]*(H[1][1]*H[2][2]-H[1][2]*H[2][1])
          - H[0][1]*(H[1][0]*H[2][2]-H[1][2]*H[2][0])
          + H[0][2]*(H[1][0]*H[2][1]-H[1][1]*H[2][0]))%P

count=ordinary=nonordinary=singular=0
for c in product(range(7),repeat=5):
    f=list(c)+[1]
    f2=mul(f,f);f4=mul(f2,f2)
    h=f2[6]
    B=[[f4[7*(i+1)-(j+1)] for j in range(3)] for i in range(3)]
    delta=res_monic_quintic(f)
    assert det3(B)==h*delta%7,(c,det3(B),h,delta)
    count+=1
    if delta==0:singular+=1
    elif h==0:nonordinary+=1
    else:ordinary+=1
assert count==7**5 and ordinary>0 and nonordinary>0
print('EXHAUSTIVE_F7_INDEPENDENT_OK',count,'ordinary',ordinary,'nonordinary',nonordinary,'singular',singular)
