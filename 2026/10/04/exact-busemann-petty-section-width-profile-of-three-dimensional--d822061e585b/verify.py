import math, random
from fractions import Fraction

# Exact algebra behind the hexagonal-section chamber.
def exact_hex_check(x,y,z):
    x=Fraction(x); y=Fraction(y); z=Fraction(z)
    a=y+z; b=z+x; c=x+y
    s=a+b+c; P=a*b+a*c+b*c; Q=a*a+b*b+c*c
    lhs_min=s*(2*P-Q)-8*a*b*c
    assert lhs_min == 8*x*y*z
    lhs_max=9*a*b*c-s*(2*P-Q)
    assert lhs_max == (x+y+z)*(x*y+x*z+y*z)-9*x*y*z
    assert lhs_min > 0 and lhs_max >= 0
    if x==y==z:
        assert lhs_max==0

for x in range(1,10):
    for y in range(1,10):
        for z in range(1,10):
            exact_hex_check(x,y,z)

# Independent geometric reconstruction of cube/parallelotope central sections.
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return [x-y for x,y in zip(a,b)]
def add(a,b): return [x+y for x,y in zip(a,b)]
def mul(t,a): return [t*x for x in a]
def norm(a): return math.sqrt(dot(a,a))
def cross(a,b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]
def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
           -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
           +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
def matvec(A,x): return [sum(A[i][j]*x[j] for j in range(3)) for i in range(3)]
def transpose(A): return [[A[j][i] for j in range(3)] for i in range(3)]
def inv3(A):
    d=det3(A); assert abs(d)>1e-9
    C=[
      [ A[1][1]*A[2][2]-A[1][2]*A[2][1], -(A[1][0]*A[2][2]-A[1][2]*A[2][0]), A[1][0]*A[2][1]-A[1][1]*A[2][0]],
      [-(A[0][1]*A[2][2]-A[0][2]*A[2][1]), A[0][0]*A[2][2]-A[0][2]*A[2][0], -(A[0][0]*A[2][1]-A[0][1]*A[2][0])],
      [ A[0][1]*A[1][2]-A[0][2]*A[1][1], -(A[0][0]*A[1][2]-A[0][2]*A[1][0]), A[0][0]*A[1][1]-A[0][1]*A[1][0]]]
    return [[C[j][i]/d for j in range(3)] for i in range(3)]

def cube_vertices():
    return [[sx,sy,sz] for sx in (-1.,1.) for sy in (-1.,1.) for sz in (-1.,1.)]

def cube_edges(vertices):
    out=[]
    for i,p in enumerate(vertices):
        for j,q in enumerate(vertices):
            if j<=i: continue
            if sum(abs(p[k]-q[k])>1e-12 for k in range(3))==1:
                out.append((p,q))
    assert len(out)==12
    return out

def section_polygon(vertices, edges, u):
    pts=[]
    for p,q in edges:
        fp=dot(u,p); fq=dot(u,q)
        if abs(fp)<1e-12: pts.append(p)
        if abs(fq)<1e-12: pts.append(q)
        if fp*fq < -1e-14:
            t=fp/(fp-fq)
            pts.append(add(p,mul(t,sub(q,p))))
    uniq=[]
    for p in pts:
        if not any(norm(sub(p,q))<1e-9 for q in uniq): uniq.append(p)
    assert len(uniq)>=3
    cen=[sum(p[k] for p in uniq)/len(uniq) for k in range(3)]
    # orthonormal basis of u-perp
    uu=[x/norm(u) for x in u]
    seed=[1.,0.,0.] if abs(uu[0])<0.8 else [0.,1.,0.]
    e1=cross(uu,seed); e1=[x/norm(e1) for x in e1]
    e2=cross(uu,e1)
    uniq.sort(key=lambda p: math.atan2(dot(sub(p,cen),e2),dot(sub(p,cen),e1)))
    area=0.0
    for i,p in enumerate(uniq):
        q=uniq[(i+1)%len(uniq)]
        area += dot(cross(sub(p,cen),sub(q,cen)),uu)/2
    return abs(area)

def width(vertices,u):
    vals=[dot(u,p) for p in vertices]
    return max(vals)-min(vals)

def cube_formula(u):
    u=[x/norm(u) for x in u]
    a,b,c=sorted([abs(x) for x in u], reverse=True)
    s=a+b+c
    if a >= b+c-1e-13:
        A=4/a
    else:
        A=(2*(a*b+a*c+b*c)-(a*a+b*b+c*c))/(a*b*c)
    return A*s/4, A

V0=cube_vertices(); E0=cube_edges(V0)
random.seed(5202024)
for _ in range(300):
    u=[random.uniform(-1,1) for _ in range(3)]
    if norm(u)<0.1: continue
    u=[x/norm(u) for x in u]
    F,A=cube_formula(u)
    Ag=section_polygon(V0,E0,u)
    Fg=Ag*width(V0,u)/8
    assert abs(A-Ag)<2e-8
    assert abs(F-Fg)<2e-8
    assert 1-1e-12 <= F <= 2.25+1e-12

# Equality checks.
for u,expected in [([1,0,0],1.0),([1,1,0],2.0),([1,1,1],2.25)]:
    F,_=cube_formula(u); assert abs(F-expected)<1e-12

# Directly test affine directional invariance on random parallelotopes by polygon geometry.
for _ in range(120):
    while True:
        A=[[random.uniform(-2,2) for _ in range(3)] for __ in range(3)]
        if abs(det3(A))>0.25: break
    VP=[matvec(A,p) for p in V0]; EP=[(matvec(A,p),matvec(A,q)) for p,q in E0]
    u=[random.uniform(-1,1) for _ in range(3)]; u=[x/norm(u) for x in u]
    areaP=section_polygon(VP,EP,u); wP=width(VP,u); volP=8*abs(det3(A))
    FP=areaP*wP/volP
    Atu=matvec(transpose(A),u); v=[x/norm(Atu) for x in Atu]
    FC,_=cube_formula(v)
    assert abs(FP-FC)<5e-8

print('VERIFY_OK parallelotope Busemann-Petty profile')
