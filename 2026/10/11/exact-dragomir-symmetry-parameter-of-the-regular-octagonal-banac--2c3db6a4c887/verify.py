import math
import sympy as sp

s2=sp.sqrt(2)
r=s2-1
d0=1/(1+r**2)
eps=sp.sqrt(1-d0**2)

assert sp.simplify(d0-(2+s2)/4)==0
assert sp.simplify(eps**2-(5-2*s2)/8)==0
q=sp.symbols('q', real=True)
assert sp.simplify(s2*(1+r*q)-(1+q)-r*(1-q))==0

SQ2=math.sqrt(2.0)
R=SQ2-1.0
D0=(2.0+SQ2)/4.0
EPS=math.sqrt((5.0-2.0*SQ2)/8.0)

verts=[
    (1.0,R),(R,1.0),(-R,1.0),(-1.0,R),
    (-1.0,-R),(-R,-1.0),(R,-1.0),(1.0,-R)
]

def N(v):
    a,b=v
    return max(abs(a),abs(b),(abs(a)+abs(b))/SQ2)

def dual_det_norm(x):
    a,b=x
    return max(abs(a*v[1]-b*v[0]) for v in verts)

def dist(y,x):
    num=abs(x[0]*y[1]-x[1]*y[0])
    return num/dual_det_norm(x)

edge_checks=0
for k in range(4001):
    t=-R+2.0*R*k/4000.0
    x=(1.0,t)
    if k not in (0,4000):
        y=(0.0,-1.0)
        assert abs(N(x)-1.0)<1e-12 and abs(N(y)-1.0)<1e-12
        assert dist(y,x)>=D0-2e-12
        edge_checks+=1

cone_checks=0
x=(1.0,R)
for k in range(4001):
    qv=k/4000.0
    raw=(qv,-1.0)
    nv=N(raw)
    y=(raw[0]/nv,raw[1]/nv)
    assert abs(N(y)-1.0)<2e-12
    assert dist(y,x)>=D0-2e-12
    cone_checks+=1

y=(0.0,-1.0)
assert abs(dist(y,x)-D0)<2e-12
assert abs(math.sqrt(1.0-D0*D0)-EPS)<2e-12

print(
    "VERIFY_OK "
    f"edge_checks={edge_checks} cone_checks={cone_checks} "
    f"d0={D0:.15f} sigmaD={EPS:.15f}"
)
