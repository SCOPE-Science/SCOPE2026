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

The exact proof of the complex triangular classification is in `RESULT.md` and does not use experimental evidence for its universal conclusions. The proof explicitly checks both inverse normalization and the boundary cases \(c=-1\), \(b=0\), and \(p=2\).

Run `python angular_zero_check.py` with Python 3. The checker has no third-party dependencies and verifies the closed angular threshold against a direct scalar numerical minimization, the exact inversion-ratio law over sample complex matrices, monotonicity of the angular factor, and the explicit quartic vector witness. Its deterministic output is `PASS: 1111 finite diagnostics; exact algebraic witness reviewed.` The quartic cancellation is algebraic and reproduced separately in the analytic proof.

The numerical diagnostics are finite checks and do not establish claims for all real exponents, arbitrary angles, or all operators. The all-exponent assertion is proved analytically. Older references are given in the main result; a full version of the motivating October 2026 preprint could not be inspected, so publication priority is not independently certified.
