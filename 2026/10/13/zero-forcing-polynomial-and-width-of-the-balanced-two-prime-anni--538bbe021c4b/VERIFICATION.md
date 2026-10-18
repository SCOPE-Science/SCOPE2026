---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Every nonzero proper ideal of Z/(p^2q^2) gives one of seven exponent pairs except (0,0) and (2,2), and two vertices are adjacent iff both coordinate exponent sums are at least 2. This graph depends only on the balanced exponent pattern, not the primes. Independent complete enumeration of all 2^7=128 blue subsets gives exact zero forcing coefficient list (4,24,33,21,7,1) for degrees 2..7, with precisely the four claimed size-2 sets. Explicit five-move forcing sequences verify upper bound Z<=2; the graph is not a path, so Z>=2. The seven bags of width 2 cover every edge and have interval incidence, and an induced C4 excludes treewidth 1, so tw=pw=2. Ring-to-graph reduction is symbolic and entire finite graph enumeration is exhaustive, not sampling.

## originality

PASS

The two-prime ideal graph structure and general definitions predate the result. The inspected same-object and near-object sources study algebraic independence or weak perfectness, not the complete standard forcing-set enumerator, four minimizers and exact width-two decomposition for this balanced exponent case. A database may contain Z=2; this scalar value is not the novelty claim.

## value

PASS

The first symmetric mixed pair of nonfield prime-power components supplies a canonical seven-vertex ideal graph that has an induced cycle and is not covered by path/tree forcing formulas. The complete 128-subset census and exact width certificates form a naturally motivated base case and sharp benchmark for p^a q^b annihilating-ideal graph forcing and decomposition questions. Its fixed size is explicitly acknowledged; no unsupported infinite classification is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
