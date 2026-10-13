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

The proof is analytic and finite-dimensional. The critical checks are:

1. At the qutrit Werner--Holevo endpoint, the six off-diagonal output eigenvalues are \(\lambda_i/4\), each twice, and the remaining three are \(\gamma_j/4\), where \(\gamma_j\) are roots of \(x^3-2x^2+x-4e_3\).
2. Newton identities give \(\sum_i\lambda_i^5=5e_2^2-5e_2e_3-5e_2+5e_3+1\) and \(\sum_j\gamma_j^5=60e_3+2\).
3. Since \(e_3\le(e_2/3)^{3/2}\) and \(e_2\le1/3\), the problem reduces to \(0\le u\le1/3\) with \(u=\sqrt{e_2/3}\).
4. The exact factorization
\[
\frac{344}{81}-\left(4-30u^2+70u^3+90u^4-30u^5\right)
=\frac{10}{81}(3u-1)(81u^4-216u^3-261u^2-6u-2)
\]
is nonnegative on that interval and vanishes only at \(u=1/3\).
5. Equality then forces \(\lambda_1=\lambda_2=\lambda_3=1/3\). The optimum fifth moment is \(43/10368\), and comparison with the single-use fifth moment \(1/16\) gives the fifth power violation ratio \(86/81\).

`verify_wh_p5.py` uses only the Python standard library and exact rational arithmetic for the recurrence identities, polynomial factorization coefficients, exact optimum, and violation factor. Its deterministic grid is supplementary and is not used as proof of the continuous statement.
