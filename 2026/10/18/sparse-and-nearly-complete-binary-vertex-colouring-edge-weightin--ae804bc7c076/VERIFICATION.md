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
# Reproducibility record

Run `python3 verify.py` with Python 3's standard library. A successful execution reports 17 fully enumerated biclique matrices (125,006 binary edge assignments), 1,200 proper configurations found within additional exhaustively searched extremal layers, 30 checks of the orbit multiplicity identities against a separate occupancy recursion, and the expected sharp three-edge-deletion boundary for additional consecutive-size rectangles.

The input edge set is the complete bipartite grid indexed in row-major order. A one-bit edge is active; vertex sums are computed independently from the support set. The acceptance test compares **every** row sum against **every** column sum, including comparisons across edges assigned zero. The brute-force tests do not reuse the star-forest characterization as an acceptance predicate.

All numerical comparisons are exact integers. The code contains an independent recurrence for occupancy counts, and a separate combinatorial proof in `RESULT.md` establishes the result for all sizes. No empirical finite bound is treated as an infinite proof. No independent external validation has been performed.
