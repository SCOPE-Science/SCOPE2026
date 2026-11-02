#!/usr/bin/env python3
"""Alternative exact-rational finite diagnostics for a three-coordinate Langevin covariance theorem.

Run: python3 checker.py . Only the Python standard library is required.
The analytic proof, not this finite checker, supplies the continuum quantifiers.
"""
from fractions import Fraction as F
from decimal import Decimal, getcontext
from random import Random


def solve(a, b):
    n = len(b)
    m = [list(a[i]) + [b[i]] for i in range(n)]
    for j in range(n):
        r = next(i for i in range(j, n) if m[i][j])
        m[j], m[r] = m[r], m[j]
        z = m[j][j]
        m[j] = [v/z for v in m[j]]
        for i in range(n):
            if i != j:
                z = m[i][j]
                m[i] = [m[i][v] - z*m[j][v] for v in range(n+1)]
    return [m[i][-1] for i in range(n)]


def exact_covariance(g, k, temperature=F(1)):
    # Solve K C + C K^T + 2 T I = 0 without symbolic covariance formulas.
    K = [[-1, g, -k], [0, -1, k], [k, -k, -1]]
    pairs = [(0,0), (0,1), (0,2), (1,1), (1,2), (2,2)]
    mats = []
    for r, t in pairs:
        e = [[F(0) for _ in range(3)] for _ in range(3)]
        e[r][t] = e[t][r] = F(1)
        mats.append(e)
    def eq(c,i,j):
        return sum(K[i][l]*c[l][j]+c[i][l]*K[j][l] for l in range(3))
    a = [[eq(e,i,j) for e in mats] for i,j in pairs]
    rhs = [-2*temperature if i==j else F(0) for i,j in pairs]
    x = solve(a,rhs)
    c = [[F(0) for _ in range(3)] for _ in range(3)]
    for (i,j),v in zip(pairs,x):
        c[i][j] = c[j][i] = v
    return c


def stated_covariance(g,k,t=F(1)):
    v = k*k
    h = 8*v*v+20*v+8
    f = (1+2*v-g*v)*(8+4*v+g*v)
    z = [[0]*3 for _ in range(3)]
    z[0][0] = h-g*(v*v+5*v)+g*g*(5*v+4)-g*g*g*v
    z[1][1] = h-g*(v*v+5*v)
    z[2][2] = h-g*(4*v*v+11*v)+3*g*g*v
    z[0][1] = z[1][0] = g*(3*v*v+8*v+4-g*v)
    z[0][2] = z[2][0] = g*k*((2*v+3)*g-(v+2))
    z[1][2] = z[2][1] = g*k*(g*v+v+2)
    return [[t*z[i][j]/f for j in range(3)] for i in range(3)]


def bpoly(g,k):
    v=k*k
    return v*g*g-(5*v*v+18*v+16)*g+4*(v+2)**2


def thresholds(k):
    v=k*k
    m=(v+2)/(2*v+3)
    d=Decimal(v.numerator)/Decimal(v.denominator)
    h=(8*(d+2)**2)/(5*d*d+18*d+16+(d+2)*(25*d*d+64*d+64).sqrt())
    return m,h,2+1/k**2


def run():
    rng=Random(10407)
    count=0
    kvals=[F(1,13),F(1,3),F(1,2),F(1),F(3,2),F(2),F(7),F(11)]
    for _ in range(360):
        k=rng.choice(kvals)
        gc=2+1/k**2
        g=F(rng.randint(0,99),100)*gc
        t=F(rng.randint(1,9),rng.randint(1,9))
        c=exact_covariance(g,k,t)
        d=stated_covariance(g,k,t)
        for i in range(3):
            for j in range(3):
                assert c[i][j]==d[i][j], (g,k,i,j)
                count+=1
        # Exact cross/minor factorization independent of the all-coordinate solver.
        lhs=c[0][1]*c[1][2]-c[0][2]*c[1][1]
        v=k*k
        f=(1+2*v-g*v)*(8+4*v+g*v)
        rhs=t*t*g*k*bpoly(g,k)/((1+2*v-g*v)*(8+4*v+g*v)**2)
        assert lhs==rhs, (g,k,lhs,rhs)
        count+=1
    c=exact_covariance(F(3,5),F(1))
    assert c[0][2]==0
    assert c[0][1]==F(2,7) and c[1][2]==F(1,14)
    assert c[1][1]==F(15,14)
    assert c[0][2]-c[0][1]*c[1][2]/c[1][1]==-F(2,105)
    count+=5
    getcontext().prec=55
    last_m=Decimal(1)
    last_h=Decimal(2)
    for a in range(1,250):
        k=F(a,37)
        m,h,gc=thresholds(k)
        md=Decimal(m.numerator)/Decimal(m.denominator)
        assert Decimal('0.5')<md<Decimal(2)/3<Decimal('0.8')<h<Decimal(1)<Decimal(gc.numerator)/Decimal(gc.denominator)
        assert md<last_m and h<last_h
        last_m=md;last_h=h
        count+=2
    print('PASS: %d independent exact-rational, masking and threshold diagnostics' % count)

if __name__=='__main__':
    run()
