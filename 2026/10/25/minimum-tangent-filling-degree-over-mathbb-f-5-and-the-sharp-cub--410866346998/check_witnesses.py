#!/usr/bin/env python3
"""Independent exact F_5 projective incidence checks for the two displayed witnesses."""
Q=5
POINTS=[(1,y,z) for y in range(Q) for z in range(Q)]+[(0,1,z) for z in range(Q)]+[(0,0,1)]
assert len(POINTS)==len(set(POINTS))==31

def tangent_data(degree, polynomial, gradient):
    t=[]
    for P in POINTS:
        if polynomial(*P)%Q==0:
            g=tuple(a%Q for a in gradient(*P))
            assert any(g), ('rational singularity',P)
            assert sum(a*b for a,b in zip(P,g))%Q==0  # Euler homogeneity
            t.append((P,g))
    cover={R for R in POINTS if any(sum(a*b for a,b in zip(R,g))%Q==0 for _,g in t)}
    return t,cover

quartic=lambda x,y,z:x**4+x**3*y+y**3*z-z**4
quartic_grad=lambda x,y,z:(4*x**3+3*x*x*y,x**3+3*y*y*z,y**3-4*z**3)
qt,qcover=tangent_data(4,quartic,quartic_grad)
assert len(qt)==11 and len(qcover)==31
six=[(1,0,z) for z in range(1,5)]+[(1,1,4),(0,1,0)]
assert all(any(P==Q for Q,_ in qt) for P in six)
for P in six:
    grad=quartic_grad(*P)
    assert (grad[0]+grad[1])%5==0 # contains common center (1:1:0)
assert len({(lambda a:a)(tuple((x*pow(next(t for t in quartic_grad(*P) if t%5),-1,5))%5 for x in quartic_grad(*P))) for P in six})==6

cubic=lambda x,y,z:x**3+3*x*x*y+2*x*x*z+x*z*z+y**3
cubic_grad=lambda x,y,z:(3*x*x+6*x*y+4*x*z+z*z,3*x*x+3*y*y,2*x*x+2*x*z)
ct,ccover=tangent_data(3,cubic,cubic_grad)
assert len(ct)==10 and len(ccover)==29
assert set(POINTS)-ccover=={(1,1,4),(1,4,4)}
print('QUARTIC_TANGENT_PENCIL=6 POINTS=11 COVERAGE=31/31')
print('CUBIC_POINTS=10 COVERAGE=29/31 OMITTED=(1,1,4),(1,4,4)')
print('WITNESS_VERIFY_OK')
