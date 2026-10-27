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

Execute `python3 verify.py` with Python 3 standard library. The checker computes the denumerant by unbounded-coin recurrence, not by the proof's root-of-unity method; it evaluates the quadratic approximation and both sides of the mean-square formula in `fractions.Fraction`. It also checks that the residual has zero average. The run completed with:

`CERTIFICATE_OK configurations=66 exact_rational_equalities=66`

Selected exact mean squares: \((a,d)=(1,1)\) gives \(209/5184\); \((3,1)\) gives \(238069/2592000\); \((5,2)\) gives \(740134/4465125\). The general result depends on the mathematical proof, since checking finitely many parameters does not establish the universal quantifiers. The derivation requires that \(a\) be odd and coprime to \(d\).
