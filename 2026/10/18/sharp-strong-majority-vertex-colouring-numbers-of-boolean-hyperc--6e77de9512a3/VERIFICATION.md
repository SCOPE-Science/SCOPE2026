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

Run `python3 verify_cube_majority.py` with Python 3.8 or later and no third-party libraries. The checker constructs explicit colourings for every dimension from 2 through 14, checks every open neighbourhood against the floor-half bound, verifies all palette colours occur, and exhaustively checks the 8,008 six-vertex subsets of the odd parity half of the five-cube in the distance-four graph. It also tests triangle-freeness and codegree at most two. Successful execution prints `CERTIFICATE_OK` followed by counts.

These are finite consistency tests. The proof in `RESULT.md` establishes the general classification via arbitrary-dimensional constructions, the five-cube double count, and the six-vertex extremal lemma. The checker is not an independent mathematical audit, and no independent audit has been performed.
