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

The proof reduces the restricted square-zero equations for an arbitrary characteristic-two field to three coordinate conditions for a vector, a two-by-two matrix, and a second vector. The nonzero-constant stratum is a product of punctured affine two-space with affine two-space; each point of its complement is shown to be a polynomial specialization of this stratum. Matrix-rank and finite-field counts follow from a complete zero/nonzero constant split.

Run `python verify.py` from the extracted folder. The verifier directly builds the four-by-four linear matrix of each derivation using Leibniz, and checks its square and rank. Exact exhaustive counts over the binary field and its degree-two extension return `VERIFY_OK`. Direct finite enumeration does not prove geometric irreducibility or the assertions for fields not enumerated; those are proved symbolically in the accompanying result.

The statement concerns the reduced underlying variety, not the nilpotent thickening of its defining scheme. The self-review is completed; independent audit is not performed.
