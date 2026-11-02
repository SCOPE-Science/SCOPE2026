"""Exact characteristic-five Cartier calculation for a genus-seven trigonal pencil.

Run: python3 verify_cartier.py
Only the Python standard library is required.
"""
from itertools import product

P=5
ZERO=(0,0); ONE=(1,0)

def plus(u,v):return ((u[0]+v[0])%P,(u[1]+v[1])%P)
def mul(u,v):return ((u[0]*v[0]+2*u[1]*v[1])%P,(u[0]*v[1]+u[1]*v[0])%P)
def power(a,n):
    z=ONE
    while n:
        if n&1:z=mul(z,a)
        a=mul(a,a);n//=2
    return z

def poly_mul(a,b):
    c=[ZERO]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=plus(c[i+j],mul(x,y))
    return c

def coeff(a,j): return a[j] if 0<=j<len(a) else ZERO

def rank(A):
    B=[[x for x in row] for row in A]; m=len(B);n=len(B[0]) if m else 0
    r=0
    for j in range(n):
        pivot=next((i for i in range(r,m) if B[i][j]!=ZERO),None)
        if pivot is None:continue
        B[r],B[pivot]=B[pivot],B[r]
        t=power(B[r][j],23)  # field inverse in F_25
        B[r]=[mul(t,x) for x in B[r]]
        for i in range(m):
            if i!=r and B[i][j]!=ZERO:
                factor=B[i][j]
                B[i]=[plus(x,mul(((-factor[0])%5,(-factor[1])%5),y)) for x,y in zip(B[i],B[r])]
        r+=1
        if r==m:break
    return r

def matmul(A,B):
    return [[sumf(mul(A[i][k],B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def sumf(items):
    z=ZERO
    for v in items:z=plus(z,v)
    return z

def frob(A): return [[power(v,5) for v in row] for row in A]

def cartier(a):
    # Basis A0,A1: x^i dx/y (i=0,1); B0,...,B4: x^j dx/y^2 (j=0,...,4)
    f=[ONE]+[ZERO]*3+[a]+[ZERO]*3+[ONE]
    f3=poly_mul(poly_mul(f,f),f)
    M=[[ZERO for j in range(7)] for i in range(7)]
    for source in range(7):
        if source<2:
            i=source;pol=f3;target_start=2; target_max=5
        else:
            i=source-2;pol=f;target_start=0;target_max=2
        for target in range(target_max):
            exponent=5*(target+1)-1-i
            M[target_start+target][source]=power(coeff(pol,exponent),5)
    return M

def stable_rank(M):
    d=len(M)
    Q=[[ONE if i==j else ZERO for j in range(d)] for i in range(d)]
    for n in range(2*d):
        Q=matmul(Q,M if n%2==0 else frob(M))
    return rank(Q)

def restricted(M,inds):
    return [[M[i][j] for j in inds] for i in inds]

def main():
    elements=list(product(range(5),repeat=2))
    bad=[];drop=[];generic=[]
    for a in elements:
        sq=power(a,2);six=power(a,6)
        nonsmooth=(plus(sq,ONE)==ZERO)
        f=cartier(a)
        a_number=7-rank(f)
        pr=stable_rank(f)
        if nonsmooth:
            bad.append(a)
            continue
        invariant=restricted(f,[1,3,5])
        anti=restricted(f,[0,2,4,6])
        assert all(f[i][j]==ZERO for i in (1,3,5) for j in (0,2,4,6))
        assert all(f[i][j]==ZERO for i in (0,2,4,6) for j in (1,3,5))
        assert rank(invariant)==2 and stable_rank(invariant)==2
        assert rank(anti)==2 and 4-rank(anti)==2
        assert a_number==3,(a,'a',a_number)
        expected=2 if plus(mul((3,0),six),ONE)==ZERO else 4
        assert pr==expected and stable_rank(anti)==expected-2,(a,pr,expected)
        (drop if pr==2 else generic).append(a)
    assert len(bad)==2 and len(drop)==6 and len(generic)==17
    assert rank(cartier((0,0)))==4 and stable_rank(cartier((0,0)))==4
    assert stable_rank(cartier((0,1)))==2 # t^2=2, so t^6=3
    print('GENUS7_TRIGONAL_CHAR5_CARTIER_EXHAUSTIVE_GF25_OK')
    print('smooth=23 rank4=17 rank2=6 excluded=2; curve a_number=3')
    print('quotient genus3 p_rank=2 a_number=1; Prym dimension4 p_rank=2 or 0 a_number=2')
    print('exceptional_parameters=',drop)
if __name__=='__main__':main()
