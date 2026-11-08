---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Direct independent graph enumeration using the frozen 30-edge list yields exactly 140 disconnected triples, Alexander-dual K f=(12,66,80,30), ordinary cut f=(12,66,220,495,792,924,792,465,140), rational boundary ranks (11,49,30), hence reduced H7 dimension1 and H8 dimension6 by combinatorial Alexander duality. Independently enumerated all 120 graph automorphisms, 60 rotations, their stable-simplex signed Lefschetz numbers (5,-3,-1,0) for rotation orders (1,2,3,5), inversion coset (-5,3,1,0) for orders (2,2,6,10). The A5 perfectness plus character table forces H8=W char(6,-2,0,1,1), H7 rotationally trivial; centrality and Lefschetz(a)=-5 force antipodal sign -1 on both. Rational invariants then give specified quotient homologies. Checked actual verify.py finite-field cycle action as corroboration; rational character conclusions rest on rational ranks and Lefschetz theory, not mod1009 alone.

## originality

PASS

An earlier published calculation of the exact same ordinary icosahedral three-cut complex already proves the nonequivariant wedge S7 ∨ 6S8 and f-vector; those are known, not claimed new. Its full Resultary RESULT.md explicitly says no equivariant homology. Bayer et al.'s cut complex theory and equivariant computations on other graph families do not supply the A5×C2 representation for this graph. The present sign-twisted rational characters and distinct quotient homologies are nontrivial refinements.

## value

PASS

Full rational G-module structure identifies how icosahedral symmetries act on the two topological spheres degrees, distinguishing A5, antipodal, and full symmetry quotient rational homologies. This is a natural symmetry invariant of an established, nontrivially homological Platonic example, not a recomputation of ordinary Betti numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
