#!/usr/bin/env python3
"""Regression checks for the exact antipodal gap-energy classification."""
import math
import sympy as sp


def enumerate_gap_vectors(n):
    for mask in range(1 << n):
        vertices = sorted(j + n*((mask >> j) & 1) for j in range(n))
        gaps = tuple(vertices[(k + 1) % n] + (2*n if k == n-1 else 0)
                     - vertices[k] for k in range(n))
        assert sum(gaps) == 2*n and max(gaps) <= n+1
        yield mask, tuple(vertices), gaps


def cyclic_rotations(seq):
    return {tuple(seq[j:]+seq[:j]) for j in range(len(seq))}

for n in range(3, 15):
    records = list(enumerate_gap_vectors(n))
    assert len(records) == (1 << n)
    min_pattern = sorted([n+1]+[1]*(n-1))
    if n % 2:
        max_pattern = {(2,)*n}
    else:
        m = n//2
        max_pattern = cyclic_rotations([1]+[2]*(m-1)+[3]+[2]*(m-1))

    target_min = -(n+1)**2-(n-1)
    target_max = -4*n if n%2 else -(4*n+2)
    energies = {mask: -sum(g*g for g in gaps) for mask, _, gaps in records}
    observed_min = min(energies.values())
    observed_max = max(energies.values())
    assert observed_min == target_min and observed_max == target_max
    min_masks = {mask for mask, _, gaps in records if energies[mask] == observed_min}
    max_masks = {mask for mask, _, gaps in records if energies[mask] == observed_max}
    expected_min = {mask for mask, _, gaps in records if sorted(gaps)==min_pattern}
    expected_max = {mask for mask, _, gaps in records if gaps in max_pattern}
    assert min_masks == expected_min and len(min_masks) == 2*n
    assert max_masks == expected_max and len(max_masks) == (2 if n%2 else 2*n)

    def perimeter(gaps):
        return 2*sum(math.sin(math.pi*g/(2*n)) for g in gaps)
    pmin = 2*((n-1)*math.sin(math.pi/(2*n))+math.cos(math.pi/(2*n)))
    if n%2:
        pmax = 2*n*math.sin(math.pi/n)
    else:
        pmax = 2*((n-2)*math.sin(math.pi/n)+math.sin(math.pi/(2*n))
                  +math.sin(3*math.pi/(2*n)))
    values = [perimeter(gaps) for _, _, gaps in records]
    assert abs(min(values)-pmin) < 1e-11
    assert abs(max(values)-pmax) < 1e-11

n,R = sp.symbols('n R', positive=True)
a = sp.symbols('a', positive=True)
defect = sp.simplify(sp.expand_trig(2*R*(2*sp.sin(2*a)-sp.sin(a)-sp.sin(3*a))))
assert sp.simplify(sp.trigsimp(defect-4*R*sp.sin(2*a)*(1-sp.cos(a)))) == 0
x=sp.symbols('x', positive=True)
leading=sp.series(4*R*sp.sin(sp.pi*x)*(1-sp.cos(sp.pi*x/2)), x, 0, 5)
assert sp.simplify(leading.removeO()-sp.pi**3*R*x**3/2)==0
print('VERIFY_OK')
print('antipodal equality classes: exact exhaustive all orders 3..14')
print('chord perimeter: numerical checks all orders 3..14')
print('symbolic perimeter penalty and cubic leading term: passed')
