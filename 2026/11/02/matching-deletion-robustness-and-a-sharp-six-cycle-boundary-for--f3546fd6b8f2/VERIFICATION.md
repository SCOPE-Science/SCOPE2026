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

The package includes `verify_direct.py` and `verify_constructive.py`; run each with Python 3 standard library, with no external data files. A direct run checks all named three-colourings for selected graph sizes independently of the structural theorem. A distinct constructive run builds the six hypercubes and the six added states per matching deletion, then checks all vertex eccentricities by exhaustive BFS, graph structure, counts and the common junction of each square.

The actual observed terminal markers are `DIRECT_ALL_PASS` and `CONSTRUCTIVE_ALL_PASS`. The direct checker includes the exceptional six-cycle and asserts six isolated colourings, while the constructive model explicitly excludes that exception. These are finite tests; validity for all parameters uses the detailed symbolic proof in `RESULT.md`. The numerical checks are not an independent scholarly audit.
