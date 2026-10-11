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

Run `python verify.py` with a standard Python 3 interpreter. The script contains the six exact published facet lists, reconstructs each simplicial complex, and checks all finite claims directly.

For every complex it verifies 12 vertices, 42 edges, 28 facets, edge degree two, vertex degree seven, and connected seven-cycle vertex links. It computes exact mod-two boundary ranks 11 and 27, so the first mod-two homology dimension is four. It then enumerates every three-vertex clique. Each facial triangle reduces to zero modulo the image of the triangle boundary map; every nonfacial one reduces to a nonzero class. Homology-class multiplicities are computed without a chosen homology basis: two cycles are grouped exactly when their sum lies in the image of the triangle boundary map.

Expected output:

`VERIFY_OK f=12,42,28 H1_F2_dim=4 missing3=20,24,24,24,18,18 class_mults=4+4+4+4+2+2;4+4+4+4+4+4;4+4+4+4+4+4;4+4+4+4+4+4;4+4+2+2+2+2+1+1;4+4+4+1+1+1+1+1+1 all_missing3_nonzero=yes`

The computation is exhaustive only for the six listed complexes and for simple three-edge cycles. It does not establish claims about longer cycles, integral systoles, or other surface triangulations.
