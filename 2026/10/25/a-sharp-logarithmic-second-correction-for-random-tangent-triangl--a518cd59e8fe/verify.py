"""Numerical diagnostics for the area tail of the unit-incircle tangent triangle.
These numerical tests supplement, and do not substitute for, the proof.
Requires Python 3, NumPy and SciPy.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import expit

PI = math.pi
L = PI / 2

def m(b):
    return 1 / math.tan(b) + 2 / math.tan((L - b) / 2)

def tail_by_exact_1d_integral(t):
    assert t > 3 * math.sqrt(3)
    blo = brentq(lambda b: m(b)-t, 1e-14, L/3)
    bhi = brentq(lambda b: m(b)-t, L/3, L - 1e-14)
    def width(b):
        q = math.sin(b) + 2 * math.cos(b) / (t-1/math.tan(b))
        return L-b-math.acos(min(1.,max(-1.,q)))
    area = L*blo - blo*blo/2 + (L-bhi)**2/2
    area += quad(width,blo,bhi,epsabs=1e-13,epsrel=2e-12,limit=500)[0]
    return area * 2 / L**2

def asymptotic_tail(t):
    return 12/(PI*t) + (48*math.log(t)-12)/(PI**2*t**2)

def geometric_area(a,b,c):
    gaps = [PI-2*a, PI-2*b, PI-2*c]
    normals = np.cumsum([0.,gaps[0],gaps[1]])
    vectors = np.stack([np.cos(normals),np.sin(normals)],axis=1)
    verts = []
    for i in range(3):
        verts.append(np.linalg.solve(np.array([vectors[i],vectors[(i+1)%3]]), np.ones(2)))
    verts=np.asarray(verts)
    return 0.5*abs(np.dot(verts[:,0],np.roll(verts[:,1],-1))-np.dot(verts[:,1],np.roll(verts[:,0],-1)))

rng=np.random.default_rng(9271101)
for _ in range(1000):
    z=rng.dirichlet([1,1,1])*L
    if min(z)<0.04: continue
    area_geom=geometric_area(*z)
    area_formula=sum(1/math.tan(x) for x in z)
    assert abs(area_geom-area_formula)<1e-9*max(1,area_geom)
print('DIRECT_THREE_TANGENT_HALFPLANE_AREA_IDENTITY_OK')

N=2**19
sp=rng.dirichlet([1.,1.,1.],size=N)*L
samples=(1/np.tan(sp)).sum(axis=1)
for t in [20.,50.,100.]:
    exact=tail_by_exact_1d_integral(t)
    empirical=np.mean(samples>t)
    sigma=math.sqrt(exact*(1-exact)/N)
    assert abs(empirical-exact)<7*sigma
    print('UNIFORM_CONDITIONAL_ANGLES_MC_OK',int(t),round(exact,9),round(empirical,9))

for t in [150.,300.,600.,1000.,2000.,5000.,10000.]:
    exact=tail_by_exact_1d_integral(t)
    pred=asymptotic_tail(t)
    resid=(exact-pred)*t*t
    assert abs(resid)<0.012
    print('SHARP_TWO_TERM_TAIL_REMAINDER_OK',int(t),round(resid,9))

# The renormalized constant must approach -12/pi^2, not merely remain bounded.
constant=[]
for t in (500.,1000.,2000.,5000.,10000.):
    exact=tail_by_exact_1d_integral(t)
    val=(exact-12/(PI*t))*t*t-(48/PI**2)*math.log(t)
    constant.append(val)
assert max(abs(v+12/PI**2) for v in constant[-3:])<1e-3
print('LOGARITHMIC_CORRECTION_AND_EXACT_CONSTANT_OK',round(constant[-1],9))
print('ALL_RANDOM_TANGENT_TRIANGLE_TAIL_CHECKS_OK')
