#!/usr/bin/env python3
"""Finite exact support checks and floating-point ambiguity spectra.

Works with the Python standard library; no downloaded data are needed.
"""
from collections import Counter
import cmath
import math

EXAMPLES = ((7, (0, 1, 3)), (13, (0, 1, 3, 9)),
            (21, (0, 1, 6, 8, 18)), (31, (0, 1, 3, 8, 12, 18)))


def abs_ambiguities(v, positions, weights, phases):
    g = [0j] * v
    for s, p, theta in zip(positions, weights, phases):
        g[s] = math.sqrt(p) * cmath.exp(1j * theta)
    vals = []
    for a in range(v):
        for b in range(v):
            z = sum(g[x].conjugate() * g[(x-a) % v] *
                    cmath.exp(2j * math.pi * b * x / v)
                    for x in range(v))
            vals.append((a, b, abs(z)))
    return vals


def main():
    for v, positions in EXAMPLES:
        k = len(positions)
        assert v == k*(k-1) + 1
        diffs = Counter((x-y) % v for x in positions
                        for y in positions if x != y)
        assert diffs == Counter({a: 1 for a in range(1, v)})
        weights = [1.0 / k] * k
        phases = [(3*i*i + 2*i + 1) * math.pi / (k+3) for i in range(k)]
        vals = abs_ambiguities(v, positions, weights, phases)
        assert len(vals) == v*v
        one = [(a,b,m) for a,b,m in vals if a==0 and b==0]
        zero_axis = [(a,b,m) for a,b,m in vals if a==0 and b!=0]
        off_axis = [(a,b,m) for a,b,m in vals if a!=0]
        assert len(one)==1 and len(zero_axis)==v-1 and len(off_axis)==v*(v-1)
        assert abs(one[0][2] - 1)<2e-12
        assert all(abs(m-math.sqrt(k-1)/k)<2e-12 for _,_,m in zero_axis)
        assert all(abs(m-1/k)<2e-12 for _,_,m in off_axis)
        assert abs(min(m for _,_,m in vals) - 1/k)<2e-12
        assert abs(sum(m*m for _,_,m in vals)-v)<2e-10
        for weights in ([float(i+1)/sum(range(1,k+1)) for i in range(k)],
                        [float(2 if i == 0 else 1)/(k+1) for i in range(k)]):
            trial = abs_ambiguities(v, positions, weights, phases)
            assert min(m for _,_,m in trial) < 1/k - 1e-9
        ratio = (v+1)/(k*k)
        assert ratio >= 0.875 - 1e-12
        print(f'order={v}; sparsity={k}; min ambiguity=1/{k}; '
              f'SIC floor fraction={ratio:.10f}; '
              f'full condition={k}; trace-free condition={math.sqrt(k-1):.10f}; PASS')

if __name__ == '__main__':
    main()
