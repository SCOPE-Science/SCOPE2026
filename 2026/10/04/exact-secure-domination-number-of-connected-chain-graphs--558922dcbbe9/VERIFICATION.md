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

The proof is symbolic and valid for arbitrary finite connected chain graphs. The executable check is supplementary: it constructs every canonical nonempty twin-block profile of total order at most \(10\), computes secure domination by exhaustive subset and swap tests, and compares the result with the closed formula. It also recomputes the leaf-twin reduction on every profile.

Replay with:

`python verify.py`

Expected output:

`VERIFY_OK profiles=511 twin_reduction_checks=511 secure_subset_checks=178382 swap_checks=88263 max_order=10 h3_gamma=3`

The explicit \(H_3\) check confirms that one bipartition side is a secure dominating set of size \(3\). The general bipartite lower-bound proof, not the finite computation, excludes size \(2\) and establishes the infinite theorem together with the constructive upper bounds.
