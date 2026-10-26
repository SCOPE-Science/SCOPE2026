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

# Verification notes

The proof in `RESULT.md` is an analytic derivation based on the exact block singular-value decomposition and the Gaussian least-squares/chi-square ratio distribution. Run `python verifier.py` in an environment with NumPy and SciPy to check the exact deterministic projection and the predicted law against independently assembled Gaussian matrices. The verifier prints `PASS 812 checks; tested deterministic algebra, full Gaussian sketches and beta-law sampling`.

Finite experiments cannot prove an almost-sure or infinite-population law. In particular, asymptotic tail and moment assertions follow from the beta density in the written proof, not from finite Monte Carlo sampling. Numerical pseudoinverses may be ill conditioned in floating-point arithmetic, which is not part of the exact-arithmetic theorem.
