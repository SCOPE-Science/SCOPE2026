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

Run `python3 verify.py certificate.json` and `python3 independent.py` with Python 3.10 or later; no extra dependencies are needed. `certificate.json` is an exact data witness, not a record of unexplained external computations. Its 247 minimal blocker masks are independently recreated by the main verifier; its complete depth-six tree is replayed path-by-path and checked against every stated terminal witness. The supplementary script independently constructs the projective plane via affine points and directions, re-enumerates minimal hitting sets using deletion minimality, recomputes every relevant trace spectrum and obtains Littlestone rank six by a different exhaustive version-space recurrence.

Checks include all 8192 candidate masks, all 286 three-point supports, 715 four-point supports, 1287 five-point supports, 1716 six-point supports, 702 geometric five-support completions, and the 64 distinct terminal path witnesses. A mathematical argument (not finite extrapolation) supplies the depth-seven impossibility and dimension additivity on disjoint unions.

Limitations: no classification for arbitrary projective orders, no claim of independent external verification and no claim that previous geometric blocker enumerations are new. The cited 2022 classification article's full text was inaccessible for complete historical-priority comparison.
