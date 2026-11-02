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

# Reproducibility and limits

The package includes `verify.py`, a complete Python program using SymPy 1.14. Run `python verify.py` after installing SymPy if necessary. It checks exact symbolic two-step-return identities, the scalar return-Jacobian identity, the quadratic Hessian at \(a=-16/7\), and 15 exact parameter/coupling substitutions. The run on the packaged program reported:

`PASS: general symbolic return, Jacobian, quadratic degeneracy, and 15 exact parameter-coordinate cases`

The proof of *all* real parameter values and the global period-two orbit census is the direct algebra in `RESULT.md`; the tests do not certify completeness by enumeration. The local stability theorem uses standard smooth contraction/expansion implications for hyperbolic periodic points. No independent mathematical audit or external certification has been performed. Online-source comparisons are limited by publication indexing and the inaccessible complete text of a related but different rational map study.
