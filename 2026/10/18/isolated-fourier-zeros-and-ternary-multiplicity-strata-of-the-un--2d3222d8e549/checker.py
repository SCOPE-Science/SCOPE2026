"""Independent checks for exact Fourier zeros of the uniform eight-digit Sierpinski carpet.
All infinite assertions are proved analytically in RESULT.md; this script supplies finite exact/numerical cross-checks.
Run: python checker.py
"""
from math import gcd, pi, cos, sin
import cmath
import sympy as sp
from mpmath import mp

z = sp.Symbol('z')
# For primitive order 2*3^h roots, the positive-oval equation
# (1+z+z^-1)(1+z^r+z^-r)=1 has no solutions.
tested = 0
for h in range(1, 5):
    n = 2 * 3**h
    cyclo = sp.Poly(sp.cyclotomic_poly(n, z), z, domain=sp.ZZ)
    # reduce a Laurent polynomial via multiplication by a monomial.
    for r in range(1, n):
        if gcd(r,n)!=1: continue
        poly = sp.Poly((1+z+z*z)*(1+z**r+z**(2*r)) - z**(r+1), z, domain=sp.ZZ)
        assert sp.gcd(poly,cyclo).degree()==0, (h,r)
        tested+=1
print('Exact cyclotomic mask-zero exclusions:',tested,'PASS')

mp.dps = 90
def mask(a,b):
    return (mp.e**(-2j*mp.pi*(a+b)) *
            ((1+2*mp.cos(2*mp.pi*a))*(1+2*mp.cos(2*mp.pi*b))-1)/8)

def transform(a,b,depth=70):
    res=mp.mpc(1)
    for j in range(1,depth+1):
        res*=mask(a/mp.power(3,j),b/mp.power(3,j))
    return res

def val3(u):
    u=abs(int(u))
    assert u%2==1
    j=0
    while u%3==0:
        j+=1;u//=3
    return j

nodes=[(1,1),(3,1),(3,3),(9,3),(9,9),(27,9),(5,15),(7,9)]
for u,v in nodes:
    a=mp.mpf(3*u)/2;b=mp.mpf(3*v)/2
    r=1+min(val3(u),val3(v))
    for j in range(1,r+1):
        av=a/mp.power(3,j); bv=b/mp.power(3,j)
        assert abs(mp.cos(2*mp.pi*av)+1)<mp.mpf('1e-75')
        assert abs(mp.cos(2*mp.pi*bv)+1)<mp.mpf('1e-75')
    for j in range(r+1,25):
        assert abs(mask(a/mp.power(3,j),b/mp.power(3,j)))>mp.mpf('1e-14'),(u,v,j)
    ratios=[]
    for delta in [mp.mpf('0.01'),mp.mpf('0.005'),mp.mpf('0.0025')]:
        ratios.append(transform(a+delta,b)/delta**(2*r))
    reldifference=abs(ratios[-1]/ratios[-2]-1)
    assert reldifference<mp.mpf('0.02'),(u,v,mp.nstr(reldifference,8))
    # The image of a small loop never circles the origin (index zero).
    phases=[]
    samples=160
    for i in range(samples+1):
        t=2*mp.pi*i/samples
        val=transform(a+mp.mpf('0.02')*mp.cos(t),b+mp.mpf('0.02')*mp.sin(t),26)
        phases.append(mp.arg(val))
    winding = sum(float(mp.arg(mp.e**(1j*(phases[i+1]-phases[i])))) for i in range(samples))/(2*pi)
    assert abs(winding)<1e-7,(u,v,winding)
    print('node',u,v,'order',2*r,'winding',round(winding,9),'local-ratio-error',mp.nstr(reldifference,4))

# Check exact multiplicity-shell identity by integer point enumeration.
for L in [20,100,300]:
    from collections import Counter
    counts=Counter()
    # Enumerate odd integer u,v yielding xi=(3u/2,3v/2).
    lim=int(2*L/3)+2
    odd=[u for u in range(-lim,lim+1) if u%2]
    for u in odd:
        for v in odd:
            if 9*(u*u+v*v) <= 4*L*L:
                counts[2*(1+min(val3(u),val3(v)))]+=1
    total=sum(counts.values())
    def N(R):
        # Direct count of isolated nodes at radius R.
        return sum(9*(u*u+v*v)<=4*R*R for u in odd for v in odd)
    for order,c in counts.items():
        r=order//2
        assert c==N(L/3**(r-1))-N(L/3**r),(L,r,c)
    print('radius',L,'isolated zeros',total,'order counts',dict(sorted(counts.items())))
print('All checks PASS')
