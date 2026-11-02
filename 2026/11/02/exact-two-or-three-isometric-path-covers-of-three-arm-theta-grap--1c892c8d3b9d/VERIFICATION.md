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

The standalone Python 3 script `verify.py` constructs each labelled theta graph from its three arm lengths, computes exact shortest-path distances using breadth-first search, enumerates all shortest paths, and checks whether two path-vertex sets cover every vertex. It verifies all 455 unordered triples with lengths between 2 and 14 and 80 additional reproducibly selected triples with maximum arm length 56. The observed Boolean answers match the stated exact classification. Direct graph-distance and coverage checks were also run on explicit constructive witnesses for all 1,140 length triples between 2 and 19. This is evidence for the finite cases; the proof in `RESULT.md` is needed for the unrestricted theorem.

Computations are deterministic and integer-only; they do not establish historical priority or independent mathematical certification. No external dependencies beyond the Python standard library are required.
