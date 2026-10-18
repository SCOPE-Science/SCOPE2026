#!/usr/bin/env python3
"""Exact rational checks for a weighted-wheel cycle-space projection theorem.

Only Python's standard library is required.  Finite tests corroborate, and do
not replace, the uniform proof stated in RESULT.md.
"""
from fractions import Fraction as F


def D(x):
    return [x[i] - x[i-1] for i in range(len(x))]


def norm1(x):
    return sum(map(abs, x), F(0))


def data(m, t):
    assert m >= 6 and F(1, 2) <= t and 2*t*t-t-2 <= 0
    z = 1 + 2*t + 2*t*t
    u = t*(1+2*t)/(2*z)
    a = [F(0)]*m
    a[0] = u
    a[m-1] = -u
    p = D(a)
    b = [-v for v in p]
    b[0] += 1
    S = norm1(a)/t + norm1(p)
    T = norm1(b) + t*norm1(D(b))
    opt = (1+2*t)**2/z
    assert S == T == opt
    assert 0 < u <= F(1, 3)
    assert norm1(p) == 4*u
    assert norm1(D(b)) == 2-4*u

    q = [F(0)]*m
    q[0] = q[m-2] = q[m-1] = 1
    q[1] = q[2] = -1
    assert max(map(abs,q)) == 1
    e0 = [F(0)]*m; e0[0] = 1
    assert sum((q[i]*D(e0)[i] for i in range(m)),F(0)) == 2
    # q^T D^2, evaluated by the explicit cyclic second-difference row.
    v = [q[i] - 2*q[(i+1)%m] + q[(i+2)%m] for i in range(m)]
    h = (m-2)//2
    coeffs=[v[j]-v[m-1-j] for j in range(h+1)]
    assert coeffs[0] == 4
    assert all(abs(c) <= 1 for c in coeffs[1:])
    if m == 6:
        assert coeffs == [4,1,1]
    elif m == 7:
        assert coeffs == [4,1,0]
    else:
        assert coeffs[1] == 1 and coeffs[3] == -1
        assert all(c == 0 for j,c in enumerate(coeffs[1:],start=1) if j not in (1,3))
    A = 2/t + 4
    alpha = 4*t/(A+4*t)
    beta = A/(A+4*t)
    assert alpha+beta == 1
    assert alpha*A-beta*4*t == 0
    assert alpha*(2/t)-beta*t > 0
    assert beta*(1+2*t) == opt
    return opt


def smaller_case(m,t):
    assert m in (3,4,5)
    if m%2:
        H=F(m+1,2)
    else:
        H=F(m*m,2*(m-1))
    u=t*(1+2*t)/(H+4*t+F(4*m,m-1)*t*t)
    a=[u*(1-F(2*j,m-1)) for j in range(m)]
    p=D(a)
    b=[F(int(i==0))-p[i] for i in range(m)]
    S=norm1(a)/t+norm1(p)
    T=norm1(b)+t*norm1(D(b))
    upper=(H+4*t)*(1+2*t)/(H+4*t+F(4*m,m-1)*t*t)
    assert S == T == upper
    assert upper < (1+2*t)**2/(1+2*t+2*t*t) if t>F(1,2) or m<5 else upper == (1+2*t)**2/(1+2*t+2*t*t)
    return upper


def main():
    ts=[F(1,2),F(3,5),F(2,3),F(3,4),F(7,8),F(1),F(9,8),F(6,5),F(5,4),F(32,25)]
    N=0
    for m in list(range(6,51))+[60,70,80,100,120,160,200]:
        for t in ts:
            data(m,t)
            N+=1
    small=0
    for m in (3,4,5):
        for t in ts:
            smaller_case(m,t)
            small+=1
    print('EXACT_OK',N,'rational weighted-wheel cases;',small,'smaller-wheel comparison cases')

if __name__=='__main__':
    main()
