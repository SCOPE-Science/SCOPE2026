---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For n=3m+2>=5 set k=m+1. Every edge of a perfect matching M of a paired-dominating set covers a six-vertex endpoint-closed neighborhood Q_e, forcing k>=ceil(n/3). At k equality the multiplicity excess is precisely 6k-2n=2. From the explicit rung/top/bottom Q_e shapes consecutive edge-start gaps cannot be 1 or >=4; gaps sum to n=3k-1, so exactly one gap is 2 and all others 3. The local three-state transition and overlap table give exactly 2k+1 compatible edge-type strings per location of the short gap, yielding n(2k+1)=n(2n+5)/3. Distinct perfect matchings of the same vertex set would form an alternating cycle of length>=4, producing >=4 multiply covered vertices, impossible under budget 2. This proves gamma_pr=2k and unique induced matching for all allowed n; n=5 boundary included. I independently enumerated all dominating k-edge matchings and endpoint vertex sets for n=5,8,11,14, getting (25,56,99,154) with no repeated endpoint set. The finite enumeration does not prove the infinite family.

## originality

PASS

Best-of-knowledge independent comparison of the precise surviving theorem to same-object primary mathematics, Resultary semantic matches, general covering results and exact numeric searches; known foundations explicitly excluded from claimed novelty. Relevant inaccessible source risks are material and unresolved historical-priority caveats, not automatic scientific failure. The full labelled minimum-set census and unique induced-matching assertion are not consequences of cardinality bounds for paired domination.

## value

PASS

An exact classification of all optimal paired-dominating vertex sets in a natural prism family, together with forced matching rigidity and a cyclic short-gap structure, is substantially more informative than a paired-domination number. Labelled-set enumeration is a natural invariant; its value could be used for extremal enumeration and random optimal-set sampling. It is not a disguised ordinary-domination count; the limitation n=3m+2 is explicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
