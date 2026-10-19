"""Reproduce finite-group Fourier-bias identities (scientific numeric checks only)."""
import cmath
import itertools
import math
import random


def cyclic(n, index):
    assert n % index == 0 and 1 < index < n
    h = {index * k for k in range(n // index)}
    mask = set(range(n)) - (h - {0})
    exps = [cmath.exp(-2j * math.pi * k * x / n) for k in range(n) for x in range(n)]
    def spectrum(mass):
        return [sum(mass.get(x, 0) * exps[k * n + x] for x in range(n)) for k in range(n)]
    return h, mask, spectrum


def planar(p):
    assert p in (2, 3, 5, 7)
    grid = list(itertools.product(range(p), repeat=2))
    h = {(x, 0) for x in range(p)}
    mask = set(grid) - (h - {(0, 0)})
    characters = {uv: [cmath.exp(-2j * math.pi * ((uv[0] * xy[0] + uv[1] * xy[1]) % p)/p) for xy in grid] for uv in grid}
    def spectrum(mass):
        return [sum(mass.get(xy, 0) * b for xy, b in zip(grid, characters[uv])) for uv in grid]
    return h, mask, spectrum


def verify(h, mask, spectrum, index, origin, count):
    assert len(h) > 1 and count == len(h) * index
    assert len(mask) == count - len(h) + 1
    best = 1 / (2 * index - 1)
    for a in (0.0, best, 0.27, 0.5, 0.85, 1.0):
        mass = {x: (a if x == origin else (1 - a) / (len(mask) - 1)) for x in mask}
        vals = spectrum(mass)
        assert abs(vals[0] - 1) < 5e-13
        bias = max(abs(v) for v in vals[1:])
        theory = max(a, abs(index * a - 1) / (index - 1))
        assert abs(bias - theory) < 1e-12, (bias, theory, index)
    a = best
    mass = {x: (a if x == origin else 2 / (len(h) * (2 * index - 1))) for x in mask}
    vals = spectrum(mass)
    assert all(abs(abs(v) - a) < 1e-12 for v in vals[1:])
    rand = random.Random(825 + index + count)
    for _ in range(4000):
        v = [rand.expovariate(1) for _ in mask]
        total = sum(v)
        trial = dict(zip(mask, (z / total for z in v)))
        bias = max(abs(z) for z in spectrum(trial)[1:])
        assert bias + 2e-12 >= best
        eps = max(0.0, bias - best)
        tv = 0.5 * sum(abs(trial.get(x, 0) - mass.get(x, 0)) for x in mask)
        stability_rhs = 0.5 * math.sqrt(2 * (len(h) - 1) * eps + (count - 1) * eps * eps)
        assert tv <= stability_rhs + 2e-11, (tv, stability_rhs, bias, count)
    print(f'PASS order={count}, Hsize={len(h)}, index={index}, support={len(mask)}, sharp={best:.12g}; 4000 random competitors')


if __name__ == '__main__':
    for n, m in ((4, 2), (6, 3), (8, 2), (12, 4)):
        verify(*cyclic(n, m), m, 0, n)
    for p in (2, 3, 5, 7):
        verify(*planar(p), p, (0, 0), p*p)
    print('All numerical consistency checks passed; general theorem requires the supplied character-orthogonality proof.')
