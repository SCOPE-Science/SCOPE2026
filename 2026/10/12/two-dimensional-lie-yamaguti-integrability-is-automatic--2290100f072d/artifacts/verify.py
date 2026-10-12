import sympy as sp
from itertools import product

b1,b2=sp.symbols("b1 b2")
a11,a12,a21,a22=sp.symbols("a11 a12 a21 a22")
b=sp.Matrix([b1,b2])
A=sp.Matrix([[a11,a12],[a21,a22]])
e1=sp.Matrix([1,0]); e2=sp.Matrix([0,1]); basis=[e1,e2]

def det2(x,y): return sp.expand(x[0]*y[1]-x[1]*y[0])
def B(x,y): return det2(x,y)*b
def T(x,y,z): return det2(x,y)*(A*z)

def bd(N,x,y):
    return sp.simplify(B(N*x,N*y)-N*(B(N*x,y)+B(x,N*y)-N*B(x,y)))

def td(N,x,y,z):
    lhs=T(N*x,N*y,N*z)
    rhs=N*(T(N*x,N*y,z)+T(N*x,y,N*z)+T(x,N*y,N*z))
    rhs-=N*N*(T(N*x,y,z)+T(x,N*y,z)+T(x,y,N*z))
    rhs+=N*N*N*T(x,y,z)
    return sp.simplify(lhs-rhs)

E0=sp.Matrix([[1,0],[0,-1]])
J0=sp.Matrix([[0,-1],[1,0]])
for N in (E0,J0):
    for x in basis:
        for y in basis:
            assert bd(N,x,y)==sp.zeros(2,1)
            for z in basis:
                assert td(N,x,y,z)==sp.zeros(2,1)

lam=sp.symbols("lam")
S=lam*sp.eye(2)
for x in basis:
    for y in basis:
        assert bd(S,x,y)==sp.zeros(2,1)
        for z in basis:
            assert td(S,x,y,z)==sp.zeros(2,1)

I=(1,0,0,1)
def mm(X,Y,q):
    a,b,c,d=X; e,f,g,h=Y
    return ((a*e+b*g)%q,(a*f+b*h)%q,(c*e+d*g)%q,(c*f+d*h)%q)
def plus(X,Y,q): return tuple((a+b)%q for a,b in zip(X,Y))

for q in (3,5,7,11):
    mats=list(product(range(q),repeat=4))
    minusI=((-1)%q,0,0,(-1)%q)
    Es=[M for M in mats if mm(M,M,q)==I and M not in (I,minusI)]
    Js=[M for M in mats if mm(M,M,q)==minusI]
    zero=(0,0,0,0)
    pairs=sum(plus(mm(J,E,q),mm(E,J,q),q)==zero for E in Es for J in Js)
    ec=q*(q+1)
    jc=q*(q+1)+2 if q%4==1 else q*(q-1)
    pc=q*(q*q-1)
    assert (len(Es),len(Js),pairs)==(ec,jc,pc)
    print({"q":q,"product":len(Es),"complex":len(Js),"complex_product_pairs":pairs})
print("VERIFY_OK")
