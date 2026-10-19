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
# Reproduction of mathematical checks

Run `python3 verify.py` in a directory containing the standalone file. No third-party modules or downloaded data are required.

The script checks all pairs of binary complementary-block specifications of lengths one through seven against direct enumeration of the length-one-longer subsequences; two independent Thue–Morse generators for blocks through level nine; absence counts using three engines (direct greedy-state transitions, matrix products, and the scalar recurrence) for levels one through nine; and complete direct missing-word enumeration through level five. It also computes explicit lower and upper bounds for the convergent exponential-base expression.

Expected output:

`VERIFY_OK ThueMorse-SAS: arbitrary_complementary_arches_k<=7; two_generators_m<=9; three_count_engines_m<=9; direct_absent_subsequences_m<=5; exact_nonlinear_recurrence; rho_in_[1.568664789150, 1.568664789150]`

This is reproducible **finite** cross-checking. Its finite range does not establish the theorem for every substitution level. The infinite proof is the alignment lemma, Thue–Morse matrix-product renormalization, scalar recurrence, and limiting logarithm analysis in `RESULT.md`. No independent formal mathematical audit or separate expert validation has been performed.
