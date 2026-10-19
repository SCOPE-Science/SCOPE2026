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

`verify_mobius.py` was executed with the dependencies in `requirements.txt` and printed `VERIFY_OK 20439 assertions`.

The program checks each Fourier mode for all integers \(4\le m\le120\), compares the proposed transition weights with independently optimized full-frequency linear programs for \(4\le m\le83\), constructs and diagonalizes the complete transition matrix for \(4\le m\le32\), checks positive three-mode lower-bound identities at many feasible probability pairs, verifies the odd/even prism relations, and numerically tests high-dimensional limits. Computed matrices are symmetric and stochastic with nonnegative edge/loop masses.

All assertions were obtained from the attached program as written. Finite sampling does not prove any infinite-dimensional quantifier, and numerical tolerances do not establish exact algebraic identities: the rigorous identities and limit statements appear in `RESULT.md`.

Independent audit has not been performed.
