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

# Reproduction and limits

The exact-integer checker `verify_modes.py` computes generating-polynomial coefficients by convolution, normalizes neither parity subarray (normalization preserves modes), identifies **all** tied maxima, and checks the claimed parity-mode distances. Run with `python3 verify_modes.py`. The recorded `verify_output.txt` documents 125439 admissible cases and explicit sharpness examples. Every integer multiplication and comparison is exact. The enumerations include boundary simplex parameters; strictly positive rational lattice parameters and random strictly positive larger arrays are tested separately.

These are stress tests only. The proof of all quantifiers uses oriented Hermite--Biehler interlacing, the Stieltjes partial-fraction representation, and the deletion-mode lemma in `RESULT.md`. No symbolic/numerical test is an infinite-dimensional certification. Independent audit has not been performed. Historical coverage by broader modal-interlacing work remains a recognized risk.
