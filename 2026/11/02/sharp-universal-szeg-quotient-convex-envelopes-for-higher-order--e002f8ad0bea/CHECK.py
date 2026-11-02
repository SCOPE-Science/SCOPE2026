"""Supplementary reproducibility checks for the sharp Szego-quotient envelope.

The finite checks below are not a substitute for the all-order proof.
Run with: python3 CHECK.py
"""
from fractions import Fraction
import cmath
import math

checks = 0
for m in (2, 3, 4, 5, 7, 12, 24):
    c0 = 1/(m+1)
    for s in (Fraction(1,17), Fraction(1,5), Fraction(1,2), Fraction(3,4), Fraction(19,20), Fraction(99,100)):
        sum_powers = sum(s**j for j in range(m+1))
        center = 1/sum_powers
        radius2 = (center*center)*s**(m+1)
        margin2 = ((1-center)/m)**2
        assert radius2 <= margin2
        checks += 1
        # Numeric disk containment via every support direction tested.
        rad = math.sqrt(float(radius2))
        for k in range(41):
            theta = 2*math.pi*k/41
            h_ring = float(center)*math.cos(theta)+rad
            h_cap = max(math.cos(theta), c0*(1+math.cos(theta)))
            assert h_ring <= h_cap+3e-12, (m,s,theta,h_ring,h_cap)
            checks += 1
    tangent = complex(1/m,math.sqrt(m*m-1)/(m*(m+1)))
    r=1/(m+1)
    D=m/(m+1)
    assert abs(abs(tangent-r)-r)<1e-12
    # Vector joining point 1 to tangent is perpendicular to disk radius.
    assert abs(((1-tangent)*(tangent-r).conjugate()).real)<1e-12
    checks += 2
    area = (math.sqrt(m*m-1)+math.pi-math.acos(1/m))/(m+1)**2
    perimeter = (2*math.sqrt(m*m-1)+2*math.pi-2*math.acos(1/m))/(m+1)
    assert 0<area<math.pi and perimeter>0
    checks+=1
    # Polygonal reconstruction from independent boundary coordinates.
    alpha=math.acos(1/m)
    N=2048
    boundary=[c0+c0*cmath.exp(1j*(alpha+(2*math.pi-2*alpha)*j/N)) for j in range(N+1)]
    boundary.append(complex(1,0))
    signed=sum((boundary[k].conjugate()*boundary[(k+1)%len(boundary)]).imag for k in range(len(boundary)))/2
    poly_perimeter=sum(abs(boundary[(k+1)%len(boundary)]-boundary[k]) for k in range(len(boundary)))
    assert abs(signed-area)<3e-7,(m,signed,area)
    assert abs(poly_perimeter-perimeter)<3e-6,(m,poly_perimeter,perimeter)
    checks+=2
    # Limiting circle of a single extremal symbol phi(z)=z^m, all phases.
    for k in range(29):
        zangle=2*math.pi*k/(29*(m-1))
        s=0.999999
        z=math.sqrt(s)*cmath.exp(1j*zangle)
        F=(1-s)/(1-z.conjugate()*z**m)
        # Better compare to its explicit radius-s disk.
        cc=(1-s)/(1-s**(m+1))
        RR=cc*s**((m+1)/2)
        assert abs(abs(F-cc)-RR)<3e-9
        checks+=1
print('CHECK_OK', checks)
