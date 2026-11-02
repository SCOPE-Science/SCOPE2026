#!/usr/bin/env python3
"""Exact checks for the exceptional-characteristic one-base-point cubic pencil.
Requires Python >=3.9 and SymPy. Finite fields below use explicit irreducible moduli.
No computer enumeration is used to infer a theorem over an algebraic closure.
"""
import sympy as s

x,y,z,t,u=s.symbols('x y z t u')
F=x*y*y+y*z*z+z*x*x
G=x**3+x*y*z-y**3
P=F+t*G
assert s.factor(s.resultant(F.subs(z,1),G.subs(z,1),y))==x**9
assert s.expand(P.subs({y:u*x,z:1})/x - (u+x*(1+t*u)+x*x*(u*u+t*(1-u**3))))==0
Q=4*t*u**4-4*u**3+t*t*u**2-2*t*u+1
assert s.expand((1+t*u)**2-4*u*(u*u+t*(1-u**3))-Q)==0
I=s.factor(12*(4*t)*1-3*(-4)*(-2*t)+(t*t)**2)
J=s.factor(72*(4*t)*(t*t)*1+9*(-4)*(t*t)*(-2*t)-27*(4*t)*(-2*t)**2-27*(-4)**2*1-2*(t*t)**3)
D=s.factor(s.discriminant(Q,u))
assert I==t*(t**3+24)
assert s.expand(J+2*(t**6+36*t**3+216))==0
assert s.expand(D+256*(t**3+27))==0
assert s.factor(4*I**3-J**2)==27*D

# Exact Groebner eliminations in each exceptional characteristic; the
# reduced zero sets of these ideals provide all affine singularities.
def groebner_forms(p):
    polys=[s.Poly(q.subs(z,1),x,y,t,modulus=p).as_expr() for q in (P,s.diff(P,x),s.diff(P,y))]
    return {s.Poly(h.as_expr(),x,y,t,modulus=p).monic().as_expr() for h in s.groebner(polys,x,y,t,order='lex',modulus=p).polys}
assert groebner_forms(2)=={x,y+t,t**3+1}
assert groebner_forms(3)=={x-y**2,y**3-1,t}

# No singularity of any finite member can be present at z=0 for p=2,3.
for p in (2,3):
    # Homogeneous coordinates can normalize y=1 or take y=0,x=1.
    inf=[(1,yy,0) for yy in range(p)]+[(0,1,0)]
    for a,b,c in inf:
        for tt in range(p):
            vals=[int(q.subs({x:a,y:b,z:c,t:tt}))%p for q in (P,s.diff(P,x),s.diff(P,y),s.diff(P,z))]
            assert any(vals)

# Hasse invariant of plane cubic in characteristic 3: coefficient of
# x^(p-1)*y^(p-1)*z^(p-1) in (F+tG)^(p-1).
H=s.Poly(s.expand(P**2),x,y,z).coeff_monomial(x*x*y*y*z*z)
assert H==t*t

# Characteristic-2 nodal quadratic at (x,y,z)=(0,t,1), t^3=1.
v=s.symbols('v')
local2=s.Poly(s.expand(P.subs({y:t+v,z:1})),x,v)
quad2=sum(coef*x**aa*v**bb for (aa,bb),coef in local2.terms() if aa+bb==2)
assert s.Poly(quad2-(x*x+t*x*v+t*t*v*v),x,v,t,modulus=2).is_zero

# Characteristic-3 cusp: at t=0, x=y=z=1.
v,w=s.symbols('v w')
local3=s.Poly(F.subs({x:1+w-v,y:1+v,z:1}),w,v,modulus=3).as_expr()
assert s.Poly(local3-(w*w+w*v*v-v**3),w,v,modulus=3).is_zero
# Characteristic-2 singular points are nodes: tangent quadratic
# X^2+tXY+t^2Y^2 has nonzero polar term tXY (at t^3=1).

MODULI={(2,1):(0,1),(2,2):(1,1,1),(2,3):(1,1,0,1),
        (3,1):(0,1),(3,2):(1,0,1)}
class FF:
    def __init__(self,p,r):
        self.p,self.r,self.q=p,r,p**r
        self.mod=MODULI[p,r]
    def digits(self,a):
        d=[]
        for _ in range(self.r):d.append(a%self.p);a//=self.p
        return d
    def pack(self,a):return sum((v%self.p)*self.p**i for i,v in enumerate(a[:self.r]))
    def add(self,a,b):return self.pack([(i+j)%self.p for i,j in zip(self.digits(a),self.digits(b))])
    def neg(self,a):return self.pack([(-i)%self.p for i in self.digits(a)])
    def mul(self,a,b):
        aa,bb=self.digits(a),self.digits(b)
        m=[0]*(2*self.r-1)
        for i,ai in enumerate(aa):
            for j,bj in enumerate(bb):m[i+j]=(m[i+j]+ai*bj)%self.p
        for k in range(len(m)-1,self.r-1,-1):
            v=m[k]%self.p
            if v:
                for j in range(self.r):m[k-self.r+j]=(m[k-self.r+j]-v*self.mod[j])%self.p
        return self.pack(m)
    def pow(self,a,n):
        v=1
        while n:
            if n&1:v=self.mul(v,a)
            a=self.mul(a,a);n//=2
        return v
    def sub(self,a,b):return self.add(a,self.neg(b))
    def polys(self,X,Y,Z,T):
        A=self.add(self.add(self.mul(X,self.pow(Y,2)),self.mul(Y,self.pow(Z,2))),self.mul(Z,self.pow(X,2)))
        B=self.sub(self.add(self.pow(X,3),self.mul(self.mul(X,Y),Z)),self.pow(Y,3))
        if T is None:return B
        return self.add(A,self.mul(T,B))
    def derivative(self,X,Y,Z,T):
        p=self.p
        dx=self.add(self.pow(Y,2),self.mul(self.add(0,2%p),self.mul(Z,X)))
        dy=self.add(self.mul(self.add(0,2%p),self.mul(X,Y)),self.pow(Z,2))
        dz=self.add(self.mul(self.add(0,2%p),self.mul(Y,Z)),self.pow(X,2))
        gx=self.add(self.mul(self.add(0,3%p),self.pow(X,2)),self.mul(Y,Z))
        gy=self.sub(self.mul(X,Z),self.mul(self.add(0,3%p),self.pow(Y,2)))
        gz=self.mul(X,Y)
        if T is None:return gx,gy,gz
        return self.add(dx,self.mul(T,gx)),self.add(dy,self.mul(T,gy)),self.add(dz,self.mul(T,gz))
    def proj(self):
        for a in range(self.q):
            for b in range(self.q):yield (1,a,b)
        for b in range(self.q):yield(0,1,b)
        yield(0,0,1)

for p,r in [(2,1),(2,2),(2,3),(3,1),(3,2)]:
    K=FF(p,r);q=K.q
    for tt in list(range(q))+[None]:
        on=[pt for pt in K.proj() if K.polys(*pt,tt)==0]
        sing=[pt for pt in on if K.derivative(*pt,tt)==(0,0,0)]
        if tt is None:
            assert sing==[(0,0,1)] and len(on)==q
        elif p==2 and K.pow(tt,3)==1:
            assert sing==[(0,1,K.pow(tt,2))]
            assert len(on)==(q if r%2==0 else q+2)
        elif p==3 and tt==0:
            assert sing==[(1,1,1)] and len(on)==q+1
        else:
            assert not sing
    print('exact finite field:',p,r,'q=',q,'PASS')
print('ONE_BASE_POINT_BAD_CHARACTERISTICS_AND_ARITHMETIC_COUNTS_PASS')
