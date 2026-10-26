"""Finite numerical sanity checks for the explicit torus skew product.
These examples do not prove the uniform bounds or entropy identity.
"""
import math


def a(t, beta):
    if t <= -1.0:
        return (1.0-t)**(-beta)
    if t < 0.0:
        return (2.0**(-beta))*(-t)
    return 0.0


def b(k, s, beta):
    return math.sin(2.0*math.pi*s)*sum(a(s+i,beta) for i in range(k))


def upper_arc(s):
    return 0.25*(1.0+math.tanh(s))


def circdist(x,y):
    d=(x-y)%1.0
    return min(d,1-d)


def checks():
    for beta in (0.25, 0.5, 0.75):
        for n in (512,1024,2048):
            for s in (-3.0*n,-n/2.0,-13.125,-2.375,0.13):
                phase=b(n,s,beta)
                assert abs(phase) <= 20*n**(1-beta)
                assert abs(phase/n) <= 20*n**(-beta)
            j=n//2
            k=j//2
            step=0.12*n**(beta-1)
            us=[0.0,step,2*step,3*step]
            assert us[-1] <= 0.125
            ph=[b(k,-j+u,beta) for u in us]
            assert all(ph[i+1]>ph[i] for i in range(3))
            for i in range(3):
                u1,u2=us[i:i+2]
                diffs=[b(t,-j+u2,beta)-b(t,-j+u1,beta) for t in range(k+1)]
                assert all(diffs[t+1] >= diffs[t]-1e-12 for t in range(k))
                assert diffs[-1]>0.02
                # A wraparound-safe separation exists no later than k.
                assert any(circdist(z,0.0)>0.01 for z in diffs)
            j2=j+6
            assert circdist(upper_arc(us[0]),upper_arc(j-j2+us[-1]))>0.1
    print('VERIFY_OK: 9 beta/horizon checks, monotone finite Birkhoff differences, modulo-one separation, and base separation')

if __name__=='__main__':
    checks()
