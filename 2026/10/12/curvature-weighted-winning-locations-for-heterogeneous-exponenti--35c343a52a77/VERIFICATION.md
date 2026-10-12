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

The analytic argument uses exact exponential survival and winner-density identities, Gaussian Laplace localization at finitely many nondegenerate interior minima, a vanishing sum-of-squared-tails bound, and a tightness argument for the rescaled winner position. It proves joint weak convergence; no fixed-row computation is an infinite proof.

Execute `python3 verify.py` in the same directory as this document. Only the Python standard library is needed. The code evaluates finite-row survival sums and exact maximum CDFs and checks the curvatures and limiting weights for a concrete polynomial rate. Its tolerance-based tests are diagnostics at stated finite sample sizes, not independent verification of originality, convergence rates, or all admissible rate functions.

The boundary, flat-minimum, dependent-sample and non-exponential cases are not covered. Independent scientific audit has not been performed.
