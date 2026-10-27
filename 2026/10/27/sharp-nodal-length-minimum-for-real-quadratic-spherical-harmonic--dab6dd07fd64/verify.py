"""Reproducible exact identities and independent numerical nodal-arclength check."""
import math
import sympy as S
from scipy.integrate import quad

d,v=S.symbols('d v', real=True)
s=(1-d*d)/4
k=(1-d*d*v*v)/4
assert S.simplify(2*k-s-4*s*s-d*d*(3-2*v*v-d*d)/4)==0
assert S.simplify(5*k-4*s*(1+s)-d*d*(6-5*v*v-d*d)/4)==0
print('Two symbolic pairwise deficit identities: exact PASS')

def length_crofton(a):
    s=a*(1-a)
    def h(phi):
        u=(1-a)*math.cos(phi)**2 + a*math.sin(phi)**2
        return math.sqrt(u/(u+s)) if u+s>0 else 1
    return 2*quad(h,0,2*math.pi,epsabs=2e-12)[0]

def length_curve(a):
    def ds(phi):
        b=a+(1-2*a)*math.sin(phi)**2
        bp=(1-2*a)*math.sin(2*phi)
        if b==0:
            return math.sqrt(2)/(1+math.sin(phi)**2)
        return math.sqrt(1/(1+b)+bp*bp/(4*b*(1+b)**2))
    return 2*quad(ds,0,2*math.pi,epsabs=1e-11)[0]

for a in (0,.001,.01,.1,.25,.4,.499, .5):
    c=length_crofton(a)
    independent=length_curve(a)
    assert abs(c-independent)<2e-7,(a,c,independent)
    assert 4*math.pi*math.sqrt(2/3)-1e-8<=c<=4*math.pi+1e-8
    print(f'a={a:g}; crofton={c:.12f}; direct_arclength={independent:.12f}')
assert abs(length_crofton(.5)-4*math.pi*math.sqrt(2/3))<1e-10
assert abs(length_crofton(0)-4*math.pi)<1e-10
print('Numerical independent curve arclength comparisons: PASS (8 parameter samples)')
