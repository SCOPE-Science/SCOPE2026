#!/usr/bin/env python3
"""Exact-rational residual checks for petal-sunflower fixation recurrences."""
from fractions import Fraction as Q

def verify(s,m,r):
    sm=s*m
    q=(r+sm)/(r*(1+sm*r))
    h=1/(1+(sm/r)*sum((q**i for i in range(m)),Q(0)))
    f0=lambda j: sm*r*h*sum((q**k for k in range(1,j+1)),Q(0))
    f1=lambda j: h*(1+(sm/r)*sum((q**k for k in range(j)),Q(0)))
    assert f0(0)==0 and f1(m)==1
    for j in range(1,m+1):
        assert (Q(j,m)*(f0(j-1)-f0(j)) + s*r*j*(f1(j)-f0(j)))==0
    for j in range(m):
        assert (r*Q(m-j,m)*(f1(j+1)-f1(j))+s*(m-j)*(f0(j)-f1(j)))==0
    leaf=r/(r+s-1+Q(1,m))*f1(1)
    ratio=Q(m)*(r+sm)/(m*(r+s-1)+1)
    assert leaf==h*ratio
    avg=(h+sm*leaf)/(sm+1)
    assert avg==h*(m*r+s*m*m-m+1)/(m*r+m*(s-1)+1)
    if r==1:
        assert h==Q(1,1+s*m*m)
        assert leaf==Q(m,1+s*m*m)
        assert avg==Q(1,1+s*m)
    if m>1:assert leaf>h
    return 2*m+7

def main():
    checked=0
    for s in range(1,9):
        for m in range(1,21):
            for r in (Q(1,3),Q(1),Q(3,2),Q(2),Q(7)):
                checked+=verify(s,m,r)
    print('PASS:',checked,'exact rational identities and inequalities')
if __name__=='__main__':main()
