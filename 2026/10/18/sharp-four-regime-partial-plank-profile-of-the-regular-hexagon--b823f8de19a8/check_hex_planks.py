#!/usr/bin/env python3
"""Independent polygon clipping tests for the hexagonal partial-plank profile."""
import math
import random

SQ3 = math.sqrt(3.0)
VERTICES = [(math.cos(k * math.pi / 3), math.sin(k * math.pi / 3)) for k in range(6)]
AREA = 1.5 * SQ3


def clip_halfplane(poly, nx, ny, h):
    out = []
    if not poly:
        return out
    for i, a in enumerate(poly):
        b = poly[(i + 1) % len(poly)]
        da = nx * a[0] + ny * a[1] - h
        db = nx * b[0] + ny * b[1] - h
        if da <= 0:
            out.append(a)
        if (da < 0 < db) or (db < 0 < da):
            t = da / (da - db)
            out.append((a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1])))
    return out


def shoelace(poly):
    if len(poly) < 3:
        return 0.0
    return abs(sum(a[0] * b[1] - a[1] * b[0]
                   for a, b in zip(poly, poly[1:] + poly[:1]))) / 2


def independent_clip(width, theta, offset=0.0):
    nx, ny = math.cos(theta), math.sin(theta)
    poly = clip_halfplane(VERTICES, nx, ny, offset + width / 2)
    poly = clip_halfplane(poly, -nx, -ny, width / 2 - offset)
    return shoelace(poly)


def fan_formula(width, theta):
    x = math.tan(theta) / SQ3
    r = math.sqrt(1 + 3*x*x)
    p = width*r/2
    b = (1 + 3*x)/2
    c = (1 - 3*x)/2
    if p <= c:
        f = 3 - 4*p
    elif p <= b:
        f = (4*p*p - 12*p*(1+x) + 9*x*x+12*x+7)/(2*(1+3*x))
    else:
        f = 4*(1-p)**2/(1-9*x*x)
    return AREA - SQ3*f/2


def kappa(x):
    return 2*(3*x + 2/(1+x))/math.sqrt(1+3*x*x)


def optimal_x(width):
    if width <= SQ3/2:
        return 1/3
    if width < 1:
        target = width + 3/width
        lo, hi = 0.0, 1/3
        for _ in range(80):
            mid = (lo+hi)/2
            if kappa(mid) < target:
                lo = mid
            else:
                hi = mid
        return (lo+hi)/2
    if width <= 1.5:
        return 0.0
    if width < SQ3:
        return math.sqrt(4*width*width-9)/(3*SQ3)
    return 1/3


def predicted_value(width):
    if width <= SQ3/2:
        return 2*width - width*width/(2*SQ3)
    if width < 1:
        return fan_formula(width, math.atan(SQ3*optimal_x(width)))
    if width <= 1.5:
        return SQ3/2*(3-(2-width)**2)
    if width < SQ3:
        return SQ3*(1+width*width/6)
    return AREA


def run():
    rng = random.Random(702611)
    checked = 0
    for _ in range(2400):
        w = rng.uniform(0.0001, SQ3 - 0.0001)
        theta = rng.uniform(0, math.pi/6)
        val = independent_clip(w, theta)
        formula = fan_formula(w, theta)
        assert abs(val - formula) < 2e-11, (w, theta, val, formula)
        checked += 1
    grid_tests = 0
    for i in range(400):
        w = SQ3*(i+0.314159)/(400+0.5)
        x = optimal_x(w)
        theta = math.atan(SQ3*x)
        val = independent_clip(w, theta)
        expected = predicted_value(w)
        assert abs(val - expected) < 5e-11, (w, val, expected)
        # A dense independent orientation grid can never exceed the predicted optimum.
        for k in range(81):
            a = math.pi * k / (6*80)
            assert independent_clip(w, a) <= expected + 2e-10, (w,a,expected)
        grid_tests += 81
    translated = 0
    for _ in range(1500):
        w = rng.uniform(0.001, SQ3 - 0.001)
        theta = rng.uniform(0, math.pi/6)
        offset = rng.uniform(-1, 1)
        assert independent_clip(w, theta, offset) <= independent_clip(w, theta) + 2e-11
        translated += 1
    for w in (SQ3/2, 1, 1.5, SQ3):
        assert abs(predicted_value(w - 1e-8)-predicted_value(w+1e-8)) < 8e-8
    print('HEX_PLANK_PROFILE_OK fan_clips=%d orientation_grid=%d translated=%d' % (
        checked, grid_tests, translated))


if __name__ == '__main__':
    run()
