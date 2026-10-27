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

# Reproducible verification

The included `verify_stewart_symmetry.py` requires Python 3 only. Run `python3 verify_stewart_symmetry.py` from the directory containing this file. Expected terminal line begins with `STEWART_SYMMETRY_PASS`.

The checker enumerates all six three-symbol Stewart patterns, reconstructs the possible length-eight factor set for every initial pattern from the exact tail languages of lengths two and three, and confirms the complement/reversal overlap vector. It checks direct prefixes for all 1,296 four-pattern directives (with a fixed legal extension); it independently checks the base-three reflection property for all directives of lengths one through four, totaling 111,150 skeleton positions. Finally, it checks factor sets from three 25,000-symbol prefixes for lengths one through one hundred.

These are finite validations only. The general reverse-complement-closure theorem uses the proof that every factor can be relocated to fully assigned Toeplitz-skeleton positions, and that every finite skeleton has the stated reflected-complement involution. The infinite cutoff follows from the exhaustive length-eight classification and factoriality. No external mathematical audit has been performed.
