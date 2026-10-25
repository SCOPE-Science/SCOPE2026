"""Independent numerical diagnostics for planar invariant-line long-chord laws.
Scientific statements require their analytic proofs; finite computations are diagnostic.
Requires Python 3 standard library only.
"""
import math
import random

PI=math.pi

def simpson(f,lo,hi,n=100000):
    if n % 2: n+=1
    dx=(hi-lo)/n
    z=f(lo)+f(hi)
    for i in range(1,n):
        z+=(4 if i%2 else 2)*f(lo+i*dx)
    return z*dx/3

def perimeter(a,b):
    return 4*simpson(lambda t: math.hypot(a*math.sin(t),b*math.cos(t)),0,PI/2,8000)

def exact_tail(a,b,eps):
    # Chord direction eta is measured from the major axis.
    P=perimeter(a,b)
    def intercept(eta):
        A=math.cos(eta)**2/a**2+math.sin(eta)**2/b**2
        # A z^2+2Bt z +C t^2 = 1, discriminant controls chord.
        # t is signed perpendicular distance from ellipse center.
        maxsq=a*a*b*b*A*(1-(a-eps/2)**2*A)
        return 2*math.sqrt(max(0,maxsq))
    return simpson(intercept,0,PI,24000)/P

def general_coeff(a,b):
    D=2*a; Rp=b*b/a; Rq=Rp
    assert D>Rp+Rq
    return 2*PI/perimeter(a,b)*math.sqrt(Rp*Rq/(D*(D-Rp-Rq)))

for a,b in ((1.5,1.0),(2.0,1.0),(3.0,2.0)):
    c=general_coeff(a,b)
    ratios=[exact_tail(a,b,e)/(c*e) for e in (.04,.02,.01,.005)]
    assert abs(ratios[-1]-1)<.01,(a,b,ratios)
    print('FIXED_ELLIPSE_DIAMETER_TAIL_OK',a,b,'predicted',round(c,8),'ratios',[round(x,6) for x in ratios])

# Non-perturbative, independent Monte Carlo of actual chord lengths.
random.seed(712319)
a,b=2.0,1.0; eps=.42
P=perimeter(a,b)
N=180000
hit=0; crossed=0
for i in range(N):
    phi=PI*random.random()
    n=(math.cos(phi),math.sin(phi)); v=(-math.sin(phi), math.cos(phi))
    # Sample in [-a,a] and reject non-crossing lines, as in planar Crofton measure.
    t=a*(2*random.random()-1)
    A=v[0]**2/a**2+v[1]**2/b**2
    B=v[0]*n[0]/a**2+v[1]*n[1]/b**2
    C=n[0]**2/a**2+n[1]**2/b**2
    discr=(B*t)**2-A*(C*t*t-1)
    if discr>0:
        crossed+=1
        z1=(-B*t-math.sqrt(discr))/A
        z2=(-B*t+math.sqrt(discr))/A
        if z2-z1>2*a-eps: hit+=1
p_mc=hit/crossed; p_exact=exact_tail(a,b,eps)
assert abs(p_mc-p_exact)<.012,(p_mc,p_exact)
print('INDEPENDENT_QUADRATIC_ROOT_CROFTON_MONTE_CARLO_OK',N,'frequency',round(p_mc,6),'integral',round(p_exact,6))

# Near-circle crossover with a^2=1+lambda, b=1 and lambda/eps -> x.
def crossover(x):
    return simpson(lambda eta: math.sqrt(max(0,1-x*math.sin(eta)**2)),0,PI,18000)/PI
for x in (0,0.25,0.75,1,2,5,12):
    target=crossover(x)
    for eps in (.002,.0005):
        a=math.sqrt(1+x*eps)
        actual=exact_tail(a,1,eps)/math.sqrt(eps)
        assert abs(actual-target)<.012,(x,eps,actual,target)
    print('NEAR_CIRCLE_CROSSOVER_OK',x,round(target,8),round(actual,8))
assert abs(crossover(0)-1)<1e-10
for x in (100,400,1600):
    ratio=2*math.sqrt(x)*crossover(x)
    assert abs(ratio-1)<.01,(x,ratio)
    print('CROSSOVER_LARGE_ARGUMENT_OK',x,round(ratio,8))
print('ALL_CROFTON_DIAMETER_TAIL_DIAGNOSTICS_OK')

# Independently reconstruct a non-elliptic support curve as a convex polygon,
# then integrate long-chord counts directly from boundary-line intersections.
def f(t): return math.cos(2*t)+.3*math.sin(3*t)
def fp(t): return -2*math.sin(2*t)+.9*math.cos(3*t)

def chord_from_edges(vertices,cs,sn,offset):
    # Unlike the perturbative derivation, this uses intersections of edges.
    nx=-sn; ny=cs
    pp=[nx*x+ny*y for x,y in vertices]
    vp=pp[1:]+pp[:1]
    pts=[]
    for i in range(len(vertices)):
        p,q=pp[i],vp[i]
        if (p-offset)*(q-offset)>0 or abs(q-p)<1e-14: continue
        z=(offset-p)/(q-p)
        if 0<=z<=1:
            a=vertices[i];b=vertices[(i+1)%len(vertices)]
            pts.append((a[0]+z*(b[0]-a[0]),a[1]+z*(b[1]-a[1])))
    if len(pts)<2:return 0.0
    vals=[cs*x+sn*y for x,y in pts]
    return max(vals)-min(vals)

# Vertex resolution is high enough that the polygonization error is far below
# the chosen sampling resolution; neither finite test proves the general result.
for eps,x in ((.035,.2),(.025,.35)):
    delta=x*eps
    nv=640
    vs=[]
    for j in range(nv):
        a=2*PI*j/nv
        h=1+delta*f(a); dh=delta*fp(a)
        vs.append((h*math.cos(a)-dh*math.sin(a),h*math.sin(a)+dh*math.cos(a)))
    ntheta=72; nt=241; Tmax=.32
    hit=0
    for j in range(ntheta):
        ang=PI*(j+.5)/ntheta
        cs,sn=math.cos(ang),math.sin(ang)
        for k in range(nt):
            t=Tmax*(2*(k+.5)/nt-1)
            if chord_from_edges(vs,cs,sn,t)>2+2*delta-eps:
                hit+=1
    measured=hit*(PI/ntheta)*(2*Tmax/nt)/(2*PI)
    G=crossover(4*x)
    target=math.sqrt(eps)*G
    assert abs(measured-target)<.012,(eps,x,measured,target)
    print('NONELLIPTIC_SUPPORT_BOUNDARY_CHORD_CROSSOVER_OK',eps,x,round(measured,6),round(target,6))
print('ALL_GENERAL_SUPPORT_CROSSOVER_CHECKS_OK')
