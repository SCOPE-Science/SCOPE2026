#!/usr/bin/env python3
"""Independent numerical arithmetic diagnostics for odd-cycle harmonic obstruction.
The all-size proof is analytic and contained in RESULT.md, not in this script.
"""
import math

def f(n,s):
    return 2*sum(r**s*math.cos(4*math.pi*r/n) for r in range(1,(n+1)//2))

def critical(n):
    lo,hi=1.0,2.0
    assert f(n,lo)<0 and f(n,hi)>0
    for _ in range(65):
        mid=(lo+hi)/2
        if f(n,mid)>0: hi=mid
        else: lo=mid
    return (lo+hi)/2

def main():
    checks=0
    for n in (5,7,9,11,15,21,31,51,101,201):
        for s,expected in (
            (0,-1),
            (1,-1/(4*math.cos(math.pi/n)**2)),
            (2,n*math.cos(2*math.pi/n)/(2*math.sin(2*math.pi/n)**2))):
            got=f(n,s)
            assert abs(got-expected)<1e-7*max(1,abs(expected)),(n,s,got,expected)
            checks+=1
        root=critical(n)
        assert 1<root<2
        assert f(n,root-1e-4)<0 and f(n,root+1e-4)>0
        checks+=1
        if n<=51:
            eig=f(n,root+0.01)
            assert eig>0
            # For cosine vector c_j=cos(4*pi*j/n), distance quadratic
            # equals eig*sum(c_j*c_j), with zero coordinate sum.
            x=[math.cos(4*math.pi*j/n) for j in range(n)]
            assert abs(sum(x))<1e-10
            norm=sum(t*t for t in x)
            assert eig*norm>0
            checks+=1
        print('N',n,'sigma',format(root,'.14f'),'scaled',format(n*n*(root-1),'.11f'))
    print('arithmetic_checks',checks)

if __name__=='__main__': main()
