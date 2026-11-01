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

# Verification and reproducibility

The full proof is in `RESULT.md`. The mathematical input from Brevig–Søvik is the outer-polynomial representation of coefficient extremizers, not any small-exponent asymptotic. The new reduction requires \(s=2/p>k\), ensuring all relevant generalized-binomial coefficients are positive. Uniform confinement of the rescaled polynomial coefficients, the negative-definite limit Hessian, and the positive perturbation directions are established analytically in the proof.

Run `python3 check.py` with a standard Python interpreter. The script checks algebraic identities and the leading two-term coefficient of an explicitly constructed polynomial trial family for a finite range of indices. It is a test of coefficient extraction and normalization, not a proof of global extremality, all-index asymptotics or historical originality. No external numerical packages are required. The residual historical-priority uncertainty and lack of independent validation remain.
