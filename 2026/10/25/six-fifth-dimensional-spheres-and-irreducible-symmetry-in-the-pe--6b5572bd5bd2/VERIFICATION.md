---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The vertex-induced forest complex on KG(5,2), not its edge-set graphic-matroid complex, has 786 faces including empty, f-vector (10,45,120,210,240,140,20), and 22 minimal nonfaces (12 five-cycles, 10 six-cycles). Independent complete 1024-mask enumeration reconstructed all faces. Pivot matching on the face poset yields 389 matched nonempty face pairs with a directed Hasse graph acyclic on 785 nonempty faces; its only critical cells are one 0-cell and six 5-cells, so integral homotopy is wedge^6 S^5. Independent exhaustive 120 group elements signed simplicial Lefschetz character equals (6,0,-2,0,0,0,1) by S5 cycle type, identical to wedge² of the standard four-dimensional rational module, irreducible S^(3,1,1). Direct matching and character computations corroborated source; finite proof is exhaustive because exactly 2^10 subsets and 120 permutations were checked.

## originality

PASS

The forest-filtration/devoid-complex literature supplies the face definition and general matching machinery. A prior published Petersen three-cut complex has the identical S5 module but different faces, cut conditions, homology degree and topology; agreement of characters is not an implication. This calculation specifically treats the induced vertex-forest complex and determines both its integral wedge homotopy and full rational equivariant character.

## value

PASS

The Petersen graph is a canonical highly symmetric nontrivial finite graph. Its complete nonpure vertex-forest topology and irreducible natural S5 homology action are a meaningful natural exact invariant, potentially a benchmark for forest-filtration/devoid complexes; no large-family theorem is claimed or needed for this exact classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
