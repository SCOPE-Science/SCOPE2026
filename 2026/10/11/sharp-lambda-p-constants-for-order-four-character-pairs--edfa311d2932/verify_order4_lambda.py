#!/usr/bin/env python3
import math

SQRT2_INV = 1.0 / math.sqrt(2.0)

def moment(s, t, phi):
    vals = [1.0 + t * math.cos(phi + k * math.pi / 2.0) for k in range(4)]
    return sum(max(0.0, v) ** s for v in vals) / 4.0

def axis_value(s):
    return (2.0 ** s + 2.0) / 4.0

def diagonal_value(s):
    return 0.5 * ((1.0 + SQRT2_INV) ** s + (1.0 - SQRT2_INV) ** s)

def predicted(s):
    if s < 2.0 - 1e-14:
        return axis_value(s), 0.0
    if abs(s - 2.0) <= 1e-14:
        return 1.5, None
    if s < 3.0 - 1e-14:
        return diagonal_value(s), math.pi / 4.0
    if abs(s - 3.0) <= 1e-14:
        return 2.5, None
    return axis_value(s), 0.0

def main():
    # The proof is analytic. This deterministic grid is only a numerical stress test.
    p_values = [2.02, 2.2, 2.8, 3.5, 3.98, 4.0, 4.02, 4.4, 5.0, 5.6, 5.98,
                6.0, 6.02, 6.5, 8.0, 12.0]
    t_grid = [j / 80.0 for j in range(81)]
    phi_grid = [j * (math.pi / 4.0) / 160.0 for j in range(161)]
    checks = 0
    max_excess = 0.0
    max_formula_err = 0.0
    max_phase_loss = 0.0
    for p in p_values:
        s = p / 2.0
        target, phase = predicted(s)
        if abs(p - 4.0) < 1e-12:
            max_formula_err = max(max_formula_err, abs(axis_value(s) - 1.5), abs(diagonal_value(s) - 1.5))
        elif abs(p - 6.0) < 1e-12:
            max_formula_err = max(max_formula_err, abs(axis_value(s) - 2.5), abs(diagonal_value(s) - 2.5))
        else:
            endpoint = axis_value(s) if phase == 0.0 else diagonal_value(s)
            max_formula_err = max(max_formula_err, abs(endpoint - target))
        for t in t_grid:
            for phi in phi_grid:
                v = moment(s, t, phi)
                checks += 1
                max_excess = max(max_excess, v - target)
        # At noncritical p, the predicted phase must beat the other endpoint.
        if phase is not None:
            chosen = moment(s, 1.0, phase)
            other = moment(s, 1.0, math.pi / 4.0 if phase == 0.0 else 0.0)
            max_phase_loss = max(max_phase_loss, other - chosen)
            assert abs(chosen - target) < 3e-14
            assert chosen > other
    # Critical moments are phase-independent for balanced coefficients.
    for p, target in [(4.0, 1.5), (6.0, 2.5)]:
        s = p / 2.0
        for j in range(1001):
            phi = 2.0 * math.pi * j / 1001.0
            assert abs(moment(s, 1.0, phi) - target) < 4e-13
    assert max_excess < 4e-13, max_excess
    assert max_formula_err < 3e-14, max_formula_err
    assert max_phase_loss <= 1e-14, max_phase_loss
    print(f"VERIFY_OK grid_checks={checks} max_excess={max_excess:.3e} max_formula_err={max_formula_err:.3e}")

if __name__ == "__main__":
    main()
