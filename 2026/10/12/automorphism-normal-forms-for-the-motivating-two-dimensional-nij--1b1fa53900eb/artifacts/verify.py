from itertools import product
from collections import Counter
import sympy as sp

a,b,c,d=sp.symbols('a b c d')
M=sp.Matrix([[a,b],[c,d]])
E=(sp.Matrix([1,0]),sp.Matrix([0,1]))

def br(x,y):
    return sp.Matrix([sp.expand(x[1]*(y[0]+y[1])),0])

def torsion(N,x,y):
    Nx=N*x; Ny=N*y
    return sp.simplify(br(Nx,Ny)-N*(br(Nx,y)+br(x,Ny)-N*br(x,y)))

eqs=[]
for x in E:
    for y in E:
        eqs.extend([sp.factor(z) for z in torsion(M,x,y) if z!=0])
assert any(sp.expand(z-c**2)==0 or sp.expand(z+c**2)==0 for z in eqs)
main=a*a-a*b-2*a*d+b*c+b*d+d*d
assert any(sp.expand(z-main)==0 or sp.expand(z+main)==0 for z in eqs)
assert sp.factor(main.subs(c,0))==(a-d)*(a-b-d)

p,q,r,s=sp.symbols('p q r s')
P=sp.Matrix([[p,q],[r,s]])
autoeq=[]
for x in E:
    for y in E:
        autoeq.extend([sp.factor(z) for z in (br(P*x,P*y)-P*br(x,y)) if z!=0])
# Directly verify claimed automorphisms and show symbolic preservation.
t=sp.symbols('t', nonzero=True)
Pt=sp.Matrix([[t,t-1],[0,1]])
for x in E:
    for y in E:
        assert sp.simplify(br(Pt*x,Pt*y)-Pt*br(x,y))==sp.zeros(2,1)

Nup=sp.Matrix([[a,b],[0,d]])
conj=sp.simplify(Pt*Nup*Pt.inv())
assert sp.simplify(conj[0,0]-a)==0
assert sp.simplify(conj[1,1]-d)==0
assert sp.simplify(conj[0,1]-(t*b+(t-1)*(d-a)))==0

# Symbolic normal families are Nijenhuis.
Q=sp.Matrix([[a,a-d],[0,d]])
J=sp.Matrix([[a,1],[0,a]])
for N in (Q,J):
    for x in E:
        for y in E:
            assert sp.simplify(torsion(N,x,y))==sp.zeros(2,1)

def brp(x,y,p):
    return (x[1]*(y[0]+y[1])%p,0)

def mv(A,x,p):
    return ((A[0][0]*x[0]+A[0][1]*x[1])%p,
            (A[1][0]*x[0]+A[1][1]*x[1])%p)

def sub(u,v,p): return tuple((u[i]-v[i])%p for i in range(2))
def add3(u,v,w,p): return tuple((u[i]+v[i]-w[i])%p for i in range(2))

def nij(A,p):
    e=((1,0),(0,1))
    for x in e:
        for y in e:
            Ax=mv(A,x,p); Ay=mv(A,y,p)
            lhs=brp(Ax,Ay,p)
            inner=add3(brp(Ax,y,p),brp(x,Ay,p),mv(A,brp(x,y,p),p),p)
            rhs=mv(A,inner,p)
            if lhs!=rhs:return False
    return True

def matmul(A,B,p):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%p for j in range(2)) for i in range(2))

def inv2(A,p):
    det=(A[0][0]*A[1][1]-A[0][1]*A[1][0])%p
    if det==0:return None
    z=pow(det,-1,p)
    return ((A[1][1]*z%p,-A[0][1]*z%p),(-A[1][0]*z%p,A[0][0]*z%p))

def isauto(A,p):
    I=inv2(A,p)
    if I is None:return False
    e=((1,0),(0,1))
    return all(brp(mv(A,x,p),mv(A,y,p),p)==mv(A,brp(x,y,p),p) for x in e for y in e)

def conjp(P,A,p):
    return matmul(matmul(P,A,p),inv2(P,p),p)

for p0 in (2,3,5,7):
    mats=[((aa,bb),(cc,dd)) for aa,bb,cc,dd in product(range(p0),repeat=4)]
    ops=[A for A in mats if nij(A,p0)]
    formula=[A for A in mats if A[1][0]==0 and ((A[0][0]-A[1][1])*(A[0][0]-A[0][1]-A[1][1]))%p0==0]
    assert set(ops)==set(formula)
    assert len(ops)==2*p0*p0-p0
    autos=[A for A in mats if isauto(A,p0)]
    expected_aut={((tt,(tt-1)%p0),(0,1)) for tt in range(1,p0)}
    assert set(autos)==expected_aut
    rem=set(ops); orbits=[]
    while rem:
        A=next(iter(rem))
        orb={conjp(P,A,p0) for P in autos}
        orbits.append(orb); rem-=orb
    assert len(orbits)==p0*p0+p0
    # Every Q is fixed; every J orbit has size q-1 (possibly 1 when q=2).
    Qs={((aa,(aa-dd)%p0),(0,dd)) for aa in range(p0) for dd in range(p0)}
    assert all(len({conjp(P,A,p0) for P in autos})==1 for A in Qs)
    Js=[((aa,1),(0,aa)) for aa in range(p0)]
    assert all(len({conjp(P,A,p0) for P in autos})==p0-1 for A in Js)
    print({'q':p0,'operators':len(ops),'automorphisms':len(autos),'orbits':len(orbits),'orbit_sizes':dict(sorted(Counter(map(len,orbits)).items()))})

print('VERIFY_OK')
