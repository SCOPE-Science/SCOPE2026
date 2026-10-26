"""Finite-dimensional checks of cubelike Grover transfer formulas.

Requires only the Python standard library. This is a finite numerical check,
not a replacement for the analytic proof at arbitrary degree.
"""
from math import acos, cos, exp, isfinite, lgamma, log, pi, sin, sqrt


def observation_time(degree):
    center = pi * degree / 2
    candidates = [t for t in range(max(1, int(center)-3), int(center)+5)
                  if t % 2 == degree % 2]
    time = min(candidates, key=lambda t: abs(t-center))
    assert abs(time-center) <= 1
    return time


def cosine_and_sine_ratio(m, time):
    theta = acos(m)
    cos_term = cos(time * theta)
    if abs(m) == 1:
        return cos_term, 0.0
    return cos_term, sin(time * theta) / sqrt(1-m*m)


def special_family_probability(h):
    assert h >= 2 and h & (h-1) == 0
    b, degree = h*h, h*h*h+1
    time = observation_time(degree)
    # Fourier character alpha is zero with probability 1/h.
    # Conditional on alpha zero, the remaining b signs are independent.
    common = 0.0
    extra_bulk = 0.0
    extra_special = 0.0
    overlap = 0.0
    for alpha_zero, alpha_prob in [(False, 1-1/h), (True, 1/h)]:
        for special_sign in (-1, 1):
            choices = range(b+1) if alpha_zero else [0]
            for j in choices:
                if alpha_zero:
                    s = b-2*j
                    weight = exp(lgamma(b+1)-lgamma(j+1)
                                 -lgamma(b-j+1)-b*log(2))
                    m = (h*s+special_sign)/degree
                else:
                    s, weight = 0, 1.0
                    m = special_sign/degree
                c, g = cosine_and_sine_ratio(m, time)
                factor = alpha_prob*weight/2
                overlap += factor*special_sign*c
                common += factor*special_sign*(c-m*g)
                extra_special += factor*g
                if alpha_zero:
                    extra_bulk += factor*special_sign*(s/b)*g
    # All bulk coordinates have equal amplitudes by Fourier symmetry.
    bulk = (common + extra_bulk)/sqrt(degree)
    special = (common + extra_special)/sqrt(degree)
    prob = (degree-1)*bulk**2 + special**2
    assert isfinite(prob) and 0 <= prob <= 1+1e-8
    return degree, time, prob, overlap


def direct_small_walk():
    h, k, b = 2, 1, 4
    dimension = k+b+1
    group_size = 1 << dimension
    generators = [(u ^ (1 << (k+j)))
                  for j in range(b) for u in range(h)]
    generators.append(1 << (k+b))
    degree = len(generators)
    time = observation_time(degree)
    state = [[0.0]*group_size for _ in generators]
    for row in state:
        row[0] = 1/sqrt(degree)
    for _ in range(time):
        coin_flipped = [[0.0]*group_size for _ in generators]
        for x in range(group_size):
            average = sum(state[j][x] for j in range(degree))/degree
            for j in range(degree):
                coin_flipped[j][x] = 2*average-state[j][x]
        state = [[coin_flipped[j][x ^ generators[j]]
                  for x in range(group_size)]
                 for j in range(degree)]
    target = generators[-1]
    direct = sum(state[j][target]**2 for j in range(degree))
    formula = special_family_probability(h)[2]
    assert abs(direct-formula) < 1e-12, (direct, formula)
    return direct


def main():
    print('full Hilbert-space, h=2:', f'{direct_small_walk():.12f}')
    print(' h    degree      T           probability       h*(1-p)')
    rows=[]
    for h in (2, 4, 8, 16, 32, 64, 128):
        degree,time,p,overlap=special_family_probability(h)
        assert p >= overlap*overlap - 2e-8
        assert 1-p <= 16*degree**(-1/3)+2e-8
        rows.append((h,p))
        print(f'{h:3d} {degree:10d} {time:8d}  {p: .12f}  {h*(1-p): .9f}')
    assert abs(128*(1-rows[-1][1])-0.3340087115) < 0.015
    print('finite checks passed')

if __name__ == '__main__':
    main()
