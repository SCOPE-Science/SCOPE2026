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

The analytic proof is primary. `artifacts/verify.py` supplies independent finite checks of the algebra and channel implementation.

The checker verifies that the unaligned Bell-overlap expression equals Zhang's printed Eq. (11) on twenty deterministic parameter points, that the displayed gain identity holds on the same grid, and that direct deterministic Bloch-sphere quadrature of the product-Pauli channel agrees with the closed aligned formula at four representative positive/negative coupling choices. It also checks representative large-\(|D|\) values for both signs of \(J\).

The executed package path returned:

`VERIFY_OK source_formula=20 gain_identity=20 quadrature=4 limits=2`

The quadrature and large-parameter evaluations are finite numerical checks only; they are not used as proofs of the identities or limits. The proof in `RESULT.md` establishes the statements for all real \(J,D\) with \(T>0\).
