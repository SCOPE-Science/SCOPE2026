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

# Reproduction and limits

The files `verify_24cell.py` and `verify_24cell_independent.py` are complete, standalone Python scripts requiring no packages beyond Python's standard library. Execute each using Python 3.10 or later. The first reconstructs the 24-vertex graph from exact integer coordinates, exhaustively enumerates all 1,493 nonempty independent sets, tests the 717 face-pair incidences, and checks the absence of directed cycles in the full 5,496-incidence Hasse graph by visiting all its nodes. It computes the exact signed \(34\times24\) Morse boundary, verifies every matrix coefficient against its sparse description in `RESULT.md`, verifies rational rank three, and verifies the determinant \(-1\) of the specified maximal minor.

The second script independently regenerates the graph and face list, and computes the full simplicial-chain boundary ranks over characteristics two, three and five. These field computations are corroboration, not a replacement for integral attaching-map verification. No infinite search, probabilistic sampling, or timeout inference is used in the finite classification.

The complete homotopy claim follows from discrete Morse equivalence, the Hurewicz identification of the second homotopy group of a wedge of two-spheres with integral degree vectors, and elementary unimodular cellular cancellation. It is limited to the 24-cell edge graph, not to a general class of polytopal graphs.
