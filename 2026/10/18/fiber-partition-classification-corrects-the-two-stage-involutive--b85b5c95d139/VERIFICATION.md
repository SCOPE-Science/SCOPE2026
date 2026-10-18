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

## Actual reproducible checks

Run `python3 verify.py` with Python 3 and only the standard library. The verifier exhaustively enumerates the function maps for 20 positive parameter pairs \((a,b)\) with \(1\leq a\leq4\), \(1\leq b\leq5\), explicitly generates their orbits under both finite symmetric groups, and checks the orbit/fiber-partition bijection and exact stabilizer formula. In those parameter pairs it processes 1,794 maps and 48 isomorphism orbits. It verifies that the two proposed 20-element counterexamples have the same dual image rank, have different fiber-size partitions, are not in a common relabeling orbit, and each obeys the eight algebraic axioms by exhaustive finite table evaluation.

Actual output: `VERIFY_OK parameter_pairs 20 maps 1794 orbits 48 strictly_smaller_shapes 11 counterexample_shape (4, 16) rank 2 distinguished_fibers ((3, 1), (2, 2)) corrected_types 3 rank_only_types 2 axioms_checked 8`.

The unrestricted classification, minimality, and automorphism formula rest on the mathematical proof in `RESULT.md`. The finite enumerations alone cannot establish a theorem for arbitrary component sizes. Full general fine-spectrum recomputation and independent validation were not performed.
