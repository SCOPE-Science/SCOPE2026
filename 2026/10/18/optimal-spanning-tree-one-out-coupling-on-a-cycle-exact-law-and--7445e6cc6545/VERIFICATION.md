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

# Mathematical verification

The analytical verification derives the deterministic cycle set identity, establishes the rotation-equivariant uniform-tree marginal, counts cyclic orientation runs with an explicit factor \(n/k\), and computes exact first and second moments of the missing-edge count. The fixed-bias limiting normal law uses a standard bounded stationary one-dependent central limit theorem. The rare-bias law couples the transition count to a binomial rare-symbol count, with error probability bounded by \(np^2\) when \(p\to0\).

The included `verify_cycle.py` is standalone (Python standard library only) and executes exhaustive exact-rational tests for every orientation on cycles of sizes \(3\) through \(10\) at probabilities \(1/2\), \(1/3\), \(2/5\) and \(3/4\). It independently checks that the constructed tree marginal is uniform, that every coupled distance equals the pointwise minimum, that the entire run-count probability law and moment formulas hold, and that the unbiased distribution agrees with the even-binomial coefficient formula. Observed outcome: `PASS 19304 exact rational assertions`.

Finite tests cannot establish infinite convergence or absence of equivalent prior results. The numerical and exact finite checks are supplementary to the written proof. External independent verification has not been conducted.
