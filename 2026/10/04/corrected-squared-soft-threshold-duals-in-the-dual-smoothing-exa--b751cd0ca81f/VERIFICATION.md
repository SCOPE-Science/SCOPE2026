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

The proof in `RESULT.md` is the primary verification. It derives the conjugate coordinatewise for all \(\lambda>0\), all finite dimensions, and all \(y\), then computes the exact difference between the correct and printed expressions.

The bundled `verify.py` is a supplementary exact-arithmetic replay. It uses Python's rational `Fraction` arithmetic only. It checks representative values in every scalar branch, verifies the exact subgradient/stationarity condition of the maximizer, verifies
\[
\widetilde h_\lambda^*(y)-h_\lambda^*(y)=\frac{C(y)^2}{\lambda},
\]
checks the exact witness \((\lambda,y)=(1,2)\), where the two values are \(3/2\) and \(1/2\), and verifies the one-sided derivative drop at the threshold. Its recorded output is `VERIFY_OK`.

The finite replay is not used to infer the universal statement. The universal statement follows from the symbolic three-case maximization and separability proof.

The accessible full source inspected was arXiv:2512.08167v1. The corresponding Springer chapter full text was not accessible, so verification does not assert that the final publisher version retains the same sign.
