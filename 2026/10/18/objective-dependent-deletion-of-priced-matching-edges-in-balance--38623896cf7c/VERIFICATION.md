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

From the directory containing this document, run `python verify.py`. It requires Python 3, NumPy, SymPy and SciPy. The observed result was `PASSED 2094 finite checks`.

The script constructs the weighted graph Laplacian directly for each tested assignment rather than using only the spectral formula. It computes rational inverse traces for small networks, reconstructs the expected eigenvalues, verifies exact symbolic derivative identities and the price-threshold separation, compares feasible asymmetric allocations, checks the budget normalization, and examines asymptotic limits with large finite parameters.

The proof's infinite claims depend on strict convexity, the complete eigenvalue decomposition and sign of the rational derivative; no finite test is used as an exhaustive or infinite-domain certificate. No independent audit or independent validation has been performed. Source novelty remains subject to literature coverage limitations described in `REVIEW.md`.
