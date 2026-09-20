"""Symbolic and numerical checks for tangency-chord identities in a bicentric quadrilateral."""
import math
import sympy as sp

r, D, u, v = sp.symbols('r D u v', positive=True)
C = 4*r**2*(D+r)/(D-r)
# Work modulo u+v=C by replacing v with C-u.
v_sub = C-u
s2 = (D-r)**2 * u*v_sub/(4*r**4)
upper = sp.factor((D+r)**2 - s2 - (D-r)**2*(u-v_sub)**2/(16*r**4))
lower = sp.factor(s2 - 8*r*(D-r) - (D-r)**2*(4*r**2-u)*(4*r**2-v_sub)/(4*r**4))
assert sp.simplify(upper) == 0
assert sp.simplify(lower) == 0

p2 = r**2*(D-3*r)/(D-r)
assert sp.simplify(4*(2*r**2-p2) - C) == 0
R2 = (D**2-r**2)/4
R2_from_C = 4*r**4*C/(C-4*r**2)**2
assert sp.simplify(R2-R2_from_C) == 0

# Numerical construction: two perpendicular chords through a fixed interior point.
def intersections(P, direction, radius=1.0):
    px, py = P
    ux, uy = direction
    norm = math.hypot(ux, uy)
    ux, uy = ux/norm, uy/norm
    b = px*ux + py*uy
    c = px*px + py*py - radius*radius
    root = math.sqrt(b*b-c)
    return [(px+t*ux, py+t*uy) for t in (-b-root, -b+root)]

def tangent_intersection(a, b, radius=1.0):
    # Tangent at q=(x,y) to x^2+y^2=r^2 is q dot X = r^2.
    (x1,y1),(x2,y2)=a,b
    det=x1*y2-y1*x2
    return ((radius*radius*(y2-y1))/det,
            (radius*radius*(x1-x2))/det)

def circumcircle(points):
    (x1,y1),(x2,y2),(x3,y3)=points[:3]
    A=2*(x2-x1); B=2*(y2-y1); Cc=x2*x2+y2*y2-x1*x1-y1*y1
    Dd=2*(x3-x1); E=2*(y3-y1); F=x3*x3+y3*y3-x1*x1-y1*y1
    det=A*E-B*Dd
    ox=(Cc*E-B*F)/det; oy=(A*F-Cc*Dd)/det
    rr=math.hypot(x1-ox,y1-oy)
    return (ox,oy),rr

for p in (0.2,0.6,0.9):
    predicted_R = math.sqrt(2-p*p)/(1-p*p)
    for alpha in (0.13,0.41,0.77):
        P=(p,0.0)
        e1=intersections(P,(math.cos(alpha),math.sin(alpha)))
        e2=intersections(P,(-math.sin(alpha),math.cos(alpha)))
        contact=e1+e2
        contact.sort(key=lambda q: math.atan2(q[1],q[0]))
        vertices=[tangent_intersection(contact[i],contact[(i+1)%4]) for i in range(4)]
        _,Rnum=circumcircle(vertices)
        k=math.dist(e1[0],e1[1]); l=math.dist(e2[0],e2[1])
        assert abs(Rnum-predicted_R) < 1e-10
        assert abs(k*k+l*l-4*(2-p*p)) < 1e-10

print('all symbolic and numerical checks passed')
