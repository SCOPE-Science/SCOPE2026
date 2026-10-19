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

## Executed mathematical checks

Execute `python verify.py` from the directory containing the embedded file. Its exact arithmetic (prime fields and a polynomial-basis representation of the field of four elements) exhaustively enumerates the homomorphism equations for cases `(ell,r,q)=(1,1,2),(1,2,3),(2,2,2),(2,2,3),(2,2,4),(3,2,2),(2,3,2)`. For all seven, actual algebraic endomorphism counts and composition-idempotent rank histograms agree with the proposed formulas. Additionally the program examines all `2**16=65536` binary four-by-four matrices (including those failing the row-sparsity condition) for the two-two-cycle algebra and confirms `25` endomorphisms and rank strata `[1,6,1]`. It prints `ALL_EXACT_CHECKS_PASSED` on success.

The checks use direct products and matrix rank rather than treating symbolic counts as oracles; their finite extent does not prove arbitrary-field or arbitrary-size assertions. All infinite-scope statements are deduced in `RESULT.md` from the basis-independence and cyclic-scalar arguments. Independent external validation is not performed.
