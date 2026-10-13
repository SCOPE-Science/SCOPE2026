import sympy as sp
from itertools import product

a,b,c,d=sp.symbols("a b c d")
M=sp.Matrix([[a,b],[c,d]])
basis=[sp.Matrix([1,0]),sp.Matrix([0,1])]

def bracket(x,y):
    return sp.Matrix([0, sp.expand(x[0]*y[0])])

def defect(R,x,y):
    Rx=R*x
    Ry=R*y
    return sp.simplify(bracket(Rx,Ry)-R*(bracket(Rx,y)+bracket(x,Ry)))

eqs=[]
for x in basis:
    for y in basis:
        eqs.extend([sp.expand(z) for z in defect(M,x,y)])
gens=sp.groebner(eqs,a,b,c,d,order="lex").polys
exprs=[sp.factor(g.as_expr()) for g in gens]
assert set(exprs)=={a*(a-2*d),a*b,b**2,b*d}, exprs

# Verify both symbolic components.
for R in (
    sp.Matrix([[0,0],[c,d]]),
    sp.Matrix([[2*d,0],[c,d]])
):
    for x in basis:
        for y in basis:
            assert defect(R,x,y)==sp.zeros(2,1)

u,v=sp.symbols("u v", nonzero=True)
Phi=sp.Matrix([[u,0],[v,u**2]])
assert sp.factor(Phi.det())==u**3
R=sp.Matrix([[a,0],[c,d]])
Conj=sp.simplify(Phi*R*Phi.inv())
Expected=sp.Matrix([[a,0],[u*c+v*(a-d)/u,d]])
assert sp.simplify(Conj-Expected)==sp.zeros(2,2)

def br(x,y,p):
    return (0,(x[0]*y[0])%p)

def mv(T,x,p):
    return ((T[0][0]*x[0]+T[0][1]*x[1])%p,
            (T[1][0]*x[0]+T[1][1]*x[1])%p)

def add(x,y,p):
    return ((x[0]+y[0])%p,(x[1]+y[1])%p)

def rb(T,p):
    e=((1,0),(0,1))
    for x in e:
        for y in e:
            Rx=mv(T,x,p); Ry=mv(T,y,p)
            lhs=br(Rx,Ry,p)
            rhs=mv(T,add(br(Rx,y,p),br(x,Ry,p),p),p)
            if lhs!=rhs:
                return False
    return True

def inv2(P,p):
    a0,b0=P[0]; c0,d0=P[1]
    det=(a0*d0-b0*c0)%p
    di=pow(det,-1,p)
    return ((d0*di%p,(-b0)*di%p),((-c0)*di%p,a0*di%p))

def mm(A,B,p):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%p for j in range(2)) for i in range(2))

def conj(T,u0,v0,p):
    P=((u0,0),(v0,u0*u0%p))
    return mm(mm(P,T,p),inv2(P,p),p)

for p in (2,3,5,7):
    mats=[((aa,bb),(cc,dd)) for aa,bb,cc,dd in product(range(p),repeat=4)]
    ops=[T for T in mats if rb(T,p)]
    expected_count=p*p if p==2 else 2*p*p-p
    assert len(ops)==expected_count

    rem=set(ops); orbits=[]
    while rem:
        T=next(iter(rem))
        orb={conj(T,u0,v0,p) for u0 in range(1,p) for v0 in range(p)}
        orbits.append(orb)
        rem-=orb
    expected_orbits=p+1 if p==2 else 2*p
    assert len(orbits)==expected_orbits

    sizes=sorted(map(len,orbits))
    if p==2:
        expected_sizes=sorted([1,1]+[p]*(p-1))
    else:
        expected_sizes=sorted([1,p-1]+[p]*(2*(p-1)))
    assert sizes==expected_sizes, (p,sizes,expected_sizes)
    print({"q":p,"operators":len(ops),"orbits":len(orbits),"sizes":sizes})

print("VERIFY_OK")
