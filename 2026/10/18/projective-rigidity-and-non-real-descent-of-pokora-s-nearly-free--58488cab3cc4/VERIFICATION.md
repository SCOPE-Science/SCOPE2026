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
Execute `python3 verify.py` with any standard Python 3 interpreter. It uses exact rational arithmetic and Gaussian-integer polynomial coefficients without nonstandard dependencies. The recorded output is `verify_output.txt`.

Checks: all twenty-one line pairs; precise multiplicities and five triple points; all collinear triples; eight compatible projective-frame permutations; exactly two valid seven-line projectivities; exact involution square; polynomial invariance of both conics; nonproportionality of original and conjugate conics. A separate harmless auxiliary check shows the free companion can be put in real coordinates, which is not part of the new non-descent claim.

Limits: this code performs a finite exact certificate for a fixed arrangement. The full impossibility of any other complex projectivity is established by the frame-exhaustion proof in `RESULT.md`. It does not certify all published literature or provide independent scientific validation.
