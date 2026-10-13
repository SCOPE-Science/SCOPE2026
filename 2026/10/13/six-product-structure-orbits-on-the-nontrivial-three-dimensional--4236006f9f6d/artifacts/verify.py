import itertools
import sympy as sp

# ---------- symbolic Nijenhuis check ----------
def det3cols(x,y,z):
    return sp.Matrix.hstack(x,y,z).det()

e=[sp.eye(3)[:,i] for i in range(3)]

def br(x,y,z):
    return sp.Matrix([sp.expand(det3cols(x,y,z)),0,0])

n=sp.symbols("n11 n12 n13 n21 n22 n23 n31 n32 n33")
N=sp.Matrix(3,3,n)

# Nijenhuis identity used for 3-Lie algebras:
# [Nx,Ny,Nz] =
# N([Nx,Ny,z]+[Nx,y,Nz]+[x,Ny,Nz])
# - N^2([Nx,y,z]+[x,Ny,z]+[x,y,Nz])
# + N^3[x,y,z]
def nij_defect(N,x,y,z):
    Nx,Ny,Nz=N*x,N*y,N*z
    return sp.expand(br(Nx,Ny,Nz)
        - N*(br(Nx,Ny,z)+br(Nx,y,Nz)+br(x,Ny,Nz))
        + (N**2)*(br(Nx,y,z)+br(x,Ny,z)+br(x,y,Nz))
        - (N**3)*br(x,y,z))

for x in e:
    for y in e:
        for z in e:
            assert nij_defect(N,x,y,z)==sp.zeros(3,1)

# ---------- finite-field helpers ----------
def invmod(a,p):
    return pow(a%p,-1,p)

def det3(M,p):
    return (
        M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
        -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
        +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
    )%p

def matmul(A,B,p):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3))%p for j in range(3)) for i in range(3))

I=((1,0,0),(0,1,0),(0,0,1))

def matsq(A,p):
    return matmul(A,A,p)

def matinv(A,p):
    M=[list(row)+[1 if i==j else 0 for j in range(3)] for i,row in enumerate(A)]
    for col in range(3):
        piv=next(r for r in range(col,3) if M[r][col]%p)
        M[col],M[piv]=M[piv],M[col]
        z=pow(M[col][col]%p,-1,p)
        M[col]=[(z*x)%p for x in M[col]]
        for r in range(3):
            if r!=col:
                z=M[r][col]%p
                M[r]=[(M[r][j]-z*M[col][j])%p for j in range(6)]
    return tuple(tuple(M[i][j+3]%p for j in range(3)) for i in range(3))

def neg(A,p):
    return tuple(tuple((-A[i][j])%p for j in range(3)) for i in range(3))

def canon_reps(p):
    two=2%p
    Es=((1,0,0),(0,1,0),(0,0,-1%p))
    Ep=((-1%p,0,0),(0,1,0),(0,0,1))
    Eg=((-1%p,0,0),((-two)%p,1,0),(0,0,1))
    return [Es,Ep,Eg,neg(Es,p),neg(Ep,p),neg(Eg,p)]

def autos(p):
    out=[]
    for lam in range(1,p):
        for r,s,a,b,c,d in itertools.product(range(p),repeat=6):
            if (a*d-b*c)%p==1:
                out.append(((lam,r,s),(0,a,b),(0,c,d)))
    return out

def conj(P,E,p):
    return matmul(matmul(P,E,p),matinv(P,p),p)

def all_involutions(p):
    out=[]
    vals=range(p)
    for flat in itertools.product(vals,repeat=9):
        A=(flat[0:3],flat[3:6],flat[6:9])
        if matsq(A,p)==I:
            out.append(A)
    return out

# product structures are nonscalar involutions, since all N are Nijenhuis.
p=3
Auts=autos(p)
assert len(Auts)==p**3*(p-1)*(p**2-1)==432
invol=all_involutions(p)
plusI=I
minusI=neg(I,p)
prod=[A for A in invol if A not in (plusI,minusI)]
assert len(invol)==236
assert len(prod)==234

