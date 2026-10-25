"""Exact checks for symmetric-design graph Hodge stability; Python standard library."""
from fractions import Fraction as F
from itertools import product

CHECKS = 0

def eq(a,b):
    global CHECKS
    CHECKS += 1
    assert a == b, (a,b)

def projective_plane_incidence(p):
    def norm(x):
        for a in x:
            if a % p:
                inv=pow(a,-1,p)
                return tuple((y*inv)%p for y in x)
        raise AssertionError
    points=sorted({norm(x) for x in product(range(p),repeat=3) if any(x)})
    a=[[int(sum(x*y for x,y in zip(pt,line))%p==0) for line in points] for pt in points]
    return a

def parameters(a):
    v=len(a); k=sum(a[0]);
    lam=sum(a[0][z]*a[1][z] for z in range(v))
    for i in range(v):
        eq(sum(a[i]),k)
        eq(sum(a[j][i] for j in range(v)),k)
        for j in range(v):
            eq(sum(a[i][z]*a[j][z] for z in range(v)),k if i==j else lam)
    eq(v-1, F(k*(k-1),lam))
    assert 1<=lam<k<v
    return v,k,lam

def solve(matrix,y):
    # exact reduced Laplacian solve, last potential fixed at zero
    n=len(matrix);rows=[[F(matrix[i][j]) for j in range(n)]+[F(y[i])] for i in range(n)]
    for c in range(n):
        pivot=next(i for i in range(c,n) if rows[i][c])
        rows[c],rows[pivot]=rows[pivot],rows[c]
        v=rows[c][c];rows[c]=[z/v for z in rows[c]]
        for i in range(n):
            if i==c or not rows[i][c]: continue
            v=rows[i][c]
            rows[i]=[x-v*y for x,y in zip(rows[i],rows[c])]
    return [r[-1] for r in rows]

def test(a,description):
    v,k,lam=parameters(a)
    edges=[(p,l) for p in range(v) for l in range(v) if a[p][l]]
    e0=edges[0];p0,l0=e0
    assert len(edges)==v*k
    mat=[[0]*(2*v) for _ in range(2*v)]
    for p,l in edges:
        mat[p][p]+=1;mat[v+l][v+l]+=1
        mat[p][v+l]-=1;mat[v+l][p]-=1
    rhs=[0]*(2*v);rhs[p0]=1;rhs[v+l0]=-1
    u=solve([r[:-1] for r in mat[:-1]],rhs[:-1])+[F(0)]
    counts=[0,0,0,0,0]
    norms=F(0)
    diag=F(2*k*(k-1)+lam,v*k*lam)
    for j,(p,l) in enumerate(edges):
        val=u[p]-u[v+l]
        algebra=F(k*(int(p==p0)+int(l==l0)) -a[p0][l]-a[p][l0],v*lam)+F(1,v*k)
        eq(val,algebra)
        if j==0:
            typ=0; eq(val,diag)
        elif p==p0 or l==l0:
            typ=1;eq(val,F(k*(k-2)+lam,v*k*lam))
        else:
            crossing=a[p0][l]+a[p][l0]
            typ={1:2,2:3,0:4}[crossing]
            predicted={2:F(lam-k,v*k*lam),3:F(lam-2*k,v*k*lam),4:F(1,v*k)}[typ]
            eq(val,predicted)
        counts[typ]+=1
        norms+=abs(val)
    predicted_counts=[1,2*(k-1),2*(k-1)*(k-lam),(k-1)*(lam-1),(k-1)*(k-lam)**2//lam]
    eq(counts,predicted_counts)
    num=(5*k**3 - 4*k*k*lam-9*k*k+2*k*lam*lam+7*k*lam+4*k-2*lam*lam-2*lam)
    grad=F(num,k*(k*k-k+lam))
    cycle=1+grad-2*diag
    compact=1+F(2*(k-1)*(2*(k-lam)**2+(lam-1)*(2*k-lam)),v*k*lam)
    eq(grad,compact)
    eq(diag,F(2*v-1,v*k))
    eq(norms,grad)
    eq(1+norms-2*diag,cycle)
    eq((cycle>grad),(k>=4))
    # Direct complement row sum from solved current field.
    eq(sum(abs(int(j==0) - (u[p]-u[v+l])) for j,(p,l) in enumerate(edges)),cycle)
    print(description, 'v,k,lambda=',(v,k,lam),'rows=',counts,'gradient=',grad,'circulation=',cycle)
    return grad,cycle

def symmetric_binary_design(d):
    nonzero=[x for x in product(range(2),repeat=d) if any(x)]
    return [[int(sum(u*v for u,v in zip(x,y))%2==1) for y in nonzero] for x in nonzero]

def main():
    test([[1,1,0],[1,0,1],[0,1,1]],'2-(3,2,1)')
    had=symmetric_binary_design(4)
    test(had,'Hadamard 2-(15,8,4)')
    test([[1-z for z in row] for row in had],'Hadamard 2-(15,7,3)')
    for p in [2,3,5]:
        a=projective_plane_incidence(p)
        test(a,f'PG(2,{p})')
        test([[1-z for z in row] for row in a],f'complement PG(2,{p})')
    print('ALL EXACT CHECKS PASSED:',CHECKS)

if __name__=='__main__': main()
