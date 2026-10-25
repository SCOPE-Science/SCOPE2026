"""Direct geometric and Fourier checks of random bounding-rectangle perimeter.
Run: python3 verify.py. Standard library only; finite checks do not prove the theorem.
"""
from __future__ import annotations
import cmath
import math

PI = math.pi

def polygon_data(vertices):
    edges=[]
    for a,b in zip(vertices, vertices[1:]+vertices[:1]):
        dx=b[0]-a[0];dy=b[1]-a[1]
        l=math.hypot(dx,dy)
        if l <= 0: raise ValueError('duplicate consecutive vertices')
        edges.append((l,math.atan2(dy,dx)))
    perimeter=sum(l for l,_ in edges)
    return perimeter, [(l/perimeter,theta) for l,theta in edges]

def bbox_ratio_vertices(vertices, theta, perimeter):
    c=math.cos(theta);s=math.sin(theta)
    x=[a*c+b*s for a,b in vertices]
    y=[-a*s+b*c for a,b in vertices]
    return 2*((max(x)-min(x))+(max(y)-min(y)))/perimeter

def bbox_ratio_edges(edges, theta):
    return sum(w*(abs(math.cos(theta-a))+abs(math.sin(theta-a))) for w,a in edges)

def variance_spectral(edges,nmax=1500):
    return 32/PI**2*sum(abs(sum(w*cmath.exp(4j*k*a) for w,a in edges))**2/(16*k*k-1)**2 for k in range(1,nmax+1))

def mean(xs): return sum(xs)/len(xs)

def var(xs):
    a=mean(xs)
    return mean([x*x for x in xs])-a*a

def convex_risk(xs):
    return (mean([x**4 for x in xs]),mean([math.exp(2*x) for x in xs]),
        *[mean([max(0.,x-t) for x in xs]) for t in (1.05,1.15,1.3,1.4)])

def coh(edges):
    return sum(w*v*math.sin(2*(a-b))**2 for w,a in edges for v,b in edges)

def assert_close(a,b,tol,label):
    if abs(a-b)>tol: raise AssertionError((label,a,b,abs(a-b),tol))

polygons={
    'rectangle': [(0.,0.),(2.,0.),(2.,1.),(0.,1.)],
    'sheared_parallelogram': [(0.,0.),(2.,0.),(2.7,1.),(0.7,1.)],
    'triangle': [(0.,0.),(2.,0.),(0.5,1.7)],
    'pentagon':[(0.,0.),(2.,-.2),(3.,1.),(1.6,2.8),(-.4,1.5)],
    'regular_19gon': [(math.cos(2*PI*j/19),math.sin(2*PI*j/19)) for j in range(19)],
}
N=16384
th=[j*PI/(2*N) for j in range(N)]
ref=[math.cos(t)+math.sin(t) for t in th]
refmean=4/PI
refvar=1+2/PI-16/PI**2
assert_close(mean(ref),refmean,3e-9,'reference_mean')
assert_close(var(ref),refvar,3e-9,'reference_variance')
ref_risks=convex_risk(ref)
for key,vertices in polygons.items():
    perim,edges=polygon_data(vertices)
    values=[]
    for t in th:
        x=bbox_ratio_vertices(vertices,t,perim)
        y=bbox_ratio_edges(edges,t)
        assert_close(x,y,5e-13,key+'_direct_geometry')
        values.append(x)
    assert_close(mean(values),refmean,1e-7,key+'_mean')
    numervar=var(values)
    exactvar=variance_spectral(edges)
    assert_close(numervar,exactvar,4e-8,key+'_spectral')
    if numervar>refvar+1e-9: raise AssertionError((key,'variance_bound'))
    deficit=refvar-exactvar
    lower=(64/(225*PI*PI))*coh(edges)
    if deficit+1e-9<lower: raise AssertionError((key,'stability',deficit,lower))
    risks=convex_risk(values)
    for a,b in zip(risks,ref_risks):
        if a>b+1e-9: raise AssertionError((key,'convex_order',a,b))
    if key=='rectangle': assert_close(exactvar,refvar,3e-12,key+'_sharp')
    else:
        if not exactvar<refvar-1e-5: raise AssertionError((key,'rigidity'))
print('DIRECT_ROTATED_VERTEX_SUPPORT_VS_TANGENT_INTEGRAL_OK',len(polygons)*N)
print('FOURIER_VARIANCE_COVARIANCE_IDENTITY_OK',len(polygons))
print('SHARP_RECTANGLE_EQUALITY_AND_NONRECTANGLE_STRICTNESS_OK')
print('UNIVERSAL_CONVEX_RISK_COMPARISON_OK',len(ref_risks))
print('POSITIVE_STABILITY_DEFECT_FOR_NONRECTANGLES_OK')
# Deterministic exact law's survival inversion, using another numerical integration.
for t in (1.05,1.15,1.3,1.4):
    empirical=sum(z>t for z in ref)/N
    formula=4/PI*math.acos(t/math.sqrt(2))
    assert_close(empirical,formula,1.2/N,'rectangular_survival')
print('RECTANGLE_ALL_THRESHOLD_CDF_FORMULA_CHECK_OK')
# Exact equilateral triangle spectrum keeps only the 12k modes in B/P.
triv=32/PI**2*sum(1/(144*m*m-1)**2 for m in range(1,10000))
tri=[(0,0),(1,0),(.5,math.sqrt(3)/2)]
_,ed=polygon_data(tri)
assert_close(triv,variance_spectral(ed),1e-12,'equilateral_spectrum')
assert 0<triv<refvar
print('EQUILATERAL_TRIANGLE_TWELVEFOLD_SPECTRUM_OK')
print('ALL_BOUNDING_RECTANGLE_PERIMETER_CHECKS_OK')
