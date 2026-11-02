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

# Verification and limits

`verify.py` requires Python, NumPy and SciPy and is run by `python verify.py`.

It evaluates the exact Gaussian-mixture score, two algebraically independent integrals for \(B\), the strict expectation bound governing the correction term, and the endpoint curvature for ten distinct signal strengths in the complete log-concave interval. It independently computes mixture entropies at four nearby mixing weights using four normal components and numerical finite differences at five moderately non-Gaussian inputs. The fourth-order coefficient is compared at four decreasing signal strengths. A full run passed 57 bounded checks.

The proof's universal quantified step is the strict Gaussian-weight covariance inequality for every \(0<v\le1/3\), not the numerical samples. The published general endpoint identity is cited and applied with its smoothness and variance-one hypotheses explicitly verified. The negative fourth cumulant excludes the centered Gaussian scale-mixture theorem's hypothesis. Independent mathematical review and independent publication-priority validation have not been performed.
