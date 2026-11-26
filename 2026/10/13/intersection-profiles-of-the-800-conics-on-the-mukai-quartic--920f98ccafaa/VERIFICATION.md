---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The replay uses all five actual vectors of Degtyarev's Table 1, not an arbitrary realization of their Gram matrix. The ordered five coordinates and octad with intersection {1,2,4,5} are unique up to M24 in the source. The independent integer replay constructs the extended Golay code and all three minimal-vector families, applies the five pairings, and gets 800 distinct conic vectors (192 Golay type, 608 octad type). In the published Néron–Severi realization, x_l=l-hbar/2 is orthogonal to hbar, the lattice form on this summand changes sign, and h^2=4, so C_l.C_m=1-x_l.x_m=2-l.m. The replay exhausts 319600 unordered pairs and returns (72240,174720,72240,400) in multiplicity order (0,1,2,4). It recovers 480 copies of (179,440,179,1) and 320 copies of (183,432,183,1), and its second pass confirms A/A (115,248,115,1), A/B (64,192,64,0), B/B (87,144,87,1), B/A (96,288,96,0). The residual vector hbar-l satisfies all constraints, has norm four, and is distinct from l. Its conic class is h-C_l; their sum is a plane section because the Picard and Néron–Severi groups agree on this K3 and every section of its hyperplane line bundle comes from a plane. Equality in the Cauchy inequality for the norm-three projected vectors shows that intersection four forces this residual partner. For nonresidual distinct pairs, the Leech minimum bounds l.m and l.(hbar-m) each above by two, so 0<=l.m<=2, an independent check of the allowable values. Projective automorphisms preserve profiles: the published 480-orbit fills A and the two 160-orbits exhaust B. The profile class B is not asserted to be a single automorphism orbit.

## originality

PASS

The distinct claim is the full typed pair census and local/cross-class profiles of this extremal quartic. The residual involution and the 400-plane count are covered and get no separate originality credit. The primary vector tables and orbit sizes alone do not supply the typed pair multiplicities, and the strongest inspected matching records on planes do not cover the rest of the census. The actual available statements are sufficient to distinguish the complete profile, subject to a residual risk from the uninspected extent of the classification's ancillary corpus.

## value

PASS

The configuration is the unique extremal 800-conic quartic, and numerical intersection products are intrinsic to its curve configuration. The complete profile and two-class quotient supply precise constraints for incidence and automorphism calculations: they distinguish the large projective orbit purely numerically and show that the two smaller orbits are not distinguished by this invariant. This is a full, motivated exact invariant, not a sample, the known residual count, or a recomputation of an inspected table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
