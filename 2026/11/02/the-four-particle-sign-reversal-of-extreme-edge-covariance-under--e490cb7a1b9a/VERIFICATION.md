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
# Verification notes

Run `python3 verify.py` in the directory containing `RESULT.md` and `verify.py`. The test script uses only Python's standard library and numerically reconstructs \(\mathbb E A_N\), \(\mathbb E(A_N B_N)\), their stationary covariance combination and a diagnostic check of \(0\le g_N\le1/N\) for \(N=2,\ldots,8\). It compares the first three exact Gaussian mean/product identities to independently evaluated quadratures. The program prints each normalized stationary covariance and terminates with a nonzero status on any assertion failure.

The exact integration identities and the Gaussian interpolation bound in `RESULT.md` are the analytical evidence for the theorem for every integer \(N\ge2\). Numerical quadrature alone cannot establish an all-population sign theorem or an asymptotic limit. The computed checks assume the normalization \(\operatorname{Var}(Z_i)=1\) and \(\operatorname{Var}(X_i\mid T)=2DT\); multiplying the diagnostic normalized bracket by \(2D/r\) recovers physical covariance. No independent audit has been performed.
