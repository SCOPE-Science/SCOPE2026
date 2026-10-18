---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Zero a_i requires W_B−y_i>=2, zero b_i requires W_A−x_i>=2: these are exact open-neighborhood sums. For total weight <=2 at n=3 or <=3 at n>=4, one side has sum <=1 and forces every vertex of the opposite side positive, contradicting the target weight. At weight 3 (n=3) only the two all-one-side functions work. At weight 4 (n>=4), any side weight <=1 forces a full opposite side, possible only for n=4 with two all-one-side functions. Otherwise both sides have weight two. Every positive label on one side must be at a positive matched index on the opposite side since a zero excludes exactly its matched opposite; supports coincide, and weight-two support has size one with each label 2 or size two with four labels 1. Hence n+binom(n,2), plus two when n=4. Independently enumerated every labeling of total weight <=4 for n=3..10; minima counts 2,12,15,21,28,36,45,55 and minima weights 3,4,...,4. The infinite result comes from the support argument, not enumeration.

## originality

PASS

Best-of-knowledge PASS: specifically minimum-function count and deleted-pair support alignment on crowns; published complete-multipartite Roman-{2} enumerators do not apply after removing a perfect matching. Distinct nearby perfect Roman and ordinary Roman parameters are not equivalent.

## value

PASS

On the natural crown graph, deleting one perfect matching changes domination constraints in a precisely measurable way; the theorem classifies every minimum Italian labeling, not just gamma=4. It proves an integer transition at n=4 and exact n+binom(n,2) optimizer counts after n=5, potentially useful for extremal enumeration/algorithm tests. This is an exact structural family classification beyond a textbook bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
