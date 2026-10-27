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
# Verification and reproducibility

Run `python3 verification.py` using Python 3 with only its standard library. The packaged program has been run successfully, reporting `PASS: exact fraction checks, 4000 inverse trials, boundary and asymptotic tests`.

The script checks the rational identity for the derivative of \(u^2/(u+2)-u+\log(1+u)\) at 39 exact rational inputs, constructs 4,000 positive synthetic parameter instances, recovers both positive parameters from their cumulative depths and times to a relative tolerance \(4\times10^{-10}\), checks the exact \(F_1=K=B=1\), \(F_2=2\) calibration instance, rejects representative infeasible ratios and both exact boundary values, and compares the short- and long-scale asymptotic formulas at specified values. All pseudo-random inputs use the fixed integer seed 77883.

A finite checker does not establish continuum monotonicity or uniqueness. The mathematical certificate is the explicit analytic derivative \(H'(u)=u^2/[(1+u)(u+2)^2]>0\), the resulting strict ratio monotonicity, and the two controlled endpoint expansions in RESULT.md. Numerical inversion is not reliable at arbitrarily close machine-precision endpoints; the analytical statements do not depend on floating-point behavior there.
