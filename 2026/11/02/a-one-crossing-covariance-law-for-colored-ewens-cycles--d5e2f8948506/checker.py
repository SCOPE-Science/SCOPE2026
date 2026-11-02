"""Exact checks for two-color Ewens cycle-composition covariance."""
from fractions import Fraction
from itertools import permutations
from math import factorial


def falling(x,k):
    z=1
    for j in range(k): z*=x-j
    return z

def rising(x,k):
    z=1
    for j in range(k): z*=x+j
    return z

def moments(m, theta):
    n=2*m; M=theta+n
    # Types A=(2 red,1 blue), B=(1 red,2 blue)
    ea=theta*m*m*(m-1)/((M-3)*(M-2)*(M-1))
    # disjoint cycles (marked distinguishable types)
    # Disjoint marked cycles: choices of three vertices from each color,
    # with two factorial arrangements cancelling two 2! denominators.
    eab2=theta**2 * falling(m,3)**2 / rising(theta+n-6,6)
    return ea,eab2

def enumerate_hist(m):
    n=2*m; H={}
    for p in permutations(range(n)):
        seen=0; k=0; x=y=0
        for i in range(n):
            if seen>>i & 1:continue
            k+=1; cur=i; red=blue=0
            while not (seen>>cur & 1):
                seen |=1<<cur
                if cur<m:red+=1
                else:blue+=1
                cur=p[cur]
            x+=(red,blue)==(2,1)
            y+=(red,blue)==(1,2)
        a,b,c,z=H.get(k,(0,0,0,0))
        H[k]=(a+1,b+x,c+x*y,z+y)
    return H

def from_hist(H, theta):
    den=sum(Fraction(theta)**k*v[0] for k,v in H.items())
    ex=sum(Fraction(theta)**k*v[1] for k,v in H.items())/den
    ey=sum(Fraction(theta)**k*v[3] for k,v in H.items())/den
    exy=sum(Fraction(theta)**k*v[2] for k,v in H.items())/den
    return ex, ey, exy


def ratio(m,theta):
    n=2*m; M=theta+n
    f=Fraction((m-2)**2,m**2)
    g=Fraction((M-1)*(M-2)*(M-3),(M-4)*(M-5)*(M-6))
    return f*g

if __name__=='__main__':
    checks=0
    for m in (3,4):
        H=enumerate_hist(m)
        assert sum(v[0] for v in H.values())==factorial(2*m)
        for theta in (Fraction(1,2),Fraction(1),Fraction(3),Fraction(20)):
            ex,ey,exy=from_hist(H,theta)
            fex,fexy=moments(m,theta)
            assert ex==ey==fex,(m,theta,ex,ey,fex)
            assert exy==fexy,(m,theta,exy,fexy)
            assert (exy-ex*ey)==ex*ey*(ratio(m,theta)-1)
            checks+=4
    for m in range(3,100):
        prev=None
        for t in (Fraction(1,100),Fraction(1),Fraction(10),Fraction(100),Fraction(1000)):
            r=ratio(m,t)
            assert prev is None or r<prev
            prev=r
            checks+=1
        if m>3:
            assert ratio(m,Fraction(1,1000000))>1
            checks+=1
    for n in (100,1000,10000):
        m=n//2
        for gamma in (Fraction(1,20),Fraction(1,8),Fraction(1,4)):
            # first-order asymptotic error decays at O(1/n)
            if n==10000:
                lim=Fraction(9,1+gamma)-8
                val=n*(ratio(m,gamma*n)-1)
                assert abs(val-lim)<Fraction(1,100)
            checks+=1
    print('PASS', checks, 'assertions', 'permutation_cases=',factorial(6)+factorial(8))
