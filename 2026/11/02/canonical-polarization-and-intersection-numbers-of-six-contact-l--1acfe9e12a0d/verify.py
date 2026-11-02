"""Exact checks of six-contact incidence intersection numbers; Python 3 stdlib only."""
from fractions import Fraction
from math import comb

def mul(a,b):
    out={}
    for (h,e),v in a.items():
        for (h2,e2),w in b.items():
            ix=(h+h2,e+e2)
            out[ix]=out.get(ix,0)+v*w
    return {k:v for k,v in out.items() if v}

def power(a,n):
    b={(0,0):1}
    for _ in range(n): b=mul(b,a)
    return b

def integrate(p):
    # P(T_P5) with eta=c1(O(1)); pi_*(eta^(4+i))=s_i(TP5)=(-1)^i*C(5+i,i)*H^i.
    return sum(v*((-1)**(e-4))*comb(5+e-4,e-4) for (h,e),v in p.items() if e>=4 and h+(e-4)==5)

def intersection(d, a, b, c):
    # Integral on F of aH+b*eta cubed, with c unused for compatibility.
    pol=power({(1,0):a,(0,1):b},3)
    for j in range(6): pol=mul(pol,{(1,0):d,(0,1):j})
    return integrate(pol)

def polynomial_pl(d): return 3*d*(d-5)*(5*d**3+25*d**2-100*d+48)
def polynomial_k(d): return 8*d*(58773*d**4-813018*d**3+4047651*d**2-8560324*d+6430320)

def fixed_point_localization(d,a,b):
    # Equivariant Euler localization, independent of projective-bundle Segre calculation.
    weights=[0,1,3,7,12,20]
    total=Fraction(0)
    for i,wi in enumerate(weights):
        for j,wj in enumerate(weights):
            if i==j: continue
            H=-wi
            eta=wi-wj
            e=1
            for k,wk in enumerate(weights):
                if k!=i: e*=wk-wi
                if k!=i and k!=j: e*=wk-wj
            top=(a*H+b*eta)**3
            for u in range(6): top*=d*H+u*eta
            total+=Fraction(top,e)
    assert total.denominator==1
    return int(total)

for d in range(6,28):
    assert intersection(d,2,1,0)==polynomial_pl(d),('pl',d)
    assert intersection(d,6*d-12,10,0)==polynomial_k(d),('k',d)
for d in range(6,15):
    assert fixed_point_localization(d,2,1)==polynomial_pl(d),('local-pl',d)
    assert fixed_point_localization(d,6*d-12,10)==polynomial_k(d),('local-k',d)
assert polynomial_pl(6)==25704
assert polynomial_k(6)==64403136
assert polynomial_pl(7)==96096
assert polynomial_k(7)==397138000
print('VERIFY_OK; 44 Segre + 18 localization checks; examples d=6,7 checked')
