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

# Verification

The executable `grid_matching_certificate.py` requires only the Python standard library. Run `python3 grid_matching_certificate.py`. Its complete, deterministic output is embedded as `CERTIFICATE_OUTPUT.txt` and ends with `CERTIFICATE_OK`.

The checker reconstructs ordinary rectangular grids from vertex coordinates, enumerates the augmented simplicial face sets (not just facets), applies five literal pivot orderings, and verifies every pair is an actual one-dimensional Hasse cover of the correct face set. The output counts prove that exactly one half of all paired faces is removed, leaving critical simplices only in the requested dimensions. The complete Hasse orientation is processed by indegree elimination; visits to all nodes certify acyclicity. The augmented Euler characteristic is separately recomputed from all masks.

In the largest of the five cases the run enumerates 196785 faces, 1239360 Hasse covers, 98365 paired covers and 55 unmatched six-simplices. Deleting the augmented empty-face pair leaves one ordinary critical vertex. Discrete-Morse CW reduction then supplies the integral wedge decomposition. The program never extrapolates from these five values to an infinite assertion.

No external independent audit has been performed; no human or third-party validation is claimed.
