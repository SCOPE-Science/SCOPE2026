"""Finite-field checks of ID-derivation dimensions for almost-abelian Lie algebras."""
from itertools import product

def rref(matrix,p):
    a=[list(row) for row in matrix]
    if not a: return [],[]
    m,n=len(a),len(a[0]); piv=[]; k=0
    for j in range(n):
        s=next((i for i in range(k,m) if a[i][j]%p),None)
        if s is None:continue
        a[k],a[s]=a[s],a[k]; u=pow(a[k][j],-1,p)
        a[k]=[x*u%p for x in a[k]]
        for i in range(m):
            if i!=k:
                t=a[i][j];a[i]=[(x-t*y)%p for x,y in zip(a[i],a[k])]
        piv.append(j);k+=1
        if k==m:break
    return a,piv

def rank(M,p):return len(rref(M,p)[1]) if M else 0

def nullspace(M,p):
    R,ps=rref(M,p); n=len(M[0]);free=[j for j in range(n) if j not in ps]
    out=[]
    for j in free:
        v=[0]*n;v[j]=1
        for i,t in enumerate(ps):v[t]=(-R[i][j])%p
        out.append(v)
    return out

def matmul(A,B,p):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))%p for j in range(n)] for i in range(n)]

def dimension_ID_mod_center(T,p):
    n=len(T)
    rows=[]
    for k in range(n):
        for l in range(n):
            c=[0]*(n*n)
            for a in range(n):
                for b in range(n):
                    c[a*n+b]=((int(k==a)*T[b][l]-T[k][a]*int(l==b)))%p
            rows.append(c)
    null_left=nullspace([[T[j][i] for j in range(n)] for i in range(n)],p)
    for h in null_left:
        for j in range(n):
            c=[0]*(n*n)
            for i in range(n):c[i*n+j]=h[i]
            rows.append(c)
    return n*n-rank(rows,p)

def check(T,p):
    n=len(T);r=rank(T,p)
    phi=dimension_ID_mod_center(T,p)
    r2=rank(matmul(T,T,p),p)
    expectation=(r==0 or (r==1 and (r2==1 or n==2)))
    observed=(phi==0 if r==0 else phi==1)
    assert expectation==observed,(p,T,r,r2,phi)
    assert phi>=int(r>0)
    return phi

def run():
    counts={}
    for n in (1,2,3):
        for entries in product(range(2),repeat=n*n):
            T=[list(entries[i*n:(i+1)*n]) for i in range(n)]
            check(T,2)
        counts[n]=2**(n*n)
    print('ALL_BINARY_ENDOMORPHISMS_DIMENSIONS_AND_SEMICOMPLETE_BOUNDARY_OK',counts)
    examples=[
      ([[0,1],[0,0]],2,1),
      ([[1,0,0],[0,0,0],[0,0,0]],3,1),
      ([[0,1,0],[0,0,0],[0,0,0]],3,2),
      ([[0,1,0],[0,0,1],[0,0,0]],3,2),
      ([[1,0,0],[0,1,0],[0,0,0]],3,4),
      ([[0,1],[1,1]],2,2),
      ([[0,1,0,0],[0,0,0,0],[0,0,0,1],[0,0,0,0]],2,4),
    ]
    for T,p,expected in examples:
        actual=check(T,p)
        assert actual==expected,(T,p,actual,expected)
    print('PRIMARY_COMPONENT_DIMENSION_EXAMPLES_OK')
    print('VERIFY_OK')
if __name__=='__main__':run()
