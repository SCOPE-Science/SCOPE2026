#!/usr/bin/env python3
"""Independent finite-block matrix checks for a coherent-reference discrimination identity.

Python >=3.9, standard library only. Numerical cases corroborate, not prove, the
all-dimensional result; its proof is in RESULT.md.
"""
from fractions import Fraction
from math import comb, sqrt, log1p, expm1

def weights(n, v, k):
    x = n * v
    y = (n + 1) * v
    return x**k / (1+x)**(k+1), y**k / (1+y)**(k+1)

def sector(n, v, k):
    a, b = weights(n, v, k)
    q = Fraction(n,n+1)**k
    return a,b,q

def matrix_checker():
    cases = 0
    for n,v in [(1,Fraction(1)),(3,Fraction(1,3)),(7,Fraction(2,5))]:
        for k in range(9):
            a,b,q=sector(n,v,k)
            # The number-state amplitudes of the coherent pair are constructed
            # independently from the claimed trace-norm formula.
            w=[sqrt(float(Fraction(comb(k,j))*Fraction(n,n+1)**j*
                                Fraction(1,n+1)**(k-j))) for j in range(k+1)]
            assert abs(sum(x*x for x in w)-1) < 2e-14
            m=[[float(b)*w[i]*w[j]-(float(a) if i==j==k else 0.0)
                for j in range(k+1)] for i in range(k+1)]
            tr=sum(m[i][i] for i in range(k+1))
            tr2=sum(m[i][j]*m[j][i] for i in range(k+1)
                    for j in range(k+1))
            # For rank at most 2 with one nonpositive and one nonnegative
            # eigenvalue, squared trace norm is 2 tr(M^2)-tr(M)^2.
            target=float((a+b)**2-4*a*b*q)
            assert abs(tr-float(b-a)) < 1e-12
            assert abs(tr2-float(a*a+b*b-2*a*b*q)) < 1e-12
            assert abs((2*tr2-tr*tr)-target) < 2e-12
            assert (a*b*(1-q)>=0)
            cases+=1
    return cases

def gaussian_exact(n,v,K):
    total=0.0
    v=Fraction(v)
    for k in range(K+1):
        a,b,q=sector(n,v,k)
        # Stable cancellation-free radicand.
        rad=float((a-b)**2+4*a*b*(1-q))
        total+=sqrt(max(0,rad))
    a_tail=float(Fraction(n)*v/(1+Fraction(n)*v))**(K+1)
    b_tail=float(Fraction(n+1)*v/(1+Fraction(n+1)*v))**(K+1)
    return 0.5-total/4, (a_tail+b_tail)/4

def endpoint_and_asymptotic_checker():
    val,err=gaussian_exact(1,Fraction(1),120)
    assert err<1e-20 and abs(val-0.21356409008208987)<2e-13
    val2,err2=gaussian_exact(3,Fraction(1,3),120)
    assert err2<1e-25 and abs(val2-0.3120728985373172)<2e-13
    # Coefficient of the nonregular local-energy scaling.
    x=1.0
    asymp=sum(sqrt(k)*x**k/(1+x)**(k+1) for k in range(1,120))/2
    n=10000
    # Avoid forming fractions with enormous integers for this check.
    total=0.0
    for k in range(120):
        a=x**k/(1+x)**(k+1)
        xn=x*(1+1/n)
        b=xn**k/(1+xn)**(k+1)
        one_minus_q=-expm1(k*log1p(-1/(n+1)))
        total+=sqrt((a-b)**2+4*a*b*one_minus_q)
    numer=sqrt(n)*total/4
    assert abs(asymp-numer)<0.001
    return val,val2,asymp,numer

if __name__=='__main__':
    count=matrix_checker()
    a,b,c,d=endpoint_and_asymptotic_checker()
    print('VERIFY_OK independent_Fock_sector_matrices=%s Gaussian_cases=2 tail_bounds=passed local_asymptotic=corroborated' % count)
    print('EXAMPLES Pe_n1_v1=%.14f Pe_n3_v1over3=%.14f local_coefficient=%.12f check_n10000=%.12f' %(a,b,c,d))
