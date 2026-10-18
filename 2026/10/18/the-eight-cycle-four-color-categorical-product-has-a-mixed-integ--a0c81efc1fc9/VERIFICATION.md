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

# Reproducible integral homotopy calculation

Run `python3 verify.py` with Python 3 and no third-party dependencies. The program checks an exhaustive recursive graph-independent-set enumeration against a separately constructed circular 16-state transfer count. Both give 196,226 nonempty faces and exactly the 17-term face-size vector recorded in `RESULT.md`.

For the first fixed-order matching, the program verifies 98,106 matched covering pairs, one critical vertex, five critical four-cells and eight critical five-cells. It enumerates and orients all 1,457,216 nonempty Hasse incidences, visits all 196,226 cells in a directed topological ordering, reconstructs the exact signed five-to-four Morse boundary printed in `RESULT.md`, checks rational rank two and locates a determinant-one maximal minor. Because the matrix is integral and has a unit maximal minor, there is no torsion Smith factor.

For a second, different fixed-order matching, the program verifies 98,104 matched pairs and one critical vertex, seven critical four-cells and ten critical five-cells. The complete Hasse test again succeeds; its signed critical boundary has rank four and a unit maximal minor. Both matchings therefore independently reduce to three four-cells and six five-cells, plus a vertex.

The chain differential alone is not used to infer a general graph-family result. The homotopy conclusion follows because the CW model has only one zero-cell and cells in the adjacent dimensions four and five; its five-cell attaching maps are classified by degrees in the fourth homotopy group of a wedge of four-spheres, so integral unit cancellations are homotopy cancellations. Neither computation establishes any result for another graph product. Independent mathematical audit remains unperformed.
