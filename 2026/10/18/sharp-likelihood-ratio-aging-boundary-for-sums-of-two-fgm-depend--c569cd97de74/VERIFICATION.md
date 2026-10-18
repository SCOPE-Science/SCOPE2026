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

# Reproducibility and proof limits

Run `python3 verify.py` using Python 3 with only the standard library. The script reproduces exact rational alternating-series lower and upper bounds on \(e^{-3/2}\), an exact positive value bound for the curvature numerator \(D(3/2)\), finite-difference checks of the density derivatives, and an exploratory numerical value of the sharp threshold. Each explicit exact check is independent of floating-point arithmetic. The analytical proof in `RESULT.md` establishes the all-parameter inequality; numerical gridding is neither exhaustive nor a proof that the reported decimal is correctly rounded.

In the primary-paper comparison, the earlier all-parameter IFR conclusion is retained, while an ILR inference from a figure is tested by exact curvature. The more general issue of prior mathematical priority and inaccessible historical literature is not resolved by the checker. No independent audit or validation has been performed.
