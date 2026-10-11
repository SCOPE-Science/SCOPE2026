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

# Finite and analytic verification

Run `python verify.py` after installing `requirements.txt` in a standard Python environment. The verifier uses exact `fractions.Fraction` arithmetic to check the critical eigenvector relation for all dimensions \(2\le n\le50\). It additionally evaluates three leading singular values of the tridiagonal \((I-rJ)^*(I-rJ)\) for \(s\in\{-2,0,1/2,1,2\}\) and \(n\in\{80,160,320\}\); each checked residual relative to the two-term expansion satisfies the displayed finite tolerance, and the correction signs agree with the formula. This execution produced `JORDAN_CRITICAL_WINDOW_CHECK_OK`.

The rational identities verify a finite sample only; the analytic positive-ground-state identity in `RESULT.md` is the source of the exact all-dimensional statement. The floating-point comparisons are diagnostics, not proofs of limits, uniform remainders, complete spectral enumeration, or originality. The analytic proof uses the exact tridiagonal boundary equation, compact kernel convergence, simplicity of the Robin spectrum, and an implicit-root Taylor expansion. No independent audit has been performed.
