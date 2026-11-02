#!/usr/bin/env python3
"""Exact Hasse polynomial identities and finite-field checks for a cyclic quintic hyperelliptic pencil."""
from itertools import permutations


def mul(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]=(c[i+j]+x*y)%p
    return trim(c)

def trim(c):
    while len(c)>1 and c[-1]==0:c.pop()
    return c

def power(a,n,p):
    r=[1]
    for _ in range(n):r=mul(r,a,p)
    return r

def add(a,b,p):
    return trim([((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%p for i in range(max(len(a),len(b)))])

def neg(a,p): return [(-v)%p for v in a]

def poly_det(mat,p):
    out=[0]
    n=len(mat)
    for perm in permutations(range(n)):
        v=[1]
        for i,j in enumerate(perm):v=mul(v,mat[i][j],p)
        inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        out=add(out,neg(v,p) if inversions%2 else v,p)
    return out

def coeffs(p):
    # t=x^5, F=(t-1)(t-L); coefficients in F_p[L].
    n=(p-1)//2
    a=[[0] for _ in range(2*n+1)]
    a[0]=[0,1]
    a[1]=neg(add([0,1],[1],p),p)
    a[2]=[1]
    b=[[1]]
    for _ in range(n):
        z=[[0] for _ in range(len(b)+2)]
        for i,r in enumerate(b):
            for j,s in enumerate(a[:3]):z[i+j]=add(z[i+j],mul(r,s,p),p)
        b=z
    return b

def hasse(p):
    cs=coeffs(p)
    z=[0]
    return [[cs[(p*i-j)//5] if p*i-j>=0 and (p*i-j)%5==0 and (p*i-j)//5<len(cs) else z for j in range(1,5)] for i in range(1,5)]

def substitute(poly,lam,p):
    out=(0,0)
    for coef in reversed(poly):out=ffadd(ffmul(out,lam,p),(coef,0),p)
    return out

def ffadd(x,y,p):return ((x[0]+y[0])%p,(x[1]+y[1])%p)

def ffmul(x,y,p):
    # Use u^2=5 in F_49; the same pairs are used for F_3 with u=0.
    return ((x[0]*y[0]+5*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)

def ff_pow(x,n,p):
    y=(1,0)
    while n:
        if n&1:y=ffmul(y,x,p)
        x=ffmul(x,x,p)
        n//=2
    return y

def matmul(a,b,p):
    return [[sumprod([a[i][t] for t in range(4)],[b[t][j] for t in range(4)],p) for j in range(4)] for i in range(4)]

def sumprod(a,b,p):
    z=(0,0)
    for x,y in zip(a,b):z=ffadd(z,ffmul(x,y,p),p)
    return z

def rank(a,p):
    a=[row[:] for row in a]
    piv=0
    for col in range(4):
        r=next((i for i in range(piv,4) if a[i][col]!=(0,0)),None)
        if r is None:continue
        a[piv],a[r]=a[r],a[piv]
        scale=ff_pow(a[piv][col],p*p-2,p) if p==7 else ff_pow(a[piv][col],p-2,p)
        for j in range(col,4):a[piv][j]=ffmul(a[piv][j],scale,p)
        for i in range(4):
            if i!=piv:
                v=a[i][col]
                for j in range(col,4):
                    t=ffmul(v,a[piv][j],p)
                    a[i][j]=ffadd(a[i][j],((-t[0])%p,(-t[1])%p),p)
        piv+=1
    return piv

def check():
    for p in (3,7):
        H=hasse(p)
        determinant=poly_det(H,p)
        if p==3:
            expected=neg(mul([0,1],mul([1,1],[1,1],p),p),p)
        else:
            expected=mul([0,0,0,3],mul(mul([1,1],[1,1],p),mul([1,3,1],[1,3,1],p),p),p)
        assert determinant==expected,(p,determinant,expected)
        print('DETERMINANT',p,determinant)
        for i in range(4):
            nz=[j+1 for j,h in enumerate(H[i]) if h!=[0]]
            assert len(nz)==1 and nz[0]%5==(p*(i+1))%5,(p,nz)
    # Exhaust all marked smooth parameters in F_7 and F_49.
    for p,elems in ((3,[(a,0) for a in range(3)]),
                    (7,[(a,b) for a in range(7) for b in range(7)])):
        H=hasse(p)
        checked=0
        nonordinary=[]
        for lam in elems:
            if lam in ((0,0),(1,0)):continue
            checked+=1
            M=[[substitute(h,lam,p) for h in row] for row in H]
            base_rank=rank(M,p)
            prod=[[(int(i==j),0) for j in range(4)] for i in range(4)]
            for step in range(4):
                twist=[[ff_pow(z,p**step,p) for z in row] for row in M]
                prod=matmul(prod,twist,p)
            stable=rank(prod,p)
            det=substitute(poly_det(H,p),lam,p)
            assert stable==(0 if det==(0,0) else 4),(p,lam,stable,det)
            assert base_rank==(2 if det==(0,0) else 4),(p,lam,base_rank)
            if stable==0:nonordinary.append(lam)
        print('FIELD',p,'checked',checked,'nonordinary',nonordinary)
        assert len(nonordinary)==(1 if p==3 else 3)
        if p==7:
            assert (6,0) in nonordinary
            assert sum(1 for z in nonordinary if z[1]==0)==1
            assert all(ffadd(ffadd(ffmul(z,z,7),ffmul((3,0),z,7),7),(1,0),7)==(0,0) for z in nonordinary if z!=(6,0))
    print('CYCLIC5_EXACT_DETERMINANTS_AND_STABLE_RANKS_OK')

if __name__=='__main__':check()
