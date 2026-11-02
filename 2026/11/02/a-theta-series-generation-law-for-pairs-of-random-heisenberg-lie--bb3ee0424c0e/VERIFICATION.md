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

# Verification and reproducibility

Run `python3 artifacts/verify.py` with Python 3 and its standard-library `decimal` arithmetic for high-precision limit checks. The checker generates all row-reduced-echelon subspaces and tests Lie-bracket closure, not merely the analytic prediction. In five prime-field examples it counts every ordered generating pair, obtaining the exact integer values stated in the result. It separately evaluates the finite \(q\)-Gaussian sum for two ordinary uniformly chosen subspaces and the infinite theta approximation at four growing dimensions for each of three field sizes. The reported result was `VERIFY_OK 5 exhaustive configurations and 12 asymptotic finite-sum checks`.

No finite enumeration establishes the all-\(n\) theorem or the convergence-rate bound. Those follow from the explicit generation/spanning equivalence, Gaussian-binomial identities, and dominated summation with uniform tails proved in `RESULT.md`. The extension-field statements are proved by the algebraic argument but not exhaustively checked in this Python script. Independent validation has not been performed.
