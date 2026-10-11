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

The inspected exact checker reconstructs all 85 source line equations over \(\mathbf Q(\sqrt[4]2,\sqrt[4]3,i)\), tests every pair by a symbolic \(4\times4\) determinant, and obtains a 20-regular graph with 850 edges. Its integer adjacency arithmetic verifies the square-free annihilating polynomial \((z-20)(z-3)(z+1)(z+3)(z+5)(z+9)\) and traces \(85,0,1700,3180,210644,2821740\). Independently solving the resulting multiplicity equations reproduces \((1,46,6,16,10,6)\); shifting by \(-3\) gives rank 39 and inertia \((1,38,46)\). The common-neighbor census \(530\) edges with three common neighbors and \(320\) with none gives 530 triangles. The computation is exhaustive for all \(\binom{85}{2}\) line pairs and uses exact number-field arithmetic.

## originality

PASS

Best-of-knowledge originality passes. Yu--Zhu's primary record establishes the 85-line surface and Picard computation; the audited source package records their reported line-intersection-matrix rank 39. Fresh Resultary and exact searches found no external statement of the 20-regular incidence graph, integral adjacency spectrum, common-neighbor census, characteristic polynomial, or inertia. The new spectral decomposition strictly refines the rank datum.

## value

PASS

The line incidence matrix is central to the source's Picard computation. Replacing a bare rank report by the complete integral spectrum, inertia, regularity, connectivity and triangle/common-neighbor data gives substantially finer structure of a distinguished extremal line configuration and supplies exact invariants useful for future geometric or combinatorial analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
