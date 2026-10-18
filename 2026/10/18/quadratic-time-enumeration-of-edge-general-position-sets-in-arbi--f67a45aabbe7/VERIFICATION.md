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

The accompanying `verify.py` is a standalone Python 3 program relying only on the standard library. Run `python3 verify.py`. Its expected single output line is reproduced verbatim in `verification_output.txt`.

The program implements the three-state coefficient recursion and, **separately**, enumerates edge subsets of explicit tree graphs, builds every unique vertex-to-vertex path by breadth-first search, and rejects a subset exactly when a path contains at least three chosen edges. Exhaustive comparisons cover all Prüfer-encoded labeled trees on one through seven vertices, supplemented by deterministic-seed tests on larger trees through thirteen vertices. In total there are 18,744 tree cases and 1,390,623 edge-subset masks checked.

Further checks use independent closed polynomial formulas for 60 stars, 60 paths, and 100 double-stars; the double-star test exercises two distinct centers with arbitrary leaf multiplicities from 1 through 10 at each center. Input labels affect none of these combinatorial assertions.

Finite tests do **not** establish the infinite-family theorem, which depends on the indicator-weighted path equivalence, induction for the two-piece merge rule, and the arithmetic-complexity accounting in `RESULT.md`. Complexity is in integer arithmetic operations, not in fixed-width machine-word instructions. No external checking or independent audit is claimed.
