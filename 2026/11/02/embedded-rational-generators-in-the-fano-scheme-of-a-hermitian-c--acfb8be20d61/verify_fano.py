#!/usr/bin/env python3
"""Exact finite-field sanity checks for the lines on a Hermitian cone.
All local-ring assertions in the accompanying theorem have independent
symbolic proofs; finite-field enumeration is not an infinite certificate.
"""
from itertools import product

class Field:
    def __init__(self, p, polynomial):
        self.p = p
        self.modulus = polynomial
        self.n = len(polynomial)-1
        self.order = p**self.n
        assert polynomial[-1] == 1
        self.coeffs = [self.digits(i) for i in range(self.order)]
        self.pows = [p**i for i in range(self.n)]
        self.zero, self.one = 0, 1
        self.muls = None

    def digits(self, a):
        return [(a//(self.p**j))%self.p for j in range(self.n)]

    def encode(self, c):
        return sum((t % self.p)*(self.p**i) for i,t in enumerate(c))

    def add(self, a,b):
        return self.encode([x+y for x,y in zip(self.coeffs[a],self.coeffs[b])])

    def neg(self, a):
        return self.encode([-x for x in self.coeffs[a]])

    def mul(self, a,b):
        if not a or not b: return 0
        r=[0]*(2*self.n-1)
        for i,ai in enumerate(self.coeffs[a]):
            for j,bj in enumerate(self.coeffs[b]):
                r[i+j]=(r[i+j]+ai*bj)%self.p
        for d in range(len(r)-1,self.n-1,-1):
            u=r[d]
            for j in range(self.n):
                r[d-self.n+j]=(r[d-self.n+j]-u*self.modulus[j])%self.p
        return self.encode(r[:self.n])

    def pow(self,a,n):
        r=1
        while n:
            if n&1:r=self.mul(r,a)
            a=self.mul(a,a)
            n//=2
        return r

    def check_field(self):
        for a in range(1,self.order):
            assert self.pow(a,self.order-1)==1,(self.p,self.n,a)

    def affine_points(self, q):
        # 1+x^(q+1)+y^(q+1)=0
        N=q+1
        values={t:self.pow(t,N) for t in range(self.order)}
        by_norm={}
        for y, val in values.items():
            by_norm.setdefault(val,[]).append(y)
        for x, val in values.items():
            rhs=self.neg(self.add(1,val))
            for y in by_norm.get(rhs,[]):
                yield x,y

    def projective_points(self, q):
        yield from ((1,x,y) for x,y in self.affine_points(q))
        # Coordinates [0:1:y] and [0:0:1] (latter does not lie on curve).
        for y in range(self.order):
            if self.add(1,self.pow(y,q+1))==0:
                yield (0,1,y)


def test(q,p,mod,extended=False):
    K=Field(p,mod)
    K.check_field()
    assert K.order%(q*q)==0
    pts=list(K.projective_points(q))
    if not extended:
        assert len(pts)==q**3+1,(q,len(pts))
    distinguished=0
    ordinary=0
    for point in pts:
        j=next(i for i,z in enumerate(point) if z)
        inv=K.pow(point[j],K.order-2)
        coords=[K.mul(point[(j+t)%3],inv) for t in range(3)]
        assert coords[0]==1
        x,y=coords[1],coords[2]
        P=K.add(K.mul(x,K.pow(y,q*q)), K.neg(K.mul(y,K.pow(x,q*q))))
        critical=(P==0)
        # The exceptional Fano generator is characterized by P=0.
        # Compare to Frobenius-fixed projective points.
        rational=all(K.pow(z,q*q)==z for z in coords)
        assert critical==rational,(q,point,coords)
        if critical:
            distinguished+=1
            # Derivative of P along the curve's tangent vector
            # (dx,dy)=(y^q,-x^q) is x^(q+1)+y^(q+1)=-1.
            tangent=K.add(K.pow(x,q+1),K.pow(y,q+1))
            assert tangent==K.neg(1)
        else:
            ordinary+=1
        # Hermitian line coefficients after solving x^q*u+y^q*v=0
        # using u=y^q*w, v=-x^q*w.
        u=K.pow(y,q)
        v=K.neg(K.pow(x,q))
        assert K.add(K.mul(K.pow(x,q),u),K.mul(K.pow(y,q),v))==0
        coeff_stq=K.add(K.mul(x,K.pow(u,q)),K.mul(y,K.pow(v,q)))
        assert coeff_stq==P
        coeff_tq1=K.add(K.pow(u,q+1),K.pow(v,q+1))
        assert coeff_tq1==K.neg(1)
    if not extended:
        assert distinguished==q**3+1
        assert ordinary==0
    else:
        assert distinguished==q**3+1
        assert ordinary>0
    print(f"q={q}, |field|={K.order}: curve_points={len(pts)}, special={distinguished}, generic={ordinary}; all coefficient tests passed")

if __name__=='__main__':
    test(2,2,[1,1,1])
    test(3,3,[1,0,1])
    test(4,2,[1,1,0,0,1])
    test(5,5,[2,0,1])
    test(7,7,[1,0,1])
    # Larger fields permit non-Hermitian-rational geometric points.
    test(2,2,[1,0,0,0,0,1,1],extended=True)
    test(3,3,[1,0,0,0,1,1,1],extended=True)
    print('HERMITIAN_CONE_FANO_FIELDS_AND_COEFFICIENTS_OK')
