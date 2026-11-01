#!/usr/bin/env python3
"""Exact finite checks for the cutoff-volume branch theorem.

No external Python packages are required. Finite checks are evidence for the
finite examples and algebraic identities; the all-dimensional result has an
independent symbolic proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial


def cube_vertices(d):
    return list(product((0, 1), repeat=d))


def threshold_masks(d, bound):
    vertices = cube_vertices(d)
    possible = set()
    full = (1 << len(vertices)) - 1
    for weights in product(range(-bound, bound + 1), repeat=d):
        if all(w == 0 for w in weights):
            continue
        dots = [sum(w * x for w, x in zip(weights, vertex)) for vertex in vertices]
        levels = sorted(set(dots))
        for lower, upper in zip(levels, levels[1:]):
            # Use 2*dot < lower+upper, keeping all operations integral.
            mask = sum(1 << i for i, dot in enumerate(dots) if 2*dot < lower + upper)
            if 0 < mask < full:
                possible.add(mask)
    return possible


def signature(d, mask):
    """Coefficients of s^(d-|T|) prod_{i in T} eta_i, up to known nonzero scales."""
    vertices = cube_vertices(d)
    result = []
    for t in range(1 << d):
        total = 0
        for i, v in enumerate(vertices):
            if (mask >> i) & 1 and all(v[j] for j in range(d) if (t >> j) & 1):
                total += (-1) ** sum(v)
        result.append(total)
    return tuple(result)


def vol_formula(weights, cut):
    d = len(weights)
    acc = F(0)
    for v in cube_vertices(d):
        delta = cut - sum(w * x for w, x in zip(weights, v))
        if delta > 0:
            acc += (-1)**sum(v) * delta**d
    den = factorial(d)
    for w in weights:
        den *= w
    return acc / den


def clip_poly(poly, a, b, cut):
    if not poly:
        return []
    out = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        fp = a*p[0]+b*p[1]-cut
        fq = a*q[0]+b*q[1]-cut
        if fp <= 0:
            out.append(p)
        if (fp < 0 < fq) or (fp > 0 > fq):
            t = fp/(fp-fq)
            out.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
        elif fp == 0 and fq > 0:
            pass
    return out


def shoelace(poly):
    if len(poly) < 3:
        return F(0)
    return abs(sum(x*y2-x2*y for (x,y),(x2,y2) in zip(poly,poly[1:]+poly[:1]))) / 2


def main():
    countchecks = 0
    expected = {1:2, 2:12, 3:102, 4:1880}
    bounds = {1:1, 2:1, 3:2, 4:3}
    for d in range(1,5):
        labels = threshold_masks(d, bounds[d])
        assert len(labels) == expected[d], (d,len(labels))
        sigs = {signature(d, mask) for mask in labels}
        assert len(sigs) == len(labels), (d,len(sigs))
        countchecks += 2*len(labels)
    # Verify injectivity among ALL Boolean assignments for d=1,2,3,4;
    # this is deliberately independent of the threshold-function filter.
    for d in range(1,5):
        num = 1 << (1 << d)
        signatures = set()
        for mask in range(num):
            s = signature(d, mask)
            assert s not in signatures
            signatures.add(s)
        assert len(signatures) == num
        countchecks += num
    # Exact area by polygon clipping versus the signed truncated-power formula.
    square=[(F(0),F(0)),(F(1),F(0)),(F(1),F(1)),(F(0),F(1))]
    for a in range(-4,5):
        if a==0: continue
        for b in range(-4,5):
            if b==0: continue
            for k in range(-18,19):
                t=F(k,2)
                area=shoelace(clip_poly(square,F(a),F(b),t))
                assert area == vol_formula((F(a),F(b)),t), (a,b,k,area)
                countchecks+=1
    print('CUBE_DEGREE_CHECK_OK:',countchecks,'exact finite checks;',
          'witness counts 2,12,102,1880;',
          'signed 2D clipping verified')

if __name__ == '__main__':
    main()
