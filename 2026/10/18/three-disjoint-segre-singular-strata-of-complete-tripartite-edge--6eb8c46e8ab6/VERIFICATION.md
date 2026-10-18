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

# Verification evidence and boundaries

The standalone artifact `verify.py` is a standalone exact-arithmetic checker. Run it with `python verify.py` in a directory containing that file. It confirms the chart decomposition formulas for all 192 choices of a pair of parts and part sizes between one and four, checks expected Segre monomial Hilbert functions for degree zero through four and third-part sizes up to six, and checks exact tangent-rank formulas for the rank-one matrix model. It also tests component dimensions in four representative examples.

Expected output: `VERIFY_OK charts=192 segre_sizes=1..6 degrees=0..4 examples=4`.

The general statement rests on the proof of the affine chart semigroup isomorphism and on standard geometry of Segre determinantal cones, not on finite enumeration. No claim is made that these checks establish uniqueness in the literature or independent certification.
