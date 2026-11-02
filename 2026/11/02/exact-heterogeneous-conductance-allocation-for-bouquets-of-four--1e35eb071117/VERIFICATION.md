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

# Reproducibility and verification

Use `python verify.py` with Python 3, SymPy and NumPy. The code reconstructs all weighted graph Laplacians from explicitly enumerated edges rather than reusing the resistance-decomposition formula. For each sampled positive rational conductance vector, it directly inverts a grounded Laplacian and computes \(N\operatorname{tr}(L_g^{-1})-\mathbf1^{\mathsf T}L_g^{-1}\mathbf1\). This exactly equals the decomposed Kirchhoff index in 52 independently specified rational examples, with up to four petals.

The script also checks the symbolic quartic derivative and equal-price factorization, verifies budget/positivity/stationarity in 84 independently sampled priced systems, and performs full-matrix two-sided perturbation tests in the unrestricted edge variables. Its recorded execution finished with `PASS: 1078 exact and numerical assertion groups`.

These computations do not exhaust all real prices, budgets or petal counts. The mathematical proof of the all-parameter statements is in `RESULT.md`; in particular it verifies strict convexity, symmetry without restricting the competitors, exact resistance identities, positivity/uniqueness of the quartic root, and sharp cross-petal budget allocation. No independent mathematical audit has been performed.
