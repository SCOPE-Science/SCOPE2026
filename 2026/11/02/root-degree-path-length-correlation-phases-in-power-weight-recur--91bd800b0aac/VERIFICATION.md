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

# Verification and limits

The standalone `verify.py` uses only Python's standard library. It enumerates every legal parent-choice sequence for \(n=2,\ldots,8\) at each exponent in \(\{-2,-1,0,1,2\}\), calculates its exact rational probability and joint root-degree/path-length moments, and compares the covariance, both variances, and normalization against the formulas. There are 35 exhaustive finite models and 175 exact rational assertions. Two further noncertifying numerical convergence assertions compare finite coefficient sums at \(n=400000\) to the separately derived linear-weight constants, for 177 assertions in total.

To reproduce: `python verify.py`. No external package, network access, or prior artifact is required.

The program does not exhaust arbitrary exponents or all sizes and does not prove infinite limits. The general theorem is established analytically in `RESULT.md`; the path-length martingale innovation formula and its fixed-exponent limit are prior published inputs. The triangular-array limits are proved by uniform domination, not numerical extrapolation. Historical originality has not been independently certified.
