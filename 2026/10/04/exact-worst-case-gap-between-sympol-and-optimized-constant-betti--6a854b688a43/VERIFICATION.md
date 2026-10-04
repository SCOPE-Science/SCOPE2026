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

The packaged script `verify_sympol_gap.py` checks the algebraic structure of the claim with deterministic examples. It verifies:

- the Bernstein expansion of the optimized constant-bet product;
- the exact values \(b_{n,k}\) and the location of their minimum at the central index or central pair;
- the universal lower bound obtained by evaluating the product at \(\lambda=k_*/n\), where \(k_*\) maximizes \(A_k\);
- the even and odd closed forms for \(1/b_n\);
- numerical convergence of the sparse family with central nonzero coordinates toward the sharp factor.

The checker is not a proof of originality and does not replace the analytic uniform-convergence argument used for sharpness. It is intended to catch transcription, indexing, and arithmetic errors in the packaged formulas.
