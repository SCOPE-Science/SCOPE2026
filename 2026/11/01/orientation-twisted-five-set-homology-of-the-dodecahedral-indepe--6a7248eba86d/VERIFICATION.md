---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Exact enumeration of independent vertex sets gives face-cardinality counts (1,20,160,660,1510,1912,1240,320,5). The cited verifier gives mod-2 boundary ranks (19,141,519,991,921,315,5) for nontrivial boundaries. Mod-two Betti ranks bound rational Betti ranks, and reduced Euler characteristic -4 forces rational H5 rank four and vanishing elsewhere, without claiming torsion absence. The Hopf trace formula on augmented chains gives tr_H5(g)=sum_{fixed sets S}(-1)^|S|sgn(g|S). Independent reconstruction enumerated all 120 graph automorphisms and all fixed independent face sets and exactly reproduced epsilon(g)(#Fix_I(g)-1), with 60 elements of each orientation and 60 even induced permutations on the five maxima. Equality of rational finite-group characters gives the module isomorphism. This is an exhaustive finite calculation, not sampled inference.

## originality

PASS

The known wedge of four S5 determines only nonequivariant topology. Lew identifies precisely the same five maximum 8-independent sets but studies a different threshold complex I_8(D), whose H15 rank4 does not imply the ordinary independence complex H5 action. Neither gives the orientation-twisted A5xC2 rational character.

## value

PASS

This is a complete symmetry action on a natural canonical twenty-vertex graph complex with a distinguished five-object A5-set, refining a known nonequivariant classification. The sign of inversion and vanishing global invariants are meaningful representation-theoretic information, rather than another Betti count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
