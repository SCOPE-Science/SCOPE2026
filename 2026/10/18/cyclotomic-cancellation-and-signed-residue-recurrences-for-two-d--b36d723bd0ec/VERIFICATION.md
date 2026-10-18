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
# Reproduction and mathematical limits

Run `python3 checker.py` alongside this document. Its residue-count dynamic program maintains counts of every congruence class in exact integers, starting with one empty string and adding either zero or the current radix-place digit. It compares each computed count after a complete orbit with the independent predicted exact recurrence. The test covers 373 parameter/length comparisons, including signed shifts modulo 9 and 27 and positive cancellations modulo 7, 15, 25, and 49. A second finite test covers 540 complete digit-prefix count vectors for perfect balancing.

Finite checking does not prove the unbounded-length assertion. The proof uses an exact root-of-unity identity valid for every nonzero character, with no numerical approximation: each `1+z` is `(1-z*z)/(1-z)`, and multiplication by two permutes the radix-power subgroup or its negative. The discrepancy then transforms by a signed permutation, which proves boundedness for all lengths and arbitrary eligible moduli.

No independent audit or external verification has been carried out.
