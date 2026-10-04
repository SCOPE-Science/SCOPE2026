#!/usr/bin/env python3
from fractions import Fraction

def run():
    matrix_cov_checks=0
    harmonic_identity_checks=0
    variance_checks=0
    correlation_checks=0

    for n in range(2,121):
        m=n-1
        mu=[Fraction(1,n-(i+1)) for i in range(m)]
        var=[x*x for x in mu]
        tau=[2*x*x*x for x in mu]
        A=[[Fraction(min(i+1,j+1)*(n-max(i+1,j+1)),n*(n-1)) for j in range(m)] for i in range(m)]
        Amu=[sum((A[i][j]*mu[j] for j in range(m)), Fraction(0)) for i in range(m)]
        cov=2*sum((var[i]*Amu[i] for i in range(m)), Fraction(0))
        cov += sum((A[i][i]*tau[i] for i in range(m)), Fraction(0))
        h=sum((Fraction(1,k) for k in range(1,n)), Fraction(0))
        h2=sum((Fraction(1,k*k) for k in range(1,n)), Fraction(0))
        assert cov==(h*h+h2)/Fraction(n-1)
        matrix_cov_checks+=1

    h=Fraction(0); h2=Fraction(0); tri=Fraction(0)
    for n in range(2,501):
        m=n-1
        h += Fraction(1,m)
        h2 += Fraction(1,m*m)
        tri += h/Fraction(m)
        assert 2*tri==h*h+h2
        harmonic_identity_checks+=1
        varR=h2
        varS=Fraction(2*(4*n-3),n*(n-1))
        assert varR>0 and varS>0
        variance_checks+=2
        cov=(h*h+h2)/Fraction(n-1)
        rho2=cov*cov/(varR*varS)
        target=(h*h+h2)**2 * Fraction(n,2*(n-1)*(4*n-3)) / h2
        assert rho2==target and 0<rho2<1
        correlation_checks+=2

    print('VERIFY_OK '
          f'matrix_cov_checks={matrix_cov_checks} '
          f'harmonic_identity_checks={harmonic_identity_checks} '
          f'variance_checks={variance_checks} '
          f'correlation_checks={correlation_checks}')

if __name__=='__main__':
    run()
