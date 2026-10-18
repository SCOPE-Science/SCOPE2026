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

The analytic proof establishes the result for every eligible convex window and every positive radius below the geometric separation threshold; the accompanying finite checker is only corroboration.

Run `python3 check.py` from the directory containing this document and the checker. The self-contained code uses only Python 3 standard-library modules, compares five geometric overlap integrals by independent angular quadrature, evaluates the first twelve formal coefficients and compares the truncated series with the direct kernel at three radii, performs exact rational Hankel reconstruction for four collinear centers with one repeated pair distance, and samples invariant random lines conditioned to meet a square.

Recorded successful output:

`LINE_TOPOLOGY_INVERSE_OK comparisons=19 exact_roots=5 sample_pair=0.065274 predicted_pair=0.065062`

The numerical quadrature and Monte Carlo cannot establish the all-configurations theorem or priority. Recovery from noisy measurements, numerical conditioning near repeated distances, and full center-coordinate identifiability are not established. Independent validation is not performed.
