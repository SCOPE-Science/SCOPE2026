---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

For \(Q=y^2+z^2\), direct differentiation in the inspected source tree gives exactly \(LQ=-2cy^2-2bz\), so stationarity yields \(b\mathbb E[z]=-c\mathbb E[y^2]\). Stationarity of \(z\) gives \(\mathbb E[xy]=b\), which rules out \(y=0\) almost surely and makes the mean-height inequality strict. Any nonempty compact invariant set would carry an invariant probability measure, so containment in \(z\ge0\) contradicts the negative mean. The divergence is exactly \(-a-c+kz\); compact support makes the derivative cocycle bounded, and Liouville plus ergodicity identifies the Lyapunov-exponent sum with the mean divergence. Substituting the stationary height balance proves the displayed law.

## originality

PASS

The complete open primary Dong--Wang article prints the same system, its pointwise divergence, numerical Lyapunov spectra, bifurcations, coexisting attractors, unstable periodic orbits and circuit realization. It does not derive the cancellation in \(L(y^2+z^2)\), the resulting negative stationary mean height, the half-space exclusion, or a system-specific exact Lyapunov-sum formula in terms of \(\mathbb E[y^2]\). Resultary searches returned the assigned finding and analogous laws for different flows, with no stronger same-model predecessor.

## value

PASS

The source interprets hyperchaos partly through numerical Lyapunov spectra and state-dependent divergence. The audited balance turns that into an exact recurrent-statistics law, fixes the sign of the mean height, excludes an entire half-space for compact recurrence and gives a consistency equation for any claimed asymptotic spectrum. Those are substantive model-level constraints.

The dated certificate retains the supplied scientific assessment, sources and limitations.
