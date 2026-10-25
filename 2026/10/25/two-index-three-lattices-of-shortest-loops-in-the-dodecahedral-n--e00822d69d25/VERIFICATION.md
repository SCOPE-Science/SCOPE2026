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

The reproducibility artifact `verify_dodeca_square_lattices.py` constructs the dodecahedral graph, its open-neighborhood simplices, every simple four-cycle and the full graph-automorphism action from their definitions. Signed cotree cycle coordinates and a unimodular twenty-row minor identify the integral first-homology quotient. Exact twenty-one-column determinants \(+3\), \(-3\), \(+1\), and \(-1\), combined with independent modulo-three ranks twenty for each single orbit, establish the two index-three orbit lattices and the mixed integral bases. The verifier prints the complete indices of those certificates.

Checks performed: graph with twenty vertices and thirty edges; twenty unique triangles, sixty edges and a connected one-skeleton; exactly twenty filled three-cycles and sixty induced four-cycles; automorphism group of order 120 with two thirty-element square orbits; first integral homology rank twenty-one; exact quotient and four determinant certificates. The primitive-cycle argument additionally uses the proved edge-disjointness of the filled-triangle boundaries. The result is restricted to this one explicitly defined complex; no independence of assessment or general family theorem is claimed.
