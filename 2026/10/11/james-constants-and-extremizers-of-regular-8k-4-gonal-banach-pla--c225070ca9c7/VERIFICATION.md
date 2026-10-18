---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For every odd m>=1 the 4m-vertex circumradius-one regular polygon has apothem c=cos(pi/(4m)) and c B2 subset P subset B2, hence Euclidean norm <= polygonal gauge <= Euclidean norm/c. For unit x,y, the parallelogram identity yields min(N(x+y),N(x-y))<=sqrt(2)/c. Every quarter-turn pair of polygon vertices has both sum and difference on edge normals because m is odd, giving equality. Any achieving pair forces both Euclidean chord norms sqrt(2), both original vectors of Euclidean length 1, so polygon vertices, and dot(x,y)=0. Those vertices are exactly (v_j, +/-v_{j+m}); converse holds, including square m=1. The full equality proof is complete, analytic and all-quantified.

## originality

PASS

PASS best-of-knowledge: The earlier dodecagon-specific theorem at 13:10:54Z establishes only m=3. The general record at 13:10:55Z establishes every odd m and complete equality set, not a routine corollary of the single instance. Komuro–Saito–Tanaka Corollary 2.7 gives only J=sqrt(2) iff pi/4 rotation invariant among pi/2 invariant norms; it implies J>sqrt(2) for odd m, not the exact formula/extremizers. Other surveyed published records concern different constants or the octagon. No older all-m covering theorem was identified after statement-based searches and checking relevant primary text.

## value

PASS

PASS: Complete exact James constant and all maximizing-pair classification across an infinite natural congruence class of regular polygonal Banach planes. This is a natural geometry-of-norms invariant, explains strict pi/4 symmetry break and rigidity of equality; useful benchmark for geometric constants. It is not inferred solely from numerical experiments or one dodecagon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
