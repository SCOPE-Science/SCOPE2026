---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For D_n with strictly increasing 0<a1<...<an and normalized height average, the trapezoidal vertex formula gives coordinates sigma_j(t_{j+1}-t_{j-1})/(4A) and -(t1+tk)/(4A) in the nth direction. For one intermediate point, squared norm is [1+(t/A)^2]/4, attaining maximum exactly at ±e_{n-1}. For k>=2 the squared norm is convex on -B<=t1<=...<=tk<=B; independently enumerated its ordered-simplex vertices for rational A>B and k=2..9 and checked the proof’s extremal forms, max Fk<=2(A+B)^2. Thus clearance >=(A-B)^2/(8A^2) and no multi-point path contacts. The antipodal extremal pair forces the minimum-radius centered origin ball, uniqueness by squared-distance averaging, and unique diametral pair; no affine-coordinate metric changes are assumed. Coherent-path enumeration relies on the genuinely applicable Black-De Loera indexing theorem; finite exact tests corroborate but are not all-real proof.

## originality

PASS

Best-of-knowledge comparison of the exact final statement, including earlier stronger/special-case results and mathematical implications, did not identify decisive coverage of the stated new component; this is not an exhaustive global priority certification.

## value

PASS

A canonical realization-sensitive geometric optimization of the cross-polytope fiber polytope: the exact minimum Euclidean enclosing radius and contacts depend solely on two largest heights despite exponentially many vertices. This is a meaningful strong geometric rigidity/clearance statement not implied by graph-flip diameter or combinatorial equivalence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
