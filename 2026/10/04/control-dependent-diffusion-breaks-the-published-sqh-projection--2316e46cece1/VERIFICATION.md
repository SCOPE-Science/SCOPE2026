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

The verification is algebraic. Running `python verify.py` checks four items with exact rational arithmetic:

1. the factor \(0.01\) in the control-dependent diffusion contribution \(D_k(1-w_1)^2\);
2. the coefficients of the augmented first-coordinate quadratic and the corrected stationary point;
3. an exact rational instance for which substituting the scalar value \(r(u^k)\) in the printed projected expression differs from the true minimizer of the displayed augmented Hamiltonian; and
4. a scalar proximal fixed-point example showing that minimization of \(H(w)+\varepsilon\lvert w-u^*\rvert^2\) at \(u^*\) does not by itself imply global minimization of \(H\).

The source equations were checked against the open-access full text identified by DOI 10.1007/s00285-026-02462-7. The proof does not require a numerical PDE solve. It also does not establish that \(D_k\neq0\) on every iterate; the theorem-level issue is that no hypothesis removes that term and the printed minimizer does not follow from the displayed Hamiltonian.
