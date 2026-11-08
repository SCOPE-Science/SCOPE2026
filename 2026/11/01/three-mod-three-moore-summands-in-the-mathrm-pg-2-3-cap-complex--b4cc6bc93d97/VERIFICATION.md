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

For the actual 13-vertex PG(2,3) no-collinear-triple complex, reconstructed 13 points, 13 four-point lines, 52 excluded triangles, face vector (13,78,234,234) and absence of 5-caps. Independently computed top boundary ranks mod 2,3,5,101 = 168,165,168,168; inspected the attached exact SymPy Smith program establishing (1^165,3^3,0^66). Every missing triangle cones outside its line, so K is simply connected; Hurewicz and Smith basis changes of three-cell degrees yield 3 Moore M(Z/3,2) plus 66 S^3. Exact integral SNF was inspected in source, not independently rerun; modular checks alone would not exclude higher 3-power torsion.

## originality

PASS

Best-of-knowledge statement/implication comparison. Known 13-point design facts determine f-vector but neither torsion diagonal nor 3-Moore attachments; ordered-injective word complex differs integrally from simplicial chains.

## value

PASS

The full integral homotopy type of a canonical 13-point projective cap complex, including three independent mod-three Moore summands, supplies a natural finite-geometric torsion benchmark not determined by elementary cap counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
