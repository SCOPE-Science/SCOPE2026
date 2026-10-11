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

The proof uses exact identities, not finite enumeration. The computational replay in `artifacts/verify.py` performs the following independent checks:

- expands the seven coefficients of \(P^3\) by direct convolution and confirms that their squared \(\ell^2\)-sum equals the numerical \(L^6\) moment computed from the algebraic coefficient formula;
- checks \(2\rho^4+5\rho^2-10=0\), the minimal-polynomial residual \(24(\mathsf C_6^6)^2+105\mathsf C_6^6-1225=0\), and equality at the stated extremizer;
- stress-tests the triangle-envelope reduction and the final sharp bound on deterministic pseudorandom complex triples;
- checks multiple affine-phase extremizers.

The random tests are corroborative only. They do not prove the inequality for untested coefficients. The universal claim rests on the exact Parseval expansion, monotonicity in \(v=x|c|\), and the one-variable derivative factorization in `RESULT.md`.
