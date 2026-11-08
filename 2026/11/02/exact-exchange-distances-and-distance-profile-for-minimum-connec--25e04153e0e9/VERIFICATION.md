---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

C PASS. For n>=3 a crown CDS has at least two vertices on each shore, except the disconnected equal 2-by-2 choice; removal shows only admissible (2,2) sets are inclusion-minimal. Token exchanges preserve each shore count, yielding the off-diagonal square of J(n,2). Case-wise bypass of the forbidden diagonal preserves Cartesian distance except for adjacent-coordinate swaps, which cost one extra step. Four common neighbors for Johnson distance-two paths ensure routes exist. Inclusion-exclusion over forbidden starts/ends gives v(v-2)(1+kt+qt^2)^2+v(1+kt^2+qt^4)+vk(t^3-t^2). Degree, diameter, token-slide rigidity follow. Independently breadth-first enumerated the entire metric and ordered-pair shells for n=3,4,5; finite checks are not a proof for all n.

## originality

PASS

Best-knowledge PASS for all-pairs exchange metric and exact distance enumerator only; the count of minimum connected dominating sets is explicitly known and excluded from novelty. No source inspected gives the particular off-diagonal Johnson-square distance correction; priority of a general two-particle collision metric remains a qualified risk.

## value

PASS

V PASS. Shortest paths and exact shells of the natural minimum-connected-dominating-set reconfiguration graph, plus a jump-versus-slide dichotomy, are useful structural data for a canonical graph family; not merely recomputation of its previously known minimum-set count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
