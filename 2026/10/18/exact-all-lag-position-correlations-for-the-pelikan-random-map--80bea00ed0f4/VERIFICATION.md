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

Execute `python verify.py` with Python 3 and its standard library. The check uses exact fractions, no sampling and no third-party dependencies. It independently composes all \(2^n\) map-choice words for each integer lag \(0\le n\le5\), partitions \([0,1)\) into a fine enough dyadic mesh to make every composition affine on each subinterval, integrates exactly against the known stationary piecewise-constant density, and compares to the new binomial formula. Tested parameters are \(3/5\), \(2/3\), \(3/4\) and \(9/10\). In addition, the known one-, two- and three-lag formulas are checked exactly for those parameters.

The expected completion line is `EXACT_FINITE_NOISE_AND_INTEGRAL_CHECKS_OK`. This is a finite independent implementation check, not an exhaustive proof for all lags. The theorem's infinite-range validity is established by binary digit composition, the reflection principle, and exact integration, as described in `RESULT.md`.

Boundary conditions: \(n=0\) is included; \(p=2/3\) is handled by an exact limit; dyadic endpoints have measure zero; the null-recurrent parameter \(p=1/2\) and any large-lag asymptotic are outside the claim.
