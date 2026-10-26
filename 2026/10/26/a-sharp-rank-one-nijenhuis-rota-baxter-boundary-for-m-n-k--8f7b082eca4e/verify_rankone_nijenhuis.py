"""Finite-field checks for rank-one associative Nijenhuis operators on M_2.
No external packages.  All bilinear defining identities are checked on the
standard matrix-unit basis, hence each reported test is exhaustive.
"""
from itertools import product

class Field:
    def __init__(self,q):
        assert q in (2,3,4)
        self.q=q
    def add(self,x,y):
        return (x^y) if self.q==4 else (x+y)%self.q
    def neg(self,x):
        return x if self.q==4 else -x%self.q
    def mul(self,x,y):
        if self.q!=4:return x*y%self.q
        if not x or not y:return 0
        # GF(4)=GF(2)[a]/(a^2+a+1), 2=a, 3=a+1.
        v=0
        for i in range(2):
            for j in range(2):
                if ((x>>i)&1) and ((y>>j)&1):
                    if i+j==2: v^=3
                    else:v^=1<<(i+j)
        return v
    def matmul(self,A,B):
        return tuple(self.add(self.mul(A[2*i],B[j]),self.mul(A[2*i+1],B[2+j])) for i in range(2) for j in range(2))
    def f(self,F,X):
        return self.add(self.add(self.mul(F[0],X[0]),self.mul(F[1],X[2])),self.add(self.mul(F[2],X[1]),self.mul(F[3],X[3])))
    def det(self,X):
        return self.add(self.mul(X[0],X[3]),self.neg(self.mul(X[1],X[2])))
    def tr(self,X):return self.add(X[0],X[3])

def verify(q):
    k=Field(q)
    basis=[tuple(int(a==b) for a in range(4)) for b in range(4)]
    M=list(product(range(q),repeat=4));nonzero=M[1:]
    proj=[U for U in nonzero if next(z for z in U if z)!=0 and next(z for z in U if z)==1]
    nij=rb=extra=0
    byshape={"nilpotent":0,"nonnilpotent":0}
    for U in proj:
        U2=k.matmul(U,U)
        left=[k.matmul(E,U) for E in basis]
        right=[k.matmul(U,E) for E in basis]
        products=[[k.matmul(X,Y) for Y in basis] for X in basis]
        for F in nonzero:
            f=[k.f(F,E) for E in basis]
            L=[k.f(F,XU) for XU in left]
            R=[k.f(F,UY) for UY in right]
            c=k.f(F,U)
            isrb=isnij=True
            for i in range(4):
                for j in range(4):
                    lhs=k.mul(f[i],f[j])
                    lr=k.add(k.mul(f[i],R[j]),k.mul(f[j],L[i]))
                    nr=k.add(lr,k.neg(k.mul(c,k.f(F,products[i][j]))))
                    if isrb and any(k.mul(lhs,U2[z])!=k.mul(lr,U[z]) for z in range(4)):isrb=False
                    if isnij and any(k.mul(lhs,U2[z])!=k.mul(nr,U[z]) for z in range(4)):isnij=False
                    if not isrb and not isnij:break
                if not isrb and not isnij:break
            if isrb:rb+=1;assert c==0
            if isnij:
                nij+=1
                if k.det(U)!=0:raise AssertionError('Nijenhuis with nonsingular image generator')
                if c!=0:
                    extra+=1
                    byshape['nilpotent' if k.tr(U)==0 else 'nonnilpotent']+=1
                    assert not isrb and k.det(F)==0 and k.tr(F)==0
                else:assert isrb
    assert extra==q*q*(q*q-1),(q,extra)
    assert rb==(q*q-1)*(2*q+1),(q,rb)
    assert nij==(q*q-1)*(q+1)**2,(q,nij)
    print('GF(%d): rank-one RB=%d, rank-one Nijenhuis=%d, exceptional=%d, exception_nonnilpotent_image=%d, exception_nilpotent_image=%d: PASS'%
        (q,rb,nij,extra,byshape['nonnilpotent'],byshape['nilpotent']))

if __name__=='__main__':
    for q in (2,3,4):verify(q)
    print('RANKONE_NIJENHUIS_BOUNDARY_OK')
