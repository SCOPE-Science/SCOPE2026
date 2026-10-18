"""Exact Laurent coefficients and independent determinant sampling for a diamond chain.
Run: python3 verify.py. Requires only the Python standard library.
"""
from fractions import Fraction as F
from itertools import permutations
from cmath import exp, pi
from random import Random

TOL = 5e-8

def direct_det(m):
    out=0j
    for p in permutations((0,1,2)):
        inversion=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        v=m[0][p[0]]*m[1][p[1]]*m[2][p[2]]
        out += (-1 if inversion&1 else 1)*v
    return out

def bloch(a,b,c,d,u,v,w,phi,z):
    f=a+b*z; g=c+d*exp(1j*phi)*z
    return [[u,f,g],[f.conjugate(),v,0],[g.conjugate(),0,w]]

def det_shift(a,b,c,d,u,v,w,phi,z,E):
    h=bloch(a,b,c,d,u,v,w,phi,z)
    for i in range(3):h[i][i]-=E
    return direct_det(h)

def coefficients(a,b,c,d,u,v,w,phi,E):
    A=a*a+b*b; B=c*c+d*d; C=a*b; D=c*d
    return ((u-E)*(v-E)*(w-E)-(w-E)*A-(v-E)*B,
            -C*(w-E)-D*exp(1j*phi)*(v-E),
            -C*(w-E)-D*exp(-1j*phi)*(v-E))

rng=Random(791701)
phases=(0,pi,pi/2,pi/3,pi*0.723)
profiles=0
entries=0
# Two independently coded determinants must match the Laurent coefficients
for _ in range(450):
    a,b,c,d=[rng.randint(1,7)/2 for k in range(4)]
    u,v,w=[rng.randint(-10,10)/3 for k in range(3)]
    phi=phases[rng.randrange(len(phases))]
    E=rng.randint(-10,10)/4
    p0,pplus,pminus=coefficients(a,b,c,d,u,v,w,phi,E)
    for j in range(13):
        z=exp(2j*pi*j/13)
        predicted=p0+pplus*z+pminus/z
        actual=det_shift(a,b,c,d,u,v,w,phi,z,E)
        assert abs(actual-predicted)<TOL,(a,b,c,d,phi,z,E,actual,predicted)
        entries+=1
    profiles+=1

# On every tuned family, each asserted flat energy is a spectral root at all momentum samples.
for _ in range(200):
    a,b,c,d=[rng.randint(1,7)/3 for k in range(4)]
    v,w=[rng.randint(-8,8)/3 for k in range(2)]
    if v==w:w+=1
    C=a*b;D=c*d;A=a*a+b*b;B=c*c+d*d
    s=(-1 if rng.getrandbits(1) else 1)
    if s==-1 and abs(C-D)<1e-8: d+=1/3;D=c*d; B=c*c+d*d
    E=(C*w+s*D*v)/(C+s*D)
    u=E+A/(v-E)+B/(w-E)
    phi=0 if s==1 else pi
    for j in range(13):
        z=exp(2j*pi*j/13)
        assert abs(det_shift(a,b,c,d,u,v,w,phi,z,E))<TOL
        entries+=1
    profiles+=1

# The robust single band, and three-band caging at balanced arm products.
for _ in range(200):
    a,b,c=[rng.randint(1,9)/3 for k in range(3)]
    d=a*b/c # C=D
    u,v=[rng.randint(-8,8)/4 for k in range(2)]
    A=a*a+b*b;B=c*c+d*d
    from math import sqrt
    energies=(v,(u+v+sqrt((u-v)**2+4*(A+B)))/2,
              (u+v-sqrt((u-v)**2+4*(A+B)))/2)
    for E in energies:
        for j in range(13):
            z=exp(2j*pi*j/13)
            assert abs(det_shift(a,b,c,d,u,v,v,pi,z,E))<TOL
            entries+=1
    for phi in phases:
        for j in range(13):
            z=exp(2j*pi*j/13)
            assert abs(det_shift(a,b,c,d,u,v,v,phi,z,v))<TOL
            entries+=1
    profiles+=1

# An exact rational certificate of the constant coefficient and the two real-flux conditions.
exact_cases=0
for s in (F(1),F(-1)):
    for aa,bb,cc,dd in ((F(1),F(2),F(2),F(1)),(F(2),F(3),F(3),F(4)),(F(3),F(1),F(5),F(2))):
        A=aa*aa+bb*bb;B=cc*cc+dd*dd;C=aa*bb;D=cc*dd
        if C+s*D==0: continue
        for vv,ww in ((F(1),F(4)),(F(-3),F(2)),(F(5),F(-1))):
            E=(C*ww+s*D*vv)/(C+s*D)
            uu=E+A/(vv-E)+B/(ww-E)
            p0=(uu-E)*(vv-E)*(ww-E)-A*(ww-E)-B*(vv-E)
            pc=-C*(ww-E)-s*D*(vv-E)
            assert p0==0 and pc==0
            exact_cases+=1

print('VERIFY_OK coefficient_profiles=',profiles,'direct_determinants=',entries,'exact_tuned=',exact_cases)
