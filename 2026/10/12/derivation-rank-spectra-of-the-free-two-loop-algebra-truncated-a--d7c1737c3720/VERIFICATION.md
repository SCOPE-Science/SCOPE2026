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

The argument derives all derivations from the images of two generators and reduces every operator rank to a two-by-two linear block, its tensor-square Leibniz block, and an arbitrary connecting block. The classification includes characteristic two and nonsplit characteristic polynomials.

The standalone `verify.py` computes the full Leibniz linear system in two characteristics, exhaustively enumerates ranks of all derivations over fields of orders two and three, and samples the nonprime field of order four. Its final output is `VERIFY_OK_FREE_TRUNC_DERIV` when the asserted comparisons hold. These finite experiments do not certify the arbitrary-field theorem; the general argument is the block-rank calculation in the mathematical proof.

No independent mathematical validation has been performed.
