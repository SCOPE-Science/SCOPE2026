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

# Verification record

The proof is analytic. On the orthonormal shifted Legendre basis, exact integration gives coefficients \(c_k=1/[2\sqrt{(2k+1)(2k+3)}]\). Subtraction of \(P_nJP_n\) leaves a skew tridiagonal tail, whose operator norm is one quarter of the top eigenvalue of the explicitly defined \(4n\)-scaled Jacobi matrix divided by \(n\). The nonnegative quadratic form yields the Dirichlet Airy form \(\int_0^\infty (|f'|^2+2x|f|^2)dx\), and its minimum is \(2^{2/3}|a_1|\).

The bundled `check_legendre_airy.py` was executed with Python, NumPy, and SciPy. It verified the first eleven nonconstant integrated Legendre identities and computed the top eigenvalue of an increasingly long finite Jacobi-tail truncation for \(n\in\{50,100,300,1000,3000,10000,30000,100000\}\). The scaled corrections increased from about \(0.79077\) to \(0.92194\) towards the predicted \(0.9278785407446\). These finite observations corroborate the algebra; they cannot establish the limit. The proof's compactness and variational argument is the infinite-dimensional justification.

Limitations: no formal proof assistant, independent audit, or proof of an explicit finite-\(n\) remainder is claimed. Numerical truncation uses a long but finite Jacobi tail; it is not an exact infinite-dimensional eigenvalue computation.
