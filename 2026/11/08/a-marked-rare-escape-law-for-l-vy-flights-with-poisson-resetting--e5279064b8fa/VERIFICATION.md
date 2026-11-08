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

The analytical chain is a marked short-time Lévy–Itô one-big-jump limit, a geometric renewal identity for the successful excursion, a Laplace-transform limit, and a stopped Poisson martingale variance identity. The Lévy jump intensity and all tail normalizations are explicit in `RESULT.md`.

The reproducibility command is `python CHECKER.py` with Python and SciPy. It tests the mark-density integrals, side weights, centered Pareto tail, joint Laplace factorization, and exact Cauchy Lévy-density normalization across a parameter grid, and then reports a seeded coarse-grid Cauchy-process diagnostic. The finite checks do not establish the infinite-population or large-domain limit and have mesh error.

The scientific review is same-model only. Independent audit is not performed. No independent scientific validation is asserted.
