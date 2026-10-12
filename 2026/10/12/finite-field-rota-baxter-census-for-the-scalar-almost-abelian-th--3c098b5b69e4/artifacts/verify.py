import sympy as sp
from itertools import product
from collections import Counter

# Symbolic reconstruction in basis (t,v1,v2), [t,vi]=vi.
a,f1,f2,u1,u2,A11,A12,A21,A22=sp.symbols(
    "a f1 f2 u1 u2 A11 A12 A21 A22"
)
M=sp.Matrix([
    [a,f1,f2],
    [u1,A11,A12],
    [u2,A21,A22],
])
basis=[sp.eye(3)[:,i] for i in range(3)]

def br(x,y):
    return sp.Matrix([
        0,
        sp.expand(x[0]*y[1]-y[0]*x[1]),
        sp.expand(x[0]*y[2]-y[0]*x[2]),
    ])

def defect(N,x,y):
    Nx=N*x
    Ny=N*y
    return sp.simplify(br(Nx,Ny)-N*(br(Nx,y)+br(x,Ny)))

actual=set()
for x in basis:
    for y in basis:
        for z in defect(M,x,y):
            z=sp.factor(z)
            if z!=0:
                actual.add(sp.factor(z))

f=sp.Matrix([[f1,f2]])
A=sp.Matrix([[A11,A12],[A21,A22]])
u=sp.Matrix([[u1],[u2]])
target=[]
for z in list(f*A+a*f)+list(A*A+u*f):
    z=sp.factor(z)
    if z!=0:
        target.append(z)

G=sp.groebner(target, A11,A12,A21,A22,f1,f2,u1,u2,a, order="grevlex")
for z in actual:
    assert G.reduce(z)[1]==0
G2=sp.groebner(list(actual), A11,A12,A21,A22,f1,f2,u1,u2,a, order="grevlex")
for z in target:
    assert G2.reduce(z)[1]==0

BAS=((1,0,0),(0,1,0),(0,0,1))

def brmod(x,y,p):
    return (
        0,
        (x[0]*y[1]-y[0]*x[1])%p,
        (x[0]*y[2]-y[0]*x[2])%p,
    )

def mv(flat,x,p):
    return tuple(
        sum(flat[3*i+j]*x[j] for j in range(3))%p
        for i in range(3)
    )

def is_rb(flat,p):
    for x in BAS:
        for y in BAS:
            Rx=mv(flat,x,p)
            Ry=mv(flat,y,p)
            lhs=brmod(Rx,Ry,p)
            q1=brmod(Rx,y,p)
            q2=brmod(x,Ry,p)
            inside=tuple((q1[i]+q2[i])%p for i in range(3))
            if lhs!=mv(flat,inside,p):
                return False
    return True

def rank_mod(flat,p):
    A=[list(flat[3*i:3*i+3]) for i in range(3)]
    r=0
    for c in range(3):
        pivot=next((i for i in range(r,3) if A[i][c]%p),None)
        if pivot is None:
            continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[(inv*x)%p for x in A[r]]
        for i in range(3):
            if i!=r and A[i][c]%p:
                k=A[i][c]%p
                A[i]=[(A[i][j]-k*A[r][j])%p for j in range(3)]
        r+=1
    return r

def formulas(q):
    return (
        1,
        q**4+2*q**3-q**2-q-1,
        q*(q*q-1)**2,
        0,
    )

for p in (2,3):
    ranks=Counter()
    for flat in product(range(p),repeat=9):
        if is_rb(flat,p):
            ranks[rank_mod(flat,p)]+=1
    got=tuple(ranks[i] for i in range(4))
    exp=formulas(p)
    assert got==exp,(p,got,exp)
    assert sum(got)==p**5+p**4-p**2
    print({"field":f"F_{p}","rank_distribution":got,"total":sum(got)})

for q in (2,3,4,5,7,8,9,11,13):
    vals=formulas(q)
    assert sum(vals)==q**5+q**4-q**2
    assert vals[3]==0

print("VERIFY_OK")
