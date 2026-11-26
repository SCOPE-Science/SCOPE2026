---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

A choice of split counts t_s yields N_s=a_s+b_s−t_s+t_{s−1}, which is automatically nonnegative for 0≤t_s≤b_s. Divisibility by s is sufficient as well as necessary because within-size labels can be grouped arbitrarily. The predecessor y must have residue t−a_s−b_s modulo s; on that residue the additive transition cost is the sum of a function of t and y/s. Thus each extremum needs only one optimally scored predecessor on that residue, equivalently optimizing m(y)+floor(y/s) or M(y)+floor(y/s). Since the sum of all state-array lengths is n+∑b_s, scanning even the full arrays at each next stage is linear, as are the timestamp operations and retained parent storage. At s=1 the residue is unique, and at s=n the only allowed output state is zero. Parent traversal and batching distinct labels into groups realizes both bounds, including n=1. Explicit output is linear in the size of its label list. The frozen checker was inspected, not executed; its finite brute-force comparisons are corroboration, not the general proof.

## originality

PASS

The general pair-approval orientation equivalence and the interval feasibility algorithm are antecedents, but the inspected statements do not give an algorithm for both extrema and labeled witnesses in time linear in the explicit input, even on the size-label path. The surviving claim is the adjacency-specific, residue-compressed optimization bound, not the orientation model, unrestricted hardness, or the existence of some polynomial-time interval algorithm.

## value

PASS

Two witnesses may differ materially even when feasibility is easy: they bracket the range of feasible coalition fragmentation and certify the endpoints. Obtaining both extrema at input/output scale exploits a natural adjacency restriction and is materially stronger than constructing one feasible partition in polynomial time.

The dated certificate retains the supplied scientific assessment, sources and limitations.
