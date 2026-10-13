import sympy as sp
from itertools import product

eps=sp.symbols("eps")
half=sp.Rational(1,2)

# vectors are columns in the basis e1,e2
e1=sp.Matrix([1,0])
e2=sp.Matrix([0,1])

def Aprod(x,y):
    a,b=x
    c,d=y
    return sp.Matrix([
        sp.expand(a*c*(1-eps)+(a*d+b*c)*half),
        sp.expand(a*c*eps+(a*d+b*c)*half+b*d)
    ])

u=e1-e2
v=e1+(2*eps-1)*e2
assert sp.simplify(Aprod(u,u)+eps*u)==sp.zeros(2,1)
assert sp.simplify(Aprod(u,v))==sp.zeros(2,1)
assert sp.simplify(Aprod(v,v)-eps*(-u+2*v))==sp.zeros(2,1)

# fixed algebra B in basis x,y
def Bprod(x,y):
    r,s=x
    t,w=y
    return sp.Matrix([
        sp.expand(-(r*t+s*w)),
        sp.expand(2*s*w)
    ])

# symbolic baric-isomorphism check under phi(u)=eps*x, phi(v)=eps*y
x=sp.Matrix([1,0])
y=sp.Matrix([0,1])
assert sp.simplify(Bprod(eps*x,eps*x)-(-eps)*(eps*x))==sp.zeros(2,1)
assert sp.simplify(Bprod(eps*x,eps*y))==sp.zeros(2,1)
assert sp.simplify(Bprod(eps*y,eps*y)-eps*(-eps*x+2*eps*y))==sp.zeros(2,1)

# B is genuinely nonassociative.
assert Bprod(Bprod(y,y),x) != Bprod(y,Bprod(y,x))

def inv2(a,q):
    return pow(a,-1,q)

def aprod_q(x,y,e,q):
    h=inv2(2,q)
    a,b=x; c,d=y
    return (
        (a*c*(1-e)+(a*d+b*c)*h)%q,
        (a*c*e+(a*d+b*c)*h+b*d)%q
    )

def bprod_q(x,y,q):
    r,s=x; t,u=y
    return (-(r*t+s*u)%q,(2*s*u)%q)

def det2(X,Y,q):
    return (X[0]*Y[1]-X[1]*Y[0])%q

def natural_bases_A(e,q):
    vec=[z for z in product(range(q),repeat=2) if z!=(0,0)]
    out=[]
    for X in vec:
        for Y in vec:
            if det2(X,Y,q) and aprod_q(X,Y,e,q)==(0,0):
                out.append((X,Y))
    return out

def is_B_automorphism(M,q):
    a,b,c,d=M  # columns: F(x)=(a,c), F(y)=(b,d)
    if (a*d-b*c)%q==0:
        return False
    Fx=(a,c); Fy=(b,d)
    # preserve x^2=-x, xy=0, y^2=-x+2y
    if bprod_q(Fx,Fx,q) != ((-a)%q,(-c)%q):
        return False
    if bprod_q(Fx,Fy,q) != (0,0):
        return False
    rhs=((-a+2*b)%q,(-c+2*d)%q)
    if bprod_q(Fy,Fy,q) != rhs:
        return False
    return True

for q in (3,5,7,11):
    expected=2*(q-1)**2
    counts={}
    for e in range(q):
        n=len(natural_bases_A(e,q))
        counts[e]=n
        if e==0:
            assert n==0
        else:
            assert n==expected

    autos=[M for M in product(range(q),repeat=4) if is_B_automorphism(M,q)]
    assert autos==[(1,0,0,1)]

    # Natural bases of B are exactly the two coordinate-axis orders.
    vec=[z for z in product(range(q),repeat=2) if z!=(0,0)]
    natB=[]
    for X in vec:
        for Y in vec:
            if det2(X,Y,q) and bprod_q(X,Y,q)==(0,0):
                natB.append((X,Y))
    assert len(natB)==expected
    predicted=set()
    for lam in range(1,q):
        for mu in range(1,q):
            predicted.add(((lam,0),(0,mu)))
            predicted.add(((0,lam),(mu,0)))
    assert set(natB)==predicted

    print({
        "q":q,
        "A0_ordered_natural_bases":counts[0],
        "nonzero_parameter_ordered_natural_bases":expected,
        "B_automorphisms":len(autos)
    })

print("VERIFY_OK")
