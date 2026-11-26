---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Set r_k=√(H‖Qx_k‖). The exact update is r_k(Q+r_k I)^−1 x_k; each spectral projection is multiplied by the positive scalar r_k/(λ+r_k). Thus x_k stays nonzero, and its norm is nonincreasing. Bounding r_k by R=√(H λ_max ‖x_0‖) gives the uniform strict norm contraction R/(λ_min+R), so r_k→0. For any active μ>λ_* the ratio of the μ component to the λ_* component contracts by at most (λ_*+R)/(μ+R)<1, while the vector within the λ_* eigenspace stays a positive multiple of its original projection. This covers ties, inactive lower modes and a single active eigenspace. With y_k=x_k/‖x_k‖ the normalized iterate quotient is √(H‖Qy_k‖)‖(Q+r_k I)^−1 y_k‖; the normalized gradient quotient is √H‖Q(Q+r_k I)^−1y_k‖/‖Qy_k‖. Their limits by the spectral-direction result and continuity are √(H/λ_*) and √H/λ_*. Both are positive and finite, so the exponent is exact under the stated hypotheses, not just an upper bound.

## originality

PASS

The update and upper-bound order 3/2 are established. The supported distinct claim is the exact positive leading constants for every nonzero quadratic trajectory and their selection by the initially active spectral subspace, including when it excludes the global bottom of the spectrum. The inspected known upper bounds or more general convergence classes do not yield those equalities.

## value

PASS

The result resolves a natural sharpness question for an established method on its canonical quadratic test class. It rules out a faster asymptotic order on each nonzero trajectory, and identifies which curvature controls both measured constants. For example, the global lowest eigenvalue can be held fixed while changing the initial invariant subspace, changing the asymptotic constants despite keeping the algorithm and problem fixed. The link between direction, invariant subspace and exact positive leading coefficient is the useful content; geometric convergence alone or the single scalar mode would not suffice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
