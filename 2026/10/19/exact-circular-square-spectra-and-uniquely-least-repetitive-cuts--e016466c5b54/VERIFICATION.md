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

`python verify.py` uses only the Python standard library and reconstructs each finite cyclic Thue–Morse block independently from bit-parity and substitution. It scans all possible circular square starts and half-lengths at levels 2 through 10, compares the full nonzero half-length spectrum, exact totals, weighted sums, maximizing cut sets and average formula, and checks larger blocks through level 15 at all theoretically permitted half-lengths. It also exhausts all 96 local three-source-symbol by sixteen-offset configurations, proving the finite local lemma used in the global induction. The boundary cases for the shortest substitution levels are directly checked.

Actual successful execution output:

`VERIFY_OK local_6x16_cases=96 full_spectrum_levels=9 cyclic_square_occurrences=1694 cut_profiles=2044 larger_period_checks=115`

Full verification of every high-level circular factor is not claimed. The all-order theorem is justified by its symbolic desubstitution argument and exhaustive finite local reduction; numerical checks independently corroborate it. The proof invokes the established external Pansiot–Brlek classification and aligned-occurrence lemma, rather than independently proving those foundational theorems. An independent expert audit has not been performed.
