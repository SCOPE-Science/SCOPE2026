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

# Verification and reproduction

Run `python3 verification_check.py` from the directory containing this document. The script requires Python 3 with standard-library mathematics only. Its archived output is in `verification_output.txt`.

The script checks: numerical dilogarithm series against independent Simpson quadrature; finite-parameter scaled cumulant generating functions against the monotone Riemann-sum enclosure; unique positive saddle-point solutions and their strict comparison with the Gaussian rate; symmetry of the rate function; its small- and large-displacement expansions; and the scaled stationary variance. The recorded run completed 79 comparisons.

The analytical proof separately establishes uniqueness of stationarity, the exact moment-generating product, the limiting pressure, exponential tightness, exponential-tilt lower bounds, and the rate's strict geometry. Computations support but do not replace those results. A positive finite numerical test cannot establish a probability large-deviation principle. The theorem does not include finite-parameter tail prefactors or uniform estimates for thresholds growing with the inverse contraction gap.
