---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The digit functions h_j are orthogonal and centered under Lebesgue measure. The observable transition operator gives P h_0=p h_1 and P h_j=p h_(j+1)+(1-p)h_(j-1) (j>=1). Its zero-to-zero 2m paths are Dyck excursions, each weighted [p(1-p)]^m, explaining C_m. Pair counting yields exact finite variance; Catalan series sums to 1/max(p,1-p), with unique neutral maximum at p=1/2. Stirling C_m/4^m=(pi m^3)^(-1/2)+O(m^-5/2) gives the sqrt(N) deficit coefficient 8 sqrt(2N/pi); differentiating the Catalan series gives the offcritical intercept. Independently propagated finite-digit stochastic operator for 25 parameter/lag checks; finite check not proof.

## originality

PASS

Homburg–Kalle establish the random affine IFS and balanced uniform stationary measure, and study synchronization/two-point laws. The exact one-point temporal first-digit Catalan covariance/variance with critical correction is not stated by those results. Pelikan-map literature uses a different nonuniform inverse mechanism. No equivalent same mathematical model symbolic-dynamics formula located in scoped searches, subject to alias risk.

## value

PASS

One-time stationary marginals are parameter-independent, making parameter-sensitive temporal covariance a natural and nontrivial observable. The precise Catalan law, sharp maximum at the zero-Lyapunov transition and distinct finite-size corrections give a complete temporal classification, not just isolated finite simulations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
