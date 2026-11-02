"""Exact independent checks for two-patch colonization-allocation identities.
Python standard library only. Run: python verify.py
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt


def solve(A, b):
    """Solve a rational linear system with Gauss-Jordan elimination."""
    n = len(b)
    a = [[F(z) for z in row] + [F(b[i])] for i, row in enumerate(A)]
    for j in range(n):
        k = next(i for i in range(j, n) if a[i][j] != 0)
        a[j], a[k] = a[k], a[j]
        a[j] = [v/a[j][j] for v in a[j]]
        for i in range(n):
            if i != j:
                v = a[i][j]
                a[i] = [x-v*y for x, y in zip(a[i], a[j])]
    return [row[-1] for row in a]


def direct(c, e, f, B, u):
    v = B-u
    Q = [[-2*c,c,c,0],
         [e,-e-c-u,0,c+u],
         [f,0,-f-c-v,c+v],
         [0,f,e,-e-f]]
    A = [[Q[i][j] for i in range(4)] for j in range(3)] + [[F(1)]*4]
    p = solve(A,[0,0,0,1])
    return p, p[1]+p[2]+2*p[3], p[3]


def analytic(c, e, f, B, u):
    t = u-B/2
    L = B+2*c+e+f
    d = f-e
    a = (B+2*c)*L/2
    beta = L*(B*c+2*c*c+2*c*(e+f)+2*e*f)/(2*c)
    den = beta-d*t-2*t*t
    en = L*L-4*t*t
    pn = a+d*t-2*t*t
    return en/den,pn/den


def check():
    n = 0
    for c,e,f,B in product((F(1,2),F(1),F(3)), repeat=4):
        for z in (F(0),F(1,7),F(1,2),F(6,7),F(1)):
            u = B*z
            p, E, P = direct(c,e,f,B,u)
            E2,P2 = analytic(c,e,f,B,u)
            assert sum(p)==1 and min(p)>0 and E==E2 and P==P2
            n += 1
    # Nontrivial finite-budget test with distinct objectives.
    c=e=F(1);f=F(3);B=F(1)
    def val(u):return analytic(c,e,f,B,u)
    import math
    u_E=(7*math.sqrt(26)-34)/2
    assert 0.84<u_E<0.86
    assert val(F(1,2))[0] < val(F(17,20))[0]
    assert val(F(17,20))[0] > val(F(1))[0]
    assert val(F(1))[1] > val(F(17,20))[1]
    # Sign of derivatives at the two candidate extremes is verified exactly.
    L=B+2*c+e+f; d=f-e;g=e*f/c; h=e+f+2*g;j=e+f+g
    def W_E(t):return d*L*L-4*L*h*t-4*d*t*t
    def W_P(t):return d*L*(L+g)-4*L*j*t+4*d*t*t
    assert W_E(F(0))>0 and W_E(B/2)<0
    assert W_P(B/2)>0
    print('PASS: exact rational stationary-distribution comparisons:',n)
    print('PASS: separated optimum behavior for c=e=1, f=3, B=1')

if __name__=='__main__':check()
