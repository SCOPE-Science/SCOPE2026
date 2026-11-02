"""Supplementary arithmetic checks for explicit Fock coherent-state overlap hull geometry.
This finite test does not substitute for the proof in RESULT.md.
"""
import math
import cmath

N=0

def check(statement, label):
    global N
    N += 1
    if not statement:
        raise AssertionError(label)

def root(k):
    left,right=math.pi,2*math.pi
    for _ in range(100):
        m=(left+right)/2
        g=math.cos(m)-k*math.sin(m)-math.exp(-k*m)
        if g>0:right=m
        else:left=m
    return (left+right)/2

def area(k,t):
    r=math.exp(-k*t)
    return -math.expm1(-2*k*t)/(4*k)-r*math.sin(t)/2

def perim(k,t):
    return math.sqrt(1+k*k)*(-math.expm1(-k*t))/k+abs(1-cmath.exp((-k+1j)*t))

for k in (0.001,0.01,0.1,0.5,1.0,2.0,5.0,12.0):
    t=root(k)
    check(math.pi<t<2*math.pi,'root interval')
    check(abs(math.cos(t)-k*math.sin(t)-math.exp(-k*t))<1e-12,'tangency')
    ak=area(k,t)
    check(0<ak<math.pi,'area bounds')
    check(perim(k,t)>2,'perimeter')
    z=cmath.exp((-k+1j)*t)
    check(abs(((1-z)*((-k-1j)*z.conjugate())).imag)<1e-10,'chord tangent ratio')
    # Numerical exposure: for all arc normals (outward sign), entire later spiral is dominated.
    for m in range(1,100):
        u=t*m/100
        w=cmath.exp((-k+1j)*u)
        # tangent = (-k+i)w; outward normal: -i tangent for CCW arc
        n=-1j*(-k+1j)*w
        n/=abs(n)
        target=(w*n.conjugate()).real
        endpoint=(1*n.conjugate()).real
        check(target+1e-10>=endpoint,'arc beats initial point')
        for j in range(151):
            v=j*(t+4*math.pi)/150
            candidate=cmath.exp((-k+1j)*v)
            check(target+1e-10>=(candidate*n.conjugate()).real,'all-spiral support')
    # Coarse polygon area from spiral path and closing segment vs Green integral.
    sampled=[cmath.exp((-k+1j)*t*j/25000) for j in range(25001)]
    shoelace=sum((sampled[j].conjugate()*sampled[j+1]).imag for j in range(len(sampled)-1))/2
    shoelace+=(sampled[-1].conjugate()*sampled[0]).imag/2
    check(abs(ak-shoelace)<4e-8,'sampled Green area')

# Monotone exact hull areas and limiting scaling benchmarks.
ks=[0.01,0.03,0.1,0.5,1,2,5,10]
areas=[area(k,root(k)) for k in ks]
for x,y in zip(areas,areas[1:]):check(x>y,'strict nesting area')
for k in (0.0001,0.000025,0.00000625):
    check(abs((math.pi-area(k,root(k)))/k-2*math.pi**2)<1.4,'small k area')
for k in (3,5,7,10):
    check(abs(4*k*area(k,root(k))-1)<0.025,'large k area')
print('CHECK_OK',N)
