---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The poset is K_{2,3}, so H_1 is the rank-two cycle lattice. The source gives a direct 197-map count by the images of the two minima. The committed verifier enumerates all 5^5 set maps, retains exactly 197 isotone maps, computes the integral chain images of an explicit cycle basis, and identifies exactly 31 matrices. A fresh independent exhaustive replay reproduced 197 maps, 31 matrices, and the rank distribution 149 zero, 36 rank one, 12 rank two. The 18 rank-one matrices are the two signs of nine distinct outer products; the six primitive q-minimal vectors generate exactly 12 integral q-isometries. Independently, Aut(P)=S_2 x S_3 has 12 elements, matching exactly the determinant plus-or-minus-one maps.

## originality

PASS

Barmak--Minian identify the five-point K_{2,3} space as a minimal model of a two-circle bouquet. Published SCOPE results for the complete height-two family classify self-homotopy components and homology ranks, but the broad p,q theorem explicitly assumes p,q>=3 and the all-q P_q theorem does not determine the exact integral H_1 matrices. The assigned 31-matrix semigroup, its rank-one outer-product description and hexagonal q-isometry group therefore remain a distinct exact invariant not covered by those results.

## value

PASS

The exact direct-map image on H_1 quantifies how a canonical cardinality-minimal finite bouquet model realizes only a tiny structured subset of the arbitrary integral matrices available classically. The hexagonal-form isometry structure and explicit rank-one repertoire are natural model invariants, not merely a self-map count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
