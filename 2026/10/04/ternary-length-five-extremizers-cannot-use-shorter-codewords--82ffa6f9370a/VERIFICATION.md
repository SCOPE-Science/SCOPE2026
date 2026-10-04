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

The standalone verifier `artifacts/verify_ternary_variable_n5.py` uses only the Python standard library. It reconstructs the full finite compatibility graph from the stated definition rather than loading a precomputed graph.

It checks the following facts exactly:

1. There are \(216\) individually self-non-overlapping ternary candidate words of lengths \(2\) through \(5\), with length distribution \(6,18,48,144\).
2. Exact maximum-clique branch-and-bound, pruned only by a proper-coloring upper bound, returns maximum \(17\).
3. For each of all \(72\) candidates of length below \(5\), the verifier forces that vertex and exactly solves the clique problem on its neighborhood; the largest resulting code has size \(16\).
4. The returned \(17\)-word and \(16\)-word witnesses are rechecked directly for self-overlap, pairwise prefix-suffix overlap, and subword containment.

The captured output in `artifacts/verification.txt` terminates with `VERIFY_OK`.

Limits: this verifies only the finite ternary maximum-length-five claim. No extrapolation to other parameters is certified. Independent audit has not been performed.
