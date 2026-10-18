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
# Verification notes

The standalone `verify.py` requires standard Python 3 only. Execute `python3 verify.py` in this directory. It checks 44 base/level pairs for \(3\le b\le9\) with \(b^k\le60000\), covering all 44 available cases and reaching word length \(59049\). Two separate word generators agree: substitution iteration and positional base-digit membership. Lexicographic cyclic shifts are ranked by a doubling algorithm; in 29 short cases, directly sorting all complete rotations gives identical order. Every leading-zero class is checked against the predicted exact BWT predecessor block. The code also checks full one-run length spectra, total run counts and the ratio's original-run count. Expected terminal message:

`VERIFY_OK generalized_Cantor_BWT base=3..9 k>=2 exact_4k cases=44 direct_rotation_sort_cases=29 independent_digit_generator_and_gap_partition max_word_length=59049`

These are finite tests, not a proof of the unbounded theorem. The proof in `RESULT.md` establishes all integer parameters through the explicit valuation-and-first-difference argument. No independent audit or external verification is asserted.
