"""Reproduce the circular-gap rate-sampling theorem and its Radau example.

Run with Python 3.10+ using only the standard library. Checks are finite
cross-checks of an analytic proof, not a substitute for quantifier arguments.
"""
import math
import random
from fractions import Fraction


def cyclic_gap(nodes):
    assert nodes and all(0 <= x < 1 for x in nodes)
    nodes = sorted(nodes)
    return max([nodes[i+1] - nodes[i] for i in range(len(nodes)-1)]
               + [1 + nodes[0] - nodes[-1]])


def inflation(nodes, amp, center):
    rho_samples = [1 - amp * math.cos(2 * math.pi * (x-center)) for x in nodes]
    return min(rho_samples)/(1-amp)


def theorem(nodes, amp):
    return (1-amp*math.cos(math.pi*cyclic_gap(nodes)))/(1-amp)


if __name__ == '__main__':
    rng = random.Random(261017842)
    tests = 0
    for n in range(1, 15):
        for _ in range(35):
            nodes = sorted(rng.random() for _ in range(n))
            amp = rng.uniform(.05, .985)
            gaps = [(nodes[(j+1)%n] - nodes[j]) % 1 for j in range(n)]
            if n == 1: gaps = [1.0]
            ix = max(range(n), key=lambda j:gaps[j])
            center = (nodes[ix]+gaps[ix]/2) % 1
            assert abs(inflation(nodes, amp, center) - theorem(nodes, amp)) < 1e-10
            tests += 1
            for _ in range(20):
                c = rng.random()
                assert inflation(nodes, amp, c) <= theorem(nodes, amp) + 1e-10
                tests += 1
            equi = [j/n for j in range(n)]
            benchmark = (1-amp*math.cos(math.pi/n))/(1-amp)
            assert theorem(nodes, amp) + 1e-10 >= benchmark
            assert abs(theorem(equi, amp)-benchmark) < 1e-10
            tests += 2
    # Two-node flipped Legendre--Gauss--Radau coordinates: tau = -1/3, 1.
    tau = [Fraction(-1,3), Fraction(1)]
    sigma = [((v + 1)/2) % 1 for v in tau]
    assert sigma == [Fraction(1,3),Fraction(0)]
    assert cyclic_gap(sigma) == Fraction(2,3)
    tests += 2
    amp=Fraction(9,10)
    # center 2/3, cos(2pi*(1/3-2/3)) = -1/2, likewise sigma=0.
    sampled_min_dilation = 1 + amp/2
    peak_dilation = 1 - amp
    assert sampled_min_dilation / peak_dilation == Fraction(29,2)
    tests += 1
    for n in (2,3,4,8,16):
        for amp in (0.1, 0.5, 0.9, 0.99):
            factor=(1-amp*math.cos(math.pi/n))/(1-amp)
            assert factor >= 1
            assert factor - 1 <= amp*math.pi**2/(2*n*n*(1-amp)) + 1e-12
            tests += 2
    print(f'PASS {tests} reproducibility checks, seeded; N=2 fLGR ratio = 29/2.')
