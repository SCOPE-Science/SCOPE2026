---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Enumerating all 16-vertex graph independent sets for step differences 1,4,8 yields full f=(16,80,144,80). Removing translated orbit of 16 tetrahedra leaves core f=(16,80,128,64), every core triangle degree two, and all 16 vertex links have f=(10,24,16), connected and edge-degree two: hence sphere links, plus connected dual graph gives closed 3-manifold. The explicitly listed nine-tetra dual walk has required orientation ratio product -1, obstructing orientation. Independent exact integer Smith computations on reconstructed ∂2,∂3 give for core 1^64 and (1^63,2) and for full 1^65,1^79, proving H1(core)=Z,H2(core)=Z/2,H3(core)=0 and H3(full)=Z. Direct integer nullspace yields primitive full 3-cycle coefficient magnitudes 1 on 64 core facets, 2 on 16 belt facets; relative 16-cycle boundary has 15 unit factors and zero. LES realizes H3(full)->H3(K,M) by ×2 and mod-two quotient. Ambient K≃S³ uses independently published shellability. This finite classification was independently enumerated and Smith-tested; source verifier inspected, not executed. No core fundamental group/homeomorphism identification claimed.

## originality

PASS

The graph C16(1,4,8) and shellable-but-not-vertex-decomposable ambient independence complex are expressly prior work. The particular canonical translated 16-tetrahedron orbit deletion, resulting nonorientable 3-manifold with integral two-torsion, and coefficient-two fundamental 3-cycle were not stated by the inspected primary work or matched literature. Best-of-knowledge; unindexed triangulation tables or appendices remain possible.

## value

PASS

The selected orbit is geometrically and group-theoretically natural inside a well-studied exceptional complex. The nonorientable 3-manifold core, exact two-torsion and doubled integral primitive cycle provide a coherent finite topological mechanism beyond old ambient shellability; finite does not mean immaterial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
