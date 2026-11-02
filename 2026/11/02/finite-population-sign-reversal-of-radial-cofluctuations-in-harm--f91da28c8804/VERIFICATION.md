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

Run `python verify.py` with Python 3 and no additional packages. The executed checker produced `PASS: 1421 exact rational assertions, including complete finite-state examples`.

The checker derives the one-particle complex mixed moments from the stationary generator recurrence rather than simply restating a numerical table. It verifies the two independent published moment formulas and contracts explicit center-projection rows; it then exhaustively enumerates independent four-direction isotropic vectors for small populations and compares their squared-radius covariance with the general contraction identity. It checks both models at multiple positive rational persistence values, multiple finite populations and the exact four-particle opposite-sign example.

No finite grid certifies a theorem over all positive real parameters or all positive integers. The analytical proof in `RESULT.md` independently covers that domain by generator identities, a fourth-order contraction, and exact polynomial sign analysis. The paper's one-particle radial moments are background formulas, also reconstructed from the generator in this package. The limit of this verification is self-review only; independent audit has not been performed.
