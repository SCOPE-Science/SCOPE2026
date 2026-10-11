import math, random
import sympy as sp

A,B=sp.symbols('A B', real=True)
x,y,z=sp.symbols('x y z', real=True)
D=4*x*x+4*x*y+4*x*z+10*x+4*y*y+4*y*z+10*y+z*z+6*z+9
s=2*A*B
prod=A*A+B*B-1
zz=2*B*B-1
D_ab=sp.expand(4*s*s-4*prod+4*zz*s+10*s+zz*zz+6*zz+9)
Q=(4*B*B-1)*A*A+B*(4*B*B+3)*A+B**4+B*B+2
assert sp.expand(D_ab-4*Q)==0
endpoint=(1-B)*((1-B)**2+B**2*(2-B))
assert sp.expand(Q.subs(A,-1)-endpoint)==0
vertex_gap=B*(4*B**2+3)-2*(4*B**2-1)
assert sp.expand(vertex_gap-(1+(1-B)*(1+4*B*(1-B))))==0

def energy(ph):
    c=[complex(math.cos(t),math.sin(t)) for t in ph]
    E=0.0
    for k in range(1,5):
        ck=sum(c[j+k]*c[j].conjugate() for j in range(5-k))
        E += abs(ck)**2
    return E

w=[0.0,0.0,0.0,math.pi,0.0]
assert abs(energy(w)-2.0)<1e-12
random.seed(20261005)
mn=1e9
for _ in range(20000):
    ph=[random.random()*2*math.pi for _ in range(5)]
    e=energy(ph)
    mn=min(mn,e)
    if e < 2-1e-10:
        raise AssertionError(e)
print(f"VERIFY_OK exact_energy=2 exact_L4_fourth=29 random_cases=20000 min_random_energy={mn:.12f}")
