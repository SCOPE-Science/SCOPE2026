#!/usr/bin/env python3
"""Standalone numerical consistency checks for the stated sine-memory two-cycle formulas.
Requires Python 3 and mpmath.  Finite checks are not the infinite proof.
"""
import mpmath as mp
mp.mp.dps = 75


def F(a,b,x,y):
    return (a*mp.cos(x)+b*mp.sin(mp.pi*y)*x, y+x)


def phi(b,t):
    C=mp.cos(mp.pi*t/2)
    return mp.sin(mp.pi*t/2)*mp.sqrt(b*b-1/(C*C))


def solve(a,b,n,sgn):
    d=min(mp.mpf('0.1'),mp.acos(1/b)/(2*mp.pi))
    def R(t):
        u=2*n+sgn*t
        return u*phi(b,t)-a*abs(mp.cos(u))
    assert R(0)<0 and R(d)>0
    lo,hi=mp.mpf(0),d
    for _ in range(300):
        m=(lo+hi)/2
        if R(m)>0:hi=m
        else:lo=m
    t=(lo+hi)/2
    u=2*n+sgn*t
    sz=-1/(b*mp.cos(mp.pi*u/2))
    cz=a*mp.cos(u)/(b*u*mp.sin(mp.pi*u/2))
    assert abs(sz**2+cz**2-1)<mp.mpf('1e-60')
    z=mp.atan2(sz,cz)/mp.pi
    A=(u,z-u/2)
    B=(-u,z+u/2)
    FA=F(a,b,*A)
    FB=F(a,b,*B)
    assert max(abs(FA[i]-B[i]) for i in (0,1))<mp.mpf('1e-60')
    assert max(abs(FB[i]-A[i]) for i in (0,1))<mp.mpf('1e-60')
    return t,u,z


def main():
    trials=0
    for atext,btext in [('0.05','1.82'),('0.5','1.2'),('0.1','1.05'),('0.05','1.01')]:
        a,b=mp.mpf(atext),mp.mpf(btext)
        for n in [20,50,100,200]:
            roots=[solve(a,b,n,sgn) for sgn in (-1,1)]
            assert roots[0][1]<2*n<roots[1][1]
            for t,u,z in roots:
                lead=a*abs(mp.cos(2*n))/(mp.pi*n*mp.sqrt(b*b-1))
                assert abs(t-lead)<(10*(a+1)/(n*n*mp.sqrt(b*b-1)))
                trials+=1
        print('PASS alpha=%s beta=%s'% (atext,btext))
    print('PASS: %d high-precision orbit returns and leading resonance estimates'%trials)

if __name__ == '__main__':
    main()
