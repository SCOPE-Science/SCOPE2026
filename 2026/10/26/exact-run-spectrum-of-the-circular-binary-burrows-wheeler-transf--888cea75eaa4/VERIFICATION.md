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

# Reproducibility

Run `python3 verify_bwt4.py` using Python 3 and the standard library. The script exhaustively enumerates the 365 ordered weak-rank and gap-difference classes, clears one universal denominator, and verifies five integer-polynomial identities exactly; this proves each rational generating-function expression for every input length when combined with the layer classification. It also directly sorts all rotations for 2401 ordered gap tuples with entries at most 6 and for every binary weight-four word of length 4 through 19. The observed finite checks corroborate but do not substitute for the all-length symbolic classification.

The output must end in `PASS`. Mathematical limits: this is not a proof for weights greater than four, and the literature comparison is not an independent priority certification.
