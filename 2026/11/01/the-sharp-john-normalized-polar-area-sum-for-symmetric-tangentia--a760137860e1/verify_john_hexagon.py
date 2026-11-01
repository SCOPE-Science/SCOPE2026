"""Independent elementary and numerical consistency checks for the normalized
area-plus-polar-area profile of centrally symmetric tangential hexagons.
Run: python3 verify_john_hexagon.py
Python 3 standard library and SymPy required. All universal claims have
separate analytic proofs; finite tests are not substituted for proofs.
"""
import math
import random
import sympy as sp

checks = 0

def check(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)

SQ2 = sp.sqrt(2)
T = 5*SQ2-1
x = sp.symbols('x', real=True)
f = sp.tan(x/2) + sp.sin(x)/2
fp = sp.diff(f,x)
fpp = sp.diff(fp,x)
check(sp.simplify(fp-(1/(1+sp.cos(x))+sp.cos(x)/2))==0, 'first derivative')
check(sp.simplify(fpp-sp.sin(x)*(1/(1+sp.cos(x))**2-sp.Rational(1,2)))==0, 'second derivative')
check(sp.simplify(2*(f.subs(x,sp.pi/2)+2*f.subs(x,sp.pi/4))-T)==0,'sharp angle value')
check(sp.simplify(2*(3*f.subs(x,sp.pi/3))-7*sp.sqrt(3)/2)==0,'regular hexagon value')
check(sp.simplify(2*(2*f.subs(x,sp.pi/2)+f.subs(x,0))-6)==0,'square boundary')
check(sp.simplify(2*(fp.subs(x,sp.pi/2)-fp.subs(x,sp.pi/4))-(-2+3*SQ2/2))==0,'linear boundary deficit')
check(sp.simplify(-2*fpp.subs(x,sp.pi/4)-(8-sp.Rational(11,2)*SQ2))==0,'quadratic boundary deficit')
check(sp.N(T) > sp.N(7*sp.sqrt(3)/2) > 6, 'strict comparisons')

v=(sp.sqrt(5)-1)/2
check(sp.simplify((1-v)*(1+v)**2-1)==0,'interior stationary equation')
check(sp.simplify(2*sp.sqrt(v)*(sp.Rational(3,2)-2*v))>0,'interior saddle direction')
check(sp.simplify(v**2+v-1)==0,'golden equation')

# The extremal body: square with two opposite corners cut off.
areaK=4*SQ2-2
areaPolar=1+SQ2
check(sp.simplify(areaK+areaPolar-T)==0,'geometric extremal sum')
check(sp.simplify(2*(sp.tan(sp.pi/4)+2*sp.tan(sp.pi/8))-areaK)==0,'extremal K area')
check(sp.simplify(sp.sin(sp.pi/2)+2*sp.sin(sp.pi/4)-areaPolar)==0,'extremal polar area')


def sf(t):
    return math.tan(t/2)+0.5*math.sin(t)


def solve2(u, v):
    # Intersect the two supporting lines u.dot(x) = 1, v.dot(x) = 1.
    det=u[0]*v[1]-u[1]*v[0]
    return ((v[1]-u[1])/det,(u[0]-v[0])/det)


def polygon_area(points):
    return abs(sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(points,points[1:]+points[:1])))/2


def independent_areas(a,b,c):
    phi=[0.0,a,a+b,math.pi,math.pi+a,math.pi+a+b]
    normals=[(math.cos(t),math.sin(t)) for t in phi]
    vertices=[solve2(normals[i],normals[(i+1)%6]) for i in range(6)]
    return polygon_area(vertices),polygon_area(normals),vertices

rng=random.Random(271828)
for i in range(25000):
    while True:
        raw=[rng.random()+1e-4 for j in range(3)]
        g=[math.pi*t/sum(raw) for t in raw]
        if max(g) < math.pi/2-2e-6 and min(g)>1e-6:
            break
    a,b,c=g
    k,pol,verts=independent_areas(a,b,c)
    k_formula=2*sum(math.tan(t/2) for t in g)
    pol_formula=sum(math.sin(t) for t in g)
    check(abs(k-k_formula)<2e-9,'shoelace/support K area')
    check(abs(pol-pol_formula)<2e-9,'shoelace/polar area')
    objective=k+pol
    check(objective <=float(T)+3e-12,'global upper check')
    check(objective>6-3e-12,'global lower check')
    if i < 1000:
        # Check John symmetric contact decomposition by three weights
        mat=sp.Matrix([[1.,1.,1.],
                       [math.cos(0),math.cos(2*a),math.cos(2*(a+b))],
                       [math.sin(0),math.sin(2*a),math.sin(2*(a+b))]])
        lam=mat.inv()*sp.Matrix([2.,0.,0.])
        check(min(float(z) for z in lam)>-1e-8,'John weights nonnegative')

for i in range(1000):
    a=math.pi/2
    b=(math.pi/2)*rng.random()
    c=math.pi/2-b
    z=math.tan(b/2)+math.tan(c/2)
    check(abs(sf(b)+sf(c)-(z+1/z-0.5))<1e-12,'boundary identity')
    check(z>=2*(math.sqrt(2)-1)-1e-12,'boundary z min')
    check(2*(sf(a)+sf(b)+sf(c))<=float(T)+1e-12,'boundary optimum')

for n in range(1,200):
    eta=1e-3/(n+1)
    delta=2e-3/(n+1)
    a=math.pi/2-eta
    b=math.pi/4+eta/2+delta
    c=math.pi/4+eta/2-delta
    deficit=float(T)-2*(sf(a)+sf(b)+sf(c))
    approximation=(1.5*math.sqrt(2)-2)*eta+(8-5.5*math.sqrt(2))*delta**2
    check(deficit > 0, 'local deficit nonnegative')
    check(abs(deficit-approximation)<4*(eta*eta+eta*delta*delta+delta**4),'local expansion error')

print(f'PASS: {checks} independent symbolic, deterministic geometric, and boundary checks')
print(f'Sharp upper area sum {float(T):.15f}; normalized {float(T)/math.pi:.15f}')
print(f'Regular tangent hexagon sum {7*math.sqrt(3)/2:.15f}; square boundary 6')
