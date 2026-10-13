import sympy as sp
from itertools import product
from math import gcd

def mul(x,y):
    z=sp.zeros(3,1)
    z[1]=sp.expand(x[0]*y[0])
    z[2]=sp.expand(x[0]*y[1]+x[1]*y[0])
    return z

basis=[sp.eye(3)[:,i] for i in range(3)]
x11,x12,x13,x21,x22,x23,x31,x32,x33=sp.symbols(
    "x11 x12 x13 x21 x22 x23 x31 x32 x33"
)
M=sp.Matrix([[x11,x12,x13],[x21,x22,x23],[x31,x32,x33]])

def defect(N,x,y):
    Nx=N*x
    Ny=N*y
    return sp.simplify(
        mul(Nx,Ny)-N*(mul(x,Ny)+mul(Nx,y)-N*mul(x,y))
    )

eq={}
for i,x in enumerate(basis):
    for j,y in enumerate(basis):
        eq[(i+1,j+1)]=[sp.factor(v) for v in defect(M,x,y)]

# Sequential field-level consequences used in the proof.
assert sp.factor(eq[(3,3)][1]) == x13**2
# After x13=0, the e2 component at (1,3) is -x23^2.
assert sp.factor(eq[(1,3)][1].subs(x13,0)) == -x23**2
# After x13=x23=0, the e2 component at (2,2) is x12^2.
assert sp.factor(eq[(2,2)][1].subs({x13:0,x23:0})) == x12**2
# Then the e2 component at (1,1) is (x11-x22)^2.
assert sp.factor(eq[(1,1)][1].subs({x13:0,x23:0,x12:0})) == (x11-x22)**2
# Finally the e3 component at (1,2) becomes (x11-x33)^2.
last=eq[(1,2)][2].subs({x13:0,x23:0,x12:0,x22:x11})
assert sp.factor(last) == (x11-x33)**2

a,b,c,d=sp.symbols("a b c d")
N=sp.Matrix([[a,0,0],[b,a,0],[c,d,a]])
for x in basis:
    for y in basis:
        assert defect(N,x,y) == sp.zeros(3,1)

u,v,w=sp.symbols("u v w", nonzero=True)
Phi=sp.Matrix([[u,0,0],[v,u**2,0],[w,2*u*v,u**3]])
assert sp.factor(Phi.det()) == u**6
Conj=sp.simplify(Phi*N*Phi.inv())
Expected=sp.Matrix([
    [a,0,0],
    [u*b,a,0],
    [u**2*c+v*(2*b-d),u*d,a],
])
assert sp.simplify(Conj-Expected) == sp.zeros(3,3)

def action(t,u0,v0,p):
    aa,bb,cc,dd=t
    return (
        aa%p,
        (u0*bb)%p,
        (u0*u0*cc+v0*(2*bb-dd))%p,
        (u0*dd)%p
    )

for p in (2,3,5,7):
    pts=list(product(range(p),repeat=4))
    remaining=set(pts)
    orbits=[]
    while remaining:
        t=next(iter(remaining))
        orb={action(t,u0,v0,p) for u0 in range(1,p) for v0 in range(p)}
        orbits.append(orb)
        remaining-=orb
    expected=p*(2*p+1+gcd(2,p-1))
    assert len(orbits)==expected
    assert len(pts)==p**4
    print({"q":p,"operators":len(pts),"orbits":len(orbits)})

print("VERIFY_OK")
