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

The mathematical statement concerns the analytic Bargmann--Fock projection on the complex plane, restricted to an expanding rectangle. The proof is analytical: Gaussian kernel calculus, rectangle overlap integrals, a complex covariance matrix, analytic continuation of an absolute-Gaussian-moment formula, and exponentially small tail bounds.

To replay the algebraic checks, install SymPy and run `python3 CHECK.py`. The program verifies the determinant-one quadratic matrix, exact covariance inversion, the nine cross-correlations, the consequent corner constant, and its strict positivity. A successful run prints `PASS`. This finite symbolic test does not prove the operator trace identities or the Gaussian tail bound and is not independent review. No independent mathematical audit has been performed.
