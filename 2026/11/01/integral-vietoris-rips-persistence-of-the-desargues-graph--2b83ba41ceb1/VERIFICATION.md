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

# Reproducibility and verification

Run `python3 verify.py` from the package directory using Python 3.9 or later; no third-party packages are required. The checker regenerates the twenty-vertex, thirty-edge Desargues graph; computes every shortest-path distance; enumerates all 260 and 3,200 simplices of the scale-two and scale-three Rips complexes; and validates every numbered operation of `certificates/r2_steps.json` and `certificates/r3_steps.json` against the then-active simplex set. Each matched lower face must have exactly one coface, namely its paired maximal upper face; each deleted critical cell must be maximal. It then independently topologically sorts **every** directed Hasse incidence of the original complex with matched arrows reversed, proving no directed gradient cycle exists.

The scale-two certificate has 140 operations: 120 matched pairs, one critical vertex, nineteen critical triangles. The scale-three certificate has 1,601 operations: 1,599 matched pairs, one critical vertex, one critical tetrahedron. Face masks use a 20-bit binary encoding with bit position equal to vertex index. The original face vectors, full matched-pair sets and counts are recoverable and verified by the supplied code. Its mod-two boundary ranks are an **independent finite numerical check**, not a substitute for integral homotopy arguments. It also verifies girth six, the twenty six-cycles with four through each edge, and that all ten graph-distance-five antipodal pairs are disjoint and exhaust the vertex set.

The recorded output is in `verification_output.txt` and ends in `VERIFY_OK`. Because `verify.py` reads all certificates relative to its own file path, the entire package is standalone; no unpublished files or absolute paths are required. The original proof explicitly invokes standard discrete Morse theory for the acyclic matching, one-point CW attachment for the perfect critical-cell configurations, and the join description of a crosspolytope boundary.

Limits: A finite verifier checks this one graph only, not a family of generalized Petersen graphs. Code and certificates are supplied for reproducibility and may themselves be inspected independently. No external mathematical audit or proof-assistant certification was carried out.
