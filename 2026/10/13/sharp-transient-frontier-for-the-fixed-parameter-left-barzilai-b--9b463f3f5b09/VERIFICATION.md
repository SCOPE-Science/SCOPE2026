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

The proof in `RESULT.md` is analytic.

`artifacts/verify_left_transient.py` symbolically reconstructs the two-dimensional exact-line-search warm-up, the following fixed-\(p\) LEFT step, and both squared-gradient and objective-gap amplification ratios. It verifies that both ratios converge to
\[
(p\kappa-1)^2
\]
as the witness parameter tends to zero, and checks representative cases on both sides of the frontier.

The script supports the proof but does not replace the dimension-independent spectral argument.
