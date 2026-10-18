---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Run `python verify.py` using Python 3 and the standard library. The script enumerates all \(n^{n-2}\) Prüfer words for each integer \(2\le n\le7\). It checks the exact finite covariance against independently computed empirical moments, the root-even class distribution, and the conditional leaf expectation for every possible class size. It also checks the sign of the exact expression for a finite range as a diagnostic only.

The analytic argument in `RESULT.md` proves the limit \(1/(8e)\). Exhaustive checks on finitely many tree sizes and numerical quadrature are reproducibility aids, not a proof of an infinite statement or a proof of originality. The conditional occupancy law uses the classical bipartite Prüfer encoding. Possible implicit prior coverage is identified in the relationship-to-prior-work discussion. Independent auditing has not been performed.
