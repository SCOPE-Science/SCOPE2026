"""Reproduce formulas for homogeneous tangent-projection transport on a rank-one loop.

Standard library only. Finite floating-point diagnostics supplement the proof.
"""
import math
from fractions import Fraction

SQRT2 = math.sqrt(2.0)
PI = math.pi


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def lin(a, x, b, y):
    return tuple(a*s + b*t for s, t in zip(x, y))


E1 = (-1/SQRT2, 0.0, 0.0, 1/SQRT2)
E2 = (0.0, -1/SQRT2, -1/SQRT2, 0.0)
E3 = (1/SQRT2, 0.0, 0.0, 1/SQRT2)
A = (0.0, 1/SQRT2, -1/SQRT2, 0.0)


def frame(t):
    phi = 2*t
    radial = lin(math.cos(phi), E1, math.sin(phi), E2)
    normal = lin(1/SQRT2, radial, 1/SQRT2, E3)
    f1 = lin(1/SQRT2, radial, -1/SQRT2, E3)
    f2 = lin(-math.sin(phi), E1, math.cos(phi), E2)
    return normal, f1, f2, A


def mm(x, y):
    return ((x[0][0]*y[0][0]+x[0][1]*y[1][0],
             x[0][0]*y[0][1]+x[0][1]*y[1][1]),
            (x[1][0]*y[0][0]+x[1][1]*y[1][0],
             x[1][0]*y[0][1]+x[1][1]*y[1][1]))


def mt(x):
    return ((x[0][0], x[1][0]), (x[0][1], x[1][1]))


def matpow(x, n):
    ans = ((1.0, 0.0), (0.0, 1.0))
    while n:
        if n & 1:
            ans = mm(ans, x)
        x = mm(x, x)
        n >>= 1
    return ans


def opnorm(x):
    tr = sum(x[i][j]*x[i][j] for i in range(2) for j in range(2))
    det = x[0][0]*x[1][1] - x[0][1]*x[1][0]
    return math.sqrt((tr + math.sqrt(max(0.0, tr*tr-4*det*det)))/2)


def minus(x,y):
    return tuple(tuple(x[i][j]-y[i][j] for j in range(2)) for i in range(2))


def data(n):
    delta = 2*PI/n
    x = math.cos(delta)
    b = math.sin(delta)/SQRT2
    v = (1-x)/4
    rho = math.cos(PI/n)
    omega = math.sqrt(b*b-v*v)
    theta = math.atan2(omega, (1+3*x)/4)
    B = (((1+x)/2, b), (-b, x))
    s = math.sin(n*theta)
    a = math.cos(n*theta)
    closed = ((rho**n*(a+s*v/omega), rho**n*s*b/omega),
              (-rho**n*s*b/omega, rho**n*(a-s*v/omega)))
    tau = v*s/omega
    singular = (rho**n*(math.sqrt(1+tau*tau)+abs(tau)),
                rho**n*(math.sqrt(1+tau*tau)-abs(tau)))
    return B,closed,singular,rho


def verify():
    checks = 0
    # Exact rational determinant and discriminant at representative grid sizes.
    c3 = Fraction(-1, 2)
    c4 = Fraction(0)
    for c in (c3,c4):
        tr = (1+3*c)/2
        det = (1+c)/2
        assert tr*tr-4*det == (c-1)*(9*c+7)/4
        checks += 1
    assert ((1+c3)/2)**3 == Fraction(1, 64)
    assert ((1+c4)/2)**4 == Fraction(1, 16)
    checks += 2
    for n in (3,4,5,6,7,8,10,12,20,32,60,100,250):
        normal0,a0,b0,skew0 = frame(0.0)
        normal1,a1,b1,skew1 = frame(PI/n)
        B,closed,singular,rho=data(n)
        derived = ((dot(a1,a0),dot(a1,b0)),(dot(b1,a0),dot(b1,b0)))
        assert all(abs(B[i][j]-derived[i][j]) < 3e-14 for i in range(2) for j in range(2))
        checks += 4
        for item in (a0,b0,skew0):
            assert abs(dot(item,normal0))<3e-14
            checks += 1
        assert abs(dot(skew0,skew1)-1)<3e-14
        checks += 1
        direct=matpow(B,n)
        assert all(abs(closed[i][j]-direct[i][j])<2e-12 for i in range(2) for j in range(2))
        checks += 4
        assert singular[0] < 1+2e-12 and singular[1] < 1 and singular[0]>=singular[1]
        checks += 1
        assert abs(opnorm(closed)-singular[0]) < 1e-12
        checks += 1
        det = closed[0][0]*closed[1][1]-closed[0][1]*closed[1][0]
        assert abs(det-rho**(2*n)) < 1e-12
        checks += 1
    theta = SQRT2*PI
    exact = ((math.cos(theta),math.sin(theta)),(-math.sin(theta),math.cos(theta)))
    coefficient = PI*PI/2+PI*abs(math.sin(theta))/(2*SQRT2)
    assert coefficient > 6.0 and coefficient < 6.01
    checks += 1
    last=None
    for n in (200,500,1000,2000,4000):
        B,closed,singular,rho=data(n)
        err = opnorm(minus(closed,exact))*n
        if last is not None:
            assert abs(err-coefficient)<abs(last-coefficient) + 1e-7
        last=err
        checks+=1
    assert abs(last-coefficient)<0.005
    checks += 1
    print('TRANSPORT_VERIFY_OK',checks,'sharp_coefficient',f'{coefficient:.15f}', 'N4000', f'{last:.15f}')


if __name__ == '__main__':
    verify()
