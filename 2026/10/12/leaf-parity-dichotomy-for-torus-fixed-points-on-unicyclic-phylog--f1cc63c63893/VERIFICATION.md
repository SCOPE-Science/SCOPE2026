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

The analytic proof classifies all vertices by their fractional-edge support, then counts them via parity of the leaf-edge assignments; the toric orbit stratification converts the exact vertex count into the ordinary complex topological Euler characteristic.

The companion `check_vertices.py` was executed with NumPy and SymPy. It enumerates all independent active-facet systems for three simple connected unicyclic trivalent graphs, reconstructs rational candidates, checks their inequalities exactly, and checks rank of all active normals over the rationals.

Observed successful finite checks:

- Three-cycle, three leaves: 8 binary and 4 half-cycle vertices, total 12.
- Four-cycle, four leaves: 16 binary and 8 half-cycle vertices, total 24.
- Three-cycle with pendant trivalent branch, four leaves: 16 binary and 8 half-cycle vertices, total 24.

These checks do not prove the theorem for larger graphs; the combinatorial perturbation and parity arguments supply that proof. The finite checks do not establish originality or independent validation. The referenced articles concern generator bounds, deformation families, and Hilbert functions; possible literature outside the inspected sources is a residual originality risk.
