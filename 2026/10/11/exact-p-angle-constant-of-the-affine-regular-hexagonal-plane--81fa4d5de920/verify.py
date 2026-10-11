from fractions import Fraction
from itertools import product

VERTICES = [(1,1),(1,0),(0,-1),(-1,-1),(-1,0),(0,1)]
PHI = [(1,0),(0,1),(1,-1)]

def add(u,v):
    return (u[0]+v[0],u[1]+v[1])

def sub(u,v):
    return (u[0]-v[0],u[1]-v[1])

def mul(a,u):
    return (a*u[0],a*u[1])

def evalf(f,z):
    return f[0]*z[0] + f[1]*z[1]

def dual_norm(f):
    return max(abs(evalf(f,v)) for v in VERTICES)

def N(z):
    s,t=z
    return max(abs(s),abs(t),abs(s-t))

# All signed facet-functional pairs.
E = [mul(sign,phi) for phi in PHI for sign in (1,-1)]
worst = 0
for f,g in product(E, repeat=2):
    value = dual_norm(add(f,g)) + dual_norm(sub(f,g))
    worst = max(worst, value)
    assert value <= 3
assert worst == 3

# Check that the listed vertices are unit and exhaust the facet intersections used by the certificate.
for v in VERTICES:
    assert N(v) == 1

# Attaining pair.
x=(1,1)
y=(1,0)
assert N(x)==N(y)==1
A=N(add(x,y))
B=N(sub(x,y))
assert (A,B)==(2,1)
cosine = Fraction(A*A+B*B-4, 2*A*B)
assert cosine == Fraction(1,4)

# Check the quadratic envelope at every vertex of the feasible (A,B)-polygon.
feasible_vertices=[(0,0),(2,0),(2,1),(1,2),(0,2)]
for A0,B0 in feasible_vertices:
    q=2*A0*A0+2*B0*B0-A0*B0
    assert q <= 8

print("VERIFY_OK")
