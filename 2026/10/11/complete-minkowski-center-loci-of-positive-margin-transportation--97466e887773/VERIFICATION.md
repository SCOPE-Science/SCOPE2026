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
# Verification details

Run `python3 verify.py` with Python 3 and SciPy installed. This program uses exact fractions to verify the coordinate-extremum construction, the nonnegative residual row/column margins, the rank-one filling, the complete Minkowski-center inequalities, the minimum-margin scalar identity, the square-case identity, and the predicted affine dimension over a reproducible finite collection. It also independently solves small linear programs to compare the coordinate maxima and minimized factor against the analytic expressions.

The available run completed with `PASS exact rational instances=648; independent LP instances=45; Birkhoff checks=8`.

Finite verification cannot prove a universal theorem for arbitrary positive real margins. The mathematical proof in RESULT.md is complete without numerical experiments. The cases of zero residual total and singleton positive residual support are covered analytically. The assumptions exclude structural-zero and individually bounded transportation tables. Scholarly originality has been reviewed against generic LP frameworks and transportation-geometry literature, but no independent audit has been performed.
