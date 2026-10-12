import sympy as sp
from itertools import product
from collections import Counter

a,b,c,d,u,v=sp.symbols("a b c d u v")
N=sp.Matrix([[a,b],[c,d]])
e1=sp.Matrix([1,0]); e2=sp.Matrix([0,1])
basis=(e1,e2)

def bracket(x,y):
    return sp.Matrix([sp.expand(x[1]*(u*y[0]+v*y[1])),0])

# Left Leibniz identity for arbitrary parameters.
for x,y,z in product(basis,repeat=3):
    D=sp.simplify(bracket(x,bracket(y,z))-bracket(bracket(x,y),z)-bracket(y,bracket(x,z)))
    assert D==sp.zeros(2,1)

def defect(x,y):
    Nx,Ny=N*x,N*y
    inside=bracket(x,Ny)+bracket(Nx,y)-N*bracket(x,y)
    return sp.simplify(bracket(Nx,Ny)-N*inside)

eqs=[]
for x,y in product(basis,repeat=2):
    for z in defect(x,y):
        z=sp.factor(z)
        if z!=0:
            eqs.append(z)

# Direct symbolic consequences used in the proof.
assert any(sp.simplify(z-c*c*u)==0 or sp.simplify(z+c*c*u)==0 for z in eqs)
assert any(sp.simplify(z-c*c*v)==0 or sp.simplify(z+c*c*v)==0 for z in eqs)
target=sp.expand((a-d)*(v*(a-d)-u*b))
reduced={sp.factor(z.subs(c,0)) for z in eqs if sp.factor(z.subs(c,0))!=0}
G=sp.groebner([target],a,b,d,u,v)
for z in reduced:
    assert G.reduce(sp.expand(z))[1]==0
G2=sp.groebner(list(reduced),a,b,d,u,v)
assert G2.reduce(target)[1]==0

# Common Nijenhuis maps act on the pencil by dual-number multiplication.
aa,bb=sp.symbols("aa bb")
M=sp.Matrix([[aa,bb],[0,aa]])
def induced(x,y):
    return sp.simplify(bracket(x,M*y)+bracket(M*x,y)-M*bracket(x,y))
assert induced(e2,e1)==sp.Matrix([aa*u,0])
assert induced(e2,e2)==sp.Matrix([bb*u+aa*v,0])
assert induced(e1,e1)==sp.zeros(2,1)
assert induced(e1,e2)==sp.zeros(2,1)

def brq(x,y,U,V,q):
    return ((x[1]*(U*y[0]+V*y[1]))%q,0)

def mv(A,x,q):
    return ((A[0]*x[0]+A[1]*x[1])%q,(A[2]*x[0]+A[3]*x[1])%q)

def is_nij(A,U,V,q):
    bas=((1,0),(0,1))
    for x,y in product(bas,repeat=2):
        Nx,Ny=mv(A,x,q),mv(A,y,q)
        lhs=brq(Nx,Ny,U,V,q)
        p1=brq(x,Ny,U,V,q)
        p2=brq(Nx,y,U,V,q)
        p3=mv(A,brq(x,y,U,V,q),q)
        inside=((p1[0]+p2[0]-p3[0])%q,(p1[1]+p2[1]-p3[1])%q)
        if lhs!=mv(A,inside,q):
            return False
    return True

def rank2(A,q):
    if all(x%q==0 for x in A):
        return 0
    return 2 if (A[0]*A[3]-A[1]*A[2])%q else 1

for q in (2,3,5,7):
    projective=[(1,t) for t in range(q)]+[(0,1)]
    fibers=[]
    total=0
    for U,V in projective:
        S={A for A in product(range(q),repeat=4) if is_nij(A,U,V,q)}
        fibers.append(S)
        total+=len(S)
        ranks=Counter(rank2(A,q) for A in S)
        got=tuple(ranks[i] for i in range(3))
        if U==0:
            assert len(S)==q*q
            assert got==(1,q-1,q*(q-1))
        else:
            assert len(S)==2*q*q-q
            assert got==(1,3*(q-1),2*(q-1)**2)

    common={(A,B,0,A) for A in range(q) for B in range(q)}
    assert set.intersection(*fibers)==common
    for i in range(len(fibers)):
        for j in range(i+1,len(fibers)):
            assert fibers[i]&fibers[j]==common
    assert total==2*q**3
    print({"q":q,"projective_incidence":total,"common_nijenhuis":len(common)})

print("VERIFY_OK")
