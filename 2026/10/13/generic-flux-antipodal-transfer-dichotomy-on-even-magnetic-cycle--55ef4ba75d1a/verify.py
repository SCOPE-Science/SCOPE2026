#!/usr/bin/env python3
"""Independent finite checks for Hermitian magnetic cycles.

This file checks finite algebraic instances and sampled transition amplitudes;
it does not replace the all-orders cyclotomic/Kronecker arguments.
"""
from math import cos, sin, pi, atan, e
import cmath


def eigenvalues(n, phi):
    return [2.0*cos(phi+2*pi*k/n) for k in range(n)]


def transition(n, phi, j, t):
    vals = eigenvalues(n, phi)
    return sum(cmath.exp(-1j*t*lam)*cmath.exp(2j*pi*j*k/n)
               for k, lam in enumerate(vals))/n


def test_quadratic_relations():
    tests = 0
    # Symbolic relation lambda[k+n/2]=-lambda[k] and index parity obstruction.
    for n in range(4, 130, 2):
        j_allowed = [j for j in range(1,n) if (2*j)%n == 0]
        assert j_allowed == [n//2]
        if n & (n-1):
            # Every non-power-of-two even integer has an odd-prime divisor.
            p = next(p for p in range(3, n+1, 2) if n % p == 0)
            d = n//p
            assert d%2 == 0
            k0 = [h*d for h in range(p)]
            k1 = [1+h*d for h in range(p)]
            assert all(k%2 == 0 for k in k0)
            assert all(k%2 == 1 for k in k1)
            assert len(set(k0+k1)) == 2*p
            assert (sum(k0)-sum(k1)) % 2 == 1
            # Exact geometric-series vanishing: (x^d-1) S(x)=x^n-1.
            coeff = [0]*(n+1)
            for h in range(p):
                coeff[(h+1)*d] += 1
                coeff[h*d] -= 1
            assert coeff[0] == -1 and coeff[n] == 1
            assert all(coeff[k]==0 for k in range(1,n))
            tests+=1
        else:
            m=n//2
            assert m%2 == 0
            # For primitive 2-power roots, P(zeta)=0 iff equal halves.
            for seed in range(17):
                coeff=[((k+1)*(seed+7))%13-6 for k in range(m)]
                rel=coeff+coeff
                assert all(rel[k]==rel[k+m] for k in range(m))
                assert sum(rel[k] for k in range(1,n,2))%2 == 0
                # Pair relations also annihilate lambda by pi-shift.
                assert sum(rel)==2*sum(coeff)
                tests+=1
    return tests


def check_uniform_obstruction():
    checked=0
    for n in range(6,66,2):
        if n & (n-1) == 0:
            continue
        p=next(p for p in range(3,n+1,2) if n%p==0)
        for phi in (0.0, 0.173, 0.71, pi/n, atan(e)):
            for t in (0.0, 0.4, 2.7, 17.2, 211.0):
                amp=abs(transition(n,phi,n//2,t))
                assert amp<=1-1/(p*n)+1e-12, (n,p,phi,t,amp)
                checked+=1
    return checked


def check_fourier_matrix():
    checks=0
    for n in range(4,23,2):
        for phi in (0.0, pi/n, atan(e)):
            for k in range(n):
                lam=eigenvalues(n,phi)[k]
                for j in range(n):
                    f=lambda v: cmath.exp(2j*pi*k*(v%n)/n)
                    h_f=cmath.exp(1j*phi)*f(j+1)+cmath.exp(-1j*phi)*f(j-1)
                    assert abs(h_f-lam*f(j)) < 3e-13
                    checks+=1
    return checks


def test_half_flux_and_numeric():
    trials=0
    maximum=0
    for n in range(4,66,2):
        phi=pi/n
        for t in (0.02,0.5,1.0,7.1,12.3):
            amp=transition(n,phi,n//2,t)
            assert abs(amp)<5e-13,(n,t,amp)
            maximum=max(maximum,abs(amp));trials+=1
    phi=atan(e)
    # Sampled fidelity is illustration, not an approximate-state-transfer proof.
    for n in (4,8):
        samples=40000 if n==4 else 80000
        best=max(abs(transition(n,phi,n//2,(k+0.37)*0.21))**2
                 for k in range(samples))
        assert best > (0.999 if n==4 else 0.97), (n,best)
        print('NUMERIC_GENERIC',n,'max_sampled_fidelity',round(best,10))
    return trials,maximum


def main():
    c=test_quadratic_relations()
    z,e=test_half_flux_and_numeric()
    f=check_fourier_matrix()
    u=check_uniform_obstruction()
    print('VERIFY_OK symbolic_cyclotomic_cases=',c,
          'fourier_matrix_checks=',f,'uniform_bound_checks=',u,
          'half_flux_zero_checks=',z,'max_abs_zero_error=',format(e,'.4g'))

if __name__=='__main__':
    main()
