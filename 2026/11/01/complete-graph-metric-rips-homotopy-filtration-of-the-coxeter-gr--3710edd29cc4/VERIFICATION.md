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

# Reproducibility and scope of checks

The proof-bearing program is `verify.py`, and its actual executed output is `verified_output.txt`. Invoke `python verify.py`. It uses only standard-library modules and regenerates all inputs from the explicit Fano-plane construction; no previously generated simplex table or intermediate certificate is read.

It verifies 28 vertices, 42 edges, graph girth seven, diameter four, 28 closed-neighborhood tetrahedra at radius two, and the radius-three face vector \((28,294,1456,3514,3864,1596,144)\). The exact deterministic radius-three matching uses the 28 pivot indices printed in `RESULT.md`; it has 5,404 disjoint pairs and precisely one critical vertex and 87 critical four-dimensional cells. It constructs **every** cover relation of the face poset, reverses the matching arrows, and performs a complete topological sort of 10,896 faces across 48,916 incidences. Any directed cycle causes the executable to fail its assertion. The radius-three mod-two boundary-rank calculation is independently computed, but is only a cross-check: the fully acyclic matching yields the stronger integral wedge homotopy conclusion.

The radius-two homotopy equivalence follows from Adamaszek's published high-girth theorem, and can additionally be verified via the 28 relative tetrahedral collapses described in `RESULT.md`. Barcodes follow using the actual inclusion at radii one to two and the contractible radius-four stage. Exact scripts do not settle publication priority or independently certify the proof.
