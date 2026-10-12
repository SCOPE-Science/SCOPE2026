"""Reproducibility checks for anchored ordinal-sum copulas.

The finite computations are illustrative. The infinite-family, Lipschitz,
compactness and independence assertions are established analytically.
"""
import math
import random
from fractions import Fraction


def base(c, u, v):
    return min(u, v, max(0.0, (u + v - c)/(2.0 - c)))


def anchor(p):
    return 2.0 - 2.0**(1.0 - 1.0/p)


def copula(p, xs, u, v):
    c = anchor(p)
    if 0.5 <= u <= 1.0 and 0.5 <= v <= 1.0:
        return 0.5 + 0.5 * base(c, (u-0.5)*2, (v-0.5)*2)
    for n, x in enumerate(xs, start=1):
        a, b = 2.0**(-n-1), 2.0**(-n)
        if a <= u <= b and a <= v <= b:
            s, t = (u-a)/(b-a), (v-a)/(b-a)
            return a + (b-a)*((1.0-x)*min(s,t)+x*base(c,s,t))
    return min(u,v)


def run():
    tests = 0
    random.seed(123456789)
    for p in [1.0, 1.5, 2.0, 4.0, 15.0]:
        c = anchor(p)
        q = math.inf if p == 1 else p/(p-1)
        slope = 1/(2-c)
        dual = slope if p == 1 else (2*slope**q)**(1/q)
        assert abs(dual-1) < 1e-13
        tests += 1
        for v in [j/20 for j in range(21)]:
            assert abs(base(c,1,v)-v)<1e-13
            assert abs(base(c,v,1)-v)<1e-13
            tests += 2
        for i in range(12):
            for j in range(12):
                a,b = i/12,(i+1)/12
                d,e = j/12,(j+1)/12
                volume=base(c,b,e)-base(c,a,e)-base(c,b,d)+base(c,a,d)
                assert volume >= -2e-14, (p,i,j,volume)
                tests += 1
        xs=[0.2,0.7,0.3,0.9]
        for i in range(22):
            for j in range(22):
                u,v=i/21,j/21
                assert abs(copula(p,xs,u,1)-u)<1e-13
                assert abs(copula(p,xs,1,v)-v)<1e-13
                assert abs(copula(p,xs,u,v)-copula(p,xs,v,u))<1e-13
                tests += 3
        for i in range(20):
            for j in range(20):
                x0, x1 = i / 20, (i+1) / 20
                y0, y1 = j / 20, (j+1) / 20
                volume = (copula(p,xs,x1,y1)-copula(p,xs,x0,y1)
                          -copula(p,xs,x1,y0)+copula(p,xs,x0,y0))
                assert volume >= -2e-14, (p,i,j,volume)
                tests += 1
        for _ in range(500):
            u,v,x,y=(random.random() for _ in range(4))
            a,b = copula(p,xs,u,v),copula(p,xs,x,y)
            dist=(abs(u-x)**p+abs(v-y)**p)**(1/p)
            assert abs(a-b)<=dist+1e-12,(p,u,v,x,y)
            tests+=1
        t=0.75
        ua=.5+.5*t
        va=ua
        h=1e-6
        g1=(copula(p,xs,ua+h,va)-copula(p,xs,ua-h,va))/(2*h)
        g2=(copula(p,xs,ua,va+h)-copula(p,xs,ua,va-h))/(2*h)
        assert abs(g1-slope)<1e-8 and abs(g2-slope)<1e-8,(p,g1,g2,slope)
        tests+=2
    # Distinct power sequences produce an invertible evaluation matrix.
    ts=[Fraction(1,4),Fraction(1,2),Fraction(3,4)]
    det=ts[0]*ts[1]*ts[2]
    for i in range(3):
        for j in range(i+1,3):
            det*=ts[j]-ts[i]
    assert det!=0 and det==Fraction(3,1024)
    tests+=1
    print('PASS',tests,'finite identities and representative inequalities')
    print('exact Vandermonde determinant:',det)

if __name__ == '__main__':
    run()
