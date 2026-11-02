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

The scientific statement is the two-site Gaussian marginal-likelihood optimization over \(t\in[0,1]\), with signal variance fixed to one, known nugget \(h>0\), and residuals \((b,-b)\). The analytic proof is in `RESULT.md`.

Execute `python verify.py` with standard Python 3. This implementation was executed on its actual packaged source path, with output: `PASS: 18374 assertions; exact rational and numerical checks completed.` Exact-rational checks verify the differentiated likelihood identity; floating-point checks cover critical endpoint ties, strict interior inequalities, numerous nugget and contrast choices, high-contrast exclusion even below the high-nugget regime, critical-curve monotonicity and finite-difference differentiation. The script is deterministic and imports only the Python standard library.

Finite assertions do not establish the theorem's quantified real-variable inequalities. Proof steps are: diagonalization of the observed two-site covariance, factorization of endpoint likelihood differences, strictly positive power-series derivative for \(h\ge1\), quadratic derivative sign to eliminate interior minima, critical-curve monotonicity, and a logarithmic bound proving the all-nugget obstruction. No computer-assisted infinite certificate, external mathematical certification or independent audit is claimed.

The compactified parameter endpoints generally correspond to limits of the actual lengthscale, not to interior finite MLEs. The result does not cover unknown signal amplitude or mean, more than two observations, negative intersite correlations or the complete small-nugget optimizer diagram.
