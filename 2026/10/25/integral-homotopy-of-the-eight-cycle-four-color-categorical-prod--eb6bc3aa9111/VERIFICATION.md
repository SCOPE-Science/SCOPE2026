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

# Reproducibility and limits
Run `python verify.py` in a directory containing the embedded `morse_boundary.json`. The script recreates exactly 196,226 nonempty faces, checks 1,457,216 oriented Hasse incidences, tests acyclicity of 98,087 simplex pairs, verifies one critical vertex/24 four-cells/27 five-cells, independently recomputes every signed entry in the 27×24 Morse boundary, and verifies an integer reduction with 21 ±1 pivots and zero remainder. It also checks Euler characteristic and prints `C8_TENSOR_K4_WEDGE_3S4_AND_6S5_VERIFIED` only after all tests. No external software packages, human-generated graph input, or other source files are needed. Finite exhaustive checks do not themselves establish infinite statements; the written topological argument upgrades the certified Morse information to a homotopy equivalence. Independent scientific validation has not been performed.
