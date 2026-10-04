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

The universal proof is analytical. The finite checker is an independent stress test of the new tied-maximum constructions.

Run:

`python3 artifacts/verify.py`

Expected terminal line:

`ALL CHECKS PASSED; tied_max_types=222; total_edges_checked=16133; max_order=16`

The checker enumerates every integer partition of each order from \(3\) through \(16\), selects multipartite types with at least three parts and at least two largest parts, constructs the appropriate odd- or even-order coloring, checks properness at every vertex, and checks that no two missing integer colors inside any incident color span are consecutive.

The checker does not attempt to verify the published unique-largest-part theorem and does not use finite success as evidence for the universal quantifier. The proof of the infinite tied-maximum family is contained in `RESULT.md`.
