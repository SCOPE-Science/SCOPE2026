"""Exact integer verification of representative hollow-symmetric determinant strata.
Standalone, Python standard library only. These finite tests corroborate, not prove,
the all-rank theorem.
"""
from fractions import Fraction
from itertools import combinations

def determinant(m):
    n=len(m)
    if n==0: return 1
    a=[[Fraction(t) for t in row] for row in m]
    d=Fraction(1)
    for i in range(n):
        p=next((j for j in range(i,n) if a[j][i]),None)
        if p is None:return 0
        if p!=i: a[i],a[p]=a[p],a[i];d=-d
        pivot=a[i][i];d*=pivot
        for j in range(i+1,n):
            z=a[j][i]/pivot
            for k in range(i+1,n):a[j][k]-=z*a[i][k]
            a[j][i]=0
    return d

def rank(m):
    if not m:return 0
    a=[[Fraction(t) for t in row] for row in m]; n=len(a);p=len(a[0]); i=0
    for j in range(p):
        w=next((k for k in range(i,n) if a[k][j]),None)
        if w is None: continue
        a[i],a[w]=a[w],a[i]; z=a[i][j]
        for c in range(j,p):a[i][c]/=z
        for k in range(n):
            if k!=i and a[k][j]:
                z=a[k][j]
                for c in range(j,p): a[k][c]-=z*a[i][c]
        i+=1
        if i==n: break
    return i

def minor(m,rows,cols):
    return determinant([[m[i][j] for j in cols] for i in rows])

def gradient_hessian(m):
    n=len(m);edges=list(combinations(range(n),2));g=[];H=[]
    for i,j in edges:
        ri=[r for r in range(n) if r!=i];cj=[c for c in range(n) if c!=j]
        g.append(2*(-1)**(i+j)*minor(m,ri,cj))
        row=[]
        for k,l in edges:
            v=0
            for a,b in [(k,l),(l,k)]:
                if a in ri and b in cj:
                    aa=ri.index(a);bb=cj.index(b)
                    v+=(-1)**(i+j+aa+bb)*minor(m,[r for r in ri if r!=a],[c for c in cj if c!=b])
            row.append(2*v)
        H.append(row)
    return g,H

def gram_example(n):
    r=n-2
    e=lambda i: [int(i==j) for j in range(r)]
    v=[e(0),e(1)]
    for j in range(2,r):
        w=[0]*r;w[0]=2;w[1]=-1;w[j]=2;v.append(w)
    v += [e(0),e(1)]
    assert len(v)==n
    def dot(a,b):
        return a[0]*b[1]+a[1]*b[0]+sum(a[i]*b[i] for i in range(2,r))
    return [[dot(v[i],v[j]) for j in range(n)] for i in range(n)]

def zero_row_example(n):
    return [[int(i!=j and i>0 and j>0) for j in range(n)] for i in range(n)]

def smooth_example(n):
    a=[[0]*n for _ in range(n)]
    a[0][1]=a[1][0]=a[1][2]=a[2][1]=1
    for i in range(3,n):
        for j in range(3,n):
            if i!=j:a[i][j]=1
    return a

def run():
    runs=0
    for n in (5,6):
        N=n*(n-1)//2
        A=gram_example(n)
        assert all(A[i][i]==0 for i in range(n))
        assert all(any(A[i][j] for j in range(n)) for i in range(n))
        assert rank(A)==n-2 and determinant(A)==0
        g,H=gradient_hessian(A)
        assert g==[0]*N and rank(H)==3
        B=zero_row_example(n)
        assert rank(B)==n-1 and determinant(B)==0
        g,H=gradient_hessian(B)
        assert g==[0]*N and rank(H)==n-1
        C=smooth_example(n)
        assert rank(C)==n-1 and determinant(C)==0
        g,H=gradient_hessian(C)
        assert any(g)
        runs+=3
        print('n=',n,'rank-R=',rank(A),'rank-L=',rank(B),'rank-smooth=',rank(C),'Hessian-R=3','Hessian-L=',n-1)
    # A nonzero symmetric hollow matrix of order >=2 is readily available.
    for n in range(5,11):
        T=[[int(i!=j) for j in range(n)] for i in range(n)]
        assert determinant(T)==(n-1)*(-1)**(n-1)
        runs+=1
    print('VERIFY_OK',runs,'exact witness groups')
if __name__=='__main__':run()
