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
# Reproduction of exact finite checks

Execute `python3 verify.py certificate.json` from the directory containing both files. Only Python 3 standard-library modules are required. The certificate contains precisely 1,870 listed codimension-one matched pairs over the six stages. The checker reconstructs all faces from the defining 24 integer triples, independently checks complete oriented Hasse acyclicity, the exact critical-cell vectors, graph-versus-Euclidean shell partitions, the embedded convex-boundary triangulation, and the radial half-space criterion. The run ends with `RADIAL_SEPARATION_OK` and `VERIFY_OK`.

The six stages contain, respectively, 60, 102, 262, 558, 1,038, and 1,758 nonempty faces, with 72, 192, 648, 1,752, 3,672, and 6,696 Hasse covers. The computed critical dimensions are exactly those stated in RESULT.md. The boundary sphere has 24 vertices, 66 edges and 44 triangles and lies in the squared-threshold-six complex.

The checker is a finite certificate verifier, not a stand-in for the separate mathematical implications: Forman's theorem converts its acyclic matchings into the CW homotopy models; a convex-polytope boundary maps to the unit sphere by radial projection with degree one; and the resulting inclusion ranks imply the stated truncated persistent barcode. The verification does not establish any statement at squared radius 14 or above, any integral equivariant classification, or independent human certification.
