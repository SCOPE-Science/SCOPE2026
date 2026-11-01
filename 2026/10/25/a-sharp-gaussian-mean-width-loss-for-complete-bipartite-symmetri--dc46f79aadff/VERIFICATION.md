---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

PASS. For full A_{n-1} root polytope the support is global maximum minus global minimum; for K_{p,q} it is the larger of two cross-part ranges. A strict loss occurs precisely when the extremal ordered indices share a part, giving [p(p-1)+q(q-1)]/[n(n-1)]. Gaussian coordinate projection to H preserves all root dot products; four independent joint upper/lower Gumbel extremes with log alpha/log beta shifts give the stated nonnegative limiting loss with zero mass 2 alpha beta. The spherical radial factor is handled via chi radius independence and Slutsky; bounded Gaussian extreme moments and E chi_d/sqrt(d)->1 justify mean convergence. Gumbel max-stability plus difference-of-Gumbels logistic integration yield E D=-log(alpha beta)-1. At positive fixed limiting proportions the identical first-order 4 sqrt(2 log n)/sqrt(n) and circumradius sqrt 2 follow. The exact scale factors 2 a_n/sqrt(d) match the support/width convention.

## originality

PASS

PASS, best knowledge: the new specific contribution is the sharp nonnegative four-Gumbel loss law, exact strict event, and evaluated imbalance-dependent scaled mean between two canonical graph-root polytopes. Facet/Ehrhart geometry and classical Gaussian extreme statistics are antecedents; their combination is not automatically a prior theorem for this pair of Euclidean widths.

## value

PASS

PASS. Comparing two canonical graph-root bodies that share circumradius and first-order mean width makes the exact second-order loss a motivated geometric statistic. The nontrivial limiting zero atom, angular strict-event probability, and imbalance-dependent mean describe a genuine sharp distinction useful to stochastic geometry and graph polytopes, not merely a renamed extreme-value theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
