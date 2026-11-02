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

# Computational reproducibility

The accompanying `verify.py` uses Python 3 standard library only. Run `python verify.py` from the directory containing this file. It exhaustively enumerates edge weights over \(\mathbb F_2\) and \(\mathbb F_3\) for ten nonisomorphic unicyclic configurations including cycles, one- and two-edge pendants, and multiple branches.

Three independently constructed quantities agree: the direct skew-matrix rank histogram computed by Gaussian elimination, the support formula with a maximum-matching cross-edge test, and the rooted-tree factorized correction with independently enumerated root-unsaturated supports. All twenty graph-field pairs satisfy the exact total \(q^{|E|}\). The reported success terminal line is `VERIFY_OK 20 direct exhaustive graph-field cases; independent rooted factorization`.

The executable verifies finite cases only and cannot establish an all-size theorem. The all-graph proof depends on the Pfaffian rank criterion, uniqueness of perfect matchings in a forest, the cycle-root matching comparison, and the finite-field binomial cancellation count, each provided in `RESULT.md`. The character conversion is a published representation-theoretic identity and is not tested by explicit character-table enumeration. No independent mathematical audit has been performed.