pool=set(prod)
orbits=[]
reps=canon_reps(p)
for R in reps:
    orb={conj(P,R,p) for P in Auts}
    assert R in orb
    orbits.append(orb)
assert len({x for O in orbits for x in O})==234
assert sorted(len(O) for O in orbits)==[9,9,36,36,72,72]
# disjoint
for i in range(6):
    for j in range(i):
        assert orbits[i].isdisjoint(orbits[j])

# F5 orbit replay without enumerating all 5^9 matrices.
p=5
Auts5=autos(p)
assert len(Auts5)==p**3*(p-1)*(p**2-1)==12000
orbits5=[{conj(P,R,p) for P in Auts5} for R in canon_reps(p)]
assert sorted(len(O) for O in orbits5)==[25,25,150,150,600,600]
assert sum(len(O) for O in orbits5)==2*p**2*(p**2+p+1)==1550
for i in range(6):
    for j in range(i):
        assert orbits5[i].isdisjoint(orbits5[j])

# ---------- direct identity checks on six integer normal forms ----------
Es=sp.diag(1,1,-1)
Ep=sp.diag(-1,1,1)
Eg=sp.Matrix([[-1,0,0],[-2,1,0],[0,0,1]])
int_reps=[Es,Ep,Eg,-Es,-Ep,-Eg]

def prod_defect(E,x,y,z):
    Ex,Ey,Ez=E*x,E*y,E*z
    return sp.expand(
        br(Ex,Ey,Ez)
        - E*(br(Ex,Ey,z)+br(Ex,y,Ez)+br(x,Ey,Ez))
        + (E**2)*(br(Ex,y,z)+br(x,Ey,z)+br(x,y,Ez))
        - (E**3)*br(x,y,z)
    )

# Abelian product equation from the eigenspace condition:
# [x,y,z]+[x,Ey,Ez]+[Ex,y,Ez]+[Ex,Ey,z] = 0.
def abelian_defect(E,x,y,z):
    Ex,Ey,Ez=E*x,E*y,E*z
    return sp.expand(br(x,y,z)+br(x,Ey,Ez)+br(Ex,y,Ez)+br(Ex,Ey,z))

# Strong condition: [x,y,z] = E([Ex,y,z]+[x,Ey,z]+[x,y,Ez])
def strong_defect(E,x,y,z):
    Ex,Ey,Ez=E*x,E*y,E*z
    return sp.expand(br(x,y,z)-E*(br(Ex,y,z)+br(x,Ey,z)+br(x,y,Ez)))

# Perfect condition: E[x,y,z]=[Ex,Ey,Ez]
def perfect_defect(E,x,y,z):
    Ex,Ey,Ez=E*x,E*y,E*z
    return sp.expand(E*br(x,y,z)-br(Ex,Ey,Ez))

labels=[]
for E in int_reps:
    assert E**2==sp.eye(3)
    assert E not in (sp.eye(3),-sp.eye(3))
    prod_ok=all(prod_defect(E,x,y,z)==sp.zeros(3,1) for x in e for y in e for z in e)
    ab_ok=all(abelian_defect(E,x,y,z)==sp.zeros(3,1) for x in e for y in e for z in e)
    st_ok=all(strong_defect(E,x,y,z)==sp.zeros(3,1) for x in e for y in e for z in e)
    pe_ok=all(perfect_defect(E,x,y,z)==sp.zeros(3,1) for x in e for y in e for z in e)
    assert prod_ok and ab_ok
    labels.append((st_ok,pe_ok))
assert labels.count((True,False))==2
assert labels.count((False,True))==2
assert labels.count((False,False))==2

print({"F3_product_structures":len(prod),
       "F3_aut_order":len(Auts),
       "F3_orbit_sizes":sorted(len(O) for O in orbits),
       "F5_aut_order":len(Auts5),
       "F5_orbit_sizes":sorted(len(O) for O in orbits5),
       "types":labels})
print("VERIFY_OK")
