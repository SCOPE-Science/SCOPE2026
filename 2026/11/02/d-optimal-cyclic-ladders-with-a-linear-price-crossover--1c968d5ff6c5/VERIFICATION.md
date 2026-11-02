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

# Verification record

Execute `python3 verify_prism.py` with standard-library Python 3. The check performs integer Bareiss elimination on grounded Laplacian minors for \(n=3,\ldots,8\) and compares against the Chebyshev tree polynomial; numerically verifies the cycle resolvent and scalar monotonicity; evaluates unrestricted independently weighted feasible competitors across several prices and sizes; and checks extreme-price limits and the linear-price transition. The exact output observed is: `PASS: 23668 checks; exact integer matrix-tree identities, spectral resolvent, monotonicity, independent-weight competitors, boundary prices, critical crossover`.

The tests cover finitely many parameter values, not all real prices or all graph sizes. Universal claims are justified by the separate analytic proof in `RESULT.md`. The public comparison does not resolve every possible unlocated specialist source and is not an independent review.
