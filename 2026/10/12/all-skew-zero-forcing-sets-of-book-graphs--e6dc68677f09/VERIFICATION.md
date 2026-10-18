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

A white set W is skew-stalled when no vertex has exactly one white neighbor. Each page vertex x_i has neighbors a,y_i, so stalled implies (a in W) iff (y_i in W); similarly each y_i forces (b in W) iff (x_i in W). The remaining hubs obey the constraint for all n>=1, leaving exactly empty set, U, V, and all vertices as skew-stalled. Failed initial S iff its white complement contains U or V, i.e. iff S misses a full bipartition class. Thus the nonempty-on-each-side polynomial factors, with min/failed counts. An independent implementation simulated arbitrary permitted unique-white-neighbor forces and all subsets of B_n for n=1..5 and checked the stalled-set classification and polynomial. The general n result follows from degree-two equivalences, not finite search. The C4 boundary n=1 is included.

## originality

PASS

DeAlba arXiv:1404.1618 gives the rule, matching-based sufficient conditions, and other Cartesian-product families. Its maximum matching theorem assumes all maximum matchings are uniquely restricted; B_n has n+1 perfect matchings and fails that hypothesis, so it does not imply the all-set book classification. Published chain-graph twin-class factorization does not imply this book formula: the book graphs have nonnested bipartition neighborhoods. The result claims book-specific all-set structure only.

## value

PASS

The exact polynomial and all-set forcing criterion classify a natural classical quadrilateral-book family and simultaneously give minimum forcing sets and maximum failed configurations. The stalled-set structure is a compact structural lemma, not mere recomputation of one known minimum. Value is family-specific, not a claim of a general zero forcing theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
