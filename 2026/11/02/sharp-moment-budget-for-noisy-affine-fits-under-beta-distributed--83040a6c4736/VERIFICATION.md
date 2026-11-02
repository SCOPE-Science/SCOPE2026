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

# Reproducible checks and limitations

Execute `python3 verify.py` from a directory containing the included verifier. Only the Python standard library is required. Its deterministic midpoint integration checks the exact uniform sampling-range identity; it checks the strict mean-square threshold on a finite grid; and it compares quadrature of four-arcsine sampling to the analytically proved constant \(48/\pi^4\).

The test is numerical corroboration for selected cases and does not establish the universal parameter theorem. The proof in `RESULT.md`, especially the order-statistic integral, two-sided range/variance bound and beta endpoint exponents, is the mathematical justification. The four-sample arcsine coefficient is separately evaluated by an exact substitution.

The most similar three-observation beta-variance research record was accessible through an indexed summary; its complete text could not be inspected. Independent scientific and publication-priority review has not been performed.
