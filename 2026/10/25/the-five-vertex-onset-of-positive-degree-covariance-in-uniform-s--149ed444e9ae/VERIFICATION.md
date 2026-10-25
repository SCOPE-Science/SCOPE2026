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

# Reproducible checks and boundaries

Run `python3 verify_degree_boundary.py` with Python 3 and no nonstandard dependencies. The program enumerates every simple labeled graph on orders two through five; it tests connectivity of each graph, enumerates every possible spanning-tree edge subset, calculates covariances exactly with integer counts and rational arithmetic, and reduces graphs to isomorphism classes by checking every vertex permutation. It asserts two positive-covariance isomorphism types at order five, with exact tree counts, positive-pair counts, and fractions; it rejects positive cases at smaller orders. It additionally checks the all-orders unicyclic formula on a finite range of cycle lengths with pendant attachments. The separate proof of the unrestricted formula is a one-line uniform-edge-deletion covariance computation and does not rely on a finite extrapolation.

The exhaustive counts for connected labeled orders two to five are respectively 1, 4, 38, 728; connected isomorphism classes are 1, 2, 6, 21. The witness covariances are exactly 1/25 and 5/121, not floating-point approximations. The finite census makes no claim about all graphs of order six or above.

Independent audit has not been performed. Historical priority remains uncertain.
