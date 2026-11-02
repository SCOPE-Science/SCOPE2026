#!/usr/bin/env python3
"""Independent polynomial-power Cartier reconstruction, finite-field smooth census, and F_121 point checks."""
from collections import Counter
P=11

def mul_poly(A,B):
    C=[0]*(len(A)+len(B)-1)
    for i,x in enumerate(A):
        for j,y in enumerate(B):C[i+j]=(C[i+j]+x*y)%P
    return C

def polypow(A,n):
    R=[1]
    for _ in range(n):R=mul_poly(R,A)
    return R

def c_at(poly,k):return poly[k] if k<len(poly) else 0

def matrix(a,b):
    f=[b,a,0,0,0,1]
    u=polypow(f,7);v=polypow(f,3)
    A=[[0]*4 for _ in range(4)]
    for ell in range(3):A[1+ell][0]=c_at(u,11*ell+10)
    for i in range(3):A[0][1+i]=c_at(v,10-i)
    return A

def minor_rank(A):
    from itertools import combinations
    def determinant(B):
        if len(B)==0:return 1
        if len(B)==1:return B[0][0]
        return sum(((-1)**j)*B[0][j]*determinant([row[:j]+row[j+1:] for row in B[1:]]) for j in range(len(B[0])))%P
    for k in (4,3,2,1):
        for rows in combinations(range(4),k):
            for cols in combinations(range(4),k):
                if determinant([[A[i][j] for j in cols] for i in rows])%P:return k
    return 0

def compose(A,B):return [[sum(A[i][k]*B[k][j] for k in range(4))%P for j in range(4)] for i in range(4)]

def invariants(a,b):
    M=matrix(a,b); r=minor_rank(M);t=M
    for _ in range(4):t=compose(t,M)
    return minor_rank(t),4-r

def smooth(a,b):
    f=[b,a,0,0,0,1]
    d=[(i*f[i])%11 for i in range(1,len(f))]
    for x in range(P):
        if sum(t*pow(x,i,P) for i,t in enumerate(f))%P==0 and sum(t*pow(x,i,P) for i,t in enumerate(d))%P==0:return False
    # F11 root-test alone not geometric, so independent resultant via formal Euclid.
    def trim(u):
        while u and u[-1]==0:u.pop()
        return u
    def rem(u,v):
        u=trim(u[:]);v=trim(v[:]);inv=pow(v[-1],-1,P)
        while u and len(u)>=len(v):
            h=u[-1]*inv%P;d0=len(u)-len(v)
            for i,z in enumerate(v):u[i+d0]=(u[i+d0]-h*z)%P
            trim(u)
        return u
    f=trim(f);d=trim(d)
    while d:
        f,d=d,rem(f,d)
    return len(f)==1
counter=Counter()
for a in range(11):
    for b in range(11):
        if smooth(a,b):counter[invariants(a,b)]+=1
assert counter=={(2,2):90,(0,4):10,(0,2):10},counter
assert matrix(1,0)==[[0]*4 for _ in range(4)]
assert invariants(1,5)==(0,2) and invariants(1,1)==(2,2)
print('INDEPENDENT_CARTIER_COUNTS_OK',dict(counter))

# F_121=F_11[t]/(t*t-2); 2 is a quadratic nonresidue in F11.
def add(x,y):return ((x[0]+y[0])%P,(x[1]+y[1])%P)
def mul(x,y):return ((x[0]*y[0]+2*x[1]*y[1])%P,(x[0]*y[1]+x[1]*y[0])%P)
def power(x,n):
    y=(1,0)
    while n:
        if n&1:y=mul(y,x)
        x=mul(x,x);n//=2
    return y
zero=(0,0)
F=[(u,v) for u in range(P) for v in range(P)]
cubes=set(power(z,3) for z in F)
assert len(cubes)==41
for a,b in [(1,0),(1,5),(1,1)]:
    n=1 # unique rational point at infinity, since gcd(3,5)=1
    for x in F:
        f=add(add(power(x,5),mul((a,0),x)),(b,0))
        n += 1 if f==zero else (3 if f in cubes else 0)
    print('F121_POINT_COUNT',a,b,n)
print('INDEPENDENT_VERIFY_OK')
