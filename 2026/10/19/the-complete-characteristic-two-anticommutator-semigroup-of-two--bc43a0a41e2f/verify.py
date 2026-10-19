"""Verify the characteristic-two symmetrized matrix-product semigroup.
Run: python verify.py. No external packages.
"""
from itertools import product

class Field:
    def __init__(self,m,poly): self.q=1<<m; self.m=m; self.poly=poly
    def add(self,a,b): return a^b
    def mul(self,a,b):
        s=0
        for _ in range(self.m):
            if b&1:s^=a
            b>>=1; a<<=1
            if a&self.q:a^=self.poly
        return s
    def power(self,a,k):
        z=1
        while k:
            if k&1:z=self.mul(z,a)
            a=self.mul(a,a);k>>=1
        return z
    def div(self,a,b): return self.mul(a,self.power(b,self.q-2))
    def wedge(self,u,v):return self.add(self.mul(u[0],v[1]),self.mul(u[1],v[0]))
    def mm(self,A,B):
        return tuple(tuple(self.add(self.add(self.mul(A[i][0],B[0][j]),self.mul(A[i][1],B[1][j])),self.add(self.mul(A[i][2],B[2][j]),self.mul(A[i][3],B[3][j])))for j in range(4))for i in range(4))
    def operator(self,lam,u):
        x,y=u
        return ((0,0,y,x),(0,0,0,0),(0,x,lam,0),(0,y,0,lam))
    def normal(self,h,p,a,c):
        return ((0,c,p[1],p[0]),(0,0,0,0),(0,a[0],h,0),(0,a[1],0,h))

def verify(q,p):
    F=Field(q.bit_length()-1,p)
    vals=range(q);pairs=list(product(vals,repeat=2))
    generators={F.operator(l,u) for l in vals for u in pairs}
    assert len(generators)==q**3
    doubles=set()
    for l,u in product(vals,pairs):
        A=F.operator(l,u)
        for mu,v in product(vals,pairs):
            B=F.operator(mu,v)
            C=F.mm(A,B)
            direct=F.normal(F.mul(l,mu), tuple(F.mul(mu,x) for x in u),tuple(F.mul(l,x) for x in v),F.wedge(u,v))
            assert C==direct
            doubles.add(C)
    expected=set()
    for h in vals:
        if h:
            for p0,a0 in product(pairs,repeat=2):
                expected.add(F.normal(h,p0,a0,F.div(F.wedge(p0,a0),h)))
        else:
            for p0,c in product(pairs,vals):expected.add(F.normal(0,p0,(0,0),c))
            for a0,c in product(pairs[1:],vals):expected.add(F.normal(0,(0,0),a0,c))
    assert doubles==expected,(q,len(doubles),len(expected))
    full=doubles|generators
    assert len(full)==(q-1)*q**4+2*q**3-q+q**2-1,(q,len(full))
    assert len(full-doubles)==q*q-1
    if q<=4:
        # Actual semigroup closure beyond two letters, direct operator-matrix products.
        for A in full:
            for B in generators:
                assert F.mm(A,B) in full
    # Compare every generator against the original unnormalized product AX+XA
    # using actual 2x2 multiplication, independent of the parametrization.
    def m2(A,B):
        return (F.add(F.mul(A[0],B[0]),F.mul(A[1],B[2])),
                F.add(F.mul(A[0],B[1]),F.mul(A[1],B[3])),
                F.add(F.mul(A[2],B[0]),F.mul(A[3],B[2])),
                F.add(F.mul(A[2],B[1]),F.mul(A[3],B[3])))
    coords=list(product(vals, repeat=4)) if q<=4 else list(product(vals, repeat=4))[::157]
    for lam,u in product(vals,pairs):
        A=(lam,u[0],u[1],0)
        op=F.operator(lam,u)
        for s,t,b,c in coords:
            X=(s,b,c,F.add(s,t))
            AX=m2(A,X); XA=m2(X,A)
            Y=tuple(F.add(x,y) for x,y in zip(AX,XA))
            w=(s,t,b,c)
            target=tuple(F.add(F.add(F.mul(op[i][0],w[0]),F.mul(op[i][1],w[1])),F.add(F.mul(op[i][2],w[2]),F.mul(op[i][3],w[3]))) for i in range(4))
            assert target==(Y[0],F.add(Y[0],Y[3]),Y[1],Y[2])
    assert F.mm(F.operator(1,(0,0)),F.operator(1,(0,0)))==F.operator(1,(0,0))
    print('FIELD',q,'generators',len(generators),'length2',len(doubles),'semigroup',len(full),'PASS')

if __name__=='__main__':
    verify(2,0b11)
    verify(4,0b111)
    verify(8,0b1011)
    print('VERIFY_OK')
