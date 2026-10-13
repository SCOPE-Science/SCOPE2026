import sympy as sp
from itertools import product

lam,x,y,z,w,b=sp.symbols("lam x y z w b")
e1=sp.Matrix([1,0])
e2=sp.Matrix([0,1])
R=sp.Matrix([[x,y],[z,w]])
Alpha=sp.Matrix([[1,0],[0,lam]])

def circ(u,v):
    return sp.Matrix([
        2*u[0]*v[0],
        2*lam*(u[0]*v[1]+u[1]*v[0]),
    ])

def alpha(u):
    return Alpha*u

def ass(u,v,t):
    return sp.simplify(circ(circ(u,v),alpha(t))-circ(alpha(u),circ(v,t)))

X=sp.Matrix(sp.symbols("X1 X2"))
Y=sp.Matrix(sp.symbols("Y1 Y2"))
assert sp.simplify(ass(circ(X,X),alpha(Y),alpha(X)))==sp.zeros(2,1)

C=sp.simplify(R*Alpha-Alpha*R)
assert sp.simplify(C-sp.Matrix([[0,(lam-1)*y],[(1-lam)*z,0]]))==sp.zeros(2,2)

def defect(u,v):
    Ru=R*u
    Rv=R*v
    return sp.simplify(circ(Ru,Rv)-R*(circ(Ru,v)+circ(u,Rv)))

D11=[sp.factor(q) for q in defect(e1,e1)]
D12=[sp.factor(q) for q in defect(e1,e2)]
D22=[sp.factor(q) for q in defect(e2,e2)]
target11=[-2*(x*x+2*lam*y*z), 4*z*(lam*(x-w)-x)]
target12=[-2*lam*y*(w+x), 2*(-lam*w*w+(lam-1)*y*z)]
target22=[-2*y*y*(2*lam-1),0]
for got,want in zip(D11+D12+D22,target11+target12+target22):
    assert sp.simplify(got-want)==0

sub={x:0,y:0,z:b,w:0}
for q in D11+D12+D22:
    assert sp.factor(q.subs(sub))==0
Csrc=sp.simplify(C.subs(sub))
assert sp.simplify(Csrc-sp.Matrix([[0,0],[(1-lam)*b,0]]))==sp.zeros(2,2)

def vmul(M,u,p):
    return ((M[0]*u[0]+M[1]*u[1])%p,
            (M[2]*u[0]+M[3]*u[1])%p)

def cmul(u,v,l,p):
    return (2*u[0]*v[0]%p,
            2*l*(u[0]*v[1]+u[1]*v[0])%p)

def rb(M,l,p):
    for u in ((1,0),(0,1)):
        Ru=vmul(M,u,p)
        au=(u[0],l*u[1]%p)
        Rau=vmul(M,au,p)
        aRu=(Ru[0],l*Ru[1]%p)
        if Rau!=aRu:
            return False
    basis=((1,0),(0,1))
    for u in basis:
        for v in basis:
            Ru=vmul(M,u,p); Rv=vmul(M,v,p)
            lhs=cmul(Ru,Rv,l,p)
            q1=cmul(Ru,v,l,p); q2=cmul(u,Rv,l,p)
            inside=((q1[0]+q2[0])%p,(q1[1]+q2[1])%p)
            rhs=vmul(M,inside,p)
            if lhs!=rhs:
                return False
    return True

for p in (3,5,7):
    counts={}
    for l in range(p):
        sols=[]
        for M in product(range(p),repeat=4):
            if rb(M,l,p):
                sols.append(M)
        counts[l]=len(sols)
        if l==0:
            expected={(0,0,0,v) for v in range(p)}
        elif l==1:
            expected={(0,0,u,0) for u in range(p)}
        else:
            expected={(0,0,0,0)}
        assert set(sols)==expected,(p,l,set(sols),expected)
    assert sum(counts.values())==3*p-2
    print({"q":p,"counts_by_parameter":counts,"pair_total":sum(counts.values())})

print("VERIFY_OK")
