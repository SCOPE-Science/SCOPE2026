---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The normalized sphere kernel solves φ″+(d−1)φ′/s+φ=0 and φ′ has the sign of −J_{d/2}. At its first two positive critical points s₁ and s₂, the values are negative and positive respectively by the Bessel recurrence and the simple-zero crossing signs. The energy φ²+φ′² decreases, bounding the magnitude after each critical point by its value there. Together with monotonicity up to s₁ and between s₁ and s₂, this proves precisely the needed global minimum and exterior maximum. For s₁≤s<s₂, the normalized transform is at most b_d(s)+t(φ(s₂)−φ(s₁)) for every admissible set; no radial moment or bounded support is needed. Its upper envelope crosses zero near s₁ with derivative −A_d<0 in frequency, and continuity plus positivity at zero then bounds every first zero. For the explicit set, subtract the integral over v∈[1−t,1] and add the integral over v∈[a^d,a^d+t], where v=r^d and the integrand is φ(sv^(1/d)). This gives the claimed C¹ first variation and O(t²) error locally in s. The resulting simple root is first by positivity below a fixed neighborhood and monotonicity inside it. The recurrence at the two J_{d/2} zeros gives the displayed coefficient, with the factor s₁/d in the unscaled Fourier convention.

## originality

PASS

The supported distinct result is the sharp first-order variational constant and two-component realization over all measurable radial sets under the stated mass-transfer budget. Qualitative outward zero movement and standard Bessel extremum facts are not new. The actual nearby perturbation and convex-body results do not supply matching radial upper and lower bounds at fixed symmetric difference.

## value

PASS

The coefficient quantifies precisely how much the known outward movement can improve per unit of volume relocated in the natural radial perturbation class. It gives a dimension-dependent sharp benchmark and the shell at which to realize it, with uniform control even for unbounded competitors. This is not just another strict-improvement example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
