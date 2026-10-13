"""Finite-field verification of zero-product-preserving bilinear forms.
Run with Python 3: python3 verify.py. No nonstandard dependencies.
The theorem for arbitrary fields is proved algebraically, not by this test.
"""
from itertools import product

def rank(rows, p, width):
    a=[list(map(lambda x:x%p,row)) for row in rows]
    k=0
    for col in range(width):
        pivot=next((i for i in range(k,len(a)) if a[i][col]),None)
        if pivot is None: continue
        a[k],a[pivot]=a[pivot],a[k]
        inv=pow(a[k][col],-1,p)
        a[k]=[(x*inv)%p for x in a[k]]
        for i in range(len(a)):
            if i!=k and a[i][col]:
                b=a[i][col]
                a[i]=[(x-b*y)%p for x,y in zip(a[i],a[k])]
        k+=1
        if k==len(a):break
    return k

def det_nonzero(mat,p):
    return rank(mat,p,len(mat))==len(mat)

def mult(a,b,p,d):
    s=a[0]; t=b[0]
    return ((s*t)%p,)+tuple((s*b[i]+t*a[i])%p for i in range(1,d+1))+((s*b[-1]+t*a[-1]+sum(a[i]*b[i] for i in range(1,d+1)))%p,)

def build_form(par,p,d):
    # a, left[d], right[d], c, e, lambda
    n=d+2
    M=[[0]*n for _ in range(n)]
    M[0][0]=par[0]
    for i in range(d):
        M[0][i+1]=par[i+1]
        M[i+1][0]=par[d+i+1]
        M[i+1][i+1]=par[-1]
    M[0][-1]=par[2*d+1]
    M[-1][0]=par[2*d+2]
    return M

def run(p,d):
    n=d+2
    els=list(product(range(p),repeat=n))
    constraints=[]
    for a in els:
        for b in els:
            if mult(a,b,p,d)==(0,)*n:
                constraints.append([a[i]*b[j]%p for i in range(n) for j in range(n)])
    dimension=n*n-rank(constraints,p,n*n)
    assert dimension==2*d+4,(p,d,dimension)
    basis=[]
    for j in range(2*d+4):
        pars=[0]*(2*d+4);pars[j]=1
        basis.append(sum(build_form(pars,p,d),[]))
    assert rank(basis,p,n*n)==dimension
    nonsingular=0
    symmetric_dimension=0
    for pars in product(range(p),repeat=2*d+4):
        M=build_form(pars,p,d)
        if det_nonzero(M,p): nonsingular+=1
    assert nonsingular==p**(2*d+1)*(p-1)**3,(p,d,nonsingular)
    # Symmetric parameter subspace has independent coordinates a, left[d], c, lambda.
    symbasis=[]
    for j in range(d+3):
        pars=[0]*(2*d+4)
        if j==0: pars[0]=1
        elif 1<=j<=d: pars[j]=pars[d+j]=1
        elif j==d+1: pars[2*d+1]=pars[2*d+2]=1
        else: pars[-1]=1
        M=build_form(pars,p,d)
        assert M==[list(x) for x in zip(*M)]
        symbasis.append(sum(M,[]))
    assert rank(symbasis,p,n*n)==d+3
    # Product-factor forms: a, equal left/right[d], c=e=lambda.
    prod=[]
    for j in range(d+2):
        pars=[0]*(2*d+4)
        if j==0:pars[0]=1
        elif j<=d: pars[j]=pars[d+j]=1
        else:pars[2*d+1]=pars[2*d+2]=pars[-1]=1
        prod.append(sum(build_form(pars,p,d),[]))
    assert rank(prod,p,n*n)==d+2
    print(f"p={p}, d={d}: all zero-product constraints rank={n*n-dimension}; admissible dim={dimension}; symmetric dim={d+3}; product-factor dim={d+2}; nonsingular forms={nonsingular}; OK")

for p,d in [(2,2),(3,2),(2,3)]:run(p,d)
print('VERIFY_OK')
