---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The reset is of Y only. The generator on x^i y^j has diagonal −(i+ρ 1_{j>0}), drift coupling i x^{i−1}y^{j+1} and diffusion coupling j(j−1)x^iy^{j−2}. A separate triangular recurrence for stationary and lagged moments reproduced the exact rational transform symbolically, including all normalizations. Partial fractions give g_1=−(12+32t)e^{−t}; away from 1, h=e^{ρt}g consists of an exponential plus an affine term. Below 1 its initial value, slope and second derivative are negative. At ρ_* the initial value vanishes and the slope is positive (11ρ_*²−9ρ_*−18=(15ρ_*−3)/2); above it all three signs are positive. In the intermediate regime the core starts negative, is strictly convex and diverges to +∞, hence has just one zero. For each of the three exponential filters, the derivative of the exponentially rescaled output has the input's sign, so its initially negative output has at most one positive-time zero, crossing from negative to positive if it occurs. Strict fixed signs persist outside that regime. Inside it, the positive e^{−t} core tail survives all three filters since their rates exceed 1, proving existence as well as uniqueness.

## originality

PASS

The transform, endpoint signs and existence of a reversal were already established for the same model. The distinct result supported here is the global zero count and strict all-lag signs, including both boundary rates. The exact antecedent explicitly did not assert uniqueness; the checked general and adjacent work does not supply the needed signed-core analysis for this observable.

## value

PASS

The sign of a time-direction statistic can depend on the observation lag; the exact regime and zero count distinguish a unique change of diagnostic direction from spurious additional reversals. This is a complete, nontrivial qualitative classification for a motivated non-Gaussian model. The earlier transform and endpoint checks alone did not give it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
