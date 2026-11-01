"""Numerical corroboration of the two-orbit polynomial intensity identities.

Uses only the Python standard library. The infinite-degree uniqueness theorem
is established analytically in RESULT.md, not by these tests.
"""
import cmath
import math
import random


def evaluate(coefficients, z):
    result = 0j
    for coefficient in reversed(coefficients):
        result = result * z + coefficient
    return result


def ring_samples(coefficients, degree, radius, angle):
    return [abs(evaluate(coefficients, radius * cmath.exp(1j*(angle+math.pi*k/degree))))**2
            for k in range(2*degree)]


def dft(samples, mode):
    n = len(samples)
    return sum(y*cmath.exp(-2j*math.pi*mode*k/n)
               for k, y in enumerate(samples))/n


def coefficients_of_intensity(coefficients, degree, radius):
    return [sum(coefficients[j+k]*coefficients[j].conjugate()*radius**(2*j+k)
                for j in range(degree-k+1)) for k in range(degree+1)]


def is_close(a, b, tolerance=2e-7):
    return abs(a-b) < tolerance * max(1, abs(a), abs(b))


def main():
    rng = random.Random(271828)
    assertions = 0
    for degree in range(1, 13):
        for repetition in range(24):
            coeff = [complex(rng.uniform(-.8,.8),rng.uniform(-.8,.8))
                     for _ in range(degree+1)]
            phi1 = rng.uniform(-1,1)
            phi2 = phi1 + math.pi/(4*degree)
            r1 = rng.uniform(.2,.8)
            r2 = rng.uniform(1.1,1.8)
            v = coeff[degree]*coeff[0].conjugate()
            projections = []
            for radius, phi in [(r1,phi1),(r2,phi2)]:
                samples = ring_samples(coeff,degree,radius,phi)
                exact = coefficients_of_intensity(coeff,degree,radius)
                for mode in range(degree):
                    expected = exact[mode]*cmath.exp(1j*mode*phi)
                    assert is_close(dft(samples,mode),expected)
                    assertions += 1
                nyquist = dft(samples,degree)
                assert is_close(nyquist, 2*radius**degree*(v*cmath.exp(1j*degree*phi)).real)
                assertions += 1
                projections.append(nyquist/(2*radius**degree))
            # Two nonparallel real projections determine the shared complex top coefficient.
            a=degree*phi1
            b=degree*phi2
            determinant=math.sin(b-a)
            assert abs(determinant)>0.1
            assertions += 1
            # Re(v e^{ia}) = Re(v) cos(a) - Im(v) sin(a)
            real_v=(-projections[0]*math.sin(b)+projections[1]*math.sin(a))/(-determinant)
            imag_v=(math.cos(a)*projections[1]-math.cos(b)*projections[0])/(-determinant)
            # Use a robust direct linear formula for correction of the determinant sign.
            predicted = complex(real_v,imag_v)
            assert is_close(predicted,v)
            assertions += 1
            # Conjugate-pair intensity samples under resonant rotation.
            bad_phi2 = phi1+math.pi/degree
            p = [0j]*(degree+1)
            q = [0j]*(degree+1)
            p[0] = q[0] = 1+0j
            p[degree] = 1j*cmath.exp(-1j*degree*phi1)
            q[degree] = -1j*cmath.exp(-1j*degree*phi1)
            for radius,phi in [(r1,phi1),(r2,bad_phi2)]:
                left = ring_samples(p,degree,radius,phi)
                right = ring_samples(q,degree,radius,phi)
                assert max(abs(x-y) for x,y in zip(left,right))<1e-7
                assertions += 1
            # Equal radius: reflection of a real linear factor.
            t=1.9*r1
            left=[-t+0j,1+0j] + [0j]*(degree-1)
            right=[-r1+0j,t/r1+0j] + [0j]*(degree-1)
            for phi in (phi1,phi2):
                ls=ring_samples(left,degree,r1,phi)
                rs=ring_samples(right,degree,r1,phi)
                assert max(abs(x-y) for x,y in zip(ls,rs))<1e-7
                assertions += 1
    print(f"PASS: {assertions} deterministic numerical assertions, degrees 1–12.")


if __name__ == '__main__':
    main()
