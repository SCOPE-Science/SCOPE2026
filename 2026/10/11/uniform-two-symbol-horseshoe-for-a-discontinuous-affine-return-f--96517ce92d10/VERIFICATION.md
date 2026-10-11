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
# Verification of the affine horseshoe certificate

Run `python3 verify_horseshoe.py` with Python 3 and no third-party modules. The script checks, using exact `fractions.Fraction` rational arithmetic, the two separated starting intervals, their full length-thirteen branch itineraries, strict distance from the discontinuity at every intermediate step, center-parameter slopes, covering of the common return interval, and the strict interior inverse images.

For the *entire* band \(a\in[-1/3-10^{-6},-1/3+10^{-6}]\), it uses rational interval arithmetic, with corner-product enclosure for all multiplications, to establish strict itineraries, opposite-side endpoint covering, and absolute derivative greater than five. All parameter dependencies are enclosed conservatively; no finite parameter grid or floating point is used. Observed result: **124 exact-rational assertions passed**. The checker is a finite certificate only; the theoretical implication to infinitely many symbolic words is proven in `RESULT.md` by nested inverse-branch contractions. Independent external scientific audit and validation are not performed.
