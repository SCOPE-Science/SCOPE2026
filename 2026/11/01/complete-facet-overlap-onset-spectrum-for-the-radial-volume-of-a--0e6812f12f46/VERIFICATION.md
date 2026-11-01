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

## Verification and limitations
Run `python3 verify.py` with Python 3 and SymPy. It exercises exact-rational Gram inverses, determinants, nearest-distances and threshold monotonicity for dimensions 2–15; it also checks the 3D spherical-cap coefficient symbolically and the planar circular-segment coefficient both symbolically and numerically. Observed output: `PASS 586 checks (Gram inverses, distances, thresholds, and cap coefficients)`. These finite computations do not certify the theorem beyond tested indices; the all-dimensional argument is given in RESULT.md.

The gamma-factor is derived by a compact simplex beta integral, not inferred by fitting. The limiting rescaled integrands are dominated by integrable simplex functions; the zero-dimensional complement uses the indicator interpretation. Historical priority and uninspected literature are not independently certified.
