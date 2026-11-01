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

# Reproduction and boundaries

From this directory run `python3 verify.py` with Python 3; only standard-library modules are required. The checker enumerates all nonempty subgraphs of the 18-arc bidirected graph and separately generates all valid path sets, confirming exactly 714 faces with vector `(18,108,264,252,72)`. It then pairs faces under the explicit deterministic arc order in `RESULT.md`, checks all 2,376 oriented Hasse incidences and acyclicity, confirms 341 matched pairs and critical cells `(1 in degree 0, 19 in degree 3, 12 in degree 4)`, and computes the exact signed integer 19-by-12 Morse differential, which is zero. The independent field-two simplicial reduction produces reduced Betti numbers `(0,0,0,19,12)`.

The proof's homotopy step is mathematical: a CW model with these critical cells has three-skeleton a wedge of 19 three-spheres, and zero attaching degrees in the integer Morse differential make all twelve four-cell attachments null in the corresponding third homotopy group. The finite computations make no claim for other digraph sizes. This is not an independent audit or external certification.
