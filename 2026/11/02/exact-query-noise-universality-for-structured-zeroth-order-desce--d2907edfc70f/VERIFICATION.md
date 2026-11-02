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

# Verification and its limits

The full analytic proof is given in `RESULT.md`. The standalone symbolic verifier `verify.py` was executed against the files in the package, using the `sympy` dependency in `requirements.txt`. It checks exact first and second moments from exhaustively enumerated signed-coordinate frames and two-point symmetric oracle noise in dimensions \(2\), \(3\), and \(4\), including \(\ell=1\) and \(\ell=d\); the two-step recurrence is checked using all \(256\) independent branches in a dimension-two instance. It further checks a separately re-evaluated baseline scheme on all 192 finite branches of a two-direction case, and verifies the optimal-radius relation and cancellation of direction count symbolically across multiple ranks and dimensions.

These finite tests are diagnostic, not an exhaustive certificate for all frame distributions, all positive parameters or unbounded iteration horizons. Those quantified conclusions follow from the displayed conditional-expectation proof. The shared-baseline comparison uses an exact noise-covariance trace identity; it asserts equality of second moments only, not equality of probability laws. Independent scientific audit has not yet been performed. No claim is made that all potentially relevant literature has been inspected.
