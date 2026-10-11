#!/usr/bin/env python3
import sympy as s

pi=s.pi
rt3=s.sqrt(3)

def u(deg):
    th=s.Rational(deg,180)*pi
    return s.Matrix([s.cos(th),s.sin(th)])

# [(3)^3] model: equilateral triangle A,B,C of side and diameter one.
A=s.Matrix([0,0])
B=s.Matrix([1,0])
C=s.Matrix([s.Rational(1,2),rt3/2])
tri=[
    A,
    C+u(-100), C+u(-80),
    B,
    A+u(20), A+u(40),
    C,
    B+u(140), B+u(160),
]

def shoelace(poly):
    total=0
    for i,p in enumerate(poly):
        q=poly[(i+1)%len(poly)]
        total += p[0]*q[1]-p[1]*q[0]
    return s.trigsimp(total/2)

A_tri=s.trigsimp(shoelace(tri))
A_tri_formula=s.Rational(9,2)*s.sin(pi/9)-rt3/2
assert s.simplify(s.trigsimp(A_tri-A_tri_formula))==0

# Every consecutive chord is 20 degrees on a unit circle.
side=2*s.sin(pi/18)
for i,p in enumerate(tri):
    q=tri[(i+1)%9]
    d2=s.trigsimp(sum((q[j]-p[j])**2 for j in range(2)))
    assert s.simplify(s.trigsimp(d2-side**2))==0

# Numerical sanity: diameter is one.
dists=[]
for i in range(9):
    for j in range(i+1,9):
        d=s.sqrt(s.N(sum((tri[i][k]-tri[j][k])**2 for k in range(2)),50))
        dists.append(d)
assert abs(float(max(dists))-1.0)<1e-12

# Regular diameter-one nonagon.
R=1/(2*s.cos(pi/18))
reg=[s.Matrix([R*s.cos(2*pi*j/9), R*s.sin(2*pi*j/9)]) for j in range(9)]
A_reg=s.trigsimp(shoelace(reg))
A_reg_formula=9*s.sin(pi/18)**2*s.cot(pi/9)
A_reg_geom=s.Rational(9,2)*R**2*s.sin(2*pi/9)
assert s.simplify(s.trigsimp(A_reg_geom/A_reg_formula))==1
assert abs(float(s.N(A_reg-A_reg_geom,50))) < 1e-40

# Its farthest cyclic separation is four steps and has length one.
diam=s.trigsimp(2*R*s.sin(4*pi/9))
assert s.simplify(s.trigsimp(diam-1))==0
reg_side=s.trigsimp(2*R*s.sin(pi/9))
assert s.simplify(s.trigsimp(reg_side-side))==0

# Exact gap identity.
gap=s.trigsimp(A_reg_formula-A_tri_formula)
gap_formula=(rt3-9*s.tan(pi/18))/2
assert abs(float(s.N(gap-gap_formula,50))) < 1e-40
assert float(s.N(gap,50))>0

# Periodic composition consequence for n=9.
def comps(total, length, prefix=()):
    if length==1:
        if total>=1:
            yield prefix+(total,)
        return
    for a in range(1,total-length+2):
        yield from comps(total-a,length-1,prefix+(a,))

classes=set()
for d in (3,9):
    total=9//d
    for length in range(1,total+1,2):
        for block in comps(total,length):
            full=block*d
            classes.add(full)
assert classes == {(3,3,3),(1,1,1,1,1,1,1,1,1)}

P=9*side
assert s.simplify(P-18*s.sin(pi/18))==0

print("VERIFY_OK")
print("classes =", sorted(classes))
print("A_tri =", s.N(A_tri,16))
print("A_reg =", s.N(A_reg,16))
print("gap =", s.N(gap,16))
print("Pmax =", s.N(P,16))
