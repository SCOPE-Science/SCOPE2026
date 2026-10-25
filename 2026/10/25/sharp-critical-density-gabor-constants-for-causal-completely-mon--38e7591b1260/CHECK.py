"""Finite numerical smoke checks for exact causal Gabor formulas.

The analytic proof of sharp bounds is in RESULT.md; finite grids are NOT proofs.
Run: python3 CHECK.py
"""
import cmath
import math


def laplace_z(x, theta, atoms, a=1.0):
    return sum(weight * cmath.exp(-rate*x)
               / (1-cmath.exp(-rate*a-1j*theta))
               for weight, rate in atoms)


def bounds(atoms, a=1.0):
    lower = sum(weight * math.exp(-rate*a)/(1+math.exp(-rate*a))
                for weight, rate in atoms)
    upper = sum(weight/(1-math.exp(-rate*a)) for weight, rate in atoms)
    return a*lower*lower, a*upper*upper


def run():
    atoms = [(1.0, 1.0), (2.0, 3.0)]
    a = 1.0
    A, B = bounds(atoms, a)
    assert A > 0 and B > A
    for j in range(151):
        x = a*j/152
        for k in range(151):
            theta = 2*math.pi*k/151
            z = math.sqrt(a)*laplace_z(x, theta, atoms, a)
            assert A-1e-11 <= abs(z)**2 <= B+1e-11
    # Test the two limiting extremal boundary locations.
    upper = abs(math.sqrt(a)*laplace_z(1e-9, 0.0, atoms, a))**2
    lower = abs(math.sqrt(a)*laplace_z(a-1e-9, math.pi, atoms, a))**2
    assert abs(upper-B) < 1e-6
    assert abs(lower-A) < 1e-6
    # The p=2 tail has exact zeta(2), eta(2) and sharp constants.
    p2_A = (1-math.pi**2/12)**2
    p2_B = math.pi**4/36
    assert abs(p2_A-0.03151795422123494) < 1e-14
    assert abs(p2_B-2.7058080842778454) < 1e-13
    # Demonstrate the divergent positive Cesaro coefficients for p<=1.
    def fejer_positive(N, p, x=0.5):
        return sum((1-k/(N+1))*(1+x+k)**(-p) for k in range(N+1))
    for p in (0.75, 1.0):
        assert fejer_positive(1000, p) > fejer_positive(100, p)
        assert fejer_positive(10000, p) > fejer_positive(1000, p)
    print('PASS: finite numerical smoke checks (analytic proof required).')
    print('A, B for mixed exponentials:', A, B)
    print('A, B for p=2:', p2_A, p2_B)


if __name__ == '__main__':
    run()
