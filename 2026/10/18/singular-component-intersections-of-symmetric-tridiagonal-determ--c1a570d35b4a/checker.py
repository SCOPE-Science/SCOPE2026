"""Exact checks for projective generic symmetric tridiagonal determinant geometry."""
from itertools import product
from random import Random
from math import comb
import sympy as sp

def cont(a,b,p=None):
    """Determinant of symmetric tridiagonal submatrix, modulo p optionally."""
    x,y=1, a[0] if a else 1
    if len(a)==0:return 1
    if p:y%=p
    for j in range(1,len(a)):
        x,y=y,a[j]*y-b[j-1]*b[j-1]*x
        if p:x%=p;y%=p
    return y

def gradient(a,b,p):
    n=len(a)
    da=[cont(a[:i],b[:max(0,i-1)],p)*cont(a[i+1:],b[i+1:],p)%p for i in range(n)]
    db=[(-2*b[i]*cont(a[:i],b[:max(0,i-1)],p)*cont(a[i+2:],b[i+2:],p))%p for i in range(n-1)]
    return da,db

def cut_locus(a,b,p):
    n=len(a)
    return any(b[i]%p==0 and cont(a[:i+1],b[:i],p)==0 and cont(a[i+1:],b[i+1:],p)==0 for i in range(n-1))

def rankmod(a,b,p):
    n=len(a)
    M=[[0]*n for _ in range(n)]
    for i in range(n):
        M[i][i]=a[i]%p
        if i+1<n: M[i][i+1]=b[i]%p; M[i+1][i]=b[i]%p
    r=0
    for c in range(n):
        v=next((i for i in range(r,n) if M[i][c]%p),None)
        if v is None: continue
        M[r],M[v]=M[v],M[r]
        z=pow(M[r][c],-1,p)
        for j in range(c,n):M[r][j]=M[r][j]*z%p
        for i in range(r+1,n):
            k=M[i][c]
            for j in range(c,n):M[i][j]=(M[i][j]-k*M[r][j])%p
        r+=1
    return r

def check_point(a,b,p):
    f=cont(a,b,p)
    g=gradient(a,b,p)
    jac=(f%p==0 and not any(g[0]+g[1]))
    cut=cut_locus(a,b,p)
    rank=rankmod(a,b,p)<=len(a)-2
    assert jac==cut==rank,(a,b,p,jac,cut,rank,g)

def run():
    # Independent full enumeration over F_3 for orders 3,4,5.
    for n in range(3,6):
        count=0
        for vals in product(range(3),repeat=2*n-1):
            if not any(vals): continue
            a,b=vals[:n],vals[n:]
            check_point(a,b,3)
            count+=1
        print(f'F3_order_{n}_nonzero_vectors={count}')
    # Check every scheme-support intersection set for n<=5 over F_3.
    for n in range(3,6):
        nonempty_subsets=[tuple(i for i in range(n-1) if mask&(1<<i))
                          for mask in range(1,1<<(n-1))]
        for vals in product(range(3),repeat=2*n-1):
            if not any(vals): continue
            a,b=vals[:n],vals[n:]
            incomp=[b[i]%3==0 and cont(a[:i+1],b[:i],3)==0 and
                    cont(a[i+1:],b[i+1:],3)==0 for i in range(n-1)]
            for S in nonempty_subsets:
                pred=all(incomp[i] for i in S)
                endpoint=(all(b[i]%3==0 for i in S) and
                          cont(a[:S[0]+1],b[:S[0]],3)==0 and
                          cont(a[S[-1]+1:],b[S[-1]+1:],3)==0)
                assert pred==endpoint,(n,a,b,S)
        print(f'F3_order_{n}_all_component_intersections=OK')
    rng=Random(20261015)
    for n in (6,7):
        for _ in range(2000):
            a=[rng.randrange(5) for i in range(n)]
            b=[rng.randrange(5) for i in range(n-1)]
            check_point(a,b,5)
        print(f'F5_order_{n}_samples=2000')
    # Symbolic continuants and irreducibility for small sizes.
    for n in range(2,7):
        a=sp.symbols('a1:'+str(n+1));b=sp.symbols('b1:'+str(n))
        F=sp.expand(cont(a,b))
        assert len(sp.factor_list(F)[1])==1
        assert sp.factor_list(F)[1][0][1]==1
        for j in range(n-1):
            lhs=F.subs(b[j],0)
            rhs=cont(a[:j+1],b[:j])*cont(a[j+1:],b[j+1:])
            assert sp.expand(lhs-rhs)==0
            assert sp.expand(F-rhs + b[j]**2*cont(a[:j],b[:max(j-1,0)])*cont(a[j+2:],b[j+2:]))==0
        print(f'symbolic_order_{n}=OK')
    # Explicit rational transverse slices at generic points of each cut component.
    x,y,w=sp.symbols('x y w')
    for n in range(3,10):
        for j in range(1,n):
            left=j; right=n-j
            a=[sp.Rational(2) for _ in range(n)]
            a[j-1]=sp.Rational(j-1,j)+x
            a[j]=sp.Rational(right-1,right)+y
            b=[sp.Integer(1) for _ in range(n-1)]
            b[j-1]=w
            F=sp.expand(cont(a,b))
            assert sp.expand(F-j*right*(x*y-w*w))==0,(n,j,F)
        print(f'transverse_slices_order_{n}=OK')
    for n in range(3,30):
        assert sum(i*(n-i) for i in range(1,n))==comb(n+1,3)
    print('VERIFY_OK')
if __name__=='__main__': run()
