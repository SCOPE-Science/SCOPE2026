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

# Verification of the fixed-composition two-deletion-ball spectrum

Execute `python3 verify.py` in the directory containing this file and `verify.py`, using standard Python 3 (no extra libraries). The program independently enumerates all binary source words of lengths 2 through 13, explicitly builds their distinct two-deletion descendant sets, and compares the counts with the proved per-word transition identity. It expands the alternating-run coefficient law as a separate dynamic program, and compares its complete histogram at every Hamming weight with direct enumeration. Lengths 14 through 18 receive coefficient-mass and exact-conditional-mean checks. The output on a successful execution is:

`PASS_FIXED_COMPOSITION_TWO_DELETION size_formula_words=16380 direct_lengths=2..13 formal_product_lengths=2..18 all_weights=verified`

The mathematical argument for arbitrary lengths is in `RESULT.md`; no finite execution can establish a universal theorem. The Gaussian limit uses the standard fixed-composition run-count central limit theorem and the explicitly proved order bound on the local singleton-run statistic. No independent external validation is claimed.
