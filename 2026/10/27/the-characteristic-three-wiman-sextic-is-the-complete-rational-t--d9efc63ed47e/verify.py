#!/usr/bin/env python3
"""Exact independent finite-field and projective-incidence checks for a plane sextic."""
from itertools import product

P=3

def scalar_mod(a): return a % P

class Field:
    def __init__(self, modulus):
        self.modulus=modulus
        self.d=len(modulus)-1
        assert modulus[-1]==1
        self.q=P**self.d
    def dec(self, a):
        return [(a//(P**i))%P for i in range(self.d)]
    def enc(self, coeff):
        return sum((coeff[i]%P)*P**i for i in range(self.d))
    def add(self, a,b):
        aa=self.dec(a); bb=self.dec(b)
        return self.enc([(aa[i]+bb[i])%P for i in range(self.d)])
    def neg(self,a):return self.enc([(-z)%P for z in self.dec(a)])
    def mul(self,a,b):
        aa=self.dec(a);bb=self.dec(b)
        c=[0]*(2*self.d-1)
        for i in range(self.d):
            for j in range(self.d):c[i+j]=(c[i+j]+aa[i]*bb[j])%P
        for i in range(2*self.d-2,self.d-1,-1):
            hi=c[i]
            for j in range(self.d):c[i-self.d+j]=(c[i-self.d+j]-hi*self.modulus[j])%P
        return self.enc(c[:self.d])
    def pow(self,a,n):
        z=1
        while n:
            if n&1:z=self.mul(z,a)
            a=self.mul(a,a);n//=2
        return z
    def inv(self,a):
        assert a
        return self.pow(a,self.q-2)
    def projective(self):
        for a in range(self.q):
            for b in range(self.q):yield (a,b,1)
        for a in range(self.q):yield (a,1,0)
        yield (1,0,0)
    def expr(self,pt):
        x,y,z=pt; add=self.add;mul=self.mul; sq=lambda a: mul(a,a)
        x2,y2,z2=[sq(a) for a in pt]
        x4,y4,z4=[sq(a) for a in (x2,y2,z2)]
        x6,y6,z6=[mul(a,b) for a,b in ((x4,x2),(y4,y2),(z4,z2))]
        C=add(add(x2,y2),z2)
        F=add(add(add(x6,y6),z6),mul(C,add(add(x4,y4),z4)))  # -12 term vanishes in char 3
        l1=add(add(x,y),z)
        l2=add(add(x,y),self.neg(z))
        l3=add(add(x,self.neg(y)),z)
        l4=add(add(self.neg(x),y),z)
        return F,C,(l1,l2,l3,l4)



# Sparse ternary polynomials, all coefficients exactly reduced modulo three.
def pa(*ps):
    z={}
    for p in ps:
        for e,c in p.items():z[e]=(z.get(e,0)+c)%3
    return {e:c for e,c in z.items() if c}
def pm(a,b):
    z={}
    for e,c in a.items():
        for f,d in b.items():
            key=tuple(e[i]+f[i] for i in range(3))
            z[key]=(z.get(key,0)+c*d)%3
    return {e:c for e,c in z.items() if c}
def pp(a,n):
    z={(0,0,0):1}
    for _ in range(n):z=pm(z,a)
    return z
def neg(a):return {e:(-c)%3 for e,c in a.items()}
def scale(a,c):return {e:(c*v)%3 for e,v in a.items() if (c*v)%3}
X={(1,0,0):1}; Y={(0,1,0):1}; Z={(0,0,1):1}
def defining_polys(x,y,z):
    C=pa(pp(x,2),pp(y,2),pp(z,2))
    F=pa(pp(x,6),pp(y,6),pp(z,6),pm(C,pa(pp(x,4),pp(y,4),pp(z,4))))
    L=[pa(x,y,z),pa(x,y,neg(z)),pa(x,neg(y),z),pa(neg(x),y,z)]
    return F,C,L

def sym_f3_factorization():
    F,C,L=defining_polys(X,Y,Z)
    out=C
    for l in L:out=pm(out,l)
    assert F==out, (F,out)

def proportional(U,V):
    return any(U==scale(V,k) for k in (1,2))

def check_finite_field(field):
    n=0
    onconic=0
    onanyline=0
    for pt in field.projective():
        F,C,L=field.expr(pt)
        assert (F==0)==(C==0 or 0 in L), (field.q,pt)
        n+=(F==0)
        onconic+=(C==0)
        onanyline+=(0 in L)
    q=field.q
    assert onconic==q+1, ('conic',q,onconic)
    assert n==5*q-5, ('pointcount',q,n)
    print(f'F_{q}: curve_points={n}, conic_points={onconic}, line_union_points={onanyline}')


def cross(a,b):
    return ((a[1]*b[2]-a[2]*b[1])%3,(a[2]*b[0]-a[0]*b[2])%3,(a[0]*b[1]-a[1]*b[0])%3)

def normalized(p):
    for v in p:
        if v:return tuple((e*pow(v,-1,3))%3 for e in p)
    raise ValueError('zero')

def incidence():
    f=Field([0,1])
    lines=[(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1)]
    pairs=[normalized(cross(a,b)) for i,a in enumerate(lines) for b in lines[i+1:]]
    assert len(set(pairs))==6
    for p in pairs:
        _,C,L=f.expr(p)
        assert C!=0 and sum(t==0 for t in L)==2
    tangent_pts=[]
    for a in lines:
        pp=normalized(a)
        _,C,L=f.expr(pp)
        assert C==0
        assert sum(x==0 for x in L)==1
        tangent_pts.append(pp)
    assert len(set(tangent_pts))==4
    assert len({p for p in f.projective() if f.expr(p)[1]==0})==4
    print('component_intersections: 6 ordinary nodes + 4 order-two tangent contacts')
    print('node_points=',pairs, 'tangency_points=',tangent_pts)
    # all invertible F3 projective matrices preserve the set of four conic points iff among 24 symmetries
    roots=set(tangent_pts)
    matrices=set()
    for A in product(range(3),repeat=9):
        determinant=(A[0]*(A[4]*A[8]-A[5]*A[7])-A[1]*(A[3]*A[8]-A[5]*A[6])+A[2]*(A[3]*A[7]-A[4]*A[6]))%3
        if not determinant:continue
        def mapP(pt):
            return normalized(tuple(sum(A[3*i+j]*pt[j] for j in range(3))%3 for i in range(3)))
        if {mapP(pt) for pt in roots}==roots:
            # projectively normalize by the first nonzero matrix entry
            nz=next(z for z in A if z)
            matrices.add(tuple((z*pow(nz,-1,3))%3 for z in A))
    assert len(matrices)==24,len(matrices)
    F,C,_=defining_polys(X,Y,Z)
    for A in matrices:
        vars=(X,Y,Z)
        U=[pa(*(scale(vars[j],A[3*i+j]) for j in range(3))) for i in range(3)]
        f,c,_=defining_polys(*U)
        assert proportional(c,C)
        assert proportional(f,F)
    print('projective_F3_stabilizer_size=',len(matrices))

if __name__=='__main__':
    sym_f3_factorization()
    incidence()
    # x, x^2 + 1, x^3 - x + 1 are irreducible mod 3
    for m in ([0,1],[1,0,1],[1,-1,0,1]):check_finite_field(Field(m))
    print('VERIFY_OK')
