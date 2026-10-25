---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For γ>1 the physical map F is positive, strictly decreasing, bounded, with one fixed point x* and a strictly increasing p1↔x* correspondence. The multiplier |F’(x*)|=p2 Φγ(γx*), and log derivative Φ’/Φ=1/t−1+(5/4)R(t) is strictly decreasing, gives unique maximizer tγ∈(1,8/3) and two critical p1 values when p2>1/max Φ. The Schwarzian identity SF=γ²[−1/2+15R²/32]−p2² h’²/2<−49γ²/128 makes Q=( (F²)’ )^{−1/2} strictly convex. It ensures at most three F² fixed points; a primitive two-cycle forces |F’(x*)|>1, excluding both multiplier -1 endpoints. If multiplier>1, H=F²−id has opposite signs near x* and at 0,∞, forcing the other two fixed points and their attraction. Monotone F² guarantees convergence of all even iterates, establishing global basin classification. Numerically rederived γ=3 p2crit 28.34317352186779 and p2=30 thresholds 1.14955199992004,4.04550763761918; illustrative numerics are not proof.

## originality

PASS

Best-of-knowledge PASS. The originating physical-model paper exhibits monotone nonchaotic behavior and numerical fixed/cycle regimes, but does not establish explicit sharp γ-dependent p2 threshold, complete re-entrant p1 window, global uniqueness and neutral endpoint convergence as a theorem. Classical negative Schwarzian techniques are known and expressly credited; applying them here with analytic sharp thresholds is the asserted advance.

## value

PASS

Sharp global phase classification of a concrete published physical recurrence converts phenomenological numerical transitions to an all-parameter theorem, with exact neutral endpoints and re-entrant two-cycle window. Distinct from reiterating linear stability or simulating a few initial values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
