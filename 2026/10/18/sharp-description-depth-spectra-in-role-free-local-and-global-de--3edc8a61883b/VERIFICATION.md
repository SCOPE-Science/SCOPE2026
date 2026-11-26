---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Every concept selects whole unary colors, and all singleton decisions depend only on counts capped at two. At a nonsingleton local point all descriptions are false there; at a singleton point a depth-one description tests absence, and the depth-two test removes a singleton other color before forming the union. Thus each of the T pointed colors has one nonsingleton class, and respectively 2^(T-1) and 3^(T-1) singleton classes. In the global language color-singleton tests either all fail (no singleton anywhere and no deeper description can help), or provide an anchor whose union with each other color detects its absence at depth one. The fixed pointed color then has 1 + 3^(T-1) + (3^(T-1)-2^(T-1)) profiles. The tests isolate every type by a Boolean conjunction, so the concept algebra has 2^N elements at each depth. The largest anchored representative needs precisely one singleton and two points of each other color; in the one-color case the nonsingleton type needs two points. The stated bound is sharp uniformly, not a claim of depth-zero sharpness. Independent exact finite check: place all capped models for k=0,1 in a disjoint union, enumerate Boolean unions of the current truth-partition blocks, generate singleton selections or broadcasts separately inside each model, and refine. Counts reproduced: local (1,2,2) and (2,6,8), global (1,2) and (2,10). This check does not prove the all-k induction. The frozen checker was inspected, not run.

## originality

PASS

The supported distinction is the exact finite pointed depth filtration for the two separate role-free languages, including the sharp collapse and parameter-only representative bound. The description operators, expressivity separation and general bisimulation machinery are prior. The Boolean algebra cardinality follows from the new depth-specific partition, not independently. No equivalent coverage was established in the sources compared.

## value

PASS

The role-free baseline separates local from global observability without relational navigation. Exact spectra and shortest collapse depths answer which counts a description can test, while the sharp model bound gives a finite universe of representative types for equivalence checks. These are structural results, not merely the powers-of-two count for an already enumerated algebra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
