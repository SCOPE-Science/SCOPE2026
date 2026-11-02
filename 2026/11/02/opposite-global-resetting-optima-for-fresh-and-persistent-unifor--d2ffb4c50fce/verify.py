#!/usr/bin/env python3
"""Independent finite-difference and numerical tests for circle-search reset protocols.

Run with Python >=3.9, standard library only. Finite tests supplement the analytic proof.
"""
import math


def exact(z, ell=1.0, diffusivity=1.0):
    assert z > 0 and ell > 0 and diffusivity > 0
    scale = ell**2 / diffusivity
    annealed = scale * ((z / math.tanh(z) - 1.0) / z**2)
    quenched = scale * ((math.cosh(z) * math.atan(math.sinh(z)) / z - 1.0) / z**2)
    return annealed, quenched


def discrete_phi(z, n):
    """FD for (phi'' - z^2 phi)=0, phi(0)=1, phi'(1)=0."""
    assert n >= 3
    h = 1.0 / n
    main = 2.0 + (z*h)**2
    # Unknowns phi[1:n+1], Dirichlet source at index 1.
    lower = [-1.0] * (n - 1)
    lower[-1] = -2.0  # reflected ghost site at the right edge
    upper = [-1.0] * (n - 1)
    rhs = [0.0] * n
    rhs[0] = 1.0
    c = [0.0] * (n - 1)
    d = [0.0] * n
    c[0] = upper[0] / main
    d[0] = rhs[0] / main
    for i in range(1, n):
        inv = 1.0 / (main - lower[i-1]*c[i-1])
        if i < n-1:
            c[i] = upper[i]*inv
        d[i] = (rhs[i] - lower[i-1]*d[i-1])*inv
    x = [0.0]*n
    x[-1] = d[-1]
    for i in range(n-2, -1, -1):
        x[i] = d[i] - c[i]*x[i+1]
    return [1.0]+x


def numerical(z, n=1600, ell=1.0, diffusivity=1.0):
    phi = discrete_phi(z, n)
    rate = diffusivity*(z/ell)**2
    integral_phi = (sum(phi[1:-1]) + (phi[0]+phi[-1])/2)/n
    annealed = (1.0 / integral_phi - 1.0)/rate
    local_mfpt = [(1.0/v-1.0)/rate for v in phi]
    quenched = (sum(local_mfpt[1:-1]) + (local_mfpt[0]+local_mfpt[-1])/2)/n
    return annealed, quenched


def check():
    ell, D = 1.7, 2.3
    t0 = ell**2/(3*D)
    tested = 0
    prev_ann = 100.0
    for z in (0.1,0.2,0.5,1.0,2.0,3.0,5.0,8.0):
        ann, que = exact(z, ell, D)
        ann_fd, que_fd = numerical(z, 1600, ell, D)
        assert ann < t0 < que, ('strict chain', z, ann, que, t0)
        assert ann < prev_ann, ('annealed monotonicity sample', z)
        assert abs(ann-ann_fd) < 4.0e-5 * max(1.0, abs(ann)), ('ann FD',z,ann,ann_fd)
        assert abs(que-que_fd) < 8.0e-5 * max(1.0, abs(que)), ('que FD',z,que,que_fd)
        # Non-reset Laplace transform directly solves Dirichlet/reflected BVP.
        phi = discrete_phi(z, 1600)
        for j in (1, 201, 803, 1327, 1600):
            ph = math.cosh(z*(1-j/1600))/math.cosh(z)
            assert abs(phi[j]-ph)<2.0e-5, ('Laplace FD',z,j,phi[j],ph)
            tested += 1
        tested += 4
        prev_ann = ann
    # These coefficients are derived independently by Taylor expansion
    # of cosh, tanh, arctan(sinh), not fitted from the finite grid.
    for z in (0.02,0.04,0.08,0.12):
        ann, que = exact(z)
        ann_low = 1/3-z*z/45+2*z**4/945-z**6/4725
        que_low = 1/3+z**4/315-2*z**6/2835+2*z**8/10395
        assert abs(ann-ann_low)<3e-8, ('ann Taylor',z)
        assert abs(que-que_low)<3e-8, ('que Taylor',z)
        tested += 2
    for z in (12.,16.,20.):
        ann, que = exact(z)
        ann_asym = 1/z
        que_asym = math.pi*math.exp(z)/(4*z**3)
        assert abs(ann/ann_asym-1)<0.1, ('ann asymptotic',z)
        assert abs(que/que_asym-1)<0.05, ('que asymptotic',z)
        tested += 2
    # The strict Cauchy-Schwarz step behind the global quenched inequality.
    for z in (0.1,0.3,0.7,1.,2.,3.,7.,13.):
        left = math.sinh(z)*math.atan(math.sinh(z))
        assert left > z*z, ('Cauchy-Schwarz', z)
        tested += 1
    print(f'PASS: {tested} independent finite-difference, asymptotic, and inequality assertions')


if __name__ == '__main__':
    check()
