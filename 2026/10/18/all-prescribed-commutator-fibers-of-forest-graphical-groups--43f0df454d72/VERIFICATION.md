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

# Computational and proof verification

The proof gives a complete combinatorial count for every finite forest, every finite field, and every prescribed central target. It distinguishes zero/nonzero vertex vectors, projective directions, and independent nonzero scalar constraints along forest edges. In particular, the exponent \(|U|-r\) is nonnegative because each of the \(r\) positive-target edges survives when \(Z\subseteq V\setminus V_+(w)\).

The attached standard-library checker `check_forest_commutators.py` enumerates all ordered vertex-vector pairs independently of the closed expression. Run using `python3 check_forest_commutators.py`. It verifies each central target for all labeled forests on one through four vertices over fields of order \(2\) and \(3\), three additional four-vertex configurations over fields of order \(4\) and \(5\), and two five-vertex binary cases. The complete test output contains `ALL_FOREST_FIBER_CHECKS_PASSED 101`. It additionally prints the eight binary four-path fibers and four full-support examples. This check is finite and does not independently verify the literature priority or an infinite theorem. Independent audit status: not performed.
