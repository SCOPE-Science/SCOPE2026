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

The mathematical proof in `RESULT.md` is analytic and applies to every integer dimension \(n\ge2\) and real cut \(-1\le a<1\). Critical steps are: reflected-core maximality at a prescribed center; strict loss from transverse translation in positive-measure parallel sections; exact axial integration; strict decrease of the ball-section quotient; and algebraic solution of the stationary equation. The thin-cap limit follows from a uniform local expansion of the two integration endpoints for each fixed dimension.

Run `python3 verify.py` using Python 3 and its standard library only. On the provided artifact, the program returned `VERIFY_OK 16566 axial tests, 420 nonaxial 2-D tests`. The tests compare the formula against sample axial centers, random off-axis planar centers, and the three-dimensional hemisphere identity. Numerical tolerances are finite, and none of these checks constitutes a proof for infinitely many dimensions or continuum-valued cut parameters.

The full original analysis is supplied in `RESULT.md`. No external proof assistant, independent audit, or machine-generated certificate is claimed.
