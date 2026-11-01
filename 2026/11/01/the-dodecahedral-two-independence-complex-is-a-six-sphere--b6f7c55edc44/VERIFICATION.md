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

Execute `python3 verify_dodecahedron.py` in a standard Python 3 installation (using integer `bit_count`; Python 3.10 or newer is sufficient). The output in `verify_dodecahedron.out` records the exact observed results.

The independent subset enumerators agree on every one of the \(2^{20}\) masks, yielding 63,143 faces including the empty set. The verifier constructs the forbidden length-two triples directly from all thirty graph edges, so no stored simplex table is assumed. It then constructs the deterministic matching from the published twenty-entry vertex order, proves disjointness and cover adjacency, checks the critical cell dimensions, and performs a topological sort of the full directed Hasse diagram. The sort visits all 63,142 nonempty faces and thereby checks acyclicity rather than merely assuming it from the matching algorithm.

The graph is a fixed finite combinatorial object. The code supplies exhaustive finite verification of all steps needed for the homotopy assertion. The theoretical implication from an acyclic matching with just a critical zero-cell and six-cell to \(S^6\) is the discrete Morse theorem. No independent audit, separate experimental sample, or claimed generalization is implied.
