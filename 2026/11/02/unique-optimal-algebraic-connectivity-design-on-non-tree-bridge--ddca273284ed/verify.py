"""Reproduce exact budget/eigenvector identities and finite spectral checks.
Uses only the Python standard library. Finite checks are not a general proof.
"""
from fractions import Fraction as F
from math import sqrt


def candidate(p, q, B=F(1)):
    n = p + q
    d = 9*p*q - 4*n
    lam = B*F(n,d)
    a = B*F(3*q,d)
    c = B*F(3*p,d)
    b = B*F(3*p*q-n,d)
    edges = [(0,i,a) for i in range(1,p)]
    edges += [(p,j,c) for j in range(p+1,n)]
    edges += [(0,p,b)]
    L = [[F(0) for _ in range(n)] for _ in range(n)]
    for i,j,w in edges:
        L[i][i] += w; L[j][j] += w
        L[i][j] -= w; L[j][i] -= w
    z = [F(2*q-p,n)] + [F(3*q,n)]*(p-1)
    z += [F(q-2*p,n)] + [F(-3*p,n)]*(q-1)
    return L,lam,a,c,b,z,edges


def jacobi_eigenvalues(L):
    n=len(L)
    A=[[float(v) for v in row] for row in L]
    for _ in range(150*n*n):
        i,j=max(((i,j) for i in range(n) for j in range(i+1,n)),
                key=lambda ij: abs(A[ij[0]][ij[1]]))
        if abs(A[i][j]) < 1e-12: break
        from math import atan2,cos,sin
        angle=0.5*atan2(2*A[i][j],A[j][j]-A[i][i])
        cc=cos(angle); ss=sin(angle)
        di,dj,off=A[i][i],A[j][j],A[i][j]
        A[i][i]=cc*cc*di-2*ss*cc*off+ss*ss*dj
        A[j][j]=ss*ss*di+2*ss*cc*off+cc*cc*dj
        A[i][j]=A[j][i]=0.0
        for k in range(n):
            if k in (i,j): continue
            x,y=A[k][i],A[k][j]
            A[k][i]=A[i][k]=cc*x-ss*y
            A[k][j]=A[j][k]=ss*x+cc*y
    return sorted(A[i][i] for i in range(n))


cases=0
outside=0
for p in range(2,11):
    for q in range(2,11):
        L,lam,a,c,b,z,edges=candidate(p,q)
        n=p+q; D=9*p*q-4*n
        assert sum(z)==0
        assert sum(t*t for t in z)==F(D,n)
        assert sum(w for _,_,w in edges)==1
        assert all(sum(L[i][j]*z[j] for j in range(n))==lam*z[i]
                   for i in range(n))
        ev=jacobi_eigenvalues(L)
        assert abs(ev[0])<2e-8
        if max(p,q)<=2*min(p,q):
            assert abs(ev[1]-float(lam))<2e-8, (p,q,ev,lam)
        else:
            outside+=1
            assert ev[1]<float(lam)-1e-8, (p,q,ev,lam)
        cases+=1
L,lam,a,c,b,z,edges=candidate(2,3)
assert (lam,a,c,b)==(F(5,34),F(9,34),F(6,34),F(13,34))
ev=jacobi_eigenvalues(L)
assert all(abs(x-float(y))<2e-9 for x,y in zip(ev,[F(0),F(5,34),F(3,17),F(9,17),F(39,34)]))
print(f"OK: {cases} exact budget/eigenvector cases, {cases} full-matrix spectral comparisons, {outside} outside-threshold strict comparisons; explicit five-vertex spectrum.")
