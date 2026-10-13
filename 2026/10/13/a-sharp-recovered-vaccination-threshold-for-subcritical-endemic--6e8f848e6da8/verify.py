#!/usr/bin/env python3
"""Exact rational checks for an eight-compartment vaccination model.

No external packages are required. The proof in RESULT.md is analytic;
this program checks the displayed equilibrium and spectral certificates.
"""
from fractions import Fraction as Q
from math import sqrt

L = Q(1067,90)
K = Q(11,3)


def state(a, theta):
    S = L/(2+a)
    V = L/((2+a)*(1+a))
    E = 4*a
    I = Q(5,4)*a
    H = Q(5,12)*a
    R = K*a/(1+theta+5*a)
    W = theta*R/(1+a)
    return [S,V,E,a,I,H,R,W]


def vector_field(x, theta):
    S,V,E,a,I,H,R,W = x
    return [L-S*a-2*S,
            S-V*a-V,
            a*(S+V+5*R+W)-3*E,
            E-4*a,
            E+a-4*I,
            I-3*H,
            2*a+I+H-5*R*a-(1+theta)*R,
            theta*R-W*a-W]


def jacobian(x, theta):
    S,V,E,a,I,H,R,W = x
    z = Q(0)
    return [
        [-a-2, z,z,-S,z,z,z,z],
        [Q(1),-a-1,z,-V,z,z,z,z],
        [a,a,-Q(3),S+V+5*R+W,z,z,5*a,a],
        [z,z,Q(1),-Q(4),z,z,z,z],
        [z,z,Q(1),Q(1),-Q(4),z,z,z],
        [z,z,z,z,Q(1),-Q(3),z,z],
        [z,z,z,Q(2)-5*R,Q(1),Q(1),-5*a-(1+theta),z],
        [z,z,z,-W,z,z,theta,-a-1],
    ]


def mmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(A))),Q(0))
             for j in range(len(B[0]))] for i in range(len(A))]


def charpoly(A):
    """Faddeev--LeVerrier: monic coefficients, computed in Q."""
    n = len(A)
    B = [[Q(int(i==j)) for j in range(n)] for i in range(n)]
    c=[Q(1)]
    for k in range(1,n+1):
        AB=mmul(A,B)
        ck=-sum((AB[i][i] for i in range(n)),Q(0))/k
        c.append(ck)
        B=[[AB[i][j]+(ck if i==j else 0) for j in range(n)] for i in range(n)]
    return c


def poly_mul(a,b):
    """Multiply coefficient arrays in descending-power order."""
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def routh(coeff):
    n=len(coeff)-1
    width=(n+2)//2
    r=[[Q(0)]*width for _ in range(n+1)]
    a=coeff[::2]; b=coeff[1::2]
    r[0][:len(a)]=a;r[1][:len(b)]=b
    for i in range(2,n+1):
        assert r[i-1][0]!=0, "zero Routh pivot"
        for j in range(width-1):
            r[i][j]=(r[i-1][0]*r[i-2][j+1]-r[i-2][0]*r[i-1][j+1])/r[i-1][0]
    signs=[1 if row[0]>0 else -1 if row[0]<0 else 0 for row in r]
    assert 0 not in signs
    crossings=sum(u!=v for u,v in zip(signs[:-1],signs[1:]))
    return signs,crossings

# All positive constants, the threshold independent of recovered vaccination.
assert L/12==Q(1067,1080)<1
assert Q(0)<Q(1)<Q(5), "vaccinated-recovered contact is protective"

# The exact endemic scalar equation is P_theta(a) = 0.
def P(a,theta):return 3750*a*a+(750*theta-505)*a+13*(1+theta)
assert P(Q(13,375),Q(0))==0
assert P(Q(1,10),Q(0))==0
for theta in (Q(0),Q(1)):
    for a in (Q(0),Q(1,100),Q(1,10),Q(3,10)):
        if a>0:
            R = K*a/(1+theta+5*a)
            W = theta*R/(1+a)
            F = L/(1+a)+5*R+W
            assert (F-12)*90*(1+a)*(1+theta+5*a)==-P(a,theta)

# At theta=0: exactly two positive endemic roots and DFE is hyperbolic stable.
# At theta=1: P_1(a)=3750*a*a+245*a+26>0 for all a>0.
assert P(Q(0),Q(0))==13 and P(Q(0),Q(1))==26

pplus=poly_mul(poly_mul(poly_mul([Q(1),Q(4)],[Q(10),Q(11)]),[Q(10),Q(21)]),
               [Q(180),Q(2268),Q(8757),Q(12832),Q(6274),Q(147)])
pplus=[t/Q(18000) for t in pplus]
pminus=poly_mul(poly_mul(poly_mul([Q(1),Q(4)],[Q(375),Q(388)]),[Q(375),Q(763)]),
                [Q(56250),Q(686700),Q(2491538),Q(3289455),Q(1411090),Q(-15925)])
pminus=[t/Q(7910156250) for t in pminus]

for theta,a,expected_right_half in [(Q(0),Q(0),0),
                                    (Q(0),Q(13,375),1),
                                    (Q(0),Q(1,10),0),
                                    (Q(1),Q(0),0)]:
    x=state(a,theta)
    assert all(v==0 for v in vector_field(x,theta))
    assert all(z>=0 for z in x)
    if a>0:assert all(z>0 for z in x[:7]); assert x[7]==0
    assert sum(x)==L-x[4]-x[5]
    poly=charpoly(jacobian(x,theta))
    if a==Q(13,375):assert poly==pminus
    elif a==Q(1,10):assert poly==pplus
    if a==0:
        # Exact full degree-eight characteristic polynomials at the DFE.
        quad = [Q(1), Q(7), Q(13,90)]
        if theta==0:
            factors=[([Q(1),Q(1)],3),([Q(1),Q(2)],1),
                     ([Q(1),Q(3)],1),([Q(1),Q(4)],1),(quad,1)]
        else:
            factors=[([Q(1),Q(1)],2),([Q(1),Q(2)],2),
                     ([Q(1),Q(3)],1),([Q(1),Q(4)],1),(quad,1)]
        exp=[Q(1)]
        for factor,mult in factors:
            for _ in range(mult):exp=poly_mul(exp,factor)
        assert poly==exp
    signs,count=routh(poly)
    assert count==expected_right_half, (theta,a,signs)
    print("theta",theta,"A",a,"Routh",''.join('+' if s>0 else '-' for s in signs),"RHP",count)

# Quadratic discriminant D(theta)=25(22500 theta^2-38100 theta+2401).
# Roots theta_minus=(127-4 sqrt(858))/150, theta_plus=(127+4 sqrt(858))/150.
critical=(127-4*sqrt(858))/150
assert 0<critical<1
assert abs(22500*critical*critical-38100*critical+2401)<1e-9
assert (750*critical-505)<0
assert (750-505)>0
print("theta_c",format(critical,'.12f'))
print('VERIFY_OK')
