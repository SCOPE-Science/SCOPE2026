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

The mathematical proof is in `RESULT.md`; no numerical experiment is used as a replacement for the global uniqueness or asymptotic arguments. The standalone `verify.py` requires only Python's standard library and can be run by `python verify.py`. Its deterministic pseudorandom seed is `453662`.

The executed checks include 400 separate Simpson-versus-closed-integral comparisons; decreasing-value tests at five noninhibited surface-light ratios; twelve supercritical optimum sign brackets and strict increases; three near-threshold checks; four intense-light cases; and the \(q=2\) example. Numeric root-solving near \(q=1\) has expected loss of floating-point precision from cancellation; the near-threshold numerical tests deliberately avoid differences below standard double-precision reliability, while the analytical proof covers all real \(q>1\).

The original light curve is historical prior work, as are integrated-column production equations. The comparison literature is not exhaustive; the 1975 Idso–Foster complete text and Murphy's 1962 full text could not be examined. No independent review or external certification is represented by these checks.
