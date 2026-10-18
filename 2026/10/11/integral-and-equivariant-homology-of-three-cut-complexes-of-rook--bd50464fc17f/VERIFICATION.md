---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

PASS. Examined frozen RESULT.md (Git blob 8ed811129d2748ccc31dd4e6a6de3ed4f7d7e519) and all of verify.py (c4bd12272cee5da319f70374e420613c2afee90d). For all m,n>=3, in the Alexander dual Gamma, any nonadjacent vertex pair forces every other admissible vertex into the two other opposite rectangle corners; otherwise a disconnected induced triple occurs. This exactly classifies Gamma facets as row and column simplices plus 2-by-2 rectangle 3-simplices. B, the union of row/column simplices, has nerve K_m,n; each rectangle attaches relative to its 4-cycle. This yields a degree-2 relative free group wedge^2(Z^m) tensor wedge^2(Z^n), with connecting map phi onto H1(B)=W_m tensor W_n because 4-cycles generate all K_m,n cycles. Thus H2(Gamma)=ker(phi) free of stated rank, no other reduced homology. Integral equivariant Alexander duality shifts to degree mn-5 and twists by sign(sigma)^n sign(tau)^m; the displayed character follows the two virtual-lattice characters. Pure Delta dimension mn-4 with nonzero lower homology is non-shellable. Direct arithmetic independent of the stored checker: (m,n)=(3,3) rank=5 and (3,4) rank=12. Checker source was inspected, NOT executed as an independent new run; its finite exhaustive small cases are not the all-size proof.

## originality

PASS

PASS best knowledge. Bayer et al.'s ordinary cut-complex theorem on clique prisms K_n square K_2 excludes m,n>=3; their sequel's path-grids P_m square P_n have different adjacency. Their cut-complex techniques do not give this rook-graph integral equivariant kernel and closed character by implication. Resultary search found the present self-result and distinct total-cut hexagonal prism, ordinary four-cut triangular, path-grid and rook-Cech homology; the self-hit is not prior evidence. Residual risk is an uncatalogued equivalent cut-complex representation.

## value

PASS

PASS. This is a motivated infinite-family structural classification of a natural graph product's ordinary cut complex, determining torsion absence, precise free ranks, group action, and the non-shellable boundary. The representation and lower-dimensional homology are not mere normalized routine finite counts; they distinguish coordinate symmetries in a family left outside the two published adjacent Cartesian graph families.

The dated certificate retains the supplied scientific assessment, sources and limitations.
