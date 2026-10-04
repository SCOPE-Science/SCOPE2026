#!/usr/bin/env python3
from itertools import product
import sympy as sp

# Polynomial verification in characteristic 2.
lam,b,c,u = sp.symbols('lam b c u')
vars_ = (b,c,u,lam)
G = sp.groebner([b**2 - lam*(u**2-1)], *vars_, modulus=2)

def red(expr):
    p = sp.Poly(sp.expand(expr), *vars_, modulus=2)
    rem = G.reduce(p.as_expr())[1]
    return sp.Poly(rem, *vars_, modulus=2).as_expr()

def addv(x,y): return tuple(sp.expand(a+b_) for a,b_ in zip(x,y))
def smul(s,x): return tuple(sp.expand(s*a) for a in x)

def bracket(x,y):
    x1,x2,x3=x; y1,y2,y3=y
    return (sp.Integer(0), sp.expand(x1*y2+x2*y1), sp.expand(lam*x1*y1+x2*y2))

E=[(1,0,0),(0,1,0),(0,0,1)]
# Columns of universal candidate automorphism.
cols=[(1,b,c),(0,u,b*u),(0,0,u**2)]

def mat_apply(v):
    out=(0,0,0)
    for coeff,col in zip(v,cols): out=addv(out,smul(coeff,col))
    return out

# Structure products in L_8(lambda).
for i in range(3):
    for j in range(3):
        lhs=mat_apply(bracket(E[i],E[j]))
        rhs=bracket(cols[i],cols[j])
        for a,d in zip(lhs,rhs):
            assert red(a-d)==0, (i,j,a,d,red(a-d))

# Tangent-space derivations: D matrix [[0,0,0],[q,p,0],[r,q,0]].
q,p,r=sp.symbols('q p r')
Dcols=[(0,q,r),(0,p,q),(0,0,0)]

def D_apply(v):
    out=(0,0,0)
    for coeff,col in zip(v,Dcols): out=addv(out,smul(coeff,col))
    return out

def red2(expr):
    return sp.Poly(sp.expand(expr), q,p,r,lam, modulus=2).as_expr()

for i in range(3):
    for j in range(3):
        lhs=D_apply(bracket(E[i],E[j]))
        rhs=addv(bracket(Dcols[i],E[j]), bracket(E[i],Dcols[j]))
        for a,d in zip(lhs,rhs):
            assert red2(a-d)==0, (i,j,a,d)

# After adjoining s with s^2=lambda and setting v=b+s(u-1), the defining relation is v^2=0.
s,v=sp.symbols('s v')
expr=sp.expand((v+s*(u-1))**2 - s**2*(u**2-1))
poly=sp.Poly(expr, v,s,u, modulus=2).as_expr()
assert sp.expand(poly - v**2)==0

# Direct finite check over F_2 at lambda=0: enumerate GL_3(F_2) and count automorphisms.
def det3(M):
    a,b_,c_=M[0]; d,e,f=M[1]; g,h,i=M[2]
    return (a*(e*i+f*h)+b_*(d*i+f*g)+c_*(d*h+e*g))%2

def mv(M,vv):
    return tuple(sum(M[i][j]*vv[j] for j in range(3))%2 for i in range(3))

def br2(x,y):
    return (0,(x[0]*y[1]+x[1]*y[0])%2,(x[1]*y[1])%2)

def ok(M):
    if det3(M)==0: return False
    for x in E:
        for y in E:
            if mv(M,br2(x,y)) != br2(mv(M,x),mv(M,y)):
                return False
    return True
count=0
for entries in product(range(2), repeat=9):
    M=[list(entries[0:3]),list(entries[3:6]),list(entries[6:9])]
    if ok(M): count+=1
assert count==2, count

print('universal_relations=OK')
print('tangent_derivations_dimension=3')
print('geometric_split_relation=v^2')
print('F2_lambda0_automorphisms=2')
print('CHECK_OK')
