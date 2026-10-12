import sympy as sp

a,b = sp.symbols("a b", nonzero=True)
e1 = sp.Matrix([1,0])
e2 = sp.Matrix([0,1])

def mul_A1(x,y):
    x1,x2=x
    y1,y2=y
    e11=sp.Matrix([-a,-a**2/b])
    e12=sp.Matrix([b,a])
    e22=sp.Matrix([-b**2/a,-b])
    return sp.simplify(x1*y1*e11 + (x1*y2+x2*y1)*e12 + x2*y2*e22)

f1=e1
f2=sp.Matrix([-a,-a**2/b])
P=sp.Matrix.hstack(f1,f2)
assert sp.simplify(P.det()+a**2/b)==0
assert sp.simplify(mul_A1(f1,f1)-f2)==sp.zeros(2,1)
assert sp.simplify(mul_A1(f1,f2))==sp.zeros(2,1)
assert sp.simplify(mul_A1(f2,f1))==sp.zeros(2,1)
assert sp.simplify(mul_A1(f2,f2))==sp.zeros(2,1)

# Canonical algebra C: (x1,x2)*(y1,y2)=(0,x1*y1).
def mul_C(x,y):
    return sp.Matrix([0, sp.expand(x[0]*y[0])])

s,t = sp.symbols("s t", nonzero=True)
Phi=sp.Matrix([[s,0],[t,s**2]])
u=sp.Matrix([1,0]); v=sp.Matrix([0,1])
for x in (u,v):
    for y in (u,v):
        assert sp.simplify(Phi*mul_C(x,y)-mul_C(Phi*x,Phi*y))==sp.zeros(2,1)

r,w=sp.symbols("r w")
D=sp.Matrix([[r,0],[w,2*r]])
for x in (u,v):
    for y in (u,v):
        lhs=D*mul_C(x,y)
        rhs=mul_C(D*x,y)+mul_C(x,D*y)
        assert sp.simplify(lhs-rhs)==sp.zeros(2,1)

H=sp.Matrix([[1,0],[0,2]])
E=sp.Matrix([[0,0],[1,0]])
assert H*E-E*H==E

print("VERIFY_OK")
