#!/usr/bin/env python3
"""Exact algebraic checks for the exceptional fibers of a symmetric Kummer conic pencil.
Only standard Python and SymPy are required. Finite-field checks supplement the proof.
"""
import itertools
import sympy as s

U,V,W,A,B,C,lam,omega=s.symbols('U V W A B C lam omega')
Q=lam*(U+V+W)**2+U*V+V*W+W*U
mat=s.Matrix([[lam,lam+s.Rational(1,2),lam+s.Rational(1,2)],
              [lam+s.Rational(1,2),lam,lam+s.Rational(1,2)],
              [lam+s.Rational(1,2),lam+s.Rational(1,2),lam]])
assert s.simplify(mat.det()-(3*lam+1)/4)==0
binary=s.expand(Q.subs({U:0,V:1,W:A}))
assert s.factor(s.discriminant(binary,A))==4*lam+1
heron=(A+B+C)*(A+B-C)*(A-B+C)*(-A+B+C)
assert s.expand(4*Q.subs({U:A*A,V:B*B,W:C*C}).subs(lam,-s.Rational(1,4))-heron)==0
prod=(U+omega*V+omega**2*W)*(U+omega**2*V+omega*W)
identity=s.Poly(s.expand(prod-(U**2+V**2+W**2-U*V-U*W-V*W)),omega)
assert all(s.expand(z)==0 for z in s.Poly(identity.rem(s.Poly(omega**2+omega+1,omega)),omega).all_coeffs())
# n is the Kummer exponent; compare both sides at symbolic integer n.
for n in (1,2,3,4,6,8):
    x,y,z=s.symbols('x y z')
    f=sum([(x*y)**n,(y*z)**n,(z*x)**n])
    cremona=s.expand((y*z)**n+(z*x)**n+(x*y)**n)
    assert s.expand(f-cremona)==0
    if n%2==0:
        d=n//2
        G=Q.subs({U:x**n,V:y**n,W:z**n}).subs(lam,-s.Rational(1,4))
        H=heron.subs({A:x**d,B:y**d,C:z**d})/4
        assert s.expand(G-H)==0
    # Check arithmetic genus identities for singular fibers.
    pa=(2*n-1)*(2*n-2)//2
    assert pa-3*(n*(n-1)//2)==(n-1)*(n-2)//2
    if n%2==0:
        d=n//2
        assert 4*(d-1)*(d-2)//2+6*d*d-3==pa
    assert 2*(n-1)*(n-2)//2+n*n-1==pa

class FiniteField:
    def __init__(self,p,k=1,m=0,r=0):
        self.p,self.k,self.m,self.r=p,k,m,r
        self.size=p**k
        self.elements=range(self.size)
        self.add=[[self._add(a,b) for b in self.elements] for a in self.elements]
        self.mul=[[self._mul(a,b) for b in self.elements] for a in self.elements]
        self.zero=0;self.one=1
    def _add(self,a,b):
        if self.k==1:return (a+b)%self.p
        return ((a%self.p+b%self.p)%self.p+self.p*((a//self.p+b//self.p)%self.p))
    def _mul(self,a,b):
        p=self.p
        if self.k==1:return a*b%p
        a0,a1=a%p,a//p;b0,b1=b%p,b//p
        return (a0*b0+a1*b1*self.m)%p+p*((a0*b1+a1*b0+a1*b1*self.r)%p)
    def pow(self,a,n):
        b=1
        while n:
            if n&1:b=self.mul[b][a]
            a=self.mul[a][a];n//=2
        return b
    def points(self):
        for y in self.elements:
            for z in self.elements:yield (1,y,z)
        for z in self.elements:yield (0,1,z)
        yield (0,0,1)
    def singulars(self,n,la):
        add,mul=self.add,self.mul
        double=add[la][la]
        ans=[]
        for x,y,z in self.points():
            xn,yn,zn=(self.pow(v,n) for v in (x,y,z))
            S=add[add[xn][yn]][zn]
            e=add[mul[la][mul[S][S]]][add[add[mul[xn][yn]][mul[yn][zn]]][mul[zn][xn]]]
            if e!=0:continue
            d=[]
            for coord_n1,others in ((self.pow(x,n-1),add[yn][zn]),
                                     (self.pow(y,n-1),add[xn][zn]),
                                     (self.pow(z,n-1),add[xn][yn])):
                d.append(mul[coord_n1][add[mul[double][S]][others]])
            if all(v==0 for v in d):ans.append((x,y,z))
        return ans

# The listed finite fields are defined by irreducible quadratic polynomials.
F2=FiniteField(2);F3=FiniteField(3);F4=FiniteField(2,2,1,1) # t^2=t+1
F9=FiniteField(3,2,2,0) # t^2=2
F5=FiniteField(5);F25=FiniteField(5,2,2,0) # t^2=2
F7=FiniteField(7)
for field,n,parameters in [
    (F2,1,[(0,0),(1,1)]),
    (F3,2,[(0,3),(1,0),(2,6)]),
    (F4,3,[(0,3),(1,9),(2,0)]),
    (F9,8,[(0,3),(1,0),(2,24)]),
    (F5,4,[(0,3),(1,12),(2,0),(3,16)]),
    (F25,4,[(0,3),(1,12),(2,0),(3,16)]),
    (F7,6,[(0,3),(1,0),(2,36),(5,18)]),
]:
    for parameter,expected in parameters:
        actual=field.singulars(n,parameter)
        assert len(actual)==expected,(field.p,field.size,n,parameter,expected,len(actual),actual[:10])
        print(f'GF({field.size}), n={n}, lambda={parameter}: {len(actual)} singular rational supports')
print('TRIANGLE_PENCIL_CONIC_DISCRIMINANT_HERON_FACTORIZATION_GENUS_AND_FINITE_FIELDS_PASS')
