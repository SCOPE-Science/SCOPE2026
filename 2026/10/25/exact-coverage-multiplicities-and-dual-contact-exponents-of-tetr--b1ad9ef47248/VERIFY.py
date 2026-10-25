"""Independent numerical checks for the tetrahedral four-cap multiplicity formulas.

Only Python standard-library modules are needed. The finite grid verifies examples,
not the all-radius theorem or its endpoint asymptotics.
"""
import math
from bisect import bisect_left

PI = math.pi
D = math.acos(-1.0 / 3.0)
R0 = D / 2.0
BETA = math.acos(1.0 / 3.0)


def lens(radius):
    if radius <= R0:
        return 0.0
    if radius > PI / 2:
        raise ValueError('lens() only supports the lower half of the radius range')
    c = math.cos(radius)
    gamma = math.acos(max(-1.0, min(1.0, math.sqrt(2) * c / math.sin(radius))))
    eta_arg = (-1.0 / 3.0 - c * c) / (1.0 - c * c)
    eta = math.acos(max(-1.0, min(1.0, eta_arg)))
    return 2 * PI - 4 * c * gamma - 2 * eta


def law(radius):
    if not 0 <= radius <= PI:
        raise ValueError('radius must be in [0,pi]')
    if radius > PI / 2:
        return law(PI - radius)[::-1]
    a = (1 - math.cos(radius)) / 2
    b = lens(radius) / (4 * PI)
    if radius <= BETA:
        return (1 - 4 * a + 6 * b, 4 * a - 12 * b, 6 * b, 0.0, 0.0)
    return (0.0, 3 - 8 * a + 6 * b, 12 * a - 12 * b - 3,
            1 - 4 * a + 6 * b, 0.0)


def fibonacci_counts(n, radius):
    threshold = math.cos(radius)
    inv = 1.0 / math.sqrt(3)
    vertices = ((1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1))
    out = [0]*5
    golden = (math.sqrt(5)-1)/2
    for j in range(n):
        z = 1 - 2*(j+0.5)/n
        t = 2*PI*((j*golden)%1)
        s = math.sqrt(1-z*z)
        x,y = s*math.cos(t),s*math.sin(t)
        k = sum((sx*x+sy*y+sz*z)*inv >= threshold for sx,sy,sz in vertices)
        out[k] += 1
    return [v/n for v in out]


def check():
    assert R0 < BETA < PI/2 < PI-BETA < PI-R0
    assert abs(math.cos(D)+1/3) < 1e-14
    assert abs(lens(BETA) - 2*PI/9) < 1e-12
    assert abs(lens(PI/2) - 2*(PI-D)) < 1e-12
    for r in (0.0, .5, R0, .98, 1.1, 1.21, BETA, 1.24, 1.4, PI/2, 1.9, 2.1, 2.5, 3.0, PI):
        p = law(r)
        assert abs(sum(p)-1) < 1e-12, (r,p)
        assert min(p) > -1e-11, (r,p)
        assert abs(sum(j*p[j] for j in range(5)) - 2*(1-math.cos(r))) < 1e-11
        if r>0 and r<PI:
            obs = fibonacci_counts(80000,r)
            assert max(abs(p[j]-obs[j]) for j in range(5)) < 0.004, (r,p,obs)
    # Pairwise contact produces the sharp three-halves exponent.
    eps = 1e-4
    v = law(R0+eps)[2] / eps**1.5
    expected = 4*2**0.75/PI
    assert abs(v/expected-1) < 0.001
    # Four identical isolated triangular gaps and ensuing triple contacts.
    gap = law(BETA-eps)[0] / eps**2
    triple = law(BETA+eps)[3] / eps**2
    expected_gap = 3*math.sqrt(3)/PI
    assert abs(gap/expected_gap-1) < 0.001
    assert abs(triple/expected_gap-1) < 0.001
    print('PASS: normalized probabilities, first moments, tetrahedral end cases,')
    print('deterministic spherical samples and both local critical exponents.')


if __name__ == '__main__':
    check()
