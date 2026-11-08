---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The F2 square-map from m/m² to m² has kernel dimension 1 for A and 0 for B. Explicit generator-image normal forms give 32 automorphisms each. The index-two elementary abelian subgroups have involutions represented by conjugation (u,v,s,r)↦(u,v,s+u,r+v) and C↦PCP, intertwined by an explicit invertible F2-linear Psi. Checking the 3 possible degree-2 monomial survivors yields exactly two classes at Hilbert (1,2,2); dimension-4 candidates have automorphism orders 8 and 24. Independent bit-vector automorphism enumeration reproduced orders 32,32,8,24 and square-map kernels; source checker additionally checks all 1024 group-law pairs.

## originality

PASS

The 2024 characteristic-zero reconstruction papers concern automorphism algebraic groups, not F2 rational point groups. Published SCOPE works classify possible short local structures or compute the coordinate-cross automorphism group, but do not give this explicit nonisomorphic pair with matching order-32 group and dimension-five minimality.

## value

PASS

The minimal-dimensional concrete failure of classification by a natural finite algebra automorphism group is structurally informative, sharply delimits characteristic-zero reconstruction and is supported by an explicit group isomorphism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
