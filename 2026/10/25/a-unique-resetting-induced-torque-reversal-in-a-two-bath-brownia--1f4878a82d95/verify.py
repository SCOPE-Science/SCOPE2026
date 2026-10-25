"""Exact-arithmetic checks for the one-coordinate-reset Brownian gyrator torque law.

Python 3 standard library only. Finite checks corroborate, but do not replace,
the analytic determinant and sign arguments in RESULT.md.
"""
from fractions import Fraction as F
from random import Random


def det3(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
            - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))


def replace_column(A, col, rhs):
    return [[rhs[i] if j == col else A[i][j]
             for j in range(3)] for i in range(3)]


def check(a, b, c, Dx, Dy, theta, r):
    assert a > 0 and b > 0 and a * b > c*c and c != 0
    assert Dx > 0 and Dy > 0 and F(0) <= theta < 1 and r > 0
    p, h, delta = r * (1-theta), 1+theta, a*b-c*c
    matrix = [[2*a+h*p, F(0), 2*c],
              [F(0), 2*b, 2*c],
              [c, c, a+b+p]]
    rhs = [2*Dx, 2*Dy, F(0)]
    determinant = det3(matrix)
    formula_determinant = (4*(a+b)*delta
                           + 2*p*((h+2)*a*b+h*b*b-h*c*c)
                           + 2*b*h*p*p)
    assert determinant == formula_determinant and determinant > 0
    u, v, w = [det3(replace_column(matrix, k, rhs))/determinant
               for k in range(3)]
    assert all(sum(matrix[i][j]*[u,v,w][j] for j in range(3)) == rhs[i]
               for i in range(3))
    torque = c*(u-v)+(b-a)*w
    numerator = (4*delta*(Dx-Dy)
                 + 2*p*(b*Dx-(a+b*h)*Dy) - h*Dy*p*p)
    assert torque == 2*c*numerator/determinant
    q, qcrit = Dx/Dy, 1+(2*p*(a+b*theta)+h*p*p)/(4*delta+2*b*p)
    assert (torque/c > 0) == (q > qcrit)
    assert (torque/c == 0) == (q == qcrit)
    assert (torque/c < 0) == (q < qcrit)
    return torque, qcrit


def main():
    rnd = Random(1729)
    n = 0
    for _ in range(360):
        a,b = F(rnd.randint(1,9), rnd.randint(1,5)), F(rnd.randint(1,9), rnd.randint(1,5))
        # Rational c with |c|<sqrt(ab), no floating-point test.
        c = F(rnd.choice([-1,1])*rnd.randint(1,5),rnd.randint(5,13))
        if c*c >= a*b:
            continue
        Dx, Dy = F(rnd.randint(1,15),rnd.randint(1,7)), F(rnd.randint(1,15),rnd.randint(1,7))
        theta = F(rnd.randint(0,5), 6)
        r = F(rnd.randint(1,20),rnd.randint(1,7))
        check(a,b,c,Dx,Dy,theta,r)
        n += 1
    assert n > 250
    # Exact zero on the stall curve, including the hard-reset endpoint.
    for theta in (F(0), F(1,2), F(3,4)):
        a=b=F(2); c=F(1); Dy=F(1); r=F(6)
        p, h, delta = r*(1-theta), 1+theta, a*b-c*c
        qcrit = 1 + (2*p*(a+b*theta)+h*p*p)/(4*delta+2*b*p)
        torque, q = check(a,b,c,qcrit*Dy,Dy,theta,r)
        assert torque == 0 and q == qcrit
        tplus,_ = check(a,b,c,(qcrit+F(1,100))*Dy,Dy,theta,r)
        tminus,_ = check(a,b,c,(qcrit-F(1,100))*Dy,Dy,theta,r)
        assert tplus > 0 and tminus < 0
    # Monotonic stall temperature ratio at rational test points.
    for theta in (F(0), F(1,3), F(3,4)):
        vals=[]
        for r in (F(1,10), F(1), F(5), F(10), F(100)):
            p=r*(1-theta); h=1+theta; delta=F(3)
            vals.append(1 + (2*p*(F(2)+F(2)*theta)+h*p*p)/(4*delta+4*p))
        assert all(x<y for x,y in zip(vals,vals[1:]))
    # The hot-first-coordinate reset changes sign in a concrete example.
    first,_=check(F(2),F(2),F(1),F(3),F(1),F(1,2),F(1))
    last,_=check(F(2),F(2),F(1),F(3),F(1),F(1,2),F(30))
    assert first > 0 > last
    print('PASS: %d exact rational parameter checks; stall and sign examples verified.'%n)


if __name__=='__main__':
    main()
