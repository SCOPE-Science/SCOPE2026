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

# Reproducibility checks

Run `python3 verify.py` in the root of this package; no nonstandard Python dependencies, external downloads, or absolute paths are needed. The complete 130-step finite certificate is `certificates/r2_matching.json`. `make_certificate.py` is a deterministic optional regeneration script; it is not necessary for replay.

The verifier rebuilds the entire \(\mathrm{GP}(8,3)\) graph and all-pairs breadth-first distances, enumerates all possible nonempty subsets of its sixteen vertices to recover the exact simplicial face sets at radii one, two, and three, and counts all six-cycles and their edge incidences. It replays every free-face deletion, verifies every critical maximal-face deletion, tests that the remaining simplicial set is down-closed after every action, checks that every original face appears exactly once as matched or critical, and confirms acyclicity by topologically sorting the complete directed Hasse graph. It then builds the two disjoint eight-vertex crosspolytope boundaries, constructs signed integral top cycles, checks their boundaries vanish, and verifies the distance-four perfect matching giving the seven-sphere at radius three.

The output captured in `verification_output.txt` is the actual verifier output ending `VERIFY_OK`. The discrete-Morse theorem, the Hurewicz isomorphism for a simply connected two-dimensional wedge, and the classification of cell attachments are ordinary mathematical arguments, not claims that the program formally certifies general topology. The finite computation covers exactly the specified sixteen-vertex graph; no arbitrary-size or equivariant assertion is made. Independent mathematical audit has not been performed.
