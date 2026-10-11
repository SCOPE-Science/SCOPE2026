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

The proof is exact. Writing \(1+r=\int(1+\lambda)d\nu\) as the product of the square roots of the variance kernel and \(1-\lambda^2\), Cauchy--Schwarz gives \(\tau_g(1-s)\ge(1+r)^2\). Equality forces all spectral mass away from \(-1\) onto one point; solving the two moments gives the stated \(q\) and mass. The displayed symmetric four-state chain has eigenvalues \(-1\) and \(q\) on the two observable components and realizes every feasible pair. In the aperiodic class, positive \(-1\) mass forbids equality, while the recalibrated lazification preserves the target first two moments exactly and approaches the boundary. The package exact-rational checker independently exercises these identities.

## originality

PASS

Best-of-knowledge originality passes. The primary literature supplies the reversible spectral representation, the standard asymptotic-variance kernel, and the fact that autocovariances form a moment sequence, but no inspected statement gives the exact lower envelope from only the first two normalized moments, its equality support, or the all-pair finite-state realization and aperiodic sharp infimum. Resultary and targeted searches found no implication-complete prior theorem.

## value

PASS

Asymptotic variance directly controls Monte Carlo error. The theorem gives the exact best guarantee obtainable from the first two autocorrelations, strictly improves the one-lag Jensen bound in the nondegenerate case, and completely characterizes global and aperiodic sharpness. This is a natural constrained spectral-moment classification rather than an arbitrary inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
