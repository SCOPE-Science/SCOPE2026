---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

PASS: Nonalgebraic complete 1-types over finite induced parameter poset P in the homogeneous random poset correspond bijectively to admissible (lower ideal D, upper filter U) one-point extensions satisfying D<U. For Q=P+v, any restriction fiber has <=3 placements (below/above/incomparable v), and exactly one existing P-profile (D,U)=(L,H) has all three. If P contains a comparable pair there is also a distinct singleton fiber: choose x above all P when v lies below some old point, below all P when v lies above some, or between a<b when v is incomparable to all P. Hence total t(Q)<=2t(P). Start from an induced C2 with t=6, append n-2 arbitrary points to get t(P)<=6*2^(n-2)=3*2^(n-1). Antichain profiles give 2^(n+1)-1. One disjoint chain plus isolated vertices and height-two star/dual attain equality. Independently enumerated every labeled strict partial order through n=5 (1,3,19,219,4231 cases n=1..5), checked all legal profiles and sharpness counts; infinite proof is the restriction-fiber lemma.

## originality

PASS

PASS best of knowledge for the sharp nonantichain extremal count and doubling lemma. The directly related published Resultary finding already proves the ideal/filter representation, algebraic plus nonalgebraic type count, antichain 2^(n+1)-1 and #P-completeness. Its full RESULT.md was independently inspected, including formulas and proof, and it does not state/derive the extremal bound 3*2^(n-1) or fiber doubling lemma. Old insertion-poset literature (Pretzel 1980) was abstract-only and access blocked, retaining possible priority overlap.

## value

PASS

PASS: The sharp extremal stability gap quantifies how a single comparability destroys half the antichain type excess; the doubling law controls arbitrary one-point parameter enlargements, and two structurally different extremal families show sharpness. Type/orbit-count extrema are natural numerical invariants of a canonical homogeneous structure, beyond the already known generic counting complexity result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
