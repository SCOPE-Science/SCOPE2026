#!/usr/bin/env python3
"""Independent finite-field coefficient, stable-rank and point-count tests."""
P=7

def multiply(f,g):
    out=[0]*(len(f)+len(g)-1)
    for i,c in enumerate(f):
        for j,d in enumerate(g):out[i+j]=(out[i+j]+c*d)%P
    return out

def polynomial_power(f,e):
    out=[1]
    for _ in range(e):out=multiply(out,f)
    return out

def entry(v,i):return v[i] if i<len(v) else 0

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%P for j in range(len(B[0]))] for i in range(len(A))]

def rank(A):
    A=[r[:] for r in A]
    m,n=len(A),len(A[0]);r=0
    for j in range(n):
        piv=next((i for i in range(r,m) if A[i][j]%P),None)
        if piv is None:continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][j],-1,P)
        A[r]=[(x*inv)%P for x in A[r]]
        for i in range(m):
            if i!=r and A[i][j]%P:
                d=A[i][j]
                A[i]=[(A[i][k]-d*A[r][k])%P for k in range(n)]
        r+=1
        if r==m:break
    return r

basis=[(1,0),(2,0),(2,1),(3,0),(3,1),(3,2)]
Ycount=[sum(pow(y,4,P)==z for y in range(P)) for z in range(P)]
counts={n:0 for n in range(5)}
for a in range(P):
 for b in range(P):
    f=[1,b,a,0,0,1]
    deriv=[i*f[i]%P for i in range(1,6)]
    # Squarefree check by testing in F_(7^5) would be insufficient;
    # use the exact universal discriminant instead.
    D=(3*a**5+a**4*b*b+3*a*a*b+3*a*b**3-3*b**5+3)%P
    if D==0:continue
    powers={e:polynomial_power(f,e) for e in (1,3,5)}
    M=[[0]*6 for _ in range(6)]
    for c,(j,i) in enumerate(basis):
        jj=next(q for q in (1,2,3) if (7*q-j)%4==0)
        e=(7*jj-j)//4
        for r,(k,h) in enumerate(basis):
            if jj==k:M[r][c]=entry(powers[e],7*(h+1)-1-i)
    H=(-2*a**4-3*a*b+3*b**3)%P
    U=(a**3-b)%P
    V=3*a%P
    exp_rank=2*(H!=0)+(U!=0)+(V!=0)
    exp_a=2 if (U and V) else 3
    K=[[int(i==j) for j in range(6)] for i in range(6)]
    for _ in range(6):K=matmul(K,M)
    assert rank(K)==exp_rank,(a,b,rank(K),exp_rank)
    assert 6-rank(M)==exp_a,(a,b,6-rank(M),exp_a)
    # Weil Lefschetz trace formula modulo p: #C(F_7) = 1 - tr(HW) mod 7.
    points=1+sum(Ycount[(pow(x,5,P)+a*pow(x,2,P)+b*x+1)%P] for x in range(P))
    assert (points+sum(M[i][i] for i in range(6))-1)%P==0,(a,b,points)
    counts[exp_rank]+=1
assert counts=={0:1,1:1,2:4,3:9,4:29},counts
print('CYCLIC4_G6_PRIMEFIELD_OK',counts)
