"""Independent exact-algebra and facet-quadrature checks of a surface-moment inequality.

Run: python verify.py
This tests examples and polynomial identities; the proof establishes the universal theorem.
"""
from fractions import Fraction
from itertools import product
from math import sqrt, isclose
from random import Random


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def norm2(v):
    return sum(q * q for q in v)


def algebra_check():
    checks = 0
    for a, b, c in product(range(1, 11), repeat=3):
        t = a*b+a*c+b*c
        s = a+b+c
        E = 3*t*s*s+6*a*b*c*s-11*t*t
        sos = (Fraction(1,2) * (
            (a-b)**2*(5*a*b+c*(a+b))
            +(a-c)**2*(5*a*c+b*(a+c))
            +(b-c)**2*(5*b*c+a*(b+c))))
        assert E == sos and E >= 0
        maximum = (b*c,a*c,a*b)
        for flags in product((0, 1), repeat=3):
            F = tuple(flags[i]*maximum[i] for i in range(3))
            T = sum(F)
            N = sum((T+2*F[i])*x*x for i,x in enumerate((a,b,c)))
            deficit = Fraction(N,1)-Fraction(5*T*T,3)
            assert deficit >= 0
            if T and deficit == 0:
                assert a == b == c and flags == (1,1,1)
            checks += 1
        # The entire closed box, not only its eight vertices.
        for q in (Fraction(1,4), Fraction(1,2), Fraction(3,4)):
            F = tuple(q * f for f in maximum)
            T = sum(F)
            N = sum((T + 2*F[i])*x*x for i,x in enumerate((a,b,c)))
            assert N > Fraction(5,3)*T*T
            checks += 1
    return checks


def geometry_check():
    rng = Random(20260820)
    node = sqrt(Fraction(3, 5)) / 2
    nodes = ((-node, 5/18), (0., 4/9), (node, 5/18))
    checks = 0
    for k in range(700):
        vectors = [tuple(rng.uniform(-3,3) for _ in range(3)) for _ in range(3)]
        U,V,W = vectors
        det = sum(U[i]*cross(V,W)[i] for i in range(3))
        if abs(det)<0.06:
            continue
        lengths2 = [norm2(v) for v in vectors]
        F = [sqrt(norm2(cross(V,W))),sqrt(norm2(cross(U,W))),sqrt(norm2(cross(U,V)))]
        T=sum(F)
        I_formula = sum((T+2*F[i])*lengths2[i] for i in range(3))/6
        I_quadrature=0.
        for i in range(3):
            a,b,c=vectors[i],vectors[(i+1)%3],vectors[(i+2)%3]
            area=F[i]
            for side in (-.5,.5):
                for t,wt in nodes:
                    for s,ws in nodes:
                        p=[side*a[j]+t*b[j]+s*c[j] for j in range(3)]
                        I_quadrature += area*wt*ws*norm2(p)
        assert isclose(I_formula,I_quadrature,rel_tol=5e-13,abs_tol=1e-10)
        assert I_formula >= Fraction(5, 72)*(2*T)**2 - 1e-10
        checks += 1
    unit=((1.,0.,0.),(0.,1.,0.),(0.,0.,1.))
    F=[sqrt(norm2(cross(unit[(i+1)%3],unit[(i+2)%3]))) for i in range(3)]
    I=sum((sum(F)+2*F[i])*norm2(unit[i]) for i in range(3))/6
    assert isclose(I,2.5,rel_tol=0,abs_tol=1e-14)
    assert isclose(I/(2*sum(F))**2,5/72,rel_tol=0,abs_tol=1e-14)
    return checks+1


if __name__=='__main__':
    n1=algebra_check()
    n2=geometry_check()
    print(f'PASS: {n1} exact integer/rational checks; {n2} independent facet geometry checks')
