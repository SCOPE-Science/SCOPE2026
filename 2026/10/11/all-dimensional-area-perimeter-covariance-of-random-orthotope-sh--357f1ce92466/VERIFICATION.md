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

# Reproducible verification

Run `python3 verify.py` using Python's standard library. The script evaluates the exact d=3 and d=4 cube mixed-moment anchors, the gamma coefficients for dimensions 3 through 999, and 120,000 Gaussian-frame Haar-plane samples across five orthotopes. Its expected success output is `VERIFY_OK 45 Haar planes 120000`.

The independent random-frame construction numerically checks the mixed moment, both individual means, one repeated-index incidence term, one disjoint-index incidence term, and the single-determinant mean. The code additionally tests positivity of the analytic sharp coefficient and the equality distinction for selected side lengths.

These are finite numerical checks, not a certificate that a claim quantified over all dimensions and positive side lengths is proved. The universal result follows from the exact beta/gamma integrals, Maclaurin's inequality, gamma log-convexity, the two-step recurrence, and Stirling's asymptotic established in the proof. Neither a Lean formalization nor an independent expert audit is claimed.
