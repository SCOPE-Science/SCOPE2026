#!/usr/bin/env python3
"""Exact-rational finite-horizon checks of asymmetric absorbing-walk formulas.
The universal classification is proved analytically in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt

def survival(b,p,tmax=9):
    q=1-p
    v={0:F(1)}
    s=[F(1)]
    for j in range(1,2*tmax+1):
        w={}
        for k,a in v.items():
            for nx,pr in ((k+1,p),(k-1,q)):
                if -1 < nx < b:
                    w[nx]=w.get(nx,F(0))+a*pr
        v=w
        if j%2==0:s.append(sum(v.values(),F(0)))
    return s

def main():
    nc=0
    for p in [F(1,10),F(1,3),F(1,2),F(3,5),F(2,3),F(9,10)]:
        q=1-p
        assert survival(1,p)==[F(1)]+[F(0)]*9
        nc+=1
        for b in (2,3,4,5,6,9):
            s=survival(b,p)
            if b==2:
                assert all(s[t]==(p*q)**t for t in range(10))
            if b==3:
                assert s[1]==p
                assert all(s[t]==p*(2*p*q)**(t-1) for t in range(1,10))
            if b==4:
                # Cayley-Hamilton: eigenvalues satisfy
                # lambda^2 - 3pq lambda + (pq)^2 =0.
                assert all(s[t+2]==3*p*q*s[t+1]-(p*q)**2*s[t] for t in range(8))
                dets=[s[t]**2-s[t-1]*s[t+1] for t in range(1,9)]
                # The sign is determined by s_1^2-s_2 = p^2 - p^2*(2-p),
                # adjusted for upper barrier at four, s_2=s_2(b>=5)-p^4.
                assert all((d>0)==(p*p > s[2]) for d in dets if d)
                assert all(d==0 for d in dets) if p*p==s[2] else True
                nc+=8
            if b>=5:
                assert s[1]==p and s[2]==p*p*(2-p)
                assert s[1]*s[1]<s[2]
                nc+=2
        nc+=3
    print('VERIFY_OK: 6 rational biases; b in {1,2,3,4,5,6,9}; grouped survival recurrences, b=4 determinants, and b>=5 initial IFR obstructions.')

if __name__=='__main__':main()
