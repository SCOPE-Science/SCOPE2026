"""Reproducible symbolic and independent space-form checks for local random-distance moments."""
from fractions import Fraction
import math
import numpy as np
from numpy.polynomial.legendre import leggauss


def exact_coefficient(n):
    n = Fraction(n)
    jacobian_density = Fraction(-4, 3) / ((n + 4) * (n + 2)**2)
    squared_distance = Fraction(-1, 3) / (n + 2)**2
    combined = jacobian_density + squared_distance
    required = -(n + 8) / (3 * (n + 4) * (n + 2)**2)
    assert combined == required
    return combined


def spaceform_moment(n, radius, curvature, order=48):
    """Independent quadrature of exact spherical/hyperbolic cosine laws."""
    xi, wi = leggauss(order)
    radii = 0.5 * radius * (xi + 1)
    radial_weights = 0.5 * radius * wi
    if curvature == 1:
        radial_weights = radial_weights * np.sin(radii)**(n-1)
    elif curvature == -1:
        radial_weights = radial_weights * np.sinh(radii)**(n-1)
    else:
        radial_weights = radial_weights * radii**(n-1)
    radial_weights = radial_weights / np.sum(radial_weights)
    a = radii[:, None, None]
    b = radii[None, :, None]
    c = xi[None, None, :]
    if curvature == 1:
        cos_distance = np.cos(a)*np.cos(b) + np.sin(a)*np.sin(b)*c
        dist2 = np.arccos(np.clip(cos_distance, -1, 1))**2
    elif curvature == -1:
        cosh_distance = np.cosh(a)*np.cosh(b) - np.sinh(a)*np.sinh(b)*c
        dist2 = np.arccosh(np.maximum(cosh_distance, 1))**2
    else:
        dist2 = a*a + b*b - 2*a*b*c
    if n == 2:
        angular_weights = wi / (math.pi * np.sqrt(np.maximum(0, 1 - xi*xi)))
        # Explicit theta quadrature to remove the integrable singularity in cos-theta density.
        z, wz = leggauss(order)
        angles = (z + 1) * math.pi / 2
        cosine = np.cos(angles)[None, None, :]
        angular_weights = wz / 2
        if curvature == 1:
            cos_distance = np.cos(a)*np.cos(b) + np.sin(a)*np.sin(b)*cosine
            dist2 = np.arccos(np.clip(cos_distance, -1, 1))**2
        elif curvature == -1:
            cosh_distance = np.cosh(a)*np.cosh(b) - np.sinh(a)*np.sinh(b)*cosine
            dist2 = np.arccosh(np.maximum(cosh_distance, 1))**2
        else:
            dist2 = a*a + b*b - 2*a*b*cosine
    elif n == 3:
        angular_weights = wi/2
    else:
        raise ValueError("Quadrature implemented for dimensions two and three only")
    return float(np.einsum('i,j,k,ijk->',radial_weights,radial_weights,angular_weights,dist2))


def main():
    for n in range(2, 21):
        exact_coefficient(n)
    print('EXACT_RIEMANN_NORMAL_COORDINATE_COEFFICIENTS_PASSED')
    for n in (2, 3):
        for curvature in (-1, 1):
            prediction = float(exact_coefficient(n)*n*(n-1)*curvature)
            errors = []
            for radius in (0.55, 0.38, 0.26):
                measured = spaceform_moment(n,radius,curvature)
                recovered_coefficient = (measured - (2*n/(n+2))*radius**2)/radius**4
                errors.append(abs(recovered_coefficient-prediction))
            assert errors[-1] < errors[0] * 0.46, (n,curvature,prediction,errors)
            assert errors[-1] < 0.005, (n,curvature,prediction,errors)
            print('SPACEFORM_TEST',n,curvature,'prediction',round(prediction,9),'errors',list(map(lambda t:round(t,9),errors)))
    print('ALL_CHECKS_PASSED')

if __name__ == '__main__':
    main()
