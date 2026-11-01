---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Endpoint conditions are exactly ∫u=-1 and ∫t u=0. For the mean -1 and |u|<=U, rearrangement against the switch point τ=(U+1)/(2U) shows the maximum first moment is U(1−2τ²)/2, giving U>=1+√2 for feasibility (U<1 is trivially impossible). A convex interpolation yields admissible moment zero. For nondecreasing u, derivative μ=Du≥0 has mass T=TV(u), and eliminating the initial level gives ∫s(1−s)dμ=1. With m=∫(1−s)dμ∈(1,U−1], Cauchy gives T>=m²/(m−1), minimal at m=U−1 in capped regime U<=3, equality forcing μ to one atom. For U>=3, s(1−s)<=1/4 forces T>=4, attained uniquely at s=1/2. Independently verified symbolic switch moments, cap threshold and saturation-branch continuity at U=3 and sampled caps; analytic inequalities cover all functions and cap values.

## originality

PASS

The nearest same-boundary primary source by Kaya proves uncapped minimum TV=4 and midpoint switch. It does not give the amplitude-capped law U<3 or its feasibility threshold. Manns and Schiemann treat integer-valued multidimensional BV controls, not this admissible family. A broader constrained-TV control theorem remains possible under different optimization terminology.

## value

PASS

Sharp actuator saturation threshold and unique minimum-switching-variation controls for a standard double-integrator boundary task. The exact cap-dependent branch is a natural refinement of the previously published uncapped minimum, not an arbitrary numerical subcase.

The dated certificate retains the supplied scientific assessment, sources and limitations.
