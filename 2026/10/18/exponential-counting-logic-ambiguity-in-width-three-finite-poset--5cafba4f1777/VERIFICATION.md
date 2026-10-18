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

# Reproducibility and limits

The proof is in `RESULT.md`. It establishes the assertion for every integer \(t\ge2\). The code uses Python 3's standard library only. From the directory containing the embedded files, run `python checker.py` and `python formula_check.py`. Compare their output with `checker_output.txt` and `formula_output.txt`.

`checker.py` generates all \(2^t\) sign sequences for \(1\le t\le7\) (254 posets), applies transitive closure, checks the predicted regular incidence matrix and level partition, and for \(t\le4\) exhaustively tests all six level-preserving coordinate permutations for each pair of sign sequences. `formula_check.py` independently computes which individual ordered pairs are related using a subset-sum rule, and compares that relation with transitive closure in 407,646 instances. Both programs completed successfully.

The computational ranges are **not** proofs for unbounded \(t\). The proof's infinite steps are the characterization of all increasing paths, the two-shortcut saturation in the three-element cyclic group, the two-variable counting induction, and the global-coordinate isomorphism argument. No claim of independent external verification, formal proof-system checking, or priority certification is made.
