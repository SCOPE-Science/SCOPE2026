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

The degree-six homogeneous map [X(u,v):Y(u,v):v^6] is base-point-free; at v=0, X=-8u^6 so unique infinity preimage and point [1:0:0]. The source verifies affine six nodes, giving generic degree one of the parametrization of a sextic, hence P1 normalization. In local s=v/u, η=Y/X has order2 and ξ=Z/X+8(Y/X)^3 has order9. Independent exact SymPy expansion reproduced ZX²+8Y³=−s^9(s²+2s−2)(7s^7−2s^6−78s^5−72s^4+96s^3+96s²−32s−32), nonzero order9 coefficient −64. A primitive (2,9) plane branch is analytically A8 over C, delta4 and Milnor8. It intersects L∞ with multiplicity6; six affine nodes add delta6 and genus sextic10 exhausts singularities. Fomin–Shustin L∞-regularity gives polar μ+intersection−1=8+6−1=13. Source-established affine hyperbolic node fact is a premise, not independently derived solely from symbolic resultant.

## originality

PASS

The complete accessible Fomin–Shustin article was inspected around exact Example 8.4, Theorem 7.17 and the infinity polar framework. Example 8.4 states the parametrization, resultant and six real hyperbolic affine nodes, but no local A8 point, Puiseux pair (2,9), genus-basket completion or specialized polar 13. These require an explicit local projective coordinate change and factorization beyond the cited statement. Resultary search found other sextic ADE classifications but no same parametrization implication. Best-of-knowledge PASS with unindexed computations as risk.

## value

PASS

The unique projective singularity is a natural invariant of a specific worked sextic in a paper concerned with infinity and expressivity. Determining it accounts for all four missing units of arithmetic genus defect, supplies complete singularity basket and a concrete L∞-polar value, not arbitrary or merely cosmetic arithmetic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
