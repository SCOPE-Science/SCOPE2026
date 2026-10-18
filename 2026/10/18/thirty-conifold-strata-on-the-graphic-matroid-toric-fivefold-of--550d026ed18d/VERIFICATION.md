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

All verification in this package was performed by direct proof and exact finite computation, not by an independent audit.

Run `python3 k4_exact_certificate.py`. The standard-library-only program constructs the 16 spanning-tree incidence vectors of \(K_4\), exhausts all 62 proper nonempty ground-set subsets for rank-inequality facets, enumerates every face as an intersection of facet masks, computes its affine dimension with exact rational elimination, and determines toric smoothness by the gcd of maximal integer minors. It checks the 30 maximal singular faces, three graph-automorphism orbits, primitive triangle/square lattices, and the four-ray relations of the transverse conifold cones. The tested program returned `VERIFY_OK` and `FACE_SURFACES_OK`.

The certificate proves a finite exhaustive classification for this fixed matroid polytope, rather than a sampling pattern or a general statement about arbitrary graphs. It does not establish an analogous classification for larger graphic matroids. Independently auditing the proof and checking for unindexed literature overlap remain open.
