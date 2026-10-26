"""Exact-arithmetic sanity checks for a uniform-spacing maximum/exceedance covariance.
Run with Python 3; standard library only.
Analytic arguments, rather than these finite checks, prove the all-size theorem.
"""
from fractions import Fraction
from math import comb
from itertools import combinations_with_replacement


def harmonic(n):
    return sum((Fraction(1, j) for j in range(1, n + 1)), Fraction())


def covariance(m, t):
    t = Fraction(t)
    h = harmonic(m)
    answer = (1-t)**(m-1)*((m-1)*t + 1-h)
    for r in range(1, m):
        answer += Fraction((-1)**(r+1)*comb(m-1, r), r*(r+1))*max(Fraction(0), 1-(r+1)*t)**m
    return answer


def conditional_max(m, x):
    """Integration of the maximum of the m-1 residual uniform spacings."""
    x = Fraction(x)
    if x == 1: return Fraction(1)
    g = x
    for r in range(1, m):
        g += (Fraction((-1)**(r+1)*comb(m-1,r),r*(m-1))
              *max(Fraction(0),1-(r+1)*x)**(m-1)/(1-x)**(m-2))
    return g


def derivative(m, t):
    t=Fraction(t)
    return -m*(m-1)*(1-t)**(m-2)*(conditional_max(m,t)-harmonic(m)/m)


def derivative_expanded(m,t):
    t=Fraction(t)
    d=-(m-1)*(1-t)**(m-2)*((m-1)*t+1-harmonic(m))
    d+=(m-1)*(1-t)**(m-1)
    for r in range(1,m):
        d-=Fraction(m*(-1)**(r+1)*comb(m-1,r),r)*max(Fraction(0),1-(r+1)*t)**(m-1)
    return d


def composition_check(m,K,t):
    """Independent lattice-simplex Riemann sum, not an exact probability law."""
    t=Fraction(t)
    total=count_m=count_n=count_mn=0
    def visit(prefix, rem):
        nonlocal total,count_m,count_n,count_mn
        if len(prefix)==m-1:
            cs=prefix+[rem]
            maxx=Fraction(max(cs),K)
            n=sum(Fraction(x,K)>t for x in cs)
            count_m+=maxx;count_n+=n;count_mn+=maxx*n;total+=1
            return
        for k in range(rem+1): visit(prefix+[k],rem-k)
    visit([],K)
    return count_mn/total -count_m*count_n/(total*total)


def run():
    checks=0
    assert covariance(2,Fraction(1,2))==0
    assert covariance(2,Fraction(1,3))==Fraction(-1,18)
    assert covariance(2,Fraction(2,3))==Fraction(1,18)
    for m in range(2,15):
        assert covariance(m,0)==0 and covariance(m,1)==0
        if m>=3:
            assert covariance(m,Fraction(1,m))<0
            assert covariance(m,Fraction(1,2))>0
        for den in range(2,45):
            for num in range(1,den):
                x=Fraction(num,den)
                assert derivative(m,x)==derivative_expanded(m,x)
                checks+=1
    # Exact rational bisection makes no asymptotic assertion.
    for m in range(2,20):
        lo=Fraction(1,m) if m>=3 else Fraction(1,4)
        hi=Fraction(1,2) if m>=3 else Fraction(3,4)
        for _ in range(45):
            mid=(lo+hi)/2
            cm=covariance(m,mid)
            if cm<0:lo=mid
            elif cm>0:hi=mid
            else:lo=hi=mid
        assert hi-lo<=Fraction(1,2**44)
        checks+=45
    # Riemann sums provide a test using the original simplex coordinates.
    for m,K,t,tol in [(2,300,Fraction(1,3),Fraction(1,80)),
                      (3,150,Fraction(1,3),Fraction(1,80)),
                      (4,65,Fraction(2,5),Fraction(1,80)),
                      (5,40,Fraction(2,5),Fraction(1,80))]:
        approx=composition_check(m,K,t)
        target=covariance(m,t)
        assert abs(approx-target)<tol,(m,K,t,approx,target)
        checks+=1
    print('PASS: exact polynomial-derivative comparisons, bisections, and independent lattice-simplex comparisons')
    print('Derivative test points:',sum(den-1 for den in range(2,45))*13)
    print('Additional rational and lattice comparisons:',18*45+4)
    print('Total inner checks:',checks)
    print('Examples: m=3, t=1/3:',covariance(3,Fraction(1,3)))
    print('Examples: m=3, t=1/2:',covariance(3,Fraction(1,2)))
    print('Examples: m=4, t=1/4:',covariance(4,Fraction(1,4)))

if __name__=='__main__':
    run()
