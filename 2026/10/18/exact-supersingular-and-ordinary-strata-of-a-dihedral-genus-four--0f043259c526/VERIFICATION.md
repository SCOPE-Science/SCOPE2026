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

# Computational verification and proof boundaries

Run `python3 verification/check_p11.py` using Python 3 without third-party packages. The checker expands the fifth power in the bivariate polynomial ring over \(\mathbf F_{11}\), extracts all 16 entries required by the Hasse–Witt formula, and checks the claimed coefficient matrix. It checks the nonsquare discriminant and norm, the smooth rational-parameter outcomes, and elementary rational-point counts. Successful output is `VERIFY_OK`.

The checker does **not** enumerate every point of the algebraic closure. The infinite-field parameter count follows from the exact quadratic irreducibility and nonsquare norm argument in RESULT.md, and supersingularity follows from the genus-two isogeny decomposition. The finite test is additional reproducibility, not a substitute for those proofs. The geometric-isomorphism criterion comes from the cited primary theorem. Independent validation has not been performed.
