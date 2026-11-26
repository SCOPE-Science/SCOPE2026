---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The result proves the CDF by conditioning on the competing first coordinate. The conditional uniform tail is \(w-d\) at distance \(d\) below the nominated first coordinate. On integrating, the upper branch's tail multiplier is \(e^w-w\), not \(1+w(e^w-1)\). Inverting the piecewise CDF identifies the nonnegative error integral and both bounds for its sharp geometric rate. The lower bound on the limit is analytic.

The standard-library script `verify.py` checks the tail probability by integrating directly over the competitor's exponential coordinate in representative cases, and compares two quadratures for the corrected integral. Running `python3 verify.py` gives `VERIFY_OK limit=0.8430788870 printed_cdf_limit=0.7323592997`. Finite-precision diagnostics do not establish the limit or the convergence rate.
