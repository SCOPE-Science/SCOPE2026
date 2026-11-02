"""Finite reproducibility checks for a phase-modulated Hardy-space operator."""
import cmath
import math


def matrix(t, n):
    z = [cmath.exp(1j*t*math.log(j+1)) for j in range(n)]
    a = [[0j for _ in range(n)] for _ in range(n)]
    for j in range(n):
        a[j][j] = z[j]
        if j:
            gap = z[j]-cmath.exp(1j*t*math.log(j))
            for k in range(j):
                a[k][j] = gap
    return a


def mul(a, b):
    n=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def run():
    assertions=0
    for n in (1,2,3,6,10):
        for t,s in ((.3,-.25),(1.25,-.7),(-2.4,3.7),(0.,1.3)):
            a,b,c=matrix(t,n),matrix(s,n),matrix(t+s,n)
            ab=mul(a,b)
            for i in range(n):
                for j in range(n):
                    assert abs(ab[i][j]-c[i][j])<2e-12
                    assertions+=1
            for j in range(1,n):
                lam=cmath.exp(1j*t*math.log(j+1))
                residual=(sum(abs(a[k][j])**2 for k in range(n) if k!=j))**.5
                assert residual<=abs(t)/(j**.5)+1e-12
                assert abs(a[j][j]-lam)<1e-13
                assertions+=2
    print('FINITE_CHECKS_OK',assertions)

if __name__=='__main__':
    run()
