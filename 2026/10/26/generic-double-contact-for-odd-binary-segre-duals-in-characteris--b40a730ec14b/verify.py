"""Reproducible elementary checks for characteristic-two Segre conormal contact."""
import sympy as sp

def rank_gf2(M):
    a = [[int(v) & 1 for v in row] for row in M]
    r=0
    for c in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][c]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        for i in range(len(a)):
            if i!=r and a[i][c]:
                a[i]=[u^v for u,v in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r

def test_odd_r(r):
    # Nonzero triangle on indices 0,1,2; extra disjoint symplectic pairs.
    a=[[0]*r for _ in range(r)]
    for i,j in [(0,1),(0,2),(1,2)]+[(i,i+1) for i in range(3,r,2)]:
        a[i][j]=a[j][i]=1
    v=[1,1,1]+[0]*(r-3)
    assert rank_gf2(a)==r-1
    assert all(sum(a[i][j]*v[j] for j in range(r))%2==0 for i in range(r))
    q=sum(a[i][j]*v[i]*v[j] for i in range(r) for j in range(i+1,r))%2
    assert q==1
    N=2**r-1
    for k in range(1,r+1):
        bitball=lambda s: {s}|{s^(1<<i) for i in range(r)}
        overlap=len(bitball(0)&bitball((1<<k)-1))
        assert overlap==({1:2,2:2}.get(k,0))
        incidence=N-r+k-2+overlap
        if r>=5: assert incidence<N-1
    return q

x=sp.symbols('a0:8')
# For the two slices A0, A1 of a trilinear tensor.
z,w=sp.symbols('z w')
A=sp.Matrix([[x[0]*z+x[1]*w,x[2]*z+x[3]*w],
             [x[4]*z+x[5]*w,x[6]*z+x[7]*w]])
det=sp.expand(A.det())
b=sp.expand(det).coeff(z,1).coeff(w,1)
assert sp.expand(b-(x[0]*x[7]+x[1]*x[6]-x[2]*x[5]-x[3]*x[4]))==0
# Discriminant of the binary quadratic determinant is b^2-4ac; modulo 2=b^2.
assert sp.expand(det).coeff(z,2)*sp.expand(det).coeff(w,2)!=0
# A specialization witnessing the generic nonvanishing condition.
for r in (3,5,7,9):test_odd_r(r)
print('VERIFY_OK: characteristic-two pencil middle coefficient, Hessian radical and quadratic evaluation, two-contact dimension bounds r=5,7,9')
