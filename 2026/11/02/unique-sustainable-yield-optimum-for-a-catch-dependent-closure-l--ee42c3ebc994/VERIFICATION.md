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

The standalone `verify.py` performs symbolic differentiation of the exact normalized yield, verifies the claimed partial derivative in the feedback-slope parameter, and expands the stationary equation and yield through the stated small-feedback order using SymPy. An exact-rational Taylor interval routine also proves opposite signs of the derivative numerator at \(s=3/8\) and \(s=3751/10000\) for \(A=1\), certifying the reported root bracket. Execution of `python3 verify.py` completed with both PASS messages. The reproducible checks do not enumerate all real parameters; the continuous and global parts of the claim rely on the explicit proof in `RESULT.md`.

The result assumes strictly positive continuous parameters and \(0<A<4\), and treats a fixed linear state-dependent closure policy rather than arbitrary optimal control. The scientific review is a self-review; no independent audit or external validation was performed. Historical priority remains contingent on sources beyond those materially compared.
