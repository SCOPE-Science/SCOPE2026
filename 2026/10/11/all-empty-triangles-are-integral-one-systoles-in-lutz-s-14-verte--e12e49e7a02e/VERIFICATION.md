---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

Run `python3 verify.py` in the same directory as `facets.txt`. The verifier uses only the Python standard library. It reconstructs the simplicial complex from the 70 tetrahedra, checks the face vector, contracts a deterministic spanning tree, forms all triangular-boundary relations, finds an exact determinant-four full-rank minor, constructs a surjective mod-four cocycle that annihilates every triangular boundary, and exhausts all three-vertex cliques.

The successful output is:

`VERIFY_OK f=14,84,140,70 H1=Z/4 det_minor=4 empty3=143 nonzero_empty3=143 primitive=105 order2=38 values=1:50,2:38,3:55 simple_integral_1_systole=3`

The values 1 and 3 depend on orientation and generator choice; only their combined count 105 is used in the claim. The exact computation proves the statement for the supplied labeled complex only. It does not test all triangulations of the lens space, and it does not provide an independent audit.
