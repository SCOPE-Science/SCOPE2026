#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, ceil, floor

def hamilton_integer(a, c, h):
    p = (a, a, c)
    P = 2*a + c
    floors = [h*x // P for x in p]
    rems = [(h*x) % P for x in p]
    surplus = h - sum(floors)
    if surplus == 0:
        return tuple(floors), True
    order = sorted(range(3), key=lambda i: rems[i], reverse=True)
    if surplus < 3 and rems[order[surplus-1]] == rems[order[surplus]]:
        return None, False
    out = floors[:]
    for i in order[:surplus]:
        out[i] += 1
    return tuple(out), True

def hamilton_fraction(a, c, h):
    p = (a, a, c)
    P = 2*a + c
    q = [Fraction(h*x, P) for x in p]
    floors = [x.numerator // x.denominator for x in q]
    rems = [x - f for x, f in zip(q, floors)]
    surplus = h - sum(floors)
    if surplus == 0:
        return tuple(floors), True
    order = sorted(range(3), key=lambda i: rems[i], reverse=True)
    if surplus < 3 and rems[order[surplus-1]] == rems[order[surplus]]:
        return None, False
    out = floors[:]
    for i in order[:surplus]:
        out[i] += 1
    return tuple(out), True

def direct_loss_residues(a, c):
    P = 2*a + c
    out = []
    for h in range(P):
        x, ux = hamilton_integer(a, c, h)
        y, uy = hamilton_integer(a, c, h+1)
        xf, uxf = hamilton_fraction(a, c, h)
        yf, uyf = hamilton_fraction(a, c, h+1)
        assert (x, ux) == (xf, uxf)
        assert (y, uy) == (yf, uyf)
        if ux and uy:
            losses = [i for i in range(3) if y[i] < x[i]]
            if losses:
                assert losses == [2]
                out.append(h)
    return out

def theorem_loss_residues(a, c):
    P = 2*a + c
    inv_a = pow(a, -1, P)
    ys = [
        y for y in range(P)
        if Fraction(P + 3*c, 6) < y < Fraction(P, 3)
    ]
    return sorted((inv_a * y) % P for y in ys)

def count_formula(a, c):
    P = 2*a + c
    return max(0, ceil(P/3) - floor((P + 3*c)/6) - 1)

checked = 0
for a in range(2, 41):
    for c in range(1, a):
        if gcd(a, c) != 1:
            continue
        direct = direct_loss_residues(a, c)
        theorem = theorem_loss_residues(a, c)
        assert direct == theorem, (a, c, direct, theorem)
        assert len(direct) == count_formula(a, c)
        P = 2*a + c
        # Periodicity check one full period later.
        for h in range(P):
            x, ux = hamilton_integer(a, c, h)
            xp, uxp = hamilton_integer(a, c, h+P)
            if ux and uxp:
                assert tuple(xp[i] - x[i] for i in range(3)) == (a, a, c)
        checked += 1

# Literature anchor example from Janson-Linusson.
assert direct_loss_residues(3, 1) == [3]
assert count_formula(3, 1) == 1

# Additional parity checks.
assert direct_loss_residues(7, 2) == [3, 12]
assert direct_loss_residues(9, 1) == [7, 9, 11]

print("VERIFY_OK")
print("primitive_equal_pair_cases_checked", checked)
print("example_(3,3,1)_loss_residues", direct_loss_residues(3, 1))
print("example_(7,7,2)_loss_residues", direct_loss_residues(7, 2))
print("example_(9,9,1)_loss_residues", direct_loss_residues(9, 1))
