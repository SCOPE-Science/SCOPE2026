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
The algebraic proof is self-contained. The computational check in `verify.py` uses Python's standard-library `fractions.Fraction` type, so its representative recurrence checks are exact rather than floating-point.

Replay from the bundled `verify.py` returned `VERIFY_OK`. The checker verifies four ingredients on rational instances: the closed feedback formula, the affine projected scheduler, the product formula when \(0<\theta<2\), and the endpoint two-cycle with linear primal magnitude when \(\theta\ge2\). It also verifies exact two-step termination at \(\theta=1\).

The finite checks do not certify the universal quantifiers. Those follow from the interval and affine-map arguments in `RESULT.md`. No claim is made for candidate sets other than \([1,2/s-1]\), for matrix-valued preconditioners, or for varying online learning rates.
