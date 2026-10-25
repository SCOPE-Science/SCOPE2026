"""Reproduce area formulas, sectional geometry and asymptotic constants for a circular double cone.
Requires Python 3, mpmath>=1.2. Numerical tests do not replace analytic proof.
"""
import mpmath as mp
mp.mp.dps=95

def F(x):
    x=mp.mpf(x)
    if x==0: return mp.mpf('0.5')
    if x<1:
        z=mp.sqrt(1-x*x)
        return (1-x*x*mp.atanh(z)/z)/(2*(1-x*x))
    if x==1: return mp.mpf(1)/3
    z=mp.sqrt(x*x-1)
    return (x*x*mp.atan(z)/z-1)/(2*(x*x-1))

def I_closed(x): return -mp.diff(F,x)/x

def area_formula(k,x): return 4*mp.sqrt(k*k+x*x)*F(x)

def area_cartesian(k,c):
    a=mp.sqrt(1-c*c)/k
    b=c
    t=1/(a+b)
    return 4*mp.quad(lambda v:mp.sqrt(max(mp.mpf(0),(1-(a+b)*t*v)*(1-(a-b)*t*v)))*t,[0,1])

def closest(a,b,tol=mp.mpf('1e-60')):
    if abs(a-b)>tol*max(mp.mpf(1),abs(a),abs(b)):
        raise AssertionError((mp.nstr(a,25),mp.nstr(b,25)))

for s in ['.05','.2','.5','2']:
    x=mp.mpf(s)
    F_integral=mp.quad(lambda v:mp.sqrt(v*v-x*x)/(1+v)**3,[x,2*x,mp.inf])
    closest(F(x),F_integral,mp.mpf('1e-65'))
    I_integral=mp.quad(lambda v:(1+x*mp.cosh(v))**(-3),[0,mp.inf])
    closest(I_closed(x),I_integral,mp.mpf('1e-65'))
print('INDEPENDENT_INTEGRAL_AND_DERIVATIVE_IDENTITY_OK',4)

for k,c in [('.25','.1'),('.25','.7'),('.5','.45'),('.5','.95'),('1','.4'),('1','.9'),('2','.1'),('2','.85'),('4','.75')]:
    k=mp.mpf(k);c=mp.mpf(c)
    x=k*c/mp.sqrt(1-c*c)
    closest(area_formula(k,x),area_cartesian(k,c),mp.mpf('1e-64'))
print('INDEPENDENT_CARTESIAN_PLANE_SECTION_CHECKS_OK',9)

def optimum_small_k(k):
    asymp=2*mp.exp(-mp.mpf('1.5')-1/(2*k*k))
    derivsign=lambda x:F(x)-(k*k+x*x)*I_closed(x)
    left=asymp/mp.mpf(10);right=asymp*10
    assert derivsign(left)<0<derivsign(right)
    for j in range(154):
        mid=(left+right)/2
        if derivsign(mid)>0:right=mid
        else:left=mid
    return (left+right)/2

for kstring in ['.4','.35','.3','.25','.2','.15','.1']:
    k=mp.mpf(kstring)
    x=optimum_small_k(k)
    predicted_x=2*mp.exp(-mp.mpf('1.5')-1/(2*k*k))
    deficit=2*k-area_formula(k,x)
    predicted_deficit=4*k*mp.exp(-3-1/(k*k))
    assert deficit>0
    if k<=mp.mpf('.35'):
        assert abs(x/predicted_x-1)<mp.mpf('.005')
        assert abs(deficit/predicted_deficit-1)<mp.mpf('.005')
    print('ASYMPTOTIC_RATIO',str(k),mp.nstr(x/predicted_x,12),mp.nstr(deficit/predicted_deficit,12))
print('ALL_BICONE_CENTRAL_SECTION_CHECKS_OK')
