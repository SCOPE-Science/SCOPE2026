---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Construct even-weight 5-bit vectors and connect Hamming-distance-four pairs; check 16 vertices, 40 edges, every degree5 with strongly regular parameters (16,5,0,2). Independently enumerate all 115536 matching faces including empty, with cardinality counts [1,40,620,4760,19190,39640,37740,12840,705]. Form full F2 simplicial boundary columns by deleting selected graph-edge bits and exact binary elimination, obtaining ranks [39,581,4179,15011,24629,12135,705]. Reduced Betti formula gives [0,0,0,0,0,976,0,0]; Euler characteristic -976 agrees. This is exhaustive finite proof of this specific GF2 homology, not inference from sampled graphs or claim about integral homotopy.

## originality

PASS

The Clebsch projective/folded 5-cube graph has an exact mod-2 matching-complex Betti vector with 976 in degree 5, distinct from published Clebsch neighborhood and independence complexes. The published-index exact hit is a mirror of this same record; no separate graph-matching table or general family formula implying 976 was found. Best-of-knowledge risk of an unindexed matching-complex calculation persists.

## value

PASS

Clebsch is a canonical small strongly regular and projective folded-cube graph; exact mod-two matching-complex homology in the natural sequence PC(2),PC(3),PC(4) gives a usable, nontrivial benchmark inaccessible from the adjacency table or ordinary graph independence homology. It is independently motivated even without a general family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
