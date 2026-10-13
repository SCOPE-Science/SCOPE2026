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

# Reproduction and scientific limits

Execute `python3 verify.py` with Python 3 (standard library only) in the same directory as the file. The verifier independently expands the finite computational-basis tensor for small system counts, checks the normalized analytic overlap including nonzero azimuths, compares the stationary equations against a dense latitude grid, and corroborates the rational six-qubit value and approach to the stated asymptotic limit. Expected output: `VERIFY_OK direct_tensor_n=4..8 grid_n=4..16 special_n6=2/9 asymptotic_n=25,80,200`.

The calculation for all qubit counts is established in RESULT.md by a known symmetric-product optimization theorem, an exact derivative, strict ratio monotonicity, and uniform explicit bounds. Grid checks are not exhaustive and do not certify infinitely many sizes. Source access and semantic research comparisons do not independently certify research originality; the significant priority risk from general positive-Dicke optimization literature is stated in REVIEW.md.
