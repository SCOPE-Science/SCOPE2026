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

The theorem is proved by a bounded harmonic Dirichlet majorant on the half-strip, strict interior subharmonic comparison, and explicit conformal boundary attainment. The coefficients follow by directly integrating the triangular boundary function, with \(\lambda_j=(j+1/2)\pi\) and coefficient \(2/\lambda_j^2\). The equality characterization uses boundary values of the disk map and strictness of harmonic majorization in the interior.

The standalone `check.py` requires Python 3 and `mpmath` and computes, at high precision, the exact Fourier-series formula, its complex-dilogarithm expression, and an independent Cauchy-boundary integral for the conformal extremizer. It verifies the derived slope and corner asymptotics. Execute `python check.py` from the same directory; an exception indicates a failed check. The cross-check uses finitely many sampled centres and does **not** replace the analytic proof or certify all parameters.

All scientific inequalities are for \(M>0\), \(B>0\) and \(|V|<B\). No independent scientific audit or external certification has been performed.
