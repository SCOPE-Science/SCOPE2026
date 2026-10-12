import sympy as sp
from itertools import product
from collections import Counter

a,b,c,d,e,f,g,h,i=sp.symbols("a b c d e f g h i")
R=sp.Matrix([[a,b,c],[d,e,f],[g,h,i]])
e1=sp.Matrix([1,0,0]); e2=sp.Matrix([0,1,0]); e3=sp.Matrix([0,0,1])
basis=(e1,e2,e3)

def omega(x,y,z):
    return sp.Matrix.hstack(x,y,z).det()

def bracket(x,y,z):
    return sp.Matrix([omega(x,y,z),0,0])

def defect(x,y,z):
    Rx,Ry,Rz=R*x,R*y,R*z
    inside=bracket(Rx,Ry,z)+bracket(x,Ry,Rz)+bracket(Rx,y,Rz)-bracket(Rx,Ry,Rz)
    return sp.simplify(bracket(Rx,Ry,Rz)-R*inside)

D=sp.factor(R.det())
sigma2=sp.factor(a*e-b*d+a*i-c*g+e*i-f*h)
s=sp.factor(sigma2-D)
target=sp.Matrix([D-s*a,-s*d,-s*g])
assert sp.simplify(defect(e1,e2,e3)-target)==sp.zeros(3,1)

for x,y,z in product(basis,repeat=3):
    got=defect(x,y,z)
    if len({tuple(x),tuple(y),tuple(z)})<3:
        assert sp.simplify(got)==sp.zeros(3,1)

def det3(M,q):
    aa,bb,cc,dd,ee,ff,gg,hh,ii=M
    return (aa*(ee*ii-ff*hh)-bb*(dd*ii-ff*gg)+cc*(dd*hh-ee*gg))%q

def sig2(M,q):
    aa,bb,cc,dd,ee,ff,gg,hh,ii=M
    return (aa*ee-bb*dd+aa*ii-cc*gg+ee*ii-ff*hh)%q

def mv(M,x,q):
    return tuple(sum(M[3*r+j]*x[j] for j in range(3))%q for r in range(3))

def detcols(x,y,z,q):
    return (
        x[0]*(y[1]*z[2]-y[2]*z[1])
        -x[1]*(y[0]*z[2]-y[2]*z[0])
        +x[2]*(y[0]*z[1]-y[1]*z[0])
    )%q

def brmod(x,y,z,q):
    return (detcols(x,y,z,q),0,0)

def add(*vs,q):
    return tuple(sum(v[j] for v in vs)%q for j in range(3))

def neg(v,q):
    return tuple((-x)%q for x in v)

def is_reynolds(M,q):
    bas=((1,0,0),(0,1,0),(0,0,1))
    for x,y,z in product(bas,repeat=3):
        Rx,Ry,Rz=mv(M,x,q),mv(M,y,q),mv(M,z,q)
        lhs=brmod(Rx,Ry,Rz,q)
        inside=add(
            brmod(Rx,Ry,z,q),
            brmod(x,Ry,Rz,q),
            brmod(Rx,y,Rz,q),
            neg(brmod(Rx,Ry,Rz,q),q),
            q=q
        )
        if lhs!=mv(M,inside,q):
            return False
    return True

def criterion(M,q):
    aa,bb,cc,dd,ee,ff,gg,hh,ii=M
    D0=det3(M,q)
    s0=(sig2(M,q)-D0)%q
    return D0==(s0*aa)%q and (s0*dd)%q==0 and (s0*gg)%q==0

def rank3(M,q):
    A=[list(M[3*r:3*r+3]) for r in range(3)]
    r=0
    for col in range(3):
        p=next((rr for rr in range(r,3) if A[rr][col]%q),None)
        if p is None:
            continue
        A[r],A[p]=A[p],A[r]
        inv=pow(A[r][col],-1,q)
        A[r]=[(inv*x)%q for x in A[r]]
        for rr in range(3):
            if rr!=r and A[rr][col]%q:
                k=A[rr][col]%q
                A[rr]=[(A[rr][j]-k*A[r][j])%q for j in range(3)]
        r+=1
    return r

def formulas(q):
    profile=(
        1,
        (q-1)*(q*q+q+1)**2,
        q*(q-1)**2*(q+1)*(q**3+3*q**2+2*q+1),
        q**3*(q-1)*(q**2-q-1),
    )
    total=q**7+3*q**6-3*q**5-2*q**4+2*q**3
    assert sum(profile)==total
    return profile,total

for q in (2,3):
    cnt=Counter()
    total=0
    for M in product(range(q),repeat=9):
        direct=is_reynolds(M,q)
        crit=criterion(M,q)
        assert direct==crit,(q,M,direct,crit)
        if direct:
            cnt[rank3(M,q)]+=1
            total+=1
    expected_profile,expected_total=formulas(q)
    got=tuple(cnt[r] for r in range(4))
    assert got==expected_profile,(q,got,expected_profile)
    assert total==expected_total
    print({"q":q,"total":total,"rank_profile":got})

for q in (2,3,5,7):
    profile,total=formulas(q)
    print({"q":q,"formula_total":total,"formula_rank_profile":profile})

print("VERIFY_OK")
