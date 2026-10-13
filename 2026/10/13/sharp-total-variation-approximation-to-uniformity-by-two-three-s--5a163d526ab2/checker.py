"""Exact arithmetic checks for the three-sided-dice total-variation theorem.

The determinant identity check is exhaustive on a degree-determining grid:
all polynomial differences have coordinatewise degree <= 3, and 4^6
Cartesian points identify the zero polynomial over the rationals.
The continuous TV proof itself is in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import product


def coeffs(a, b, c, d, e, f):
    return (a*d, a*e+b*d, a*f+b*e+c*d, b*f+c*e, c*f)


def determinant_identity(a, b, c, d, e, f):
    r0, r1, r2, r3, r4 = coeffs(a,b,c,d,e,f)
    left = r1*r2*r3-r4*r1*r1-r0*r3*r3
    right = b*e*((a*f-c*d)**2+a*b*e*f+a*c*e*e+b*b*d*f+b*c*d*e)
    return left == right


def tv(r):
    return sum(abs(z-Q(1,5)) for z in r)


def run():
    checks = 0
    for a,b,c,d,e,f in product(range(4),repeat=6):
        assert determinant_identity(a,b,c,d,e,f)
        checks += 1
    # By coordinatewise-degree <= 3, the 4^6 identity tests are complete.
    for i in range(101):
        s = Q(1,5)+Q(i,500)
        p = (Q(1,2),Q(0),Q(1,2))
        q = (s,Q(2,5),Q(3,5)-s)
        assert sum(p)==sum(q)==1
        r=coeffs(*p,*q)
        assert r[1]==r[3]==Q(1,5) and r[2]==Q(3,10)
        assert tv(r)==Q(1,5)
        assert all(z>=0 for z in r)
        checks += 4
    # Deterministic exact-rational stress tests away from the sharp family.
    for a,b,c,d,e,f in product(range(4),repeat=6):
        if a+b+c==0 or d+e+f==0:continue
        p=[Q(z,a+b+c) for z in (a,b,c)]
        q=[Q(z,d+e+f) for z in (d,e,f)]
        assert tv(coeffs(*p,*q))>=Q(1,5)
        checks+=1
    # The explicit rational dual bounds used in the proof.
    for m in range(1,501):
        t=Q(1,1)+Q(m,200)
        if t<=2:
            h=(1/t,(t-2)/(2*t),-1,-(t-2)/2,t)
            assert min(h)==-1 and max(h)==t
            assert sum(h)==(t+1)/2
            checks+=2
        else:
            h=(1/t,0,-1,0,t)
            assert min(h)==-1 and max(h)==t
            assert (t+1/t-1)/5-(t+1)/10==(t-1)*(t-2)/(10*t)
            checks+=2
    print(f"PASS {checks} exact checks including 4096 identity-grid points")

if __name__=='__main__':run()
