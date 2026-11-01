"""Reproducibility checks for the sharp square-contained triangle perimeter profile.

The infinite statement is proved analytically in RESULT.md; these finite
checks corroborate the formula and its equality constructions.
Python 3.10+, standard library only.
"""
from fractions import Fraction
from math import sqrt, isclose
from random import Random


def area(v):
    (x1,y1),(x2,y2),(x3,y3)=v
    return abs((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))/2


def perimeter(v):
    return sum(sqrt(float((v[i][0]-v[(i+1)%3][0])**2 +
                          (v[i][1]-v[(i+1)%3][1])**2)) for i in range(3))


def bound(a):
    return sqrt(2)+2*float(a)+sqrt(1+(1-2*float(a))**2)


def representatives(a):
    q=Fraction(1)-2*a
    # Opposite corners on main diagonal; reflections/rotations yield all cases.
    return [[(Fraction(0),Fraction(0)),(Fraction(1),Fraction(1)),
             (Fraction(0),2*a)],
            [(Fraction(0),Fraction(0)),(Fraction(1),Fraction(1)),
             (q,Fraction(1))]]


def check():
    count=0
    for j in range(1,500):
        a=Fraction(j,1000)
        for v in representatives(a):
            assert area(v)==a
            assert isclose(perimeter(v),bound(a),rel_tol=1e-13,abs_tol=1e-13)
            count+=1
    rnd=Random(902810)
    for _ in range(25000):
        v=[(Fraction(rnd.randint(0,10000),10000),
            Fraction(rnd.randint(0,10000),10000)) for j in range(3)]
        a=area(v)
        assert Fraction(0)<=a<=Fraction(1,2)
        assert perimeter(v)<=bound(a)+1e-11
        count+=1
    for j in range(1,500):
        q=Fraction(j,500)
        for k in range(0,251):
            s=float(q)+(1-float(q))*k/250
            t=float(q)/s
            p=s+t
            U=sqrt(1+s*s)+sqrt(1+t*t)
            D=sqrt((1-s)**2+(1-t)**2)
            assert isclose(U*U,2+p*p-2*float(q)+2*sqrt(p*p+(1-float(q))**2),rel_tol=1e-12)
            assert U+D<=sqrt(2)+(1-float(q))+sqrt(1+float(q)**2)+1e-11
            count+=1
    print(f'PASS: {count} deterministic geometric/one-variable checks')

if __name__=='__main__':
    check()
