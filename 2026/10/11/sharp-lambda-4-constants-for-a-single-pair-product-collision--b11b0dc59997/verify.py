#!/usr/bin/env python3
import cmath, math, random
from fractions import Fraction

rng=random.Random(431946)

# Exact algebra behind the three cases.
for _ in range(1000):
    u=Fraction(rng.randrange(0,50), rng.randrange(1,25))
    v=Fraction(rng.randrange(0,50), rng.randrange(1,25))
    lhs=-u*u/Fraction(2)-v*v+2*u*v
    rhs=(u+v)*(u+v)/7-(3*u-4*v)*(3*u-4*v)/14
    assert lhs==rhs
assert Fraction(2,1)==Fraction(2,1)
assert 2 + Fraction(1,7)==Fraction(15,7)
assert 2 + Fraction(1,4)==Fraction(9,4)

def fibers(freqs, mods):
    d={}
    for i in range(len(freqs)):
        for j in range(i,len(freqs)):
            key=tuple((freqs[i][r]+freqs[j][r])%mods[r] for r in range(len(mods)))
            d.setdefault(key,[]).append((i,j))
    return [v for v in d.values() if len(v)>1]

cases=[
 ('A',[(0,0),(1,0),(0,1)],(2,11),2.0),
 ('B',[(0,),(1,),(2,)],(17,),15/7),
 ('C',[(0,0),(1,0),(0,1),(1,1)],(7,7),9/4),
]
assert fibers(cases[0][1],cases[0][2])==[[(0,0),(1,1)]]
assert fibers(cases[1][1],cases[1][2])==[[(0,2),(1,1)]]
assert fibers(cases[2][1],cases[2][2])==[[(0,3),(1,2)]]

def direct_moment(freqs,mods,a):
    total=0.0
    pts=1
    for q in mods: pts*=q
    # mixed radix enumeration
    for z in range(pts):
        zz=z; x=[]
        for q in mods:
            x.append(zz%q); zz//=q
        F=0j
        for c,f in zip(a,freqs):
            phase=sum(f[r]*x[r]/mods[r] for r in range(len(mods)))
            F += c*cmath.exp(2j*math.pi*phase)
        total += abs(F)**4
    return total/pts

def predicted(kind,a):
    x=[abs(c)**2 for c in a]; S=sum(x)
    val=2*S*S-sum(t*t for t in x)
    if kind=='A': val += 2*(a[0]**2*(a[1].conjugate()**2)).real
    elif kind=='B': val += 4*(a[1]**2*a[0].conjugate()*a[2].conjugate()).real
    else: val += 8*(a[0]*a[3]*a[1].conjugate()*a[2].conjugate()).real
    return val

checks=0
for kind,freqs,mods,K4four in cases:
    for _ in range(300):
        a=[]
        for _j in freqs:
            a.append(complex(rng.uniform(-1,1),rng.uniform(-1,1)))
        m=direct_moment(freqs,mods,a)
        p=predicted(kind,a)
        assert abs(m-p) < 2e-9*max(1.0,abs(p))
        S=sum(abs(c)**2 for c in a)
        assert m <= K4four*S*S + 2e-9*max(1.0,S*S)
        checks+=1

# Equality witnesses.
a=[1,1,0]
assert abs(direct_moment(cases[0][1],cases[0][2],a)/(sum(abs(c)**2 for c in a)**2)-2)<1e-12
a=[math.sqrt(2),math.sqrt(3),math.sqrt(2)]
assert abs(direct_moment(cases[1][1],cases[1][2],a)/(sum(abs(c)**2 for c in a)**2)-15/7)<1e-12
a=[1,1,1,1]
assert abs(direct_moment(cases[2][1],cases[2][2],a)/(sum(abs(c)**2 for c in a)**2)-9/4)<1e-12
print(f'VERIFY_OK collision_types=3 exact_B_identities=1000 direct_checks={checks} equality_witnesses=3')
