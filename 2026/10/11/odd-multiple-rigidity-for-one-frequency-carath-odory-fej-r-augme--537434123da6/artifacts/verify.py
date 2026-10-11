#!/usr/bin/env python3
import math

TOL = 5e-10
base_cases = 0
resonance_checks = 0
perturbation_checks = 0
worst_base = 1.0
worst_perturbed = 1.0

for m in range(3, 31):
    alpha = math.pi/(2.0*m)
    C = math.cos(alpha)
    S = math.sin(alpha)
    lam = 1.0/C
    b = ((-1.0)**m)*math.tan(alpha)/m

    def P(theta):
        return 1.0 + lam*math.cos(theta) + b*math.cos(m*theta)

    for theta in (math.pi-alpha, math.pi+alpha):
        assert abs(P(theta)) < 2e-13
        assert abs(math.cos(m*theta)) < 2e-13
        assert abs(math.cos(theta)+C) < 2e-13

    # Corroborate the global supporting-tangent inequality on a dense y-grid.
    local_min = 1.0
    for j in range(6001):
        y = -1.0 + 2.0*j/6000.0
        Tm = math.cos(m*math.acos(max(-1.0,min(1.0,y))))
        gap = Tm - (m/S)*(y-C)
        local_min = min(local_min, gap)
    assert local_min > -TOL

    # Corroborate nonnegativity directly on the circle.
    circle_min = 1.0
    for j in range(8001):
        theta = 2.0*math.pi*j/8000.0
        circle_min = min(circle_min, P(theta))
    assert circle_min > -TOL
    worst_base = min(worst_base, circle_min)
    base_cases += 1

    for n in range(2, 6*m+2):
        if n == m:
            continue
        q = ((-1.0)**n)*math.cos(n*alpha)
        resonance = (n % (2*m) == m)
        assert (abs(q) < 2e-12) == resonance
        resonance_checks += 1

    tests = sorted(set([2, m-1, m+1, 2*m, 3*m, 3*m+1, 5*m]))
    for n in tests:
        if n < 2 or n == m:
            continue
        q = ((-1.0)**n)*math.cos(n*alpha)
        if abs(q) < 1e-11:
            continue
        def R(theta):
            return math.cos(theta) + (2.0*C/q)*math.cos(n*theta)
        for theta in (math.pi-alpha, math.pi+alpha):
            assert abs(R(theta)-C) < 2e-11

        bound = float('inf')
        samples = []
        for j in range(10001):
            theta = 2.0*math.pi*j/10000.0
            p = P(theta)
            r = R(theta)
            samples.append((p,r))
            if r < -1e-12:
                bound = min(bound, p/(-r))
        assert math.isfinite(bound) and bound > 0.0
        eps = 0.2*bound
        mn = min(p+eps*r for p,r in samples)
        assert mn > -2e-9
        worst_perturbed = min(worst_perturbed, mn)
        perturbation_checks += 1

print(f"VERIFY_OK base_cases={base_cases} resonance_checks={resonance_checks} perturbation_checks={perturbation_checks} worst_base={worst_base:.3e} worst_perturbed={worst_perturbed:.3e}")
