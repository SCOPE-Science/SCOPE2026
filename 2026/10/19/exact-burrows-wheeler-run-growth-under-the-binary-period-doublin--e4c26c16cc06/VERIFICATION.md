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

# Reproducibility checks

Run `python verify_bwt.py` using Python 3, without external dependencies. It performs:

1. All 282 primitive cyclically \(11\)-free binary inputs of lengths \(1\)–\(10\): brute cyclic BWT equals the four-block transfer after substitution, and the substituted word is primitive.
2. The independently coded naive cyclic-rotation sorter and cyclic suffix-array prefix-doubling sorter agree for period-doubling iterates \(k=1,\ldots,9\).
3. The transfer identity and exact number of linear equal-symbol BWT runs hold through \(k=14\), covering a final word length of \(16384\).

The expected successful output is:

`VERIFY_OK general_primitive_no11_n_le10_cases=282 two_independent_BWT_algorithms_k_le9 cyclic_suffix_doubling_k_le14 exact_BWT_transfer_and_runs_k_le14 run_formula_k_2_to14`

These are actual finite tests, not an exhaustive search of all binary words at unbounded length. The infinite claims depend on the proved strict rotation-block comparison, odd-one primitivity, and run recurrence in `RESULT.md`.
