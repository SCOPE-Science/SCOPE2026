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

# Reproducibility and proof boundaries

Run `python3 check.py` with a standard Python 3 interpreter. The output saved as `check_output.txt` is reproducible. The program performs exact arithmetic checks of six low-rank tensor products by a tableau algorithm independent of the displayed decomposition, and verifies all coefficients of the full fourth-moment polynomial through Weyl constant-term integration. It checks the exact derivative polynomial; a final bisection reports approximate algebraic values.

Analytic checks that must be read rather than inferred from the finite program: strict maximization of \(q=xy\) for fixed \(s=x^2+y^2\) and \(z\); exclusion of the pure adjoint boundary; the unique positive cubic zero by Descartes' rule; the sign of the derivative on the positive real axis; and simultaneous phase congruences with all coefficients nonzero. Their proofs are in `RESULT.md`.

No numerical sweep establishes an infinite-domain claim. No independent audit was performed. Novelty and historical coverage remain subject to independent bibliographic checking.
