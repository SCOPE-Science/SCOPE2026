---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The finite domain has exactly six antipodal pairs of the 12 explicitly specified vertices, hence 2^6=64 configurations. Read the source's exhaustive exact Z[phi] support-plane, facet-cycle, outward determinant certificate; its sign comparisons are exact since phi=(1+sqrt5)/2. Reconstructed the hull independently using a separate scipy.spatial.ConvexHull algorithm for every one of 64 signed selections and compared to the four algebraic levels, obtaining counts 12/20/20/12 with numerical discrepancies below 2e-13. The original exact integer-pair certificate establishes the finite exhaustive claim; floating corroboration is not a separate exact proof. The scale is edge length two and neither degeneracies nor arbitrary antipodal sets are claimed.

## originality

PASS

Best-knowledge the exact all-64 six-vertex hull spectrum and multiplicities are not in the inspected primary antipodal-polytope study. The closest published icosahedral table computes volumes of 495 unconstrained four-vertex tetrahedra, a different cardinality and extremal functional, so it does not imply these six-vertex hull volumes.

## value

PASS

An antipodal selection is a canonical combinatorial class for a centrally symmetric regular polyhedron. Its full exact volume distribution, not merely an arbitrary selected configuration, resolves a natural finite extremal-statistic classification with a meaningful maximum/minimum and orbit multiplicities. It is deliberately restricted to the icosahedron and not claimed to settle higher-dimensional antipodal optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
