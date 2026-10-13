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

# Reproducibility checks and boundaries

Run `python3 verify_moments.py` from the directory containing the package. The verifier uses only the Python standard library and checks two-variable polynomial identities by exact rational coefficient arithmetic. It establishes that subtracting \(y(y-1-v)^2Q_v(y)\) from \((y-1)^5\) leaves a polynomial of degree at most two whose fixed-first-two-moment expectation is \(v(v-1)(v^2+1)\). It verifies exact formulae for the two branches of \(Q_v(y)-C(v)\), and then uses 32 explicitly normalized three-point distributions to compare the moment-excess ratio against the stated optimal coefficient.

The 32 examples use eight rational variance ratios and four rational perturbation strengths per ratio. These finite tests are checks of formula implementation, not a proof of all variance ratios or all probability distributions. The universal nonnegative-support inequality follows from a polynomial factorization valid for all \(y\ge0\) and \(v>0\); optimality is the explicit small-mass perturbation limit at every chosen support location. The proof handles both the positive-vertex and endpoint-vertex regimes, including the coincident-atom limiting case \(\(v=1/4\)\).

All statements require a positive mean, positive variance, and finite fifth moment. The bound is a sharp *linear* comparison at fixed first two moments; no global higher-order moment-space classification or independent external validation is claimed.
