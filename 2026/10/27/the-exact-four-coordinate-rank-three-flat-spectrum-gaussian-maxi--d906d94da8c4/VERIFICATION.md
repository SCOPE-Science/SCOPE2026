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

# Reproducibility and limits

Run `python verify.py` with Python 3, SymPy, NumPy, and SciPy. The script uses exact rational Gram matrices and symbolic projections for all \(16\) possible null-vector sign choices. It verifies \(261\) finite assertions, including class counts, all six pairwise projections per sign choice, closed-form expectation identities, and exact projector properties. A deterministic seeded Sobol integration uses \(2^{18}\) standard Gaussian points to corroborate each orbit value independently of the facet evaluation. The captured output is in `verification_output.txt`.

The mathematical proof of the exact minimum is given in `RESULT.md`. Finite assertions and quadrature are supplementary diagnostics only; they cannot certify Gaussian integration by parts, a probability law at infinitely many points, or historical novelty. The public literature explicitly provides general evaluation formulas, and no claim to independent mathematical audit is made.
