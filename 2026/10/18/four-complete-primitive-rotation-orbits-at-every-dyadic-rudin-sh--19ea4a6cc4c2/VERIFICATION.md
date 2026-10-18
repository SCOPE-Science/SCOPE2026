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

# Reproduction and verification

Run `python3 verify_rudin_rotations.py` in the same directory as this document. The program requires Python 3 with standard library only, and prints `VERIFY_OK` on success. It checks, for every exponent from 3 through 12, all four coded block lengths, primitive status, exact one-count profiles, cyclic pattern-count separation, and the two-scale recurrence matrix. It separately constructs the Rudin–Shapiro sequence directly from binary digits and verifies every rotation of each four-state block appears for exponents 3 through 9. It compares the independent morphic coding with direct digit generation at exponents up to 8 and identifies both alternating triple contexts used in the proof.

The checks are finite and do **not** certify an infinite statement. The proof of the all-exponent lower bound and primitivity is in `RESULT.md`. Nothing here asserts the absence of additional complete cyclic classes, an exact Lie-complexity formula, or independent validation. The originating 2014 cyclic-complexity source and later Lie-complexity literature are cited in `RESULT.md`.
