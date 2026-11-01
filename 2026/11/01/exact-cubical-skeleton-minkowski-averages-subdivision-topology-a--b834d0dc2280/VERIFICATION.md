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

# Reproducible checks and limits

Run `python verify.py` from the extracted package directory using Python 3 and only the standard library. The program verifies 23 exact finite lattice-sum/set-identity cases, counting 23,988 target lattice points, computes independent mod-two cellular boundary ranks for 23 low-dimensional cubical complexes, and tests six exact-rational Euclidean deep-hole instances. It terminates with `PASS`. These finite examples neither certify arbitrary dimensions nor establish novelty. The general membership identity is proved by slot assignment and tiled one-free-coordinate intervals; the metric formulas follow from nearest-grid rounding; the homotopy result follows from CW connectivity and Euler characteristic. No independent audit was requested or performed.
