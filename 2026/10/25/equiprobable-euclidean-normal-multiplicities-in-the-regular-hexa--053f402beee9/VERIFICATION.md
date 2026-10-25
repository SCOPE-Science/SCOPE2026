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

# Reproducibility

Run `python verify_hexagon.py` using any standard Python 3 installation. The program depends only on the standard library, performs all polygon clipping in exact rational coordinates, and checks every sign chamber as well as all cap intersections. Its successful output displays probabilities 1/3 at multiplicities 4, 8, and 12; corresponding equal side/vertex counts; mean 8; and variance 32/3.

The normal-incidence characterization, absence of positive-area triple intersections, and combinatorial probability deduction are proved in `RESULT.md`. Finite execution is supplementary to the proof, not an independently certified proof or a general theorem for other polygons.
