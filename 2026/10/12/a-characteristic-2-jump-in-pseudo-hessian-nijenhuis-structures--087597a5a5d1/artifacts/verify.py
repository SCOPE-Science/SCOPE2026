import sympy as sp
from itertools import product

x,y,z,a,b,c,d=sp.symbols("x y z a b c d")
B=sp.Matrix([[x,y],[y,z]])
N=sp.Matrix([[a,b],[c,d]])
e1=sp.Matrix([1,0])
e2=sp.Matrix([0,1])
basis=(e1,e2)

def pre(u,v):
    return sp.Matrix([-u[1]*v[0], u[1]*v[1]])

def bil(M,u,v):
    return (u.T*M*v)[0]

# Symbolic cocycle equations.
coc=set()
for u in basis:
    for v in basis:
        for w in basis:
            q=sp.factor(
                bil(B,pre(u,v),w)-bil(B,u,pre(v,w))
                -bil(B,pre(v,u),w)+bil(B,v,pre(u,w))
            )
            if q!=0:
                coc.add(q)
assert coc=={-2*x,2*x}

# Symbolic Nijenhuis torsion.
tor=set()
for u in basis:
    for v in basis:
        Nu=N*u
        Nv=N*v
        D=sp.simplify(pre(Nu,Nv)-N*(pre(Nu,v)+pre(u,Nv)-N*pre(u,v)))
        for q in D:
            q=sp.factor(q)
            if q!=0:
                tor.add(q)
assert tor=={-2*b*c,2*b*c,2*c**2,2*b*(a-d)}

# Selfadjointness and B1 cocycle.
selfadj=sp.simplify(N.T*B-B*N)
assert selfadj[0,1]==a*y-b*x+c*z-d*y
B1=sp.simplify(B*N)
# Under selfadjointness, B1 is symmetric. The symmetric cocycle criterion
# for this algebra is twice the (1,1) entry, which here is a*x+c*y.
assert sp.factor(B1[0,0]) == a*x+c*y

def inv2(M,p):
    return (M[0]*M[3]-M[1]*M[2])%p != 0

def premod(u,v,p):
    return ((-u[1]*v[0])%p,(u[1]*v[1])%p)

def mv(M,u,p):
    return ((M[0]*u[0]+M[1]*u[1])%p,
            (M[2]*u[0]+M[3]*u[1])%p)

def bval(Bm,u,v,p):
    return (u[0]*(Bm[0]*v[0]+Bm[1]*v[1])
            +u[1]*(Bm[1]*v[0]+Bm[2]*v[1]))%p

def is_cocycle(Bm,p):
    for u in ((1,0),(0,1)):
        for v in ((1,0),(0,1)):
            for w in ((1,0),(0,1)):
                lhs=(bval(Bm,premod(u,v,p),w,p)-bval(Bm,u,premod(v,w,p),p))%p
                rhs=(bval(Bm,premod(v,u,p),w,p)-bval(Bm,v,premod(u,w,p),p))%p
                if lhs!=rhs:
                    return False
    return True

def is_nij(M,p):
    for u in ((1,0),(0,1)):
        for v in ((1,0),(0,1)):
            Nu=mv(M,u,p); Nv=mv(M,v,p)
            lhs=premod(Nu,Nv,p)
            t1=premod(Nu,v,p); t2=premod(u,Nv,p); t3=mv(M,premod(u,v,p),p)
            inside=((t1[0]+t2[0]-t3[0])%p,(t1[1]+t2[1]-t3[1])%p)
            if lhs!=mv(M,inside,p):
                return False
    return True

def selfadjoint(Bm,M,p):
    for u in ((1,0),(0,1)):
        for v in ((1,0),(0,1)):
            if bval(Bm,mv(M,u,p),v,p)!=bval(Bm,u,mv(M,v,p),p):
                return False
    return True

def B1_tuple(Bm,M,p):
    # Matrix B*N, guaranteed symmetric if selfadjoint.
    Bmat=((Bm[0],Bm[1]),(Bm[1],Bm[2]))
    Nmat=((M[0],M[1]),(M[2],M[3]))
    C=[[sum(Bmat[i][k]*Nmat[k][j] for k in range(2))%p for j in range(2)] for i in range(2)]
    assert C[0][1]==C[1][0]
    return (C[0][0],C[0][1],C[1][1])

def is_pair(Bm,M,p):
    if (Bm[0]*Bm[2]-Bm[1]*Bm[1])%p==0:
        return False
    if not is_cocycle(Bm,p):
        return False
    if not inv2(M,p) or not is_nij(M,p):
        return False
    if not selfadjoint(Bm,M,p):
        return False
    return is_cocycle(B1_tuple(Bm,M,p),p)

for p in (2,3,5):
    forms=[Bm for Bm in product(range(p),repeat=3)
           if (Bm[0]*Bm[2]-Bm[1]*Bm[1])%p!=0 and is_cocycle(Bm,p)]
    total=0
    fibers=[]
    for Bm in forms:
        n=0
        for M in product(range(p),repeat=4):
            if is_pair(Bm,M,p):
                n+=1
        fibers.append(n)
        total+=n
    expected=p**4*(p-1)**2 if p==2 else p**2*(p-1)**2
    assert total==expected,(p,total,expected)
    if p==2:
        assert len(forms)==p**2*(p-1)
        assert set(fibers)=={p**2*(p-1)}
    else:
        assert len(forms)==p*(p-1)
        assert set(fibers)=={p*(p-1)}
    print({"q":p,"forms":len(forms),"fiber_sizes":sorted(set(fibers)),"structures":total})

print("VERIFY_OK")
