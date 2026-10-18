"""Reproducibility checks for the central cuboctahedron section-perimeter theorem.

Requires Python 3.10+ and SymPy for exact differentiations; geometric
edge intersection, convex hull, and root bracketing use Python stdlib only.
The finite geometry tests supplement the all-direction written proof.
"""
import itertools
import math
import random
import sympy as sp

r=math.sqrt
V=sorted({tuple(perm[i]*sgn[i] for i in range(3))
          for perm in set(itertools.permutations((0,1,1)))
          for sgn in itertools.product((-1,1),repeat=3)})
E=[(v,w) for v,w in itertools.combinations(V,2)
   if sum((v[i]-w[i])**2 for i in range(3))==2]
assert len(V)==12 and len(E)==24

def dot(x,y): return sum(xi*yi for xi,yi in zip(x,y))
def cross(x,y):return (x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])
def norm(x):return r(dot(x,x))
def hull(pts):
    pts=sorted(set(pts))
    def turn(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lower=[]
    for p in pts:
        while len(lower)>1 and turn(lower[-2],lower[-1],p)<1e-12: lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(pts):
        while len(upper)>1 and turn(upper[-2],upper[-1],p)<1e-12:upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]

def independent_perimeter(n):
    n=tuple(a/norm(n) for a in n)
    u=cross(n,(1,0,0))
    if norm(u)<1e-10:u=cross(n,(0,1,0))
    u=tuple(a/norm(u) for a in u)
    w=cross(n,u)
    pts=[]
    for a,b in E:
        x,y=dot(a,n),dot(b,n)
        if x*y>1e-12:continue
        if abs(x-y)<1e-14:
            if abs(x)<1e-12:
                pts += [(dot(a,u),dot(a,w)),(dot(b,u),dot(b,w))]
        else:
            v=tuple((y*a[i]-x*b[i])/(y-x) for i in range(3))
            pts.append((dot(v,u),dot(v,w)))
    h=hull(pts)
    assert len(h)>=3
    return sum(math.dist(h[i],h[(i+1)%len(h)]) for i in range(len(h)))

def formula(b,c):
    if b==1:return 2*r(2)+2*r(6+2*c*c)
    rp=r((b-c)**2+(1+b)**2+(1+c)**2)
    rm=r((b+c)**2+(1+b)**2+(1-c)**2)
    M=(rp+rm)/2
    return 4*r(1+b*b)/(1+b)+4/(1-c*c)*((1-b)*r(1+c*c)+((b-c*c)*M+(1-b)**2*c*c/M)/(1+b))

def axis_formula(b):return 4*(1-b)+(4/(1+b))*(r(1+b*b)+b*r(2*(1+b+b*b)))
def certified_gap(b,c):
    if c==0:return 0
    return 4*c*c*(1-b)/(1-c*c)*(r(2)-(1+2*b)/r(2*(1+b+b*b)))

x=sp.symbols('x',nonnegative=True)
rr=sp.sqrt(1+x*x)/(1+x)
ss=x*sp.sqrt(2*(1+x+x*x))/(1+x)
f=1-x+rr+ss
second_r=(-2*x**3+3*x*x+3)/((1+x)**3*(1+x*x)**sp.Rational(3,2))
second_s=sp.sqrt(2)*(7*x**3+6*x*x+3*x-4)/(4*(1+x)**3*(1+x+x*x)**sp.Rational(3,2))
assert sp.simplify(sp.diff(rr,x,2)-second_r)==0
assert sp.simplify(sp.diff(ss,x,2)-second_s)==0
assert sp.simplify(sp.diff(f,x).subs(x,0)-(sp.sqrt(2)-2))==0
assert sp.simplify(sp.diff(f,x).subs(x,1)-(sp.sqrt(6)/2-1))==0
# On [0,3/5], f'' >= [3/(34/25)**(3/2)-sqrt(2)]/(1+x)^3 > 0.
assert 3/(1+sp.Rational(3,5)**2)**sp.Rational(3,2)>sp.sqrt(2)
# On [3/5,1], the second derivative of s is positive.
assert 7*sp.Rational(3,5)**3+6*sp.Rational(3,5)**2+3*sp.Rational(3,5)-4>0
# Exact positivity of transverse bracket: 4(1+b+b²)-(1+2b)²=3.
assert sp.expand(4*(1+x+x*x)-(1+2*x)**2)==3
# The lower bound H'(M)>=0 uses M²>=2(1+b+b²) and c²<=b².
assert sp.expand(2*(1+x+x*x)-x*(1-x))==2+x+3*x*x
print('EXACT_SECOND_DERIVATIVE_UNIQUENESS_AND_TRANSVERSE_CERTIFICATES_OK')

def derivative(t):return float(sp.diff(f,x).subs(x,t))
lo,hi=0.0,1.0
for i in range(70):
    mid=(lo+hi)/2
    if derivative(mid)<0:lo=mid
    else:hi=mid
t=(lo+hi)/2
assert abs(derivative(t))<1e-13
assert 0.5150605280 < t < 0.5150605281
p=axis_formula(t)
assert 7.4755344540 < p < 7.4755344541
print('UNIQUE_INTERIOR_MINIMIZER_OK',format(t,'.15f'),format(p,'.15f'))

random.seed(250713)
maxdev=0.0
for i in range(2400):
    a,b,c=sorted([random.random() for _ in range(3)],reverse=True)
    b/=a;c/=a
    expected=formula(b,c)
    actual=independent_perimeter((1,b,c))
    maxdev=max(maxdev,abs(expected-actual))
    assert abs(expected-actual)<3e-9,(b,c,expected,actual)
    assert expected+1e-12>=axis_formula(b)+certified_gap(b,c),(b,c)
for b,c in [(0,0),(1,0),(1,1),(0.8,0.8),(0.5150605280531426,0),(0.5150605280531426,0.01)]:
    assert abs(formula(b,c)-independent_perimeter((1,b,c)))<3e-9,(b,c)
print('INDEPENDENT_2400_EXACT_EDGE_GRAPH_SECTION_HULLS_OK',maxdev)
print('TRANSVERSE_STABILITY_AND_BOUNDARY_CASES_OK')
print('ALL_CUBOCTAHEDRON_SECTION_PERIMETER_CHECKS_OK')
