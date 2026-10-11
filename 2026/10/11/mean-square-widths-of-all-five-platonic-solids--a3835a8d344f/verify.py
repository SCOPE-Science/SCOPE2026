#!/usr/bin/env python3
import math
import numpy as np
from scipy.integrate import quad

pi = math.pi
sq5 = math.sqrt(5.0)

T = (1.0/3.0)*(1.0 + (3.0+math.sqrt(3.0))/pi)
CUBE = 1.0 + 4.0/pi
OCT = 2.0/3.0 + 4.0/(pi*math.sqrt(3.0))
DOD = (3.0+sq5)/2.0 + 10.0/pi*math.sqrt(1.0+2.0/sq5)
ICO = (5.0+sq5)/6.0 + 10.0/(pi*math.sqrt(3.0))

def I_closed(q, R):
    delta = math.asin(1.0/(2.0*R))
    a = pi/q
    y = math.sin(a)*math.cos(delta)
    return (q/3.0)*(2*a - 2*math.asin(y)
        + 2*(math.sin(delta)**2)*y/math.sqrt(1-y*y))

def I_quad(q, R):
    delta = math.asin(1.0/(2.0*R))
    a = pi/q
    td = math.tan(delta)
    f = lambda psi: (math.cos(psi)**3) / ((math.cos(psi)**2 + td*td)**1.5)
    J, err = quad(f, -a, a, epsabs=2e-13, epsrel=2e-13)
    return (q/3.0)*(2*a-J)

R_cube = math.sqrt(3.0)/2.0
R_oct = 1.0/math.sqrt(2.0)
R_ico = math.sqrt((5.0+sq5)/8.0)
phi = (1.0+sq5)/2.0
R_dod = math.sqrt(3.0)*phi/2.0

cases = [
    ("cube",8,3,R_cube,CUBE),
    ("octahedron",6,4,R_oct,OCT),
    ("dodecahedron",20,3,R_dod,DOD),
    ("icosahedron",12,5,R_ico,ICO),
]
for name,N,q,R,target in cases:
    ic = I_closed(q,R)
    iq = I_quad(q,R)
    assert abs(ic-iq) < 2e-12, (name,ic,iq)
    got = N*R*R*ic/pi
    assert abs(got-target) < 2e-12, (name,got,target)

# Exact-special-angle regression identities.
assert abs(math.sin(pi/4)*math.sqrt(1-1/(4*R_oct*R_oct)) - 0.5) < 2e-15
assert abs(math.sin(pi/5)*math.sqrt(1-1/(4*R_ico*R_ico)) - 0.5) < 2e-15
assert abs(math.sin(pi/3)*math.sqrt(1-1/(4*R_dod*R_dod)) - math.cos(pi/5)) < 2e-15
assert abs(1/(math.tan(pi/5)) - math.sqrt(1+2/sq5)) < 2e-15

# Standard vertex sets, scaled to edge 1.
tet = np.array([
    [0.0,0.0,1.0],
    [2*math.sqrt(2)/3,0.0,-1/3],
    [-math.sqrt(2)/3,math.sqrt(2/3),-1/3],
    [-math.sqrt(2)/3,-math.sqrt(2/3),-1/3]
]) / (2*math.sqrt(2/3))

cube = np.array([[sx/2,sy/2,sz/2]
                 for sx in (-1,1) for sy in (-1,1) for sz in (-1,1)], float)

octa = []
for i in range(3):
    for s in (-1,1):
        v=np.zeros(3); v[i]=s/math.sqrt(2); octa.append(v)
octa=np.array(octa)

ico=[]
for a,b in [(0,1),(1,phi)]:
    pass
ico = np.array(
    [(0,s1/2,s2*phi/2) for s1 in (-1,1) for s2 in (-1,1)] +
    [(s1/2,s2*phi/2,0) for s1 in (-1,1) for s2 in (-1,1)] +
    [(s1*phi/2,0,s2/2) for s1 in (-1,1) for s2 in (-1,1)], float)

invphi=1/phi
scale=phi/2
dod = np.array(
    [(sx,sy,sz) for sx in (-1,1) for sy in (-1,1) for sz in (-1,1)] +
    [(0,s1*invphi,s2*phi) for s1 in (-1,1) for s2 in (-1,1)] +
    [(s1*invphi,s2*phi,0) for s1 in (-1,1) for s2 in (-1,1)] +
    [(s1*phi,0,s2*invphi) for s1 in (-1,1) for s2 in (-1,1)], float) * scale

def min_nonzero_dist(V):
    ds=[]
    for i in range(len(V)):
        for j in range(i+1,len(V)):
            d=np.linalg.norm(V[i]-V[j])
            if d>1e-12: ds.append(d)
    return min(ds)

for name,V in [("tetrahedron",tet),("cube",cube),("octahedron",octa),
               ("dodecahedron",dod),("icosahedron",ico)]:
    assert abs(min_nonzero_dist(V)-1.0) < 2e-12, (name,min_nonzero_dist(V))

# Deterministic Fibonacci-sphere support integration.
def fib_sphere(n):
    k=np.arange(n,dtype=float)
    z=1.0-2.0*(k+0.5)/n
    golden=(1+math.sqrt(5.0))/2.0
    th=2*pi*k/golden
    r=np.sqrt(np.maximum(0.0,1-z*z))
    return np.column_stack((r*np.cos(th),r*np.sin(th),z))

U=fib_sphere(220000)
def mean_width_sq(V):
    hp=np.max(U@V.T,axis=1)
    hm=np.max((-U)@V.T,axis=1)
    return float(np.mean((hp+hm)**2))

for name,V,target in [
    ("tetrahedron",tet,T),
    ("cube",cube,CUBE),
    ("octahedron",octa,OCT),
    ("dodecahedron",dod,DOD),
    ("icosahedron",ico,ICO),
]:
    got=mean_width_sq(V)
    assert abs(got-target)<2.5e-5,(name,got,target)

print("VERIFY_OK")
print("normal_cell_integrals = passed")
print("unit_edge_coordinates = passed")
print("deterministic_spherical_quadrature = passed")
